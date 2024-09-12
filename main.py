from fastapi import FastAPI
from infrastructure.injector import Injector
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.controllers import send_single_email_controller,save_purchase_controller

app = FastAPI()


app.include_router(send_single_email_controller.router)
app.include_router(save_purchase_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)