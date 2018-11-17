# -*- coding: utf-8 -*-

import numpy as np
import json
import asyncio
import websockets
from gradient_descent import run


async def iterate(websocket, num_iter, alpha):
    async def logging(it, _theta, _theta_gradient, cost):
        theta = [x[0] for x in _theta]
        theta_gradient = [x[0] for x in _theta_gradient]
        encoded_json = json.dumps({'it': it, 'theta': theta, 'theta_gradient': theta_gradient, 'cost': cost})
        await websocket.send(encoded_json)
        # print(encoded_json)

    # X = np.array([[1., 1., 1., 1.], [1., 2., 2., 2.]])
    # y = np.array([[1.], [2.]])
    # alpha = 0.01
    # num_iter = 5
    # _theta, cost_list = await gradient_descent(X, y, alpha, num_iter, logging)
    await run(func=logging, num_iter=num_iter, alpha=alpha)
    return


async def socket(websocket, path):
    message = await websocket.recv()

    alpha = 0.01
    num_iter = 100

    if message == 'start':
        await iterate(websocket, num_iter, alpha)
    elif 'alpha' in message:
        alpha = int(message.split('=')[1])
    elif 'num_iter' in message:
        num_iter = int(message.split('=')[1])

    # await websocket.send()


def main():
    start_server = websockets.serve(socket, 'localhost', 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()
