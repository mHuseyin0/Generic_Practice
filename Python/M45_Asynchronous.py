import asyncio

async def switchLight(isLightOn):
    print("Light is gonna be switched.")
    await asyncio.sleep(5)
    isLightOn = not isLightOn
    print("Light is currently " + "on." if isLightOn else "off.")
    return isLightOn

async def switchBox(isBoxOpened):
    print("Box is gonna be switched.")
    await asyncio.sleep(4)
    isBoxOpened = not isBoxOpened
    print("Box is currently " + "opened." if isBoxOpened else "closed.")
    return isBoxOpened

async def main():
    print("Entered the main coroutine.")
    
    isLightOn = False
    isBoxOpened = False

    # This runs them without concurrency
    #lightSwitcher = switchLight(isLightOn)
    #boxSwitcher = switchBox(isBoxOpened)
    #currentLight = await lightSwitcher
    #currentBox = await boxSwitcher


    # Create tasks to run coroutines concurrently
    #lightTask = asyncio.create_task(switchLight(isLightOn))
    #boxTask = asyncio.create_task(switchBox(isBoxOpened))

    #isLightOn = await lightTask
    #isBoxOpened = await boxTask

    # Do the same thing above (create tasks and run concurrently) and return the results as a list
    # TaskGroup is preferred over gather() function since it provides error handling
    # If any task in a TaskGroup fails, all the other tasks  will be cancelled
    
    #results = await asyncio.gather(switchLight(isLightOn), switchBox(isBoxOpened))

    # Exits the block after all the tasks are finished
    async with asyncio.TaskGroup() as tg:
        tg.create_task(switchLight(isLightOn))
        tg.create_task(switchBox(isBoxOpened))

    # Lock is a synchronmisation tool which allows us to change only 1 coroutine to modify a shared resource (variable)
    # Semaphore is another synchronmisation tool which allows us to change a specified number of coroutines to modify 
    # a shared resource
    # Event is another and basic synchronisation tool

    print("Ended the main coroutine.")

asyncio.run(main()) # main() returns a coroutine object. We need to pass it to the run() function