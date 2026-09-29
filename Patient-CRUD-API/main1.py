from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Optional,Literal
from fastapi.responses import JSONResponse
import json
app=FastAPI()
class Patient(BaseModel):
    id:Annotated[str,Field(...,description="The ID of the patient",example="P001")]
    name:Annotated[str,Field(...,description="The name of the patient",example="John Doe")]
    city:Annotated[str,Field(...,description="The city of the patient",example="New York")]
    age:Annotated[int,Field(...,gt=0,lt=120,description="The age of the patient",example=30)]
    gender:Annotated[Literal["Male","Female",'others'],Field(...,description="The gender of the patient",example="Male")]
    height:Annotated[float,Field(...,gt=0,description="The height of the patient in meters",example=1.75)]
    weight:Annotated[float,Field(...,gt=0,description="The weight of the patient in kilograms",example=70.5)]
    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Underweigth"
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi <30:
            return 'Normal'
        else:
            return 'Obese'
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data
def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)
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
@app.post('/create')
def create_patient(patient:Patient):
    #load existing data
    data=load_data()
    #check if the patient already exixts
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exists')
    
    #new patient add to the database
    data[patient.id]=patient.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code=201,content={'message':'patient created successfully'})
@app.put('/edit/{patient_id}')
def update_patient(patient_id:str,patient_update:PatientUpdate):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Patient not found')
    existing_patient_info= data[patient_id]
    update_patient_info=patient_update.model_dump(exclude_unset=True)
    for key ,value in update_patient_info.items():
        existing_patient_info[key]=value

    patient_pydantic_obj =Patient(**existing_patient_info)
    # pydantic object ->dict
    existing_patient_info=patient_pydantic_obj.model_dump(exclude='id')
    #add this dict to value
    data[patient_id]=existing_patient_info
    save_data(data)
    return JSONResponse(status_code=200,content={'message':'patient update'})

    
