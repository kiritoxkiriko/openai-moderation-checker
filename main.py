import os

from fastapi import FastAPI
from util import check_moderation, get_res, PASSCODE

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is a OpenAI Moderation Checker."}


@app.get("/check/{text}")
async def moderation(text: str, passcode: str, origin: bool = False):
    if passcode != PASSCODE:
        return {"message": "Passcode is incorrect"}
    return {"text": text, "result": check_moderation(text) if origin else get_res(check_moderation(text))}
