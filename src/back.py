import asyncio # library to write concurrent code
import websockets # websocket library
import random

async def echo(websocket, path):
  """
  Handler coroutine executed once for each websocket connection
  """

  # Greeting message
  await websocket.send("Find a number between 0 and 10.")
  secretNumber = random.randint(0, 10) # Generating the secret number randomly

  # Handling websocket messages. Terminate when the client is disconnected
  async for message in websocket:
    # If the message is valid, ie is a number
    if message.isdigit():
      message = int(message)
      # Compare the input number to the secret number and send a response
      if message == secretNumber:
        await websocket.send("Success")
      elif message < secretNumber:
        await websocket.send("More")
      elif message > secretNumber:
        await websocket.send("Less")
    # If the message is invalid, send an error message    
    else:
      await websocket.send("Invalid")


server = websockets.serve(echo, "127.0.0.1", 3012)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
