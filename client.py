from socket import *
s_name, s_port = 'localhost', 12000

c_soc = socket(AF_INET, SOCK_STREAM)
c_soc.connect((s_name, s_port))
print('Connected to Remote Server')

data = input("Enter a Name\n")
c_soc.send(data.encode())
print("")

data = input("Enter an integer between 1 and 100\n")
c_soc.send(data.encode())
print("")

print('Data sent... waiting for the response.')
resp = c_soc.recv(1024)
print('Server', resp.decode())
c_soc.close()
