from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from service.url_short_service import short_url, tiny_url

app = FastAPI()


@app.post("/return_a_tinyurl")
def return_a_tinyurl(url: str):
    shorted_url = tiny_url(url)
    return JSONResponse(
        content={"new_url": shorted_url}, status_code=status.HTTP_200_OK
    )


@app.post("/short_url")
def return_short_url(url: str):
    # recebe uma url, salva ela no banco com uma encurtada como referencia
    # com um prazo de validade.
    shorted_url = short_url(url)
    return JSONResponse(
        content={"new_url": shorted_url}, status_code=status.HTTP_200_OK
    )


@app.get("/normal_url_by_short")
def return_normal_url_by_short(url: str):
    # ao receber uma url encurtada, devo redirecionar pra url "original"
    ...