from socket import *
from random import randint

port = 12000
s_soc = socket(AF_INET, SOCK_STREAM)
s_soc.bind(('localhost', port))
s_soc.listen(1)
ServerName = "Universal Server"
print(ServerName + " is now ONLINE")
print("")

# server returns a string containing (name, random number, sum)
while True:
        con, addr = s_soc.accept()
        
        # Get name
        inputName = con.recv(1024).decode()

        # Get number
        inputNum = con.recv(1024).decode()        
        try:
                # convert to int
                inputNum = int(inputNum)
                # check if input is in bounds
                if inputNum < 1 or inputNum > 100:
                        raise Exception("Number out of range")
        except:
                # if error, send error message in response
                print("Error: Client entered an invalid number")
                print("")
                resp = "Error: Please input a valid number"
        else:
                # if no error
                # Generate random number
                randNum = randint(1,100)
                
                # Create proper response
                resp = "Server of %s, Random Int %i, Sum %i" % (inputName, randNum, inputNum+randNum)
                print("")
                print("   Server of: " + inputName)
                print("Random value: " + str(randNum))
                print("         Sum: " + str(inputNum+randNum))
                print("")
                print("Sent response")
                print("")
        finally:
                # send response
                con.send(resp.encode())
        #con.close()
