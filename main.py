from infrastructure.injector import Injector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.controllers import (send_single_email_controller,
                                        save_purchase_controller,
                                        send_bulk_email_controller,
                                        get_all_emails_sent_controller)

app = FastAPI()
injector = Injector()
app.container = injector

app.include_router(send_single_email_controller.router)
app.include_router(save_purchase_controller.router)
app.include_router(send_bulk_email_controller.router)
app.include_router(get_all_emails_sent_controller.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)