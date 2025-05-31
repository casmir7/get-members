from telethon.sync import TelegramClient
import asyncio
import os

# Load API credentials securely from environment variables
api_id = int(os.getenv('TELEGRAM_API_ID', '0'))
api_hash = os.getenv('TELEGRAM_API_HASH', '')

async def scrape_group_members(group_link, session_name):
    async with TelegramClient(session_name, api_id, api_hash) as client:
        # Get the group entity
        entity = await client.get_entity(group_link)

        members = []
        async for member in client.iter_participants(entity):
            if member.username:
                members.append(member.username)

        print(f"Scraped {len(members)} members:")
        for username in members:
            print(username)

async def main():
    group_link = 'https://t.me/nnnn'  # Replace with your group link
    session_name = 'single_session'  # Session file name

    if api_id == 0 or not api_hash:
        print("ERROR: Please set TELEGRAM_API_ID and TELEGRAM_API_HASH environment variables.")
        return

    await scrape_group_members(group_link, session_name)

if __name__ == "__main__":
    asyncio.run(main())
