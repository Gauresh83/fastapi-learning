from pydantic import BaseModel, ValidationError, Field
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
class Patient(BaseModel):
    name:str
    gender:str='male'
    age:int
    address:Address
address_dict = {"city": "New York", "state": "NY", "street": "123 Main St", "zip_code": "10001"}
patient_dict= {
    "name": "John Doe",
    "age": 30,
    "address": address_dict
}
patient = Patient(**patient_dict)
print(patient)
# temp=patient.model_dump() it returns a dictionary representation of the model instance, which can be useful for serialization or storage purposes.
# temp=patient.model_dump_json() it returns a JSON string representation of the model instance, which can be useful for serialization or storage purposes.
# temp=patient.model_dump(mode='json') # it returns a dictionary representation of the model instance
# temp=patient.model_dump(include={'name','age'}) # it returns a dictionary representation of the model instance with only the specified fields included.
# temp=patient.model_dump(exclude={'address'}) # it returns a dictionary representation of the model instance with the specified fields excluded.
temp=patient.model_dump(exclude_unset=True) # it returns a dictionary representation of the model instance with only the fields that have been explicitly set included it does not include fields that were not explicitly set wgile making patient_dict the gender were not  set  so if export our model gender not appear.
print(temp)
print(type(temp)) 