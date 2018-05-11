from Crypto.Cipher import AES
import socket
import sys
backlog = 5
size = 10240
host = '127.0.0.1'
def printinfo():
        print('The IP Is ' + host)
        print('The Port Is ' + str(port))
        print('The Password Is ' + password)
        print('The IV Key Is ' + IV)
if len(sys.argv) == 2:
        if sys.argv[1] == "-help":
                print("Usage: " + sys.argv[0] + " Port Password IV")
                sys.exit(1)
if not len(sys.argv) == 4:
    print("Incorrect Usage, Use -help For Help")
    sys.exit(1)
else:
        port = sys.argv[1]
        IV = sys.argv[3]
        password =sys.argv[2]
printinfo()
padding = "o"
extra = len(IV) % 16
if extra > 0:
        IV = str(IV) + (padding * (16 - extra))
extra = len(password) % 16
if extra > 0:
        password = str(password) + (padding * (16 - extra))
def do_decrypt(ciphertext):
        obj2 = AES.new(password, AES.MODE_CBC, IV)
        message = obj2.decrypt(ciphertext)
        return message
def setupsocket():
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, int(port)))
        sock.listen(backlog)
def WaitForMessage():
        global sock
        conn, addr = sock.accept()
        print("New Connection " + str(addr[0]))
        while True:
                conn, addr = sock.accept()
                while True:
                        try:
                                data = conn.recv(size)
                                unencdata = do_decrypt(data)
                                stringdata = unencdata.decode('utf-8')
                                print(stringdata)
                                break
                        except KeyboardInterrupt:
                                print("\n\n[*] User Requested An Interrupt")
                                print("[*] Application Shutting Down.")
                                sock.close()
                                sys.exit(1)
                        except socket.error as msg:
                            sock.close()
                            conn.close()
                            return
setupsocket()
while True:
        try:
                WaitForMessage()
                print("Client Closed Connection")
                setupsocket()
        except KeyboardInterrupt:
                print("\n\n[*] User Requested An Interrupt")
                print("[*] Application Shutting Down.")
                sock.close()
                sys.exit(1)
