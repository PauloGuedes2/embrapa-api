import uvicorn

from api.controllers.production_controller import app


class App:
    def __init__(self, host: str = "0.0.0.0", port: int = 8000):
        self.host = host
        self.port = port

    def run(self):
        uvicorn.run(app, host=self.host, port=self.port)

if __name__ == "__main__":
    application = App()
    application.run()