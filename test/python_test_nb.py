import asyncio
from asyncio import AbstractEventLoop
from timeit import default_timer as timer

import colorama

async def print_fo(txt:str) -> None:
    print(colorama.Fore.GREEN + txt + str(timer()), flush=True)

async def wat(sec:float) -> None:
    start = timer()
    print(colorama.Fore.BLUE + "Wait function has been called " +str(sec) + ', At ' + str(start), flush=True)
    await asyncio.sleep(sec)
    print(colorama.Fore.CYAN + "Wait function has been finished " +str(sec) + "took " + str(timer() - start) + " Seconds", flush=True)

def main():
    print(colorama.Fore.RED + "App has started", flush=True)
    loop: AbstractEventLoop = asyncio.get_event_loop()
    task = asyncio.gather(
        wat(0.8),
        wat(1),
        wat(0.5),
        print_fo("first "),
        print_fo("second "),
        print_fo("third "),
        print_fo("fourth "),
        wat(0.1),
        print_fo("fifth"),
    )
    loop.run_until_complete(task)

if __name__ == "__main__":
    main()