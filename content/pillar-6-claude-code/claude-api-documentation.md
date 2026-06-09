---
title: "Claude for Writing API Documentation (2026 Guide)"
slug: claude-api-documentation
pillar: claude-code
meta_description: "Use Claude to write API documentation — READMEs, OpenAPI specs, docstrings, and endpoint docs — from your code in minutes. Full guide with examples for 2026."
primary_keyword: "Claude API documentation"
secondary_keywords:
  - "Claude write API docs"
  - "Claude OpenAPI spec generator"
  - "AI API documentation"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "Can Claude write API documentation?"
    a: "Yes — Claude can write API documentation from your source code, route definitions, or a plain-English description. It generates READMEs, docstrings, OpenAPI/Swagger YAML specs, endpoint reference docs, and code examples in multiple languages. The output is detailed, consistent, and follows documentation best practices. Claude Code (the CLI) can read your entire codebase and generate documentation that accurately reflects how your API actually works."
  - q: "What format should API docs be in?"
    a: "The most common formats are: OpenAPI 3.1 YAML (for machine-readable specs that generate interactive Swagger UI), Markdown (for GitHub READMEs and developer portals), and docstrings inside the code (Python, JS, etc). Claude can generate all three. For public APIs, an OpenAPI spec is the gold standard — it drives documentation sites, client SDK generation, and testing tools."
  - q: "Can Claude generate OpenAPI specs?"
    a: "Yes — Claude generates valid OpenAPI 3.1 YAML from your route definitions, function signatures, or a plain-English description of your API. It includes proper schemas with types, required fields, example values, error responses, and authentication schemes. The generated YAML is compatible with Swagger UI, Redoc, and code generation tools like openapi-generator."
summary: "Claude generates accurate, comprehensive API documentation — from OpenAPI specs to README files to inline docstrings — by reading your actual code and converting it to clear developer-facing docs. This guide covers every documentation type with prompt templates and a full OpenAPI YAML example."
hero_image: "/assets/images/heroes/photo-029-122100400227357116.jpg"
hero_alt: "Paste your route definitions or function signatures into Claude and it returns a complete OpenAPI 3."
---

# Claude for Writing API Documentation (2026 Guide)

*Last updated: 2026-06-07*

Claude API documentation generation turns one of the most tedious parts of software development into a fast, largely automated task. Give Claude your route definitions, function signatures, or existing code, and it produces complete, accurate documentation: OpenAPI 3.1 YAML specs, Markdown endpoint references, inline docstrings, README sections, and multi-language code examples. The output follows documentation best practices — request/response schemas, error codes, authentication details, and example payloads included. This guide covers every documentation format, the exact prompts that produce the best output, and a complete OpenAPI spec example generated from a real API.

## Why Claude Excels at API Documentation

API documentation has two hard parts: completeness (covering every endpoint, parameter, and error case) and accuracy (matching what the code actually does). Human-written docs suffer from both — sections get skipped when deadlines hit, and docs drift from the implementation over time. Claude handles both by reading the actual source code:

- **Completeness** — Claude generates docs for every route, every query parameter, every response code it sees in the code.
- **Accuracy** — Claude reads your Pydantic models, TypeScript interfaces, or function signatures and uses them directly for schema definitions.
- **Consistency** — every endpoint follows the same format, tone, and detail level.
- **Multi-language examples** — Claude generates curl, Python, JavaScript, and other language examples for each endpoint automatically.

## How to Write API Documentation with Claude — Step by Step

### Step 1: Choose Your Documentation Type

Decide what you need before prompting:

| Documentation type | Best for | Format |
|---|---|---|
| OpenAPI 3.1 spec | Public APIs, SDK generation, Swagger UI | YAML |
| README / Quickstart | GitHub repos, developer onboarding | Markdown |
| Endpoint reference | Developer portal pages | Markdown |
| Inline docstrings | Code maintainability, IDE tooltips | Language-native |
| Code examples | SDK docs, tutorials | Code blocks |

### Step 2: Prepare Your Source Material

Give Claude the most direct source of truth available:

- **For existing APIs** — paste your route definitions and request/response models
- **For new APIs** — describe the endpoints in plain English
- **For Claude Code** — no preparation needed; Claude reads your files directly

### Step 3: Generate an OpenAPI Spec

Paste your FastAPI (or Express, or Rails) route code and ask:

```
Generate a complete OpenAPI 3.1 YAML spec from these FastAPI routes. 
Include all schemas, required fields, response codes (200, 400, 401, 404, 500), 
example values, and Bearer token authentication. Use the function docstrings 
as the endpoint descriptions.
```

### Step 4: Generate a README Section

For a developer-facing README:

```
Write a "Getting Started" README section for this REST API. Cover: 
authentication (Bearer token), base URL, rate limits (100 req/min), 
and show a complete curl example for each endpoint. Use markdown 
with code blocks.
```

### Step 5: Generate Docstrings in Bulk with Claude Code

In a multi-file project, Claude Code can add docstrings to all undocumented functions:

```bash
claude
> Add Google-style docstrings to every function in the services/ 
  directory that currently lacks one. Use the function logic and 
  existing type hints to infer the parameter and return descriptions.
```

## Documentation Types and Prompt Templates

### OpenAPI 3.1 YAML — Complete Example

Below is a Claude-generated OpenAPI spec for a simple user authentication API:

```yaml
openapi: 3.1.0
info:
  title: User Auth API
  version: 1.0.0
  description: Handles user registration, login, and token management.

servers:
  - url: https://api.example.com/v1
    description: Production
  - url: https://staging-api.example.com/v1
    description: Staging

security:
  - BearerAuth: []

paths:
  /auth/register:
    post:
      summary: Register a new user
      operationId: registerUser
      security: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RegisterRequest'
            example:
              email: alice@example.com
              password: "S3cure!Pass"
              display_name: Alice Johnson
      responses:
        '201':
          description: User created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuthResponse'
        '409':
          description: Email already registered
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: email_already_registered
                message: An account with this email address already exists.

  /auth/login:
    post:
      summary: Log in and receive access token
      operationId: loginUser
      security: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LoginRequest'
      responses:
        '200':
          description: Login successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuthResponse'
        '401':
          description: Invalid credentials
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

  /auth/refresh:
    post:
      summary: Exchange a refresh token for a new access token
      operationId: refreshToken
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [refresh_token]
              properties:
                refresh_token:
                  type: string
                  description: Long-lived refresh token issued at login.
      responses:
        '200':
          description: New access token issued
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuthResponse'
        '401':
          description: Invalid or expired refresh token

  /users/me:
    get:
      summary: Get the authenticated user's profile
      operationId: getCurrentUser
      responses:
        '200':
          description: User profile
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserProfile'
        '401':
          description: Missing or invalid token

components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

  schemas:
    RegisterRequest:
      type: object
      required: [email, password, display_name]
      properties:
        email:
          type: string
          format: email
        password:
          type: string
          minLength: 8
        display_name:
          type: string
          minLength: 2
          maxLength: 60

    LoginRequest:
      type: object
      required: [email, password]
      properties:
        email:
          type: string
          format: email
        password:
          type: string

    AuthResponse:
      type: object
      properties:
        access_token:
          type: string
          description: Short-lived JWT (expires 15 minutes).
        refresh_token:
          type: string
          description: Long-lived token for acquiring new access tokens (expires 30 days).
        token_type:
          type: string
          enum: [bearer]
        expires_in:
          type: integer
          example: 900

    UserProfile:
      type: object
      properties:
        id:
          type: string
          format: uuid
        email:
          type: string
          format: email
        display_name:
          type: string
        created_at:
          type: string
          format: date-time

    ErrorResponse:
      type: object
      required: [error, message]
      properties:
        error:
          type: string
          description: Machine-readable error code.
        message:
          type: string
          description: Human-readable error description.
```

### Generating Python Docstrings

**Prompt:**

```
Add comprehensive Google-style docstrings to these functions. 
Infer the parameter types and meanings from the code and type hints.
Include: summary, Args, Returns, Raises sections.
```

**Before:**
```python
def create_invoice(customer_id, line_items, due_days=30):
    if not line_items:
        raise ValueError("line_items cannot be empty")
    total = sum(item["amount"] for item in line_items)
    ...
```

**After (Claude-generated docstring):**
```python
def create_invoice(customer_id: str, line_items: list[dict], due_days: int = 30) -> Invoice:
    """Create a new invoice for a customer.

    Calculates the total from the provided line items and sets the due date
    relative to today based on `due_days`. Saves the invoice to the database
    and returns the created Invoice object.

    Args:
        customer_id: The UUID of the customer to invoice.
        line_items: List of line item dicts, each with keys:
            - description (str): Human-readable item description.
            - amount (float): Amount in the account currency, must be > 0.
            - quantity (int): Number of units, default 1.
        due_days: Number of days from today until payment is due. Defaults to 30.

    Returns:
        The created Invoice object with id, total, and due_date populated.

    Raises:
        ValueError: If line_items is empty or any amount is not positive.
        CustomerNotFoundError: If no customer exists with the given customer_id.
    """
```

### Generating Endpoint Reference Docs (Markdown)

**Prompt:**

```
Write Markdown endpoint reference documentation for these routes. 
For each endpoint include: HTTP method and path, description, 
authentication requirements, request parameters (path, query, body), 
response schema, error codes, and a curl example.
```

Claude generates structured Markdown that can go directly into a docs site, GitHub wiki, or developer portal.

## Tips for Best Results

**Paste schemas alongside routes.** If your routes reference Pydantic models or TypeScript interfaces, include those too. Claude generates accurate schemas from them rather than guessing field types.

**Ask for error documentation explicitly.** Documentation often skips the error cases. Add "document all error responses including status codes, error codes, and when they occur" to your prompt.

**Request multi-language examples.** "Include code examples in curl, Python (using httpx), and JavaScript (using fetch)" gets you examples your users actually want.

**Use Claude Code for living documentation.** Set up a `docs:generate` script that runs Claude Code against your routes directory and regenerates the OpenAPI spec. Documentation stays in sync with the code automatically.

## Related Claude Guides

- [Claude Code Getting Started](/claude-code-getting-started/)
- [Claude Python Scripting](/claude-python-scripting/)
- [Claude API Getting Started](/claude-api-getting-started/)
- [Debug Code with Claude](/debug-code-with-claude/)
- [Claude Code Reviews](/claude-code-reviews/)
