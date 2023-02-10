import sys, getopt
from termcolor import colored
import random
import re
import ipaddress
import os
import socket
import listener




def gen_agent():
    print("gen_agent")

def rev_conn(argv):
    """This is essentially the listener for the reverse shells the beacons create"""
    
    SERVER_PORT = argv[1]

    ## Checking if we have valid stuff 
    try:
        int(SERVER_PORT) not in range(1, 65535)
    except ValueError:
        print(colored("Given SERVER_PORT is not a valid portnumber", "red"))
        sys.exit(2)
    
    listener.main(SERVER_PORT)

def host_files():
    print("host_files")






def print_banner():
    motds = [
        "I use arch btw",
        "There is literally an entire Taylor Swift Counter-Threat Team with analysts and infrastructure and developers.",
        "If he cheats on you put hair remover in his shampoo, you wanna act like Andrew Tate you're gonna look like him - Book of toxicity 1:34",
        "This WinRAR copy has succesfully been registered. Thank you!",
        "This video has been Sponsored by ProtonVPN!",
        "Counter Strike > Cobalt Strike",
        "It was a mistake to make sand think",
        "Борис, ты где? Виски зовет тебя",
        "Does Jonathan Scott think this is mobile malware?",
        "That will be four dabloon and one dinkywink sir.",
        "keep your talking...the more you tweet at me, the more I can trace your IP ...please continue. - @jonathandata1",
        "I have no idea what I am doing as a service",
        "Dont be part of the problem, be the entire problem",
        "SSEEEEEEECREEET TUNNNEEEEEL!!!!! SeeCCREEET TUNNELLL!!!",
        "Your CPU is a flattened electrocuted rock that someone tricked into doing math homework",
        "Abun de la kaka",
        "1337e2ef42b9bee8de06a4d223a51337",
        "Hola señor, necesitas más píxeles?",
        "Döp döp Euro?",
        "Œh das euro, super geil ganz tol",
        "'Kharlorr can fuck anything' is exactly how ransomware operators speak.",
        "The dildo of consequences rarely arrives lubed.",
        "Be a thermostat, not a thermometer",
        "'Meow' - Yoran",
        "East west, Antoha MC best",
        "teledildonics: https://youtu.be/RnxcPeemHSc",
        "In mudge, we trust",
        "Wait, the world did not end in 2012?!",
        "I dont wear hats",
        "Kajit got me into RAMP",
        "Malware is illegal, and for nerds!"
        "Brvtal Vision - Mercury 200 / March 11 / 9pm-10pm --> 56:10",
        "Sometimes I feel like lester from GTA V, other days I feel like Rian van Rijbroek",
        "Please putin dont nuke",
        "La Caution - Thé à la Menthe - The Laser Dance Song"
    ]
    print(colored("""
    
███████╗██╗  ██╗ ██████╗ ██████╗ ██╗   ██╗███████╗     ██████╗██████╗ 
██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██║   ██║██╔════╝    ██╔════╝╚════██╗
█████╗   ╚███╔╝ ██║   ██║██║  ██║██║   ██║███████╗    ██║      █████╔╝
██╔══╝   ██╔██╗ ██║   ██║██║  ██║██║   ██║╚════██║    ██║     ██╔═══╝ 
███████╗██╔╝ ██╗╚██████╔╝██████╔╝╚██████╔╝███████║    ╚██████╗███████╗
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝     ╚═════╝╚══════╝
                                                          
    ""","red"))
    print(colored(random.choice(motds), "yellow"))
    print()


def post_help(func_name):
    if func_name == "conn":
        print("Usage: > server.py --conn/-c <server_port>")
        print("Example: > server.py --conn 1337")
        print()
        sys.exit()
    else:
        print("> server.py --help/-h       |    Prints this help page") 
        print("> server.py --gen/-g        |    Generate new agent/beacon")
        print("> server.py --conn/-c       |    Connects to a chosen deployed beacon")  
        print("> server.py --files/-f      |    Lists options for file hosting")  
        print()
        sys.exit()



def main(argv):
    print_banner()
    if os.name == 'nt':
        print(colored("Dont run python in windows you pleb, wtf is wrong with you?!", "red"))
        sys.exit(2)
    try:
        opts, args = getopt.getopt(argv,"hgcf",["help","gen","conn","files"])
    except Exception as e:
        print(e)
        post_help()


    for opt, arg in opts:
        if opt in ("-h","--help"):
            post_help()
            sys.exit()
        elif opt in ("-g", "--gen"):
            gen_agent()
            sys.exit()
        elif opt in ("-l", "--listen"):
            listen_conns() 
            sys.exit()
        elif opt in ("-c", "--conn"):
            if len(argv) != 2:
                post_help("conn")
            rev_conn(argv) 
            sys.exit()
        elif opt in ("-f", "--files"):
            host_files() 
            sys.exit()
    if opts == []:
        post_help("main")
        

if __name__ == "__main__":
   main(sys.argv[1:])