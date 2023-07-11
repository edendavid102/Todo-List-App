from fastapi import APIRouter

from config.database import db
from models.task import Task
router = APIRouter(
    prefix="/task"
)

collection_name = db["tasks"]


@router.get("/")
def get_tasks():
    documents = collection_name.find({})
    # Convert ObjectId to string
    documents = [{**doc, "_id": str(doc["_id"])} for doc in documents]
    return documents


@router.post("/")
async def create_task(task: Task):
    collection_name.insert_one(dict(task))


# @router.post("/")
# def create_task(request: Request, task: Task):
#     task = jsonable_encoder(task)
#     new_book = collection.insert_one(task)
#     # created_book = request.app.database["books"].find_one(
#     #     {"_id": new_book.inserted_id}
#     )
#
#     return created_book

# @router.get("",
#             summary="Get Tasks"
#             )
# def get_accounts(request: Request):
#     logger.info("Fetching accounts with query params")
#     condition_dict = dict(request.query_params)
#
#     try:
#         accounts = select(table_name=table_name, condition_dict=condition_dict)
#         return accounts
#
#     except Exception:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

