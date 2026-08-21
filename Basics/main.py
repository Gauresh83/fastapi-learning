from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message":"My FastAPI Learning Journey"}
@app.get("/about")
def about():
    return {"message":"This is a FastAPI application created for learning purposes."}
