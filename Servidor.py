import asyncio
import websockets
import hashlib


user_passwords = {"user1": "password1", "user2": "password2"}


def create_hash(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    return sha256.hexdigest()

async def servidor(websocket, path):
    try:
        senha = await websocket.recv()
        await websocket.send("Senha recebida com sucesso!")

        mensagem = await websocket.recv()
        hash_mensagem = create_hash(mensagem)

        await websocket.send(f"Mensagem criptografada: {hash_mensagem}")

        senha_usuario = await websocket.recv()

        if check_password(senha_usuario, senha):
            await websocket.send(f"Mensagem original: {mensagem}")
        else:
            await websocket.send("Senha incorreta. Não é possível descriptografar a mensagem.")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed unexpectedly: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_password(user_password, stored_password):

    return user_password == user_passwords.get("user1")

async def main():
    server = await websockets.serve(servidor, "localhost", 8765)

    await server.wait_closed()

asyncio.get_event_loop().run_until_complete(main())

