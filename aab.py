from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="aa")

@app.get("/{name}")
async def root(request: Request,name:str):
    return name



@app.get("/}")
async def root(request: Request):
    return ''



