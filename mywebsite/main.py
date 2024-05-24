
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles

app= FastAPI()
templates=Jinja2Templates(directory="template")
app.mount("/assets",StaticFiles(directory="assets"), name="assets")

@app.get('/')
def root(request: Request):
    return templates.TemplateResponse("from.html",{'request', request})