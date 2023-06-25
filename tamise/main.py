import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tamise.config import settings
from tamise.database import Base, engine
from tamise.routers import auth, contact, dish, menu, order, user

app = FastAPI()
origins = [str(origin) for origin in settings.CLIENT_ORIGIN.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["Auth"], prefix=f"{settings.API_PREFIX}/auth")
app.include_router(user.router, tags=["Users"], prefix=f"{settings.API_PREFIX}/users")
app.include_router(
    order.router, tags=["Orders"], prefix=f"{settings.API_PREFIX}/orders"
)
app.include_router(dish.router, tags=["Dishs"], prefix=f"{settings.API_PREFIX}/dishs")
app.include_router(menu.router, tags=["Menu"], prefix=f"{settings.API_PREFIX}/menu")
app.include_router(
    contact.router, tags=["Comment"], prefix=f"{settings.API_PREFIX}/contact"
)


@app.get("/api/test")
def root():
    return {"message": "Hello World"}


def run_app(args=None):
    uvicorn.run(
        "tamise.main:app", port=8000, log_level="info", host="0.0.0.0", reload=True
    )
