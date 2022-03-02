import uvicorn
from fastapi import FastAPI
from movies.router import movie_router

app = FastAPI()

app.include_router(movie_router.movie_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
