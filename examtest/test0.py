
from typing import Optional
from fastapi import FastAPI
from fastapi import UploadFile, File
from PIL import Image
from io import BytesIO
from tensorflow.keras.models import load_model
import numpy as np
import os


# 모델 불러오기
print(os.getcwd())
# model_path = './checkpoints'
# model = load_model(model_path)
# input_shape = model.layers[0].input_shape

app = FastAPI()

@app.get("/")
def root():
    return {"error": "use GET /prediction instead of root route"}
    # # 데이터 준비
    # # 여기서 어떻게든 Image 데이터를 받아보자. 아마 POST 방식으로 받아올 것이다.
    # image = getting_image()

    # # 예측 및 반환
    # # 받아온 이미지를 불러온 모델에 입력으로 주면 될것이다.
    # result = model(image)

    # return {"result": result}


@app.post('/prediction')
async def prediction_route(file: UploadFile = File(...)):
    #데이터 준비
    contents = await file.read()
    pil_image = Image.open(BytesIO(contents))
    pil_image = pil_image.resize((input_shape[1], input_shape[2]))
    pil_image = pil_image.convert('L')
		
    numpy_array = np.array(pil_image)
    numpy_array = np.expand_dims(numpy_array, axis=-1)   # (28, 28) to (28, 28, 1)
    numpy_array = numpy_image / 255.0

    if numpy_array.sum() > 200:
        numpy_array = 1 - numpy_array

    prediction_array = np.array([numpy_array])   # (28, 28, 1) to (1, 28, 28, 1)

	# 예측 및 반환
    predictions = model.predict(prediction_array)
    prediction = np.argmax(predictions[0])
    return {"result": int(prediction)}



for c in s:
    print(c)

    s = 'k'
    c = '0' 
    c = '123' 
    c = '12' 
    if c in "0123Xx":
        print(c)
    else:
        print("NOT")