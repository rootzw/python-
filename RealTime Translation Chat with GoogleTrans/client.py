import socket

#prompting user to input language code, they speak e.g sn for shona
lang = input("Enter your language code: ")

client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',5555))

while True:
    message = input("")
    if message == "!q":
        client.close()
        break
    else:
        client.send(f"[{lang}]{message}".encode())