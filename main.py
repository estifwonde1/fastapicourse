from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
  return{"message": "hello from wsl ubunutu world","just so i can commit am really tired","another day another comment the streak must continuex rule number 1 consistency always matters no matter how tired u are","misssed my streak god dammmit"}
