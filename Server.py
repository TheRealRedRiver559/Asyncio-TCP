import socket
import threading
import json

def main():
    host = 'localhost'
    port = 9090

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    banned_users = []
    clients = [] 
    #clients and users will be combined in a dictionary soon
    users = []
    commands = {}
    prefix = '//' #changable prefix for all commands and descriptipns

    #descriptions of commands. Added speratly for each command but may change later
    #Will have a seperate file for them eventually or a better way of storing them
    descriptions = {
    'connections':{'description':'Lists the # of clients connected.', 'usage':f'{prefix}connections', 'examples':'Clients Online: 2\n'},
    'users':{'description':'Prints a list of connected users.', 'usage':f'{prefix}users', 'examples':'[\'joe\', \'bob\']\n'},
    'banned-users':{'description':'Prints a list of all banned users.', 'usage':f'{prefix}banned-users', 'examples':'[\'badperson2123\', \'banned_user12\']\n'},
    'ban':{'description':'Bans the specified user. Use the silent argument for silent ban messages', 'usage':f'{prefix}ban <user> \[silent] \[reason]', 'examples':f'{prefix}ban joe\n{prefix}ban joe you were being bad!\n{prefix}ban test silent\nRequired Argument: <>\nOptional Argument: []\n'},
    'unban':{'description':'Unbans the specified user.', 'usage':f'{prefix}unban <user> \[silent]', 'examples':f'{prefix}unban test\n{prefix}unban test silent\n'},
    'kick':{'description':'Kicks the specified user.', 'usage':f'{prefix}kick <users> \[silent]', 'examples':f'{prefix}kick test\n{prefix}kick test silent\n'},
    'help':{'description':'Prints a general set of available commands.', 'usage':f'{prefix}help \[command]', 'examples':f'{prefix}help\n{prefix}help ban\n'},
    }

    error_message = {
        'Leave': 'Connection closed by client.',
        'Close': 'Connection closed by server.',
        'Connection': 'User already connected.',
        }

    #Command decorator, for adding new commands rather than adding each one to a dictionary and easier to use.
    def command(name, role_id):
        def inner(func):
            commands[name] = [func, role_id]
            return func
        return inner

    #broadcasts a message specifying the current # of connections
    @command('connections', 1)
    def client_connections(username):
        client_connections = len(clients)
        broadcast(f'{username}: {prefix}connections'.encode())
        broadcast(f'Server: Clients online: {client_connections}'.encode())
        print(f'Command: {prefix}connections (Username: {username})')
    
    #broadcasts a list of users online
    @command('users', 2)
    def users_online(username):
        broadcast(f'{username}: {prefix}users'.encode())
        user_list = [user for user in users]
        broadcast(f'Server: Users: {user_list}'.encode())
        print(f'Server: Command: {prefix}users (Username: {username})')
    
    #sends a list of all users inside the 'banned user' list
    @command('banned-users', 3)
    def users_banned(username):
        broadcast(f'{username}: {prefix}banned-users'.encode())
        banned_list = [user for user in banned_users]
        broadcast(f'Server: Banned Users: {banned_list}'.encode())
        print(f'Server: Command: {prefix}banned-users (Username: {username})')
    
    #bans users (Command syntax : ban <username> [silent] [reason])
    @command('ban', 3)
    def ban_user(username, arguments):
        reason=None
        silent_ban=False
        client = clients[users.index(username)]

        if len(arguments) >= 2:
            reason = " ".join(arguments[1:])
            if (arguments[1]).lower() == 'silent':
                silent_ban = True
                reason = " ".join(arguments[2:])

        with open('Tcp Server\\users.json', 'r') as f:
            data = json.load(f)

            user_role_id = data[username]['role_id']
            target_username = arguments[0]
            if target_username in data:
                target_role_id = data[arguments[0]]['role_id'] 
            else:
                client.send(f"Server: No user named '{target_username}' was found!".encode())
                return
            
        target_role_id = data[target_username]['role_id']

        if user_role_id <= target_role_id:
            client.send(f'Server: Server: You cannot ban this member!'.encode())
            return
        if target_username in banned_users:
            client.send(f"Server: '{target_username}' already banned!".encode())
            return
        if target_username not in users:
            client.send(f'Server: This user is not currently in the server'.encode())
            return

        banned_users.append(target_username)
        target_client = clients[users.index(target_username)]
        target_client.send(f'Server: You have been banned.\n\tReason: {reason}'.encode())
        print(f'Command: {prefix}ban {target_username} Silent={silent_ban} Reason:{reason} (Username: {username})')
        user_leave(target_client, error_message['Close'])

        if silent_ban == True:
            client.send(f'Server: {target_username} has been banned.\n\tReason: {reason}'.encode())
        else:
            broadcast(f"{username}: {prefix}ban {target_username} {reason}".encode())
            broadcast(f"Server: '{target_username}' has been banned.\n\tReason: {reason}".encode())

    #unbans users
    @command('unban', 3)
    def unban_user(username, arguments):

        silent_unban=False
        client = clients[users.index(username)]

        if len(arguments) > 1:
            if (arguments[1]).lower() == 'silent':
                silent_unban = True

        with open('Tcp Server\\users.json', 'r') as f:
            data = json.load(f)

            user_role_id = data[username]['role_id']
            target_username = arguments[0]
            if target_username in data:
                target_role_id = data[arguments[0]]['role_id'] 
            else:
                client.send(f'Server: No user named {target_username} was found!'.encode())
                return

        if len(arguments) > 2:
            client.send(f'Server: This command only takes 2 argument. {len(arguments)} Given!'.encode())
            return
        if user_role_id <= target_role_id: #permission check
            client.send(f'Server: Server: You cannot unban this member!'.encode())
            return
        if target_username not in banned_users: #checks to see if they are not in users
            client.send('Server: User is not currently banned!'.encode())
            return

        banned_users.remove(target_username)
        
        if silent_unban == True:
            client.send(f'Server: {target_username} has been unbanned.'.encode())
        else:
            broadcast(f'{username}: {prefix}unban {target_username}'.encode())
            broadcast(f'Server: {target_username} has been unbanned by: {username}.'.encode())

        print(f'Server: Command: {prefix}unban {target_username} silent={silent_unban} (Username: {username})')

    @command('kick', 2)
    def kick_user(username, arguments):
        #kicks users but still allows them to join back
        reason=None
        silent_kick=False
        client = clients[users.index(username)]

        if len(arguments) >= 2:
            reason = " ".join(arguments[1:])
            if (arguments[1]).lower() == 'silent':
                silent_kick = True
                reason = " ".join(arguments[2:])

        with open('Tcp Server\\users.json', 'r') as f:
            data = json.load(f)
            
            user_role_id = data[username]['role_id']
            target_username = arguments[0]
            if target_username in data:
                target_role_id = data[arguments[0]]['role_id'] 
            else:
                client.send(f'Server: No user named {target_username} was found!'.encode())
                return
            
        target_role_id = data[target_username]['role_id']

        if user_role_id <= target_role_id:
            client.send(f'Server: You cannot kick this member!'.encode())
            return
        if target_username in banned_users:
            client.send(f'Server: This member is not currently in the server'.encode())
            return
        if target_username not in users:
            client.send(f'Server: This member is not currently in the server'.encode())
            return

        target_client = clients[users.index(target_username)]
        target_client.send(f'Server: You have been kicked.\n\tReason: {reason}'.encode())
        print(f'Command: {prefix}kick {target_username} Silent={silent_kick} Reason:{reason} (Username: {username})')
        user_leave(target_client, error_message['Close'])

        if silent_kick == True:
            client.send(f'{target_username} has been kicked\n\tReason: {reason}.'.encode())
        else:
            broadcast(f'{username}: {prefix}kick {target_username} {reason}'.encode())
            broadcast(f'Server: {target_username} has been kicked.\n\tReason: {reason}'.encode())

    @command('help', 2)
    def help_command(username, arguments=None):
        #sends a list of all commands. Can show specific details about a command with a argument (Command syntax : //help [command])
        #Soon to change to show commands accessable to that permission level.
        index = users.index(username)
        client = clients[index]

        if arguments != None:
            if len(arguments) != 1:
                client.send(f'Server: This command only takes 1 argument. {len(arguments)} Given!'.encode())
                return
            command_name = arguments[0]
            try:
                role_id = commands[command_name][1]
                detials = (f'-{command_name}-\n{descriptions[command_name]["description"]}\n\n-Usage-\n{descriptions[command_name]["usage"]}\n\n-Examples-\n{descriptions[command_name]["examples"]}\n\n-Permissions-\nPermission Level : {role_id}+')
                client.send(f'Server:\n{detials}'.encode())
                print(f'Server: Command: {prefix}help {command_name} (Username: {username})')
                return
            except KeyError:
                client.send(f'Server: Could not find any command named: {command_name}'.encode())
                return
        index = users.index(username)
        client = clients[index]
        help_text = (f'Server: [bold white]Commands[/bold white][green]\n{prefix}help \[command]\n{prefix}users\n{prefix}connections\n{prefix}banned-users\n{prefix}kick\n{prefix}ban\n{prefix}unban\n')
        client.send(help_text.encode())

        print(f'Server: Command: {prefix}help (Username: {username})')
    
    #message for missing permission
    def missing_permissions(client, message):
        client.send(f'Server: Missing permissions for the command named: {message.lower()}'.encode())
    
    #broadcasts a message to all clients. Can send to all axcept certain clients.
    def broadcast(message, dont_send_to=None):
        for client in clients:
            if dont_send_to != None:
                if dont_send_to != client:
                    client.send(message)
                else:
                    pass
            else:
                client.send(message)

    #command proccesing, checks for permissions and command validity
    def proccess_command(client, message, username):
        command_name, *arguments = message.split(" ")
        try:
            command = commands[command_name][0]
        except KeyError:
            client.send(f'Server: Invalid Command! no command named: {command_name.lower()}'.encode())
            return

        with open('Tcp Server\\users.json', 'r') as f:
            data = json.load(f)

            role_id = data[username]['role_id']

        if role_id >= commands[command_name][1]: #checking if users perms is >= to command perms
            if len(message) > len(command_name):
                try:
                    command(username, arguments=arguments) #checks if message is valid for args
                except TypeError:
                    client.send(f'Server: Command: {command_name} : Requires no arguments!'.encode())
                    return
            else:
                try:
                    command(username)
                except TypeError:
                    client.send(f'Server: Command: {command_name} : Requires 1 or more arguments!'.encode())
                    return
        else:
            missing_permissions(client ,command_name)      

    #main client listener for messages and commands.
    def handle_client(client):
        while True:
            try:
                message = client.recv(1024).decode()
                username = users[clients.index(client)]

                if len(message) > 200:
                    client.send('Server: Message size exceeds the 200 character limit!'.encode())
                    continue
                if message[:len(prefix)] == prefix: #command prefix
                    proccess_command(client, message[len(prefix):].lower(), username)
                else:
                    broadcast(f'{username}: {message}'.encode())
            except ConnectionAbortedError:
                break #Server Closed Connetion
            except ConnectionResetError:
                user_leave(client, error_message['Leave'])
                break

    #error handling for users leaving. Leave message on ban is optional
    def user_leave(client, leave_reason, broadcast_leave=True):
        address = client.getpeername()
        client.close()
        try:
            username = users[clients.index(client)]
            clients.remove(client)
            users.remove(username)
        except ValueError: #User did not finish login
            username = 'N/A'

        if broadcast_leave == True:
            broadcast(f'Server: {username} has disconnected...'.encode())
        print(f'Server: Client:({username} {address} has disconnected (Reason: {leave_reason})')
    
    def failed_login(client):
        client.send('Username or Password is incorrect!'.encode())
        user_leave(client, 'User failed login', broadcast_leave=False)

    #accepts clients, and checks login crediantials.
    def receive():
        while True:
            client, address = server.accept()
            print(f'{str(address)} has connected...')
            client.send('LOGIN'.encode()) #Sends message to start the login proccess. May change to be the first 2 inputs rather than sending a message.

            try:
                username = client.recv(1024).decode().lower()[1:]
                password = client.recv(1024).decode()[1:]
            except ConnectionResetError: #User left during login
                user_leave(client, 'Left during login')
                continue

            if username in banned_users:
                client.send('You are banned!'.encode())
                print('User is banned. Connection ended...')
                client.close()
                continue
            if username in users:
                client.send('User already connected!'.encode())
                user_leave(client, error_message['Conn'], broadcast_leave=False)
                continue
            else:
                pass

            #No hashing or anything of the sort is being added until later.
            with open('Tcp Server\\users.json', 'r') as f:
                data = json.load(f)

                if username in data:
                    user_info = data[username]
                    user = (username, user_info['password'])
                else:
                    failed_login(client)
                    continue

                user_password = user[1]

                if user_password == password:
                    client.send('Logged In!'.encode())
                                        
                    clients.append(client)
                    users.append(username.lower())
                else:
                    failed_login(client)
                    continue

            broadcast(f'Server: {username} has connected...'.encode(), dont_send_to=client) #sends a message to everyone but that client
            client.send(f'Server: You are connected to : {address}'.encode())

            t1 = threading.Thread(target=handle_client, args=(client,))
            t1.start()


    print('Server is running and listening...')
    receive()

if __name__ == "__main__":
    t1 = threading.Thread(main())
    t1.start()
