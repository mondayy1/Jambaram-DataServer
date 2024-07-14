from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load('./test_model.pkl')

@app.get('/')
async def root():
    return {'message': 'Hello World!'}

