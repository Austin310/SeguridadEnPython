import socket
from sys import path_importer_cache

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("Nombre del pc: " + hostname)
print("la Ip es: " + ip)

