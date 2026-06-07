// netlify/functions/ask.js
// Proxy for Anthropic API — keeps ANTHROPIC_API_KEY off the browser.
// POST /.netlify/functions/ask
// Body: { message, pageContext: { title, pillar, keyword }, history: [...] }

'use strict';

const CORS = {
  'Content-Type': 'application/json',
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

exports.handler = async (event) => {
  // CORS preflight
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers: CORS, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers: CORS, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  // Parse body
  let body;
  try {
    body = JSON.parse(event.body || '{}');
  } catch {
    return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: 'Invalid JSON' }) };
  }

  const { message, pageContext = {}, history = [] } = body;

  if (!message || typeof message !== 'string' || !message.trim()) {
    return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: 'message required' }) };
  }

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    console.error('[ask] ANTHROPIC_API_KEY not set');
    return { statusCode: 500, headers: CORS, body: JSON.stringify({ error: 'Server configuration error' }) };
  }

  // Build system prompt with page context
  const pageTitle = String(pageContext.title || 'Claude AI').slice(0, 200);
  const keyword   = String(pageContext.keyword || 'Claude AI').slice(0, 100);

  const systemPrompt =
    `You are the AI assistant for HowToClaudeAtoZ.com — the definitive encyclopaedia for Claude AI. ` +
    `You are an expert on every Claude use case, integration, workflow, and feature. ` +
    `You are currently embedded on a page about: ${pageTitle} (${keyword}). ` +
    `Answer questions about this topic and related Claude use cases with clarity and precision. ` +
    `Keep answers concise — 2 to 4 short paragraphs maximum. ` +
    `If relevant, mention that the full guide is on this page. ` +
    `Never recommend leaving this site. ` +
    `Always end your response with one follow-up question to keep the conversation going. ` +
    `Do not answer questions unrelated to Claude AI or AI tools — politely redirect back to Claude topics.`;

  // Sanitise and cap conversation history at last 6 turns (12 messages)
  const safeHistory = (Array.isArray(history) ? history : [])
    .slice(-12)
    .filter(m => m && (m.role === 'user' || m.role === 'assistant') && m.content)
    .map(m => ({
      role:    m.role,
      content: String(m.content).slice(0, 1000),
    }));

  const messages = [
    ...safeHistory,
    { role: 'user', content: message.trim().slice(0, 500) },
  ];

  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type':    'application/json',
        'x-api-key':       apiKey,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify({
        model:      'claude-haiku-4-5-20251001',
        max_tokens: 400,
        system:     systemPrompt,
        messages,
      }),
    });

    if (!response.ok) {
      const errText = await response.text().catch(() => '');
      console.error(`[ask] Anthropic ${response.status}:`, errText.slice(0, 300));
      return {
        statusCode: 502,
        headers:    CORS,
        body:       JSON.stringify({ error: 'Upstream API error' }),
      };
    }

    const data = await response.json();
    const text = data?.content?.[0]?.text || '';

    console.log(`[ask] OK — ${text.length} chars, model=${data.model}, tokens=${data.usage?.output_tokens}`);

    return {
      statusCode: 200,
      headers:    CORS,
      body:       JSON.stringify({ response: text }),
    };

  } catch (err) {
    console.error('[ask] fetch error:', err.message);
    return {
      statusCode: 500,
      headers:    CORS,
      body:       JSON.stringify({ error: 'Internal error' }),
    };
  }
};
