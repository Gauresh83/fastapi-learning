from fastapi import FastAPI, HTTPException,Path, Query
import json

app = FastAPI()
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data
@app.get('/')
def home():
    return {"message": "My FastAPI Learning Journey"}
@app.get('/about')
def about():
    return {"message": "This is a FastAPI application created for learning purposes."}  


@app.get('/view')
def view():
    data=load_data()
    return data
@app.get('/patient/{patient_id}')
def view_patient(patient_id:str = Path(...,description="The ID of the patient to retrieve",examples="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found")
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc')):
    data=load_data()
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field selected from {valid_fields}')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order selected. Choose "asc" or "desc".')
    sort_order = True if order == 'desc' else False
    sorted_data= sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data
