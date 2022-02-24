from fastapi import FastAPI
from movies.router import movie_router

app = FastAPI()

app.include_router(movie_router.movie_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
