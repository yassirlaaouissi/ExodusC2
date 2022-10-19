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




