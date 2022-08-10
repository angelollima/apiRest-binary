from typing import ItemsView
import uvicorn
from fastapi import FastAPI
import string
import json

app = FastAPI()

*teste, = string.ascii_lowercase
*lista, = "".join(c + c.upper() for c in teste)

items = {}

@app.get("/")
async def root():
    for i in lista:
        key = i
        value = f"{ord(i):08b}"
        items[key] = value
    return {"items":[items]}
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)