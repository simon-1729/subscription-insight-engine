from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/mission/{name}")
def say_hello(name: str):
    return {"message": f"{name}, your mission is to explore strange new code, to seek out new infrastructure, to boldly deploy where no developer has deployed before"}