from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Added CORS middleware
from typing import List, Optional
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

with open('q-vercel-python.json') as f:
    data = json.load(f)

# Fixed the generator expression to return the correct data
def find_data_by_name(name: str):
    return next((item['marks'] for item in data if item['name'] == name), None)

@app.get("/api")
def get_data(name: List[str] = Query(...)):
    result = []
    for n in name:
        data_item = find_data_by_name(n)  # Corrected from 'name' to 'n'
        if data_item is not None:  # Check if data exists
            result.append(data_item)
        else:
            raise HTTPException(status_code=404, detail=f"Data for name '{n}' not found")
    
    return {
        "marks": result
    }
