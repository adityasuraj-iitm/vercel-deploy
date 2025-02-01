from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional  # Added List import
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
        data_item = find_data_by_name(n)  # Corrected from 'name' to 'n'
        if data_item:  # Check if data exists
            result.append(data_item)
        else:
            raise HTTPException(status_code=404, detail=f"Data for name '{n}' not found")
    
    return {
        "marks": result
    }
