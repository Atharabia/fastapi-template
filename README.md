# fastapi-template

A [pyportion](https://github.com/Atharabia/pyportion) template for scaffolding Python FastAPI projects.

## Structure

```
fastapi-template/
├── base/                        # Main application source
│   ├── app/
│   │   ├── __init__.py          # FastAPI app with lifespan
│   │   ├── __main__.py          # Entry point (uvicorn)
│   │   ├── api/                 # Route definitions
│   │   │   └── health.py        # GET /health
│   │   ├── controller/          # Business logic layer
│   │   │   └── user.py          # UserController (CRUD)
│   │   ├── database/            # SQLModel engine & session
│   │   │   └── tables.py        # UserTable definition
│   │   ├── dependencies/        # FastAPI dependencies
│   │   │   └── auth.py          # JWT & OAuth2 auth
│   │   ├── middleware/          # Middleware registry
│   │   │   └── cors.py          # CORS (enabled in debug mode)
│   │   ├── models/
│   │   │   ├── schemas/         # Request / input models
│   │   │   └── responses/       # Response models
│   │   ├── external/            # Third-party integrations
│   │   ├── settings/            # Config via pydantic-settings
│   │   ├── templates/           # HTML templates (Jinja2)
│   │   └── utils/               # Logger & helpers
│   ├── pyproject.toml
│   └── .pre-commit-config.yaml
│
├── .portions/                   # Pyportion boilerplate templates
│   ├── controller.py
│   ├── router.py
│   ├── schema.py
│   ├── response.py
│   └── external.py
└── .pyportion.yml               # Pyportion scaffold configuration
```
