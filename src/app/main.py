from fastapi import FastAPI
from api.controllers import auth_controller, producao_controller

app = FastAPI()

app.include_router(auth_controller.router)
app.include_router(producao_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)