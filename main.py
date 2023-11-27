from fastapi import FastAPI
import pickle
import random
import uvicorn
from FootballPlayers import FootballPlayer
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()
model = pickle.load(open('classifier.pkl', 'rb'))

pos_dict = {0:'Goalkeeper', 1:'Defender', 2:'Midfielder', 3:'Forward'}


@app.get('/')
async def root():
    return {'message': 'Football Player Position Predictor API'}


@app.post('/position/predict')
def predict_position(data:FootballPlayer, pos_dict):
    data = data.model_dump()

    Age = data['Age']
    MP = data['MP']
    Starts = data['Starts']
    Min = data['Min']
    nineties = data['nineties']
    Gls = data['Gls']
    Ast = data['Ast']
    GA = data['GA']
    GnoPK = data['GnoPK']
    PK = data['Pk']
    PKatt = data['PKatt']
    CrdY = data['CrdY']
    CrdR = data['CrdR']
    xG = data['xG']
    npxG = data['npxG']
    xAG = data['xAG']
    npxGxAG = data['npxGxAG']
    PrgC = data['PrgC']
    PrgP = data['PrgP']
    PrgR = data['PrgR']

    prediction = model.predict([[Age, MP, Starts, Min, nineties, Gls, Ast, GA, GnoPK, PK, PKatt, CrdY, CrdR, xG, npxG, xAG, npxGxAG, PrgC, PrgP, PrgR]])

    prediction = int(prediction[0])

    prediction = pos_dict.get(prediction)

    return {'prediction': prediction}


@ app.get("/figures/{figure_name}")
def get_figure(figure_name: str):
    figure_path = Path("C:/Users/laure/Documents/APITestTechonomy") / figure_name
    return FileResponse(figure_path, media_type="image/png")


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
