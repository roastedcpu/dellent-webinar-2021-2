import uuid
import time
from fastapi import FastAPI


class GlobalContext:
    pass


app = FastAPI()
GlobalContext.instance_uuid = uuid.uuid4()
GlobalContext.n_calls = 0

@app.get("/")
async def root():
    GlobalContext.n_calls = GlobalContext.n_calls + 1
    time.sleep(0.1 * GlobalContext.n_calls)
    return {"message": "Hello World", 'instanceUUID': str(GlobalContext.instance_uuid)}
