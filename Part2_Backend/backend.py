import uvicorn
import pandas as pd
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

df = None
verbose = False


# Load data at the start of the application
@asynccontextmanager
async def lifespan(app: FastAPI):
    global df
    df = pd.read_csv("./Part2_Backend/US_cities_2022.csv")
    if verbose:
        print(df.head())
    yield


# Create FastAPI instance
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


# Get all cities
@app.get("/cities")
async def get_cities():
    global df
    return df.to_dict(orient="records")


if __name__ == "__main__":
    # Run the FastAPI application
    uvicorn.run("backend:app", host="localhost", port=8000, reload=False)
