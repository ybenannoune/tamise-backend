import uvicorn
from fastapi import FastAPI, exceptions
from fastapi.middleware.cors import CORSMiddleware
from tamise.config import settings
from tamise.database import Base, engine
from tamise.routers import auth, dish, menu, order, user


def run_app(args=None):
    uvicorn.run("tamise.main:app", port=8000, log_level="info", host="localhost", reload=True)


app = FastAPI()

# @app.exception_handler(exceptions.RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return {"detail": exc.errors(), "body": exc.body}


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


@app.get("/api/healthchecker")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    Base.metadata.create_all(engine)
