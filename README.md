
# Pyagent

Pyagent is a modular Python framework for building intelligent APIs with FastAPI and Google Gemini. It supports function/tool calling, easy extensibility, and rapid prototyping for LLM-powered applications.

---

## Features

- **FastAPI** for high-performance, async API development
- **Google Gemini** integration for LLM and function-calling
- **Tool/Function Calling**: Register Python functions as tools callable by Gemini
- **Modular Structure**: All code under the `pyagent/` package for maintainability
- **Automated Testing**: Pytest-based suite for endpoints and logic

---

## Project Structure

```
pyagent/
  __main__.py           # CLI entrypoint
  main.py               # Entrypoint: loads config, imports app
  app.py                # FastAPI app instance, router includes
  api/
    v1/
      endpoints/        # Version 1 endpoints (e.g., chat.py)
  core/                 # Config and error handling
  services/             # Business logic, Gemini invocation
  clients/              # External service clients (e.g., Gemini)
  tools/                # Tool/function definitions (e.g., weather)
  models/               # Pydantic models for API
tests/                  # Automated tests
README.md               # Project documentation
ADDING_ENDPOINTS.md     # Guide for adding endpoints
requirements.txt        # Python dependencies
```

---

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/calebbsides/Pyagent.git
   cd Pyagent
   ```
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables**
   - Copy `.env.sample` to `.env` and fill in your values.
   - You need a Google Gemini API key: https://aistudio.google.com/apikey
5. **Run the app**
   ```bash
   uvicorn pyagent.main:app --reload
   ```
   - API: http://127.0.0.1:8000
   - Docs: http://127.0.0.1:8000/docs

---

## API Endpoints

### POST `/v1/post-message`
- **Request:** `{ "message": "Hello LLM!" }`
- **Response:** `{ "response": "..." }`
- Returns a Gemini-generated response to the message.

---

## Tool/Function Calling

- Register new callable tools in `pyagent/tools/`.
- Expose them via `pyagent/services/invoke.py`.
- Gemini can call registered Python functions as tools during chat.

---

## Testing

Run all tests:
```bash
venv/bin/pytest tests/
```
- Tests use FastAPI's `TestClient` and pytest's `monkeypatch` for mocking LLM responses.

---

## Extending the Project

- Add new endpoints in `pyagent/api/v1/endpoints/`.
- Register routers in `pyagent/api/v1/__init__.py`.
- Add business logic in `services/` and models in `models/`.
- See `ADDING_ENDPOINTS.md` for step-by-step instructions.

---

## Notes

- All code is under the `pyagent/` package.
- Endpoints are versioned for scalability.
- Use `.env` for secrets and API keys.

---

**Pyagent** is designed for extensibility—add your own tools, clients, and endpoints as needed!
