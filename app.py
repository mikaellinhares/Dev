from fastapi import FastAPI


app = FastAPI()


@app.get("/api/v1/hello-world")
def hello_world():
    return "Hello World"
