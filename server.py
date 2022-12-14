import socket
import threading

class Servers:
    
    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        
        client, addr = server.accept()
        
        threading.Thread(target=self.handle_connection, args=(client,)).start()
        server.close()