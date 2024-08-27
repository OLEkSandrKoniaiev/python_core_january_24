import asyncio


async def print_num(time: float):
    num = 1
    while True:
        text = ''
        if time < 1:
            text = ' count'
        print(f'{num=}{text}')
        num += 1
        await asyncio.sleep(time)


async def main():
    task1 = asyncio.create_task(print_num(1.0))
    task2 = asyncio.create_task(print_num(0.1))
    await asyncio.gather(task1, task2)

asyncio.run(main())
