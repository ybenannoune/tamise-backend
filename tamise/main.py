import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tamise.config import settings
from tamise.database import Base, engine
from tamise.routers import auth, contact, dish, menu, order, user

app = FastAPI()
origins = [settings.CLIENT_ORIGIN, "http://127.0.0.1:8000/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["Auth"], prefix="/api/auth")
app.include_router(user.router, tags=["Users"], prefix="/api/users")
app.include_router(order.router, tags=["Orders"], prefix="/api/orders")
app.include_router(dish.router, tags=["Dishs"], prefix="/api/dishs")
app.include_router(menu.router, tags=["Menu"], prefix="/api/menu")
app.include_router(contact.router, tags=["Comment"], prefix="/api/contact")


@app.get("/api/healthchecker")
def root():
    return {"message": "Hello World"}


def run_app(args=None):
    uvicorn.run("tamise.main:app", port=8000, log_level="info", host="0.0.0.0", reload=True)


def build_db(args=None):
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    run_app()
