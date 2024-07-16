from fastapi import FastAPI
from pydantic import BaseModel 

# object 



# endpoint 
@app.get("/home")
def get_home():
    return {"data": "Hello World!"}

# to raise our site we should use uvicorn
# terminal: uvicorn main:app --reload 
# "--reload" - allows us to change the site page automaticaly 