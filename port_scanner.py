import socket
import threading
import queue
import time
import os
import sys
import re
from datetime import datetime
import port_versions

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
M = '\033[95m'
C = '\033[96m'
W = '\033[97m'
BR = '\033[1m'
RS = '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""
{R}████████████████████████████████████████████████████████████████████████████{RS}
{R}████████████████████████████████████████████████████████████████████████████{RS}
{R}████████████████████████████████████████████████████████████████████████████{RS}
{R}████████{Y}▒▒▒{R}██████████{Y}▒▒▒▒▒▒▒▒▒▒▒▒███{Y}▒▒▒▒▒▒▒▒▒▒▒▒▒{R}███████████████████████████{RS}
{R}████████{Y}▒▒▒{R}██████████{Y}▒▒▒▒▒▒▒▒▒▒▒▒█{Y}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{R}████████{Y}▒▒{R}███████{Y}▒{R}███████{RS}
{R}████████{Y}▒▒▒{R}██████████{Y}▒▒▒{R}██████████{Y}▒▒▒▒{R}█████████{Y}▒▒▒▒{R}████████{Y}▒▒{R}███████{Y}▒{R}███████{RS}
{R}████████{Y}▒▒▒{R}██████████{Y}▒▒▒{R}██████████{Y}▒▒███{Y}▒▒▒▒▒▒▒███{Y}▒▒{R}████████{Y}▒▒{R}███████{Y}▒{R}███████{RS}
{R}████████{Y}▒▒▒{R}██████████{Y}▒▒▒▒▒▒▒▒▒▒▒▒█{Y}▒▒███{R}▒█████{Y}▒███{Y}▒▒{R}████████{Y}▒▒{R}███████{Y}▒{R}███████{RS}
{R}████████{Y}▒▒▒{R}██████████{Y}▒▒▒▒▒▒▒▒▒▒▒▒█{Y}▒▒███{R}▒█████{Y}▒███{Y}▒▒{R}████████{Y}▒▒{R}███████{Y}▒{R}███████{RS}
{R}████████{Y}▒▒▒{R}██████████{Y}▒▒▒{R}██████████{Y}▒▒███{Y}▒▒▒▒▒▒▒███{Y}▒▒{R}█████████████████████████{RS}
{R}████████{Y}▒▒▒{R}██████████{Y}▒▒▒{R}██████████{Y}▒▒▒▒{R}█████████{Y}▒▒▒▒{R}█████████████████████████{RS}
{R}████████{Y}▒▒▒▒▒▒▒▒▒▒▒▒█{Y}▒▒▒▒▒▒▒▒▒▒▒▒█{Y}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██{Y}▒▒▒{R}████████████████{Y}▒▒▒█{RS}
{R}████████{Y}▒▒▒▒▒▒▒▒▒▒▒▒█{Y}▒▒▒▒▒▒▒▒▒▒▒▒███{Y}▒▒▒▒▒▒▒▒▒▒▒▒▒██████{Y}▒▒▒{R}████████████{Y}▒▒▒███{RS}
{R}█████████████████████████████████████████████████████████{Y}▒▒▒▒██████{Y}▒▒▒▒█████{RS}
{R}████████████████████████████████████████████████████████████{Y}▒▒▒▒▒▒▒▒{R}████████{RS}
{R}████████████████████████████████████████████████████████████████████████████{RS}
""")

def menu():
    print(f"\n{C}{'='*70}{RS}")
    print(f"{BR}{Y}{' ' * 25}MAIN MENU{RS}")
    print(f"{C}{'='*70}{RS}")
    print(f"\n  {G}[1]{RS} Start Port Scan")
    print(f"  {G}[2]{RS} Quick Scan (Common Ports)")
    print(f"  {G}[3]{RS} Full Scan (All Ports)")
    print(f"  {G}[4]{RS} Custom Scan")
    print(f"  {G}[5]{RS} About")
    print(f"  {G}[6]{RS} Exit")
    print(f"\n{C}{'='*70}{RS}")
    print(f"\n {BR}{G}┌──({C}Iceman{G}㉿{M}new hacking era!{G})-[~]{RS}")
    print(f"{BR}{G}└─$ {RS}", end="")

def get_target():
    print(f"\n{C}{'='*60}{RS}")
    print(f"{BR}{Y}TARGET CONFIGURATION{RS}")
    print(f"{C}{'='*60}{RS}")
    
    while True:
        target = input(f"\n{Y}[?]{RS} Enter target IP or hostname: ").strip()
        if target:
            try:
                host = socket.gethostbyname(target)
                print(f"{G}[+]{RS} Resolved: {target} -> {host}")
                return host
            except:
                print(f"{R}[!]{RS} Could not resolve hostname. Try again.")
        else:
            print(f"{R}[!]{RS} Target cannot be empty.")

def get_ports():
    while True:
        try:
            start = int(input(f"{Y}[?]{RS} Start port: ").strip())
            end = int(input(f"{Y}[?]{RS} End port: ").strip())
            if 1 <= start <= 65535 and 1 <= end <= 65535 and start <= end:
                print(f"{G}[+]{RS} Range: {start}-{end}")
                return start, end
            else:
                print(f"{R}[!]{RS} Invalid range. Ports must be 1-65535.")
        except:
            print(f"{R}[!]{RS} Enter valid numbers.")

def get_speed():
    print(f"\n{Y}[?]{RS} Select speed:")
    print(f"  {G}[1]{RS} Fast (200 threads)")
    print(f"  {G}[2]{RS} Normal (100 threads)")
    print(f"  {G}[3]{RS} Slow (50 threads)")
    
    while True:
        choice = input(f"\n{Y}[?]{RS} Choose (1-3): ").strip()
        if choice == "1":
            print(f"{G}[+]{RS} Fast mode")
            return 200
        elif choice == "2":
            print(f"{G}[+]{RS} Normal mode")
            return 100
        elif choice == "3":
            print(f"{G}[+]{RS} Slow mode")
            return 50
        else:
            print(f"{R}[!]{RS} Invalid choice.")

def get_version_check():
    print(f"\n{Y}[?]{RS} Enable version detection?")
    print(f"  {G}[1]{RS} Yes - Show service versions")
    print(f"  {G}[2]{RS} No - Quick scan only")
    
    while True:
        choice = input(f"\n{Y}[?]{RS} Choose (1-2): ").strip()
        if choice == "1":
            print(f"{G}[+]{RS} Version detection enabled")
            return True
        elif choice == "2":
            print(f"{G}[+]{RS} Version detection disabled")
            return False
        else:
            print(f"{R}[!]{RS} Invalid choice.")

def get_service_version(host, port):
    try:
        probe = port_versions.get_probe(port)
        service_name = port_versions.get_service_name(port)
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((host, port))
        
        if probe:
            sock.send(probe)
        
        data = sock.recv(1024).decode('utf-8', errors='ignore')
        sock.close()
        
        if data:
            data = re.sub(r'[\x00-\x1f\x7f]', ' ', data)
            data = ' '.join(data.split())
            
            version = port_versions.extract_version(service_name, data)
            if version:
                return f"{service_name} {version}"
            
            lines = data.split('\n')
            if lines and len(lines[0].strip()) > 0:
                banner = lines[0].strip()
                if len(banner) > 100:
                    banner = banner[:97] + "..."
                return banner
        
        if service_name:
            return service_name
            
        return "Unknown"
    except:
        return "Unknown"

def scan_port(host, port, open_ports, lock, show_version, port_info_cache):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.5)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            with lock:
                open_ports.append(port)
                
                service = port_versions.get_service_name(port)
                if service == 'unknown':
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                
                version = ""
                if show_version:
                    if port in port_info_cache:
                        version = port_info_cache[port]
                    else:
                        version = get_service_version(host, port)
                        port_info_cache[port] = version
                    
                    if version and version != "Unknown":
                        print(f"{G}[+]{RS} Port {C}{port:5d}{RS} is {G}OPEN{RS} ({M}{service}{RS}) - {Y}Version:{RS} {C}{version}{RS}")
                    else:
                        print(f"{G}[+]{RS} Port {C}{port:5d}{RS} is {G}OPEN{RS} ({M}{service}{RS})")
                else:
                    print(f"{G}[+]{RS} Port {C}{port:5d}{RS} is {G}OPEN{RS} ({M}{service}{RS})")
        return result == 0
    except:
        return False

def worker(host, queue, open_ports, lock, show_version, port_info_cache):
    while not queue.empty():
        try:
            port = queue.get_nowait()
            scan_port(host, port, open_ports, lock, show_version, port_info_cache)
            queue.task_done()
        except:
            break

def scan(host, start, end, threads, show_version):
    total = end - start + 1
    port_info_cache = {}
    
    print(f"\n{C}{'='*60}{RS}")
    print(f"{BR}{Y}SCANNING{RS}")
    print(f"{C}{'='*60}{RS}")
    print(f"{G}Target:{RS} {host}")
    print(f"{G}Ports:{RS} {start}-{end} ({total} ports)")
    print(f"{G}Threads:{RS} {threads}")
    print(f"{G}Version Detection:{RS} {Y}Enabled{RS}" if show_version else f"{G}Version Detection:{RS} {C}Disabled{RS}")
    print(f"{G}Known Ports in DB:{RS} {len(port_versions.PORT_VERSIONS)}")
    print(f"{G}Started:{RS} {datetime.now().strftime('%H:%M:%S')}")
    print(f"{C}{'-'*60}{RS}")
    
    start_time = time.time()
    port_queue = queue.Queue()
    open_ports = []
    lock = threading.Lock()
    
    for port in range(start, end + 1):
        port_queue.put(port)
    
    thread_list = []
    for _ in range(min(threads, total)):
        t = threading.Thread(target=worker, args=(host, port_queue, open_ports, lock, show_version, port_info_cache))
        t.start()
        thread_list.append(t)
    
    while any(t.is_alive() for t in thread_list):
        scanned = total - port_queue.qsize()
        progress = (scanned / total) * 100
        print(f"\r{Y}Progress:{RS} {progress:.1f}% ({scanned}/{total})  ", end="", flush=True)
        time.sleep(0.5)
    
    for t in thread_list:
        t.join()
    
    elapsed = time.time() - start_time
    
    print(f"\n{C}{'-'*60}{RS}")
    print(f"{BR}{G}COMPLETED{RS}")
    print(f"{C}{'='*60}{RS}")
    print(f"{G}Time:{RS} {elapsed:.2f}s")
    print(f"{G}Open ports:{RS} {BR}{Y}{len(open_ports)}{RS}")
    
    if open_ports:
        print(f"\n{BR}{G}OPEN PORTS:{RS}")
        print(f"{C}{'-'*80}{RS}")
        if show_version:
            print(f" {BR}Port    Service         Version{RS}")
            print(f"{C}{'-'*80}{RS}")
            for port in sorted(open_ports):
                service = port_versions.get_service_name(port)
                if service == 'unknown':
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                
                version = port_info_cache.get(port, "Unknown")
                if version and version != "Unknown":
                    print(f" {C}{port:5d}{RS}  {M}{service:15}{RS}  {Y}{version}{RS}")
                else:
                    print(f" {C}{port:5d}{RS}  {M}{service:15}{RS}  {C}No version info{RS}")
        else:
            print(f" {BR}Port    Service{RS}")
            print(f"{C}{'-'*80}{RS}")
            for port in sorted(open_ports):
                service = port_versions.get_service_name(port)
                if service == 'unknown':
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                print(f" {C}{port:5d}{RS}  {M}{service}{RS}")
    else:
        print(f"\n{Y}[!]{RS} No open ports found")
    
    print(f"{C}{'='*60}{RS}")
    
    save = input(f"\n{Y}[?]{RS} Save results? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"scan_{host}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Port Scan Results\n")
            f.write(f"Target: {host}\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"Ports: {start}-{end}\n")
            f.write(f"Version Detection: {'Enabled' if show_version else 'Disabled'}\n")
            f.write(f"Known Ports in DB: {len(port_versions.PORT_VERSIONS)}\n")
            f.write(f"Open ports: {len(open_ports)}\n")
            f.write(f"{'-'*60}\n")
            for port in sorted(open_ports):
                service = port_versions.get_service_name(port)
                if service == 'unknown':
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                if show_version:
                    version = port_info_cache.get(port, "Unknown")
                    f.write(f"Port {port}: {service} - Version: {version}\n")
                else:
                    f.write(f"Port {port}: {service}\n")
        print(f"{G}[+]{RS} Saved to {BR}{filename}{RS}")
    
    input(f"\n{C}Press Enter to continue...{RS}")

def quick_scan():
    host = get_target()
    show_version = get_version_check()
    scan(host, 1, 1024, 100, show_version)

def full_scan():
    print(f"\n{R}[!]{RS} {BR}Warning:{RS} This will take a long time!")
    confirm = input(f"{Y}[?]{RS} Continue? (y/n): ").strip().lower()
    if confirm == 'y':
        host = get_target()
        show_version = get_version_check()
        scan(host, 1, 65535, 200, show_version)
    else:
        print(f"{G}[+]{RS} Cancelled")
        input(f"\n{C}Press Enter to continue...{RS}")

def custom_scan():
    host = get_target()
    start, end = get_ports()
    threads = get_speed()
    show_version = get_version_check()
    print(f"\n{C}{'='*60}{RS}")
    input(f"{C}Press Enter to start...{RS}")
    scan(host, start, end, threads, show_version)

def about():
    clear()
    banner()
    print(f"{C}{'='*70}{RS}")
    print(f"{BR}{Y}{' ' * 25}ABOUT{RS}")
    print(f"{C}{'='*70}{RS}")
    print(f"\n {BR}{C}Port Scanner v3.0{RS}")
    print(f" {G}Multi-threaded port scanner with version database{RS}")
    print(f"\n {BR}Features:{RS}")
    print(f"  {G}• Fast multi-threaded scanning{RS}")
    print(f"  {G}• Version database with {len(port_versions.PORT_VERSIONS)} known ports{RS}")
    print(f"  {G}• Service version detection{RS}")
    print(f"  {G}• Progress tracking{RS}")
    print(f"  {G}• Save results{RS}")
    print(f"  {G}• Colorful output{RS}")
    print(f"\n {BR}Author:{RS} {C}Iceman{RS}")
    print(f" {BR}Version:{RS} 3.0")
    print(f"\n{C}{'='*70}{RS}")
    input(f"\n{C}Press Enter to continue...{RS}")

def main():
    while True:
        try:
            clear()
            banner()
            menu()
            
            choice = input().strip()
            
            if choice == "1":
                custom_scan()
            elif choice == "2":
                quick_scan()
            elif choice == "3":
                full_scan()
            elif choice == "4":
                custom_scan()
            elif choice == "5":
                about()
            elif choice == "6":
                print(f"\n{G}[+]{RS} Goodbye!")
                sys.exit(0)
            else:
                print(f"{R}[!]{RS} Invalid choice")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n\n{R}[!]{RS} Interrupted")
            sys.exit(0)
        except Exception as e:
            print(f"\n{R}[!]{RS} Error: {e}")
            input(f"\n{C}Press Enter to continue...{RS}")

if __name__ == "__main__":
    main()
