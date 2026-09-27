from pydantic import BaseModel, ValidationError, Field
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
address_dict = {"city": "New York", "state": "NY", "street": "123 Main St", "zip_code": "10001"}
patient_info = {
    "name": "John Doe",
    "gender": "Male",
    "age": 30,
    "address": address_dict
}
patient = Patient(**patient_info)
print(patient)
print(patient.address.city)  # Accessing nested model attribute
print(patient.address.zip_code)  # Accessing nested model attribute
