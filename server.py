from socket import *
from random import randint
import itertools
import threading
import time

port = 12000
s_soc = socket(AF_INET, SOCK_STREAM)
s_soc.bind(('localhost', port))
s_soc.listen(1)
ServerName = "Universal Server"
print(ServerName + " is now ONLINE")
print("")

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
t = threading.Thread(target=animate, daemon=True)
t.start()

# server returns a string containing (name, random number, sum)
while True:
        animating = True

        # Wait for connection from client
        con, addr = s_soc.accept()
        stopAnimating()
        print("Connected to Client")
        
        # Get name from client
        animating = True
        inputName = con.recv(1024).decode()
        stopAnimating()
        print("    Server of: " + inputName)

        # Get number
        animating = True
        inputNum = con.recv(1024).decode()
        stopAnimating()
        try:
                # convert to int
                inputNum = int(inputNum)
                # check if input is in bounds
                if inputNum < 1 or inputNum > 100:
                        raise Exception("Number out of range")
        except:
                # if error, send error message in response
                print("        Error: Client entered an invalid number: " + str(inputNum))
                print("")
                resp= "        Error: Please input a valid number"
        else:
                # if no error
                # Generate random number
                randNum = randint(1,100)
                
                # Create response for valid userInput
                resp = ("   User Input: " + str(inputNum) + "\n"
                        " Random value: " + str(randNum) + "\n"
                        "          Sum: " + str(inputNum+randNum) + "\n")
                print(resp)
                resp = "     Server of: " + inputName +"\n" + resp
        finally:
                # send response
                con.send(resp.encode())
                print(" Sent response")
                print("")
        #con.close()
