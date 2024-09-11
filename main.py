from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.controllers import send_single_email_controller

app = FastAPI()


app.include_router(send_single_email_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)