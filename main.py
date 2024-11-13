import asyncio
from storage import module
from pydantic import BaseModel
import json

api_hash = "520c4df78f2953fcdba322e1bed1cf83"
api_id = "23217360"
token = "7210394912:AAGInvfYt_iYpcKQlPYQffsi8YARjPDx6eg"
channel = -1002273847906
phone_number = "+989981628575"

class User(BaseModel):
    Model: str
    Username: str
    Password: str

async def main():
    client = module.Storage(api_hash=api_hash, api_id=api_id, token=token, phone_number=phone_number,
                            channel_id=channel)
    first_user = User(Model="Users", Username="pourya", Password="1235")
    status = await client.add(model_name="user", data=first_user.json())
    status = await client.get_all("user")
    print(status)

asyncio.run(main())