#!/usr/bin/env python

# WS server example that synchronizes state across clients
# Demo Clients : Android and JS


import asyncio
import json
import logging
import websockets

logging.basicConfig()

STATE = {'value': 0}
USERS = set()
# You can use localhost to test and port forwading it with ngrok  $ ./ngrok http 6789
# For clients, Copy ngrok's url to js and Android client
SERVER_IP = 'PYTHON SERVER IP'
# port 6789 is just an example. 
SERVER_PORT = 6789


def state_event():
    return json.dumps({'type': 'state', **STATE})


def users_event():
    return json.dumps({'type': 'users', 'count': len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data['action'] == 'forward':
                print("FORWARD")
                STATE['value'] = 'FORWARD'
                await notify_state()

            elif data['action'] == 'backward':
                print("BACK");
                STATE['value'] = 'BACKWARD'
                await notify_state()

            elif data['action'] == 'left':
                print("LEFT");
                STATE['value'] = "LEFT"
                await notify_state()

            elif data['action'] == 'right':
                print("RIGHT");
                STATE['value'] = 'RIGHT'
                await notify_state()

            elif data['action'] == 'stop':
                print("STOP");
                STATE['value'] = 'STOP'
                await notify_state()

            else:
                logging.error(
                    "unsupported event: {}", data)
    finally:
        await unregister(websocket)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(counter, SERVER_IP, SERVER_PORT))
asyncio.get_event_loop().run_forever()
