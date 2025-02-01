from fastapi import FastAPI, Query, HTTPException
from typing import Optional
import json

app = FastAPI()

with open('q-vercel-python.json') as f:
    data = json.load(f)

def find_data_by_name(name: str):
    return next((item for item in data if item['name'] == name), None)

@app.get("/api")
def get_data(name: List[str] = Query(...)):
    result = []
    for n in name:
        data = find_data_by_name(name)
        result.append(data)
    return {
        "marks":result
    }
