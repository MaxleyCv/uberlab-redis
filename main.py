from fastapi import FastAPI

from operators import DataController

app = FastAPI()


@app.get("/")
async def root():
    controller = DataController()
    result = controller.start_populating()
    return {'message': result}
