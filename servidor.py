import  socket

with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as so:
    so.bind(('127.0.0.1', 9191))
    so.listen()
    print('servidor encendido, esperando conexion...')
    conexion, direccion = so.accept()
    with conexion:
        print('conexion establecidad desde: ', direccion)
        while True:
            # ----- envio de informacion----
            datos_recividos = conexion.recv(1024)
            if not datos_recividos:
                break
            print('he recivido datos desde el cliente: ', datos_recividos.decode())
            #recibi la infromacion de cliente y le voy a enviar un saludo
            conexion.sendall(b'hola desde el servidor')
