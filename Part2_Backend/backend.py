import uvicorn
from fastapi import FastAPI
import pandas as pd
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

df = None
verbose = False


@asynccontextmanager
async def lifespan(app: FastAPI):
    global df
    df = pd.read_csv("./Part2_Backend/US_cities_2022.csv")
    if verbose:
        print(df.head())
    yield


app = FastAPI(lifespan=lifespan)
# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def root():
    return {"message": "This is a web map application"}


@app.get("/cities")
async def get_cities():
    global df
    return df.to_dict(orient="records")


if __name__ == "__main__":
    uvicorn.run("backend:app", host="localhost", port=8000, reload=False)
