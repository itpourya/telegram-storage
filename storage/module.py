import time
import json
from telethon import TelegramClient
from python_socks import ProxyType
from telethon.errors import FloodWaitError
from storage.utils import merge


class Storage:
    def __init__(self, api_hash, api_id, token, phone_number :str, channel_id :int) -> None:
        self.phone_number = phone_number
        self.channel_id = channel_id
        self.api_hash = api_hash
        self.api_id = api_id
        self.token = token
        self.session = TelegramClient("session", api_id, api_hash,  proxy=(ProxyType.SOCKS5, '127.0.0.1', 12334))

    async def add(self, model_name, data: str) -> bool :
        await self.session.start(phone=self.phone_number)
        all_table = await self.get_all(model_name)
        print(all_table)
        if all is not None:
            jsonData = json.loads(data)
            msg = merge(all_table, jsonData)
            async with self.session:
                await self.session.send_message(self.channel_id, model_name + str(msg))
                return True

        async with self.session:
            await self.session.send_message(self.channel_id, model_name+str(data))
            return True

    async def get_all(self, model_name :str) -> str:
        await self.session.start(phone=self.phone_number)
        async with self.session:
            try:
                channel = await self.session.get_entity(self.channel_id)

                async for message in self.session.iter_messages(channel, limit=100):
                    if model_name in message.text:
                        data = json.loads(message.text.replace(model_name, ""))
                        return data

            except FloodWaitError as e:
                print(f"Rate limited. Sleeping for {e.seconds} seconds.")
                time.sleep(e.seconds)
        return ""