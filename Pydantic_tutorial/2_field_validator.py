from pydantic  import BaseModel,Field,AnyUrl,EmailStr,FieldValidationInfo,field_validator
from typing import Optional,List ,Dict,Annotated
class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:Optional[bool]
    allergies:List[str]
    contact_details:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=["hdfc.com","gmail.com","yahoo.com","icici.com"]
        #abc@gmail.com
        domain_name=value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Invalid email domain: {domain_name}. Allowed domains are: {valid_domains}")
        return value
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
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
        "address": "123 Main St, Anytown, USA"
    }
}
patient1=Patient(**patient_info)
update_patient_data(patient1)
create_patient_data(patient1)