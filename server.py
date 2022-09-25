import sys, getopt
from termcolor import colored
import random

def gen_agent():
    print("gen_agent")

def listen_conns():
    print("listen_conns")

def bind_conn():
    print("bind_conn")

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
        "The dildo of consequences rarely arrives lubed."
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


def post_help():
    print("> server.py --help/-h       |    Prints this help page") 
    print("> server.py --gen/-g        |    Generate new agent/beacon")
    print("> server.py --listen/-l     |    Listens for all deployed agents/beacons")
    print("> server.py --bind/-b       |    Binds to the chosen deployed agent/beacon")  
    print("> server.py --files/-f      |    Lists options for file hosting")  
    print()
    sys.exit()



def main(argv):
    print_banner()
    try:
        opts, args = getopt.getopt(argv,"hglbf",["help","gen","listen","bind","files"])
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
        elif opt in ("-b", "--bind"):
            bind_conn() 
            sys.exit()
        elif opt in ("-f", "--files"):
            host_files() 
            sys.exit()
    if opts == []:
        post_help()
        

if __name__ == "__main__":
   main(sys.argv[1:])