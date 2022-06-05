from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello, i am alive"

@app.post("/preduct")
async def predict(
    file: UploadFile = File()
):
    pass
    
        

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port='8000')
