import rich, sys, os, time
from rich.console import Console
from rich.progress import track
from rich import print
from rich.theme import Theme
from time import sleep
import nmap

console = Console()
console.log("[blue] [+] starting NmapScan")
for step in track(range(300)):
    sleep(0.1)
    step

time.sleep(2)
os.system('clear')
print("""[bold green]
 _____               _____             
|   | |_____ ___ ___|   __|___ ___ ___ 
| | | |     | .'| . |__   |  _| .'|   |
|_|___|_|_|_|__,|  _|_____|___|__,|_|_|
                |_|                    
[/bold green]""")
time.sleep(0.1)
print("[blue][+] type (help) for more options")
time.sleep(1)
print("[blue][+] modules: 9 scripts: 2 nmap modules: ")
time.sleep(0.1)
print("""[blue]
[+] command <topic> (help)
----------------------------
[/blue]""")
time.sleep(0.1)
print("[blue]example: use (help) show (help) or help[/blue]")

def input_menu():
    nmap = input("[+] scan: ")

    if nmap == "help":
        print("""[bold blue]
[+] help                        show this help menu
[+] show                        show modules
[+] use                         use modules
[+] clear
[+] exit
        [/bold blue]""")

    elif nmap == "show":
         print("[blue][+] type show (help) for more info[/blue]")

    elif nmap == "show help":
         print("""[bold blue]
[+] show modules              list all modules
[+] show scripts              list all scripts
[+] show banner               show banner
         [/bold blue]""")

    elif nmap == "show modules":
         print("""[bold blue]
[+] nmap-port-scan                 -Pn
[+] nmap-service-scan              -sV
[+] nmap-detail-scan               -A
[+] nmap-network-scan              -sn
[+] nmap-portnet-scan              -Pn
[+] nmap-open-port                 -p
[+] nmap-debug-scan                -d
[+] nmap-camera-scan               -p 554
[+] nmap-open-scan                 --open
[+] nmap-dns-brute                 dns-brute.nse
[+] nmap-heartbleed-scan           ssl-heartbleed.nse
[+] nmap-smb-brute-scan            smb-brute.nse
[+] nmap-vuln-scan                 vulners.nse
         [/bold blue]""")

    elif nmap == "show scripts":
         print("""[bold blue]
[+] nmap-dns-brute                 dns-brute.nse
[+] nmap-heartbleed-scan           ssl-heartbleed.nse
[+] nmap-smb-brute-scan            smb-brute.nse
[+] nmap-vuln-scan                 vulners.nse
         [/bold blue]""")

    elif nmap == "use":
         print("[blue][+] type use (help) for more info[/blue]")

    elif nmap == "use help":
         print("""[bold blue]
[+] nmap-port-scan                 -Pn
[+] nmap-service-scan              -sV
[+] nmap-detail-scan               -A
[+] nmap-network-scan              -sn
[+] nmap-portnet-scan              -Pn
[+] nmap-open-port                 -p
[+] nmap-debug-scan                -d
[+] nmap-camera-scan               -p 554
[+] nmap-open-scan                 --open
[+] nmap-dns-brute                 dns-brute.nse
[+] nmap-heartbleed-scan           ssl-heartbleed.nse
[+] nmap-smb-brute-scan            smb-brute.nse
[+] nmap-vuln-scan                 vulners.nse
         [/bold blue]""")
         print("[blue][+] use module <nmap> [/blue]")

    elif nmap == "use module nmap-port-scan":
         ip_port_scan = input("[+] set target ip/domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_port_scan+" for ports[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -Pn '+ip_port_scan+'')
         elif verbose == "n":
              os.system('nmap -Pn '+ip_port_scan+'')

    elif nmap == "use module nmap-service-scan":
         ip_service_scan = input("[+] set target ip/domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_service_scan+" for ports and services[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -Pn -sV '+ip_service_scan+'')
         elif verbose == "n":
              os.system('nmap -Pn -sV '+ip_service_scan+'')

    elif nmap == "use module nmap-detail-scan":
         ip_d_scan = input("[+] set target ip/domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_d_scan+" detailed scan[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -A -Pn '+ip_d_scan+'')
         elif verbose == "n":
              os.system('nmap -A -Pn '+ip_d_scan+'')

    elif nmap == "use module nmap-network-scan":
         ip_n_scan = input("[+] set target ip/domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_n_scan+"/24 for network scan[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -sn '+ip_n_scan+'/24')
         elif verbose == "n":
              os.system('nmap -sn '+ip_n_scan+'/24')

    elif nmap == "use module nmap-portnet-scan":
         ip_op_scan = input("[+] set target ip/domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_op_scan+"/24 open port network scan[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -Pn '+ip_op_scan+'/24')
         elif verbose == "n":
              os.system('nmap -Pn '+ip_op_scan+'/24')

    elif nmap == "use module nmap-open-port":
         ip_open_only = input("[+] set target ip/domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_open_only+" open ports ONLY! network scan[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -Pn --open '+ip_open_only+'')
         elif verbose == "n":
              os.system('nmap -Pn --open '+ip_open_only+'')

    elif nmap == "use module nmap-debug-scan":
         ip_debug = input("[+] set target ip/domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_debug+" debug scan[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -d -Pn '+ip_debug+'')
         elif verbose == "n":
              os.system('nmap -d -Pn '+ip_debug+'')

    elif nmap == "use module nmap-camera-scan":
         ip_cam = input("[+] set target ip/domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_cam+"/24 scan[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -p 554 -Pn '+ip_cam+'/24')
         elif verbose == "n":
              os.system('nmap -p 554 -Pn '+ip_cam+'/24')

    elif nmap == "use module nmap-open-scan":
         ip = input("[+] set target ip/domain: ")
         port = input("[+] set port to scan: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip+" scanning port "+port+"[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -p '+port+' --open -Pn '+ip+'')
         elif verbose == "n":
              os.system('nmap -p '+port+' --open -Pn '+ip+'')

    elif nmap == "use module nmap-dns-brute":
         dns = input("[+] type a domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+dns+" dns brute scan[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v --script=dns-brute.nse -Pn '+dns+'')
         elif verbose == "n":
              os.system('nmap --script=dns-brute.nse -Pn '+dns+'')

    elif nmap == "use module nmap-heartbleed-scan":
         ip_hb = input("[+] set target ip/domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_hb+" heartbleed scan[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v --script=ssl-heartbleed.nse -Pn -sV '+ip_hb+'')
         elif verbose == "n":
              os.system('nmap --script=ssl-heartbleed.nse -Pn -sV '+ip_hb+'')

    elif nmap == "use module nmap-smb-brute-scan":
         ip_brute_smb = input("[+] set target ip/domain: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_brute_smb+" smb brute scan[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -A --script=smb-brute.nse -Pn -sV '+ip_brute_smb+'')
         elif verbose == "n":
              os.system('nmap -A --script=smb-brute.nse -Pn -sV '+ip_brute_smb+'')

    elif nmap == "use module nmap-vuln-scan":
         ip_vuln = input("[+] set target ip: ")
         console.log("[bold yellow][!][/bold yellow] [blue]scanning "+ip_vuln+" smb brute scan[/blue]")
         verbose = input("[!] do you want to add -v for verbose[y/n]: ")
         if verbose == "y":
            os.system('nmap -v -A --script=vulners.nse -Pn -sV '+ip_vuln+'')
         elif verbose == "n":
              os.system('nmap -A --script=vulners.nse -Pn -sV '+ip_vuln+'')

    elif nmap == "exit":
         print("[bold blue][+] bye bye[/bold blue]")
         sys.exit()

    elif nmap == "clear":
         print("[bold green][+] Done![/bold green]")
         time.sleep(2)
         os.system('clear')

    elif nmap == "show banner":
         print("""[bold green]
 _____               _____
|   | |_____ ___ ___|   __|___ ___ ___
| | | |     | .'| . |__   |  _| .'|   |
|_|___|_|_|_|__,|  _|_____|___|__,|_|_|
                |_|
         [/bold green]""")
         time.sleep(0.1)
         print("[blue][+] type (help) for more options")
         time.sleep(1)
         print("[blue][+] modules: 9 scripts: 2 nmap modules: ")
         time.sleep(0.1)
         print("""[blue]
[+] command <topic> (help)
----------------------------
         [/blue]""")

    else:
        print("[bold red]NOTE![/bold red][bold blue] not a option[/bold blue]")
    input_menu()

input_menu()
