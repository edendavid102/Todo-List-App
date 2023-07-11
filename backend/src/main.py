from fastapi import FastAPI

from routes.task import router

app = FastAPI()

# @app.on_event("shutdown")
# def shutdown_db_client():
#     app.mongodb_client.close()

app.include_router(router, prefix="/api/v1")
