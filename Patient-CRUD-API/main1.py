from fastapi import FastAPI, HTTPException,Path
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