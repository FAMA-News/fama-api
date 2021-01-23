'''
app.py

CREATED:   22.01.2021 4:7
EDITED:    22.01.2021 4:7
PROJECT:   fama_processing
AUTHOR:    Noah Kamara (developer@noahkamara.com)
LICENSE:   Mozilla Public License 2.0
COPYRIGHT: Noah Kamara
'''


import uvicorn
from fastapi import FastAPI, Cookie, Depends
from data import Data
from routers import *

OPEN_API = Data.load("openapi.json")


# App
app = FastAPI(
    debug=True,
    title="FAMA API",
    description="",
    version="1.0.0",
    openapi_tags=OPEN_API,
)


# ROUTERS
# System Router
app.include_router(
    system_router,
    prefix="/api/system",
    tags=["System Status"],
    dependencies=[],
    responses={404: {"description": "Not found"}}
)


# Feed & Entries
app.include_router(
    feed_router,
    prefix="/api/feed",
    tags=["Feed & Entries"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)


