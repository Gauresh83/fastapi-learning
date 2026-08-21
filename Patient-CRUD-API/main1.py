from fastapi import FastAPI
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