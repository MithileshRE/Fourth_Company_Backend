from fastapi import FastAPI,Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from typing import Union
import uvicorn
from celery_ser import add

app = FastAPI()
auth_scheme = HTTPBearer()


VALID_TOKEN = "supersecrettoken"

def validate_token(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return credentials.credentials


@app.get("/")
def read_root(token: str = Depends(validate_token)):
    result = add.delay(4, 6)  # Runs the task in the background
    return {"Task_ID": result.id,
            "Result:": result.get(timeout=10)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__=="__main__":
    uvicorn.run(app)