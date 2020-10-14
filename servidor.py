import  socket

with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as so:
    so.bind(('127.0.0.1', 7879))
    so.listen()
    print('servidor encendido, esperando conexion...')
    conexion, direccion = so.accept()
    with conexion:
        print('conexion establecidad desde: ', direccion)

        ingreso2 = 0
            # ingreso = int(input())
        while ingreso2 != 2:
            conexion.sendall("1: calcular masa, \n"
                             "2: salir del programa".encode())

            try:
                print("algo")
                ingreso = conexion.recv(1024).decode()
                ingreso1 = str(ingreso)
                ingreso2 = int(ingreso1)
                if ingreso2 == 1:
                    ban = True
                    while ban == True:

                        try:
                            conexion.sendall("ingresar altura en metro".encode())
                            altura = conexion.recv(1024).decode()
                            altura2 = float(altura)
                            conexion.sendall("ingresar peso".encode())
                            peso = conexion.recv(1024).decode()
                            peso2 = float(peso)
                            indice = peso2 / (altura2 * altura2)
                            indice2 = str(indice)
                            print("su indice de masa es:", indice2)
                            ban = False
                        except ValueError:
                            conexion.sendall("elija una opcion valida".encode())
                        except ZeroDivisionError:
                            conexion.sendall("la altura no puede ser 0".encode())

                        if indice < 18.5:
                            conexion.sendall("usted se encuentra bajo de peso".encode())

                        if indice > 18.5 and indice < 24.9:
                            conexion.sendall("se encuentra en un estado normal".encode())

                        if indice > 25 and indice < 29.9:
                            conexion.sendall("se encuentra en sobre peso".encode())

                        if indice > 30 and indice < 34.9:
                            conexion.sendall("se encuentra en obesidad 1".encode())

                        if indice > 35 and indice < 39.9:
                            conexion.sendall("se encuentra en obesidad 2".encode())

                        if indice > 40 and indice < 49.9:
                            conexion.sendall("se encuentra en obesidad 3".encode())

                        if indice > 50:
                            conexion.sendall("se encuentra en obesidad 4".encode())



            except ValueError:
                print("elija una opcion valida")

