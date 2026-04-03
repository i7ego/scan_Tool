import socket
import colorama
import time
import getpass
import platform
colorama.init(autoreset=True)

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except:
        return "127.0.0.1"

def mask_ip(ip):
    """Mask an IP address for privacy"""
    parts = ip.split('.')
    if len(parts) == 4:
        return ip
    return ip

def show_menu():
    local_ip = get_local_ip()
    masked_local_ip = mask_ip(local_ip)
    
    welcome = '''\033[31m
                                                               ,----, 　　　　　　　　　　　　
                                                             ,/   .`| 　　　　　　　　　　　　
  .--.--.                                                  ,`   .'  :                    ,--,    
 /  /    '.                                              ;    ;     /                  ,--.'|    
|  :  /`. /                              ,---,         .'___,/    ,'  ,---.     ,---.  |  | :    
;  |  |--`                           ,-+-. /  |        |    :     |  '   ,'\   '   ,'\ :  : '    
|  :  ;_       ,---.     ,--.--.    ,--.'|'   |        ;    |.';  ; /   /   | /   /   ||  ' |    
 \  \    `.   /     \   /       \  |   |  ,"' |        `----'  |  |.   ; ,. :.   ; ,. :'  | |    
  `----.   \ /    / '  .--.  .-. | |   | /  | |            '   :  ;'   | |: :'   | |: :|  | :    
  __ \  \  |.    ' /    \__\/: . . |   | |  | |            |   |  ''   | .; :'   | .; :'  : |__  
 /  /`--'  /'   ; :__   ," .--.; | |   | |  |/             '   :  ||   :    ||   :    ||  | '.'| 
'--'.     / '   | '.'| /  /  ,.  | |   | |--'              ;   |.'  \   \  /  \   \  / ;  :    ; 
  `--'---'  |   :    :;  :   .'   \|   |/                  '---'     `----'    `----'  |  ,   /  
          \033[31m   \   \  / |  ,   .-./'---'\033[31m    \033[35m by Ahmed Hagag \033[35m     \033[31m       ---`-'   
             `----'   `--`---'             \033[35m  scan tool 2026                                                
'''
    print(welcome)
    print(f"\033[32mYour IP: {local_ip}")
    print("===========================")
    print("\033[34m 1] Scan Port IP (Range)")
    print("\033[34m 2] Scan Port Number (Service)")
    print("\033[34m 3] Scan Port Name")
    print("\033[34m 4] Scan Port URL")
    print("\033[34m 5] Scan Single Port on IP/URL")
    print("\033[34m 6] Exit.")
    print("===========================")
    return int(input("Please choose option : "))


def scan_ip_ports():
    target = input("Enter the target IP address: ")
    masked_target = mask_ip(target)
    
    choice = input("Do you want to search all ports (1) or a port range (2)? ")
    
    if choice == "1":
        start_port = 1
        end_port = 65535
        print(f"Scanning {target} on all 65535 ports please wait... press [Ctrl+c] for stop scan.")
    elif choice == "2":
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        print(f"Scanning {target} from port {start_port} to {end_port}...")
    
    start_time = time.time()  # Start timing
    
    total_ports = end_port - start_port + 1
    scanned = 0
    open_ports_list = []
    open_ports_found = False
    
    # Calculate estimated time (realistic: includes network overhead)
    time_per_port = 0.014  # Realistic time per port (includes timeout + overhead)
    estimated_seconds = time_per_port * total_ports
    if estimated_seconds < 60:
        estimated_time = f"{estimated_seconds:.1f} seconds"
    else:
        minutes = int(estimated_seconds // 60)
        seconds = int(estimated_seconds % 60)
        estimated_time = f"{minutes}m {seconds}s"
    
    print(f"\033[33mEstimated scan time: {estimated_time}\033[0m")
    
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.001)  # 1 second scan for 800 ports
        
        try:
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports_found = True
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                open_ports_list.append(f"\033[32m{port}\topen\t{service}\033[0m")
        except:
            pass
        finally:
            s.close()
        
        scanned += 1
        # Update progress bar with elapsed time
        if scanned == 1 or scanned % max(1, total_ports // 20) == 0 or port == end_port:
            percent = int((scanned / total_ports) * 100)
            bar = '█' * (percent // 5) + '-' * (20 - (percent // 5))
            elapsed = time.time() - start_time
            print(f"\r\033[36m[{bar}] {percent}% | Elapsed: {elapsed:.1f}s\033[0m", end='', flush=True)
    
    elapsed_time = time.time() - start_time  # Calculate elapsed time
    
    print()  # New line after progress
    
    print(f"\033[35mScan time: {elapsed_time:.2f} seconds\033[0m")  # Show scan time here
    
    style='''
=================================
PORT	STATE	SERVICES
=================================
'''
    print(style)
    
    # Show all open ports found
    if open_ports_list:
        print("\n".join(open_ports_list))
    
    if not open_ports_found:
        print(f"\033[33mNo open ports found on {target}\033[0m")
    else:
        print(f"\033[32mScan completed! Found {len(open_ports_list)} open port(s) on {target}\033[0m")
    
    print("=============================")
    input("Press Enter to return to main menu...")


def scan_port_number():
    def scan(port):
        try:
            socket.getservbyport(port)
            return True
        except:
            return False
    
    port = int(input("Enter port number : "))
    if scan(port):
        name1 = socket.getservbyport(port)
        print(f"Port name of {port} = {name1}")
    else:
        print("Unknown Port")
    time.sleep(1.4)
    input("Press Enter to return to main menu...")

def scan_port_name():
    def name(name2):
        try:
            socket.getservbyname(name2)
            return True
        except:
            return False
    
    name2 = str(input("Enter port Name : "))
    if name(name2):
        res = socket.getservbyname(name2)
        print(f"Port Number of {name2} = {res}")
    else:
        print("Unknown Port")
    time.sleep(1.4)
    input("Press Enter to return to main menu...")


def scan_url_ports():
    target = str(input("Enter Url :"))
    start_port = int(input("from port: "))
    end_port = int(input("to port: "))
    
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    
    start_time = time.time()  # Start timing
    
    total_ports = end_port - start_port + 1
    scanned = 0
    open_ports_list = []
    open_ports_found = False
    
    # Calculate estimated time (realistic: includes network overhead)
    time_per_port = 0.014  # Realistic time per port (includes timeout + overhead)
    estimated_seconds = time_per_port * total_ports
    if estimated_seconds < 60:
        estimated_time = f"{estimated_seconds:.1f} seconds"
    else:
        minutes = int(estimated_seconds // 60)
        seconds = int(estimated_seconds % 60)
        estimated_time = f"{minutes}m {seconds}s"
    
    print(f"\033[33mEstimated scan time: {estimated_time}\033[0m")
    
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.001)  # Fast timeout
        
        try:
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports_found = True
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                open_ports_list.append(f"\033[32m{port}\topen\t{service}\033[0m")
        except:
            pass
        finally:
            s.close()
        
        scanned += 1
        # Update progress bar with elapsed time
        if scanned == 1 or scanned % max(1, total_ports // 20) == 0 or port == end_port:
            percent = int((scanned / total_ports) * 100)
            bar = '█' * (percent // 5) + '-' * (20 - (percent // 5))
            elapsed = time.time() - start_time
            print(f"\r\033[36m[{bar}] {percent}% | Elapsed: {elapsed:.1f}s\033[0m", end='', flush=True)
    
    elapsed_time = time.time() - start_time  # Calculate elapsed time
    
    print()  # New line after progress
    
    print(f"\033[35mScan time: {elapsed_time:.2f} seconds\033[0m")  # Show scan time here
    
    style='''
=================================
PORT	STATE	SERVICES
=================================
'''
    print(style)
    
    # Show all open ports found
        
    if open_ports_list:
        print("\n".join(open_ports_list))
    
    if not open_ports_found:
        print(f"\033[33mNo open ports found on {target}\033[0m")
    else:
        print(f"\033[32mScan completed! Found {len(open_ports_list)} open port(s) on {target}\033[0m")
    
    print("=============================")
    input("Press Enter to return to main menu...")


def scan_single_port():
    target = input("Enter IP or URL: ")
    port = int(input("Enter port number to check: "))
    
    print(f"\nChecking port {port} on {target}...")
    
    start_time = time.time()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    
    try:
        result = s.connect_ex((target, port))
        elapsed = time.time() - start_time
        
        style='''
=================================
PORT\tSTATE\tSERVICES
=================================
'''
        print(style)
        
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"\033[32m{port}\topen\t{service}\033[0m")
            print(f"\n\033[35mScan time: {elapsed:.3f} seconds\033[0m")
            print(f"\033[32mPort {port} is OPEN on {target}\033[0m")
        else:
            print(f"\033[31m{port}\tclosed\t-\033[0m")
            print(f"\n\033[35mScan time: {elapsed:.3f} seconds\033[0m")
            print(f"\033[31mPort {port} is CLOSED on {target}\033[0m")
    except Exception as e:
        print(f"\033[33mError: {e}\033[0m")
    finally:
        s.close()
    
    print("=============================")
    input("Press Enter to return to main menu...")


def main():
    while True:
        choose = show_menu()
        
        if choose == 1:
            scan_ip_ports()
        elif choose == 2:
            scan_port_number()
        elif choose == 3:
            scan_port_name()
        elif choose == 4:
            scan_url_ports()
        elif choose == 5:
            scan_single_port()
        elif choose == 6:
            print("Exiting....")
            time.sleep(1.4)
            break
        else:
            print("Invalid option! Please try again.")
            time.sleep(1)


if __name__ == "__main__":
    main()