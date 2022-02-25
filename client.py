from socket import *
import itertools
import threading
import time

s_name, s_port = 'localhost', 12000

# https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
animating = False
# animation function
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if animating:
                print('\r     Waiting ' + c, end="")
                time.sleep(0.25)

def stopAnimating():
        global animating
        animating=False
        print('\r                               \r', end="")

# Start animation thread
animating = True
t = threading.Thread(target=animate, daemon=True)
t.start()

c_soc = socket(AF_INET, SOCK_STREAM)
c_soc.connect((s_name, s_port))
stopAnimating()
print('Connected to Remote Server')
print("")

data = input("Enter a Name\n")
c_soc.send(data.encode())
print("")

data = input("Enter an integer between 1 and 100\n")
c_soc.send(data.encode())
print("")

print('Data sent... waiting for the response.')
animating = True
resp = c_soc.recv(1024)
stopAnimating()
print(resp.decode())

c_soc.close()
