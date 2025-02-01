from fastapi import FastAPI, Query, HTTPException
from typing import Optional
import json

app = FastAPI()

# Load data from the JSON file
with open('q-vercel-python.json') as f:
    data = json.load(f)

# Helper function to find data by name
def find_data_by_name(name: str):
    return next((item for item in data if item['name'] == name), None)

@app.get("/api")
def get_data(name1: str = Query(...), name2: Optional[str] = Query(None)):
    result = {}

    data1 = find_data_by_name(name1)
    if data1:
        result['name1_data'] = data1
    else:
        raise HTTPException(status_code=404, detail=f"Data for name '{name1}' not found")

    if name2:
        data2 = find_data_by_name(name2)
        if data2:
            result['name2_data'] = data2
        else:
            raise HTTPException(status_code=404, detail=f"Data for name '{name2}' not found")

    return result
