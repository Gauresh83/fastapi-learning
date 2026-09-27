from pydantic  import BaseModel,Field,AnyUrl,EmailStr
from typing import Optional,List ,Dict,Annotated
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Name of the paatient",description="This field is used to store the name of the patient")]
    age:int =Field(ge=0,le=120)
    weight:float =Annotated[float,Field(gt=0,strict=True)]
    married:Annotated[bool,Field(default=None,description="This field is used to store the marital status of the patient")]
    linkedin:Optional[AnyUrl] = Field(default=None)
    allergies:Optional[List[str]] = Field(default=None)
    email:EmailStr = Field(default=None)
    contact_details:Dict[str,str] = Field(default=None)
def update_patient_data(existing_patient:Patient):
    print(existing_patient.name)
    print(existing_patient.age)
    print(existing_patient.weight)
    print(existing_patient.married)
    print(existing_patient.linkedin)
    print(existing_patient.allergies)
    print(existing_patient.contact_details)
    print("Patient data updated successfully.")
def create_patient_data(new_patient:Patient):
    print(new_patient.name)
    print(new_patient.age)
    print(new_patient.weight)
    print(new_patient.married)
    print(new_patient.linkedin)
    print(new_patient.allergies)
    print(new_patient.contact_details)
    print("Patient data created successfully.")
patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
    "linkedin": "https://www.linkedin.com/in/johndoe",
    "married": True,
    "email": "john.doe@example.com",
    "allergies": ["Peanuts"],
    "contact_details": {"phone": "123-456-7890"}
}
patient1=Patient(**patient_info)
update_patient_data(patient1)
create_patient_data(patient1)