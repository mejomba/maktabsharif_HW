from fastapi import FastAPI, Response, Request, status, Form, Body
from pydantic import BaseModel, EmailStr
from utils import write_file, read_file
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    first_name: str
    last_name: str
    phone: int
    email: EmailStr


@app.get('/create_user')
def create_user(first_name: str, last_name: str, phone: int, email: EmailStr):
    data = {'first_name': first_name, 'last_name': last_name, 'phone': phone, 'email': email}
    write_file(data)
    return {'data': 'success'}


@app.get('/info/{email}')
def get_info(request: Request, email: EmailStr):
    result = []
    data = read_file()
    for first_name, last_name, phone, email_ in data:
        if email == email_:
            result.append([first_name, last_name, phone, email_])
    return templates.TemplateResponse('info.html', {'request': request, 'data': result}, status_code=status.HTTP_200_OK)


@app.get('/list')
def get_phone_list(request: Request):
    result = []
    data = read_file()
    for first_name, last_name, phone, email_ in data:
        result.append([first_name, last_name, phone, email_])
    return templates.TemplateResponse('list.html', {'request': request, 'data': result}, status_code=status.HTTP_200_OK)
