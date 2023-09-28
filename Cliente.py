import asyncio
import websockets

async def main():
    server_uri = "ws://localhost:8765"

    try:
        async with websockets.connect(server_uri) as websocket:
            senha = await get_password_input("Digite a senha: ")
            await websocket.send(senha)
            resposta = await websocket.recv()
            print(resposta)

            mensagem = input("Digite a mensagem: ")
            await websocket.send(mensagem)

            resposta = await websocket.recv()
            print(resposta)

            senha_usuario = await get_password_input("Digite a senha para descriptografar: ")
            await websocket.send(senha_usuario)

            resposta = await websocket.recv()
            print(resposta)
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed unexpectedly: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def get_password_input(prompt):
    return input(prompt)

asyncio.get_event_loop().run_until_complete(main())

