from pydantic  import BaseModel,Field,AnyUrl,EmailStr,FieldValidationInfo,field_validator,model_validator,computed_field
from typing import Optional,List ,Dict,Annotated
class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:Optional[bool]
    allergies:List[str]
    contact_details:Dict[str,str]
    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi

def update_patient_data(existing_patient:Patient):
    print(existing_patient.name)
    print(existing_patient.age)
    print(existing_patient.weight)
    print('BMI',existing_patient.calculate_bmi)
    print(existing_patient.married)
    print(existing_patient.allergies)
    print(existing_patient.contact_details)
    print("Patient data updated successfully.")
patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
    "height": 1.75,
    "married": True,
    "email": "john.doe@hdfc.com",
    "allergies": ["penicillin", "shellfish"],
    "contact_details": {
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, USA",
        "emergency": "123-456-7890"
    }
}
patient1=Patient(**patient_info)
update_patient_data(patient1)
