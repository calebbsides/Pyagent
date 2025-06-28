## Adding New Endpoints

To add a new API endpoint to Pyagent, follow these steps:

1. **Create the Endpoint Module**
   - Add a new Python file in `pyagent/api/v1/endpoints/`, e.g., `example.py`.
   - Define your FastAPI route(s) in this file.
   - Example:
     ```python
     from fastapi import APIRouter

     router = APIRouter()

     @router.get("/example")
     async def get_example():
         return {"message": "This is an example endpoint."}
     ```

2. **Register the Router**
   - In `pyagent/api/v1/__init__.py`, import and include your new router:
     ```python
     from .endpoints import example
     from fastapi import APIRouter

     router = APIRouter()
     router.include_router(example.router)
     # ...include other routers as needed
     ```

3. **Include the Versioned Router in the App**
   - In `pyagent/app.py`, ensure the versioned API router is included:
     ```python
     from pyagent.api.v1 import router as v1_router
     app.include_router(v1_router, prefix="/v1")
     ```

4. **Test Your Endpoint**
   - Run the app:
     ```bash
     uvicorn pyagent.main:app --reload
     ```
   - Test your endpoint:
     ```bash
     curl http://127.0.0.1:8000/v1/example
     ```

5. **(Optional) Add Models and Services**
   - Place Pydantic models in `pyagent/models/` if needed.
   - Add business logic in `pyagent/services/` as appropriate.

---

**Example: Adding a `/hello` endpoint**

1. Create `pyagent/api/v1/endpoints/hello.py`:
   ```python
   from fastapi import APIRouter

   router = APIRouter()

   @router.get("/hello")
   async def say_hello():
       return {"message": "Hello, world!"}
   ```
2. Register in `pyagent/api/v1/__init__.py`:
   ```python
   from .endpoints import hello
   router.include_router(hello.router)
   ```
3. Access at: `http://127.0.0.1:8000/v1/hello`

---

See the `weather.py` endpoint for a complete example.
