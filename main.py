from fastapi import FastAPI
from typing import Union
import uvicorn
from celery_ser import add

app = FastAPI()


@app.get("/")
def read_root():
    result = add.delay(4, 6)  # Runs the task in the background
    return {"Task_ID": result.id,
            "Result:": result.get(timeout=10)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__=="__main__":
    uvicorn.run(app)