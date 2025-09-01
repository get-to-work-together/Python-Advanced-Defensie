import asyncio

data = []

async def doe_iets(i):
    print(f'{i} - Doing it ...')
    data.append(i)
    await asyncio.sleep(1)
    data.append(i)
    print(f'{i} - Done')

async def main():
    await asyncio.gather(doe_iets(1), doe_iets(2), doe_iets(3))


if __name__ == "__main__":
    asyncio.run(main())
    print(data)
