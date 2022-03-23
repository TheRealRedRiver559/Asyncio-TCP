import threading
import socket
import datetime
from rich import print
import json

class client():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.username = None
        self.connected = False
    
    def connect(self, client):
        while self.connected == False:
            if client.connect_ex((self.host, self.port)) != 0:
                pass
            else:
                print('Connected!')
                self.connected = True
                self.login(client)

    def login(self, client):
        self.username = input('Username: ')
        data = json.dumps({'username':self.username, 'password':input('Password: ')})
        client.send(data.encode())
    
    @staticmethod
    def get_time():
        time = datetime.datetime.now()
        setting = 'AM'
        hours = int(time.strftime("%H"))
        if hours > 12:
            setting = 'PM'
            hours -= 12
        return (time.strftime(f"%m/%d/%Y {hours}:%M {setting}"))
    
    def send_message(self, client):
        while True:
            message = input()

            if len(message) > 2000:
                print('Too Long!')
            else:
                data = json.dumps({'length':len(message), 'username':self.username, 'message':message})
                client.send(data.encode())

    def recv_message(self, client):
        while True:
            message_data = json.loads(client.recv(1024))
            message = f"{message_data['username']}: {message_data['message']}"

            if message_data['username'] == self.username: #Blue for your username
                print(f"[blue]{message[:len(self.username)]} [white]{message[len(self.username):]}[/white] [grey37]{self.get_time()}")
            elif message_data['username'] == 'Server':
                print(f"[yellow]{message[:6]} [white]{message[6:]}[/white] [grey37]{self.get_time()}")
            else:
                print(f"[red]{message[:len(message_data['username'])]} [white]{message[len(message_data['username']):]} [grey37]{self.get_time()}")
    
    def run_client(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(client)
        recv_thread = threading.Thread(target=self.recv_message, args=(client,))
        recv_thread.start()
        message_thread = threading.Thread(target=self.send_message, args=(client,))
        message_thread.start()

Client = client('127.0.0.1', 9090)
Client.run_client()
