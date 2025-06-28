from fastapi import HTTPException

def http_500_error(exc: Exception):
    return HTTPException(status_code=500, detail=f"Internal server error: {exc}")
