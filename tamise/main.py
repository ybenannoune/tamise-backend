import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tamise.config import settings
from tamise.database import Base, engine
from tamise.routers import auth, order, user


def run_app(args=None):
    uvicorn.run("tamise.main:app", port=8000, log_level="info", host="localhost", reload=True)


app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["Auth"], prefix="/api/auth")
app.include_router(user.router, tags=["Users"], prefix="/api/users")
app.include_router(order.router, tags=["Orders"], prefix="/api/order")


@app.get("/api/healthchecker")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    Base.metadata.create_all(engine)
