from Crypto.Cipher import AES
import socket
import sys

def exitmessage():  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, int(port)))
    exitmessage1 = Username + " Has Left The Server"
    padding = " "
    extra = len(exitmessage1) % 16
    if extra > 0:
      exitmessage1 = exitmessage1 + (padding * (16 - extra))
    stringencoded = exitmessage1.encode('utf-8')
    stringencrypted = do_encrypt(stringencoded)
    sock.send(stringencrypted)
def do_encrypt(message):
    obj = AES.new(Password, AES.MODE_CBC, IV)
    ciphertext = obj.encrypt(message)
    return ciphertext
if len(sys.argv) == 2:
        if sys.argv[1] == "-help":
                print("Usage: " + sys.argv[0] + " Host Port Password IV")
                sys.exit(1)
if not len(sys.argv) == 5:
    print("Incorrect Usage Refer To -help for Usage")
    sys.exit(1)
else:
    host = sys.argv[1]
    port = sys.argv[2]
    Password = sys.argv[3]
    IV = sys.argv[4]
    padding = "o"
    extra = len(IV) % 16
    if extra > 0:
        IV = str(IV) + (padding * (16 - extra))
    extra = len(Password) % 16
    if extra > 0:
        Password = str(Password) + (padding * (16 - extra))
#host = input('What Is The Host:')
#port = input('What Is The Port:')
#IV = input('What Is The IV Key:')
#Password = input('What Is The Password:')
exitcode = "exit now"
Username = input('Enter your username:')
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, int(port)))
    joinmessage = Username + " Has Joined The Server"
    padding = " "
    extra = len(joinmessage) % 16
    if extra > 0:
      joinmessage = joinmessage + (padding * (16 - extra))
    stringencoded = joinmessage.encode('utf-8')
    stringencrypted = do_encrypt(stringencoded)
    sock.send(stringencrypted)
except socket.error:
    print("Error Connecting To Server")
    sys.exit(1)
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, int(port)))
        stringsend = input('Enter String To Send:')
        if stringsend == exitcode:
            print("\n\n[*] User Requested An Interrupt")
            print("[*] Application Shutting Down.")
            exitmessage()
            sock.close()
            sys.exit(1)
        stringsend = Username + ':' + stringsend
        padding = " "
        extra = len(stringsend) % 16
        if extra > 0:
            stringsend = stringsend + (padding * (16 - extra))
        stringencoded = stringsend.encode('utf-8')
        stringencrypted = do_encrypt(stringencoded)
        sock.send(stringencrypted)
    except KeyboardInterrupt:
                print("\n\n[*] User Requested An Interrupt")
                print("[*] Application Shutting Down.")
                sock.close()
                sys.exit(1)
    except socket.error:
        print("There Was An Error You Fucked It Up")
        sys.exit(1)
