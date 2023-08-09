import asyncio

async def fetch_data(url):
    print(f"Fetching data from {url}")
    await asyncio.sleep(2)
    print(f"Data fetched from {url}")

async def main():
    tasks = [
        fetch_data("https://api.example.com/data/1"),
        fetch_data("https://api.example.com/data/2"),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
