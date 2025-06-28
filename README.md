# Pyagent

Pyagent is a modern Python agent framework that leverages FastAPI, Google Gemini, and function/tool calling to build intelligent, extensible APIs. It is designed for rapid prototyping and production use, with a clean, maintainable structure.

## Features

- **FastAPI**: High-performance, easy-to-use web framework for building APIs.
- **Google Gemini**: Integrates with Gemini for advanced language and function-calling capabilities.
- **Tool/Function Calling**: Easily register and expose Python functions as callable tools for the LLM.
- **Modular Structure**: All code is organized under the `pyagent/` package for clarity and maintainability.

## Project Structure

- `pyagent/` - Main package
  - `main.py` - Entrypoint (loads config, imports app)
  - `app.py` - FastAPI app instance and router includes
  - `api/` - API versioning and endpoints
    - `v1/endpoints/` - Version 1 endpoints (e.g., `weather.py`)
  - `core/` - Configuration and error handling (e.g., `config.py`, `errors.py`)
  - `services/` - Business logic and function invocation (e.g., `gemini_service.py`, `invoke.py`)
  - `clients/` - External service clients (e.g., Gemini)
  - `tools/` - Tool and function definitions (e.g., weather)
  - `models/` - Pydantic models for API responses
  - `http/` - HTTP request examples for development/testing
- `tests/` - Automated tests
- `README.md` - Project documentation

## Setup Instructions

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
   - You will need a Google Gemini API key. Get it here: https://aistudio.google.com/apikey

5. **Run the app**
   ```bash
   uvicorn pyagent.main:app --reload
   ```
   - The API will be available at http://127.0.0.1:8000
   - Interactive docs: http://127.0.0.1:8000/docs


## Example Usage

You can test the weather endpoint with:
```bash
curl http://127.0.0.1:8000/v1/weather
```

## Running Tests

To run all automated tests, use:
```bash
venv/bin/pytest tests/
```
This will discover and run all tests in the `tests/` directory using your virtual environment.

## Notes

- All new code should go under the `pyagent/` package.
- Endpoints are versioned under `api/v1/endpoints/` for scalability.
- Business logic and function invocation are in `services/`.
- Configuration and error handling are in `core/`.
- Data models are in `models/`.
- Use `services/invoke.py` to register new callable tools/functions for Gemini.
- Add new tests in the `tests/` directory.

**Pyagent** is designed for extensibility—add your own tools, clients, and endpoints as needed!

## Adding New Endpoints

See `ADDING_ENDPOINTS.md` for step-by-step instructions and examples on how to add new API endpoints to Pyagent.
