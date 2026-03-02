#pip install fastapi strawberry-graphql uvicorn
#python main.py

import uuid
from typing import List

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

devices_db = []

@strawberry.type
class Device:
    id: strawberry.ID
    serial: str

@strawberry.type
class Query:
    @strawberry.field
    def devices(self) -> List[Device]:
        return devices_db

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_device(self, serial: str) -> Device:
        new_id = str(uuid.uuid4())
        device = Device(id=new_id, serial=serial)
        devices_db.append(device)
        return device

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8246)