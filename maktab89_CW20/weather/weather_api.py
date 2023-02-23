from fastapi import FastAPI, HTTPException, status
import uvicorn


app = FastAPI()

API_KEY = "d65b2383484c4cb193c125648232302"
@app.get('/weather')
def get_task():
    return {"task": ''}


if __name__ == "__main__":
    uvicorn.run(f'{__name__}:app', reload=True)
