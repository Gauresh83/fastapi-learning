from pydantic  import BaseModel,Field,AnyUrl,EmailStr,FieldValidationInfo,field_validator,model_validator
from typing import Optional,List ,Dict,Annotated
class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:Optional[bool]
    allergies:List[str]
    contact_details:Dict[str,str]
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age >60 and 'emergency ' not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact in their contact details.")
        return model



def update_patient_data(existing_patient:Patient):
    print(existing_patient.name)
    print(existing_patient.age)
    print(existing_patient.weight)
    print(existing_patient.married)
    print(existing_patient.allergies)
    print(existing_patient.contact_details)
    print("Patient data updated successfully.")
def create_patient_data(new_patient:Patient):
    print(new_patient.name)
    print(new_patient.age)
    print(new_patient.weight)
    print(new_patient.married)
    print(new_patient.allergies)
    print(new_patient.contact_details)
    print("Patient data created successfully.")
patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
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
create_patient_data(patient1)