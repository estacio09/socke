import socket

HOST = "127.0.0.1"
PORT = 7879
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("conexion establecidad con el servidor")

    while True:
        data = s.recv(1024).decode()
        if not data:
            break
        print("Mensaje recibido del servidor:", data)
        mensaje_enviar = input()
        s.sendall(mensaje_enviar.encode())
