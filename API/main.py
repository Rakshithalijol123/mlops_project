from pydantic import BaseModel
from fastapi import FastAPI
import joblib
app = FastAPI()


model = joblib.load("myModel")


class DataModel(BaseModel):
    sepal_length: float = 0.0
    sepal_width: float = 0.0
    petal_length: float = 0.0
    petal_width: float = 0.0


@app.post("/ml")
def predict_flower(data: DataModel):
    # 'sepal_length', 'sepal_width', 'petal_length', 'petal_width','species'
    data = dict(data)
    flower_type = model.predict([[
        data.get("sepal_length"),
        data.get("sepal_width"),
        data.get("petal_length"),
        data.get("petal_width")
    ]])
    print(flower_type)
    return {"flower_type": flower_type[0]}