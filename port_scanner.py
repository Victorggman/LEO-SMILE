#!/usr/bin/env python3
import socket
import threading
import queue
import time
import os
import sys
import re
import urllib.request
import urllib.parse
import requests
from datetime import datetime

# ============================================================
# SUPPRESS SSL WARNINGS
# ============================================================
import warnings
warnings.filterwarnings("ignore")
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import port_versions
import xss_payloads
import subdomains
import admin_panels
import directories
import sql_payloads

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

def main_menu():
    print(f"""
{C}{'='*80}{RS}
{BR}{Y}{' ' * 28}MAIN MENU{RS}
{C}{'='*80}{RS}
{BR}PORT SCANNER:
  {G}[1]{RS} Quick Scan (Common Ports)
  {G}[2]{RS} Full Scan (All Ports)
  {G}[3]{RS} Custom Scan

{BR}WEB SECURITY:
  {G}[4]{RS} XSS Scanner
  {G}[5]{RS} Admin Panel Finder
  {G}[6]{RS} Subdomain Scanner
  {G}[7]{RS} Directory Bruteforcer
  {G}[8]{RS} SQL Injection Scanner

{BR}INFORMATION:
  {G}[9]{RS} About
  {G}[0]{RS} Exit
{C}{'='*80}{RS}
""")
    print(f"\n {BR}{G}┌──({C}Iceman{G}㉿{M}new hacking era!{G})-[~]{RS}")
    print(f"{BR}{G}└─$ {RS}", end="")

def port_scanner_menu():
    print(f"\n{C}{'='*70}{RS}")
    print(f"{BR}{Y}{' ' * 22}PORT SCANNER MENU{RS}")
    print(f"{C}{'='*70}{RS}")
    print(f"\n  {G}[1]{RS} Quick Scan (Common Ports)")
    print(f"  {G}[2]{RS} Full Scan (All Ports)")
    print(f"  {G}[3]{RS} Custom Scan")
    print(f"  {G}[4]{RS} Back to Main Menu")
    print(f"\n{C}{'='*70}{RS}")
    print(f"\n {BR}{G}┌──({C}Iceman{G}㉿{M}new hacking era!{G})-[~]{RS}")
    print(f"{BR}{G}└─$ {RS}", end="")

def xss_scanner_menu():
    print(f"\n{C}{'='*70}{RS}")
    print(f"{BR}{Y}{' ' * 22}XSS SCANNER MENU{RS}")
    print(f"{C}{'='*70}{RS}")
    print(f"\n  {G}[1]{RS} Light Mode (Basic XSS Detection)")
    print(f"  {G}[2]{RS} Medium Mode (Intermediate XSS Detection)")
    print(f"  {G}[3]{RS} Hard Mode (Advanced XSS Detection)")
    print(f"  {G}[4]{RS} Extreme Mode (Full XSS Detection)")
    print(f"  {G}[5]{RS} Back to Main Menu")
    print(f"\n{C}{'='*70}{RS}")
    print(f"\n {BR}{G}┌──({C}Iceman{G}㉿{M}new hacking era!{G})-[~]{RS}")
    print(f"{BR}{G}└─$ {RS}", end="")

def sql_scanner_menu():
    print(f"\n{C}{'='*70}{RS}")
    print(f"{BR}{Y}{' ' * 20}SQL INJECTION SCANNER MENU{RS}")
    print(f"{C}{'='*70}{RS}")
    print(f"\n  {G}[1]{RS} Light Mode (Basic SQLi Detection)")
    print(f"  {G}[2]{RS} Medium Mode (Advanced SQLi Detection)")
    print(f"  {G}[3]{RS} Extreme Mode (Full SQLi Detection) {R}⚠️ SLOW!{RS}")
    print(f"  {G}[4]{RS} Back to Main Menu")
    print(f"\n{C}{'='*70}{RS}")
    print(f"\n {BR}{G}┌──({C}Iceman{G}㉿{M}new hacking era!{G})-[~]{RS}")
    print(f"{BR}{G}└─$ {RS}", end="")

def get_target():
    print(f"\n{C}{'='*60}{RS}")
    print(f"{BR}{Y}TARGET CONFIGURATION{RS}")
    print(f"{C}{'='*60}{RS}")
    
    while True:
        target = input(f"\n{Y}[?]{RS} Enter target URL (http://example.com): ").strip()
        if target:
            if not target.startswith('http'):
                target = 'http://' + target
            try:
                return target
            except:
                print(f"{R}[!]{RS} Invalid URL. Try again.")
        else:
            print(f"{R}[!]{RS} Target cannot be empty.")

def get_target_for_scan():
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

def run_port_scan(host, start, end, threads, show_version):
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
    host = get_target_for_scan()
    show_version = get_version_check()
    run_port_scan(host, 1, 1024, 100, show_version)

def full_scan():
    print(f"\n{R}[!]{RS} {BR}Warning:{RS} This will take a long time!")
    confirm = input(f"{Y}[?]{RS} Continue? (y/n): ").strip().lower()
    if confirm == 'y':
        host = get_target_for_scan()
        show_version = get_version_check()
        run_port_scan(host, 1, 65535, 200, show_version)
    else:
        print(f"{G}[+]{RS} Cancelled")
        input(f"\n{C}Press Enter to continue...{RS}")

def custom_scan():
    host = get_target_for_scan()
    start, end = get_ports()
    threads = get_speed()
    show_version = get_version_check()
    print(f"\n{C}{'='*60}{RS}")
    input(f"{C}Press Enter to start...{RS}")
    run_port_scan(host, start, end, threads, show_version)

# ============================================================
# SQL INJECTION SCANNER WITH LEVELS
# ============================================================

def sql_injection_scanner():
    """SQL Injection Scanner with Light/Medium/Extreme modes"""
    while True:
        clear()
        banner()
        sql_scanner_menu()
        choice = input().strip()
        
        if choice == "1":
            sql_scan_level('light')
        elif choice == "2":
            sql_scan_level('medium')
        elif choice == "3":
            sql_scan_level('extreme')
        elif choice == "4":
            break
        else:
            print(f"{R}[!]{RS} Invalid choice")
            time.sleep(1)

def sql_scan_level(level):
    """Run SQL Injection scan at specified level"""
    
    # Define payload levels
    light_payloads = [
        "' OR '1'='1", "' OR '1'='1'--", "' OR 1=1--", "' OR 'x'='x",
        "' UNION SELECT NULL--", "' UNION SELECT NULL,NULL--", "' UNION SELECT database()--",
        "' UNION SELECT user()--", "' UNION SELECT @@version--", "' AND 1=1--",
        "' AND 1=0--", "' AND SLEEP(5)--", "' OR 1=1 AND 1=1", "' OR 'admin'='admin",
        "' OR 'password'='password", "' OR 'username'='username",
    ]
    
    medium_payloads = [
        "' OR '1'='1'#", "' OR '1'='1'/*", "' OR 1=1#", "' OR 1=1/*",
        "' UNION SELECT NULL,NULL,NULL--", "' UNION SELECT NULL,NULL,NULL,NULL--",
        "' UNION SELECT table_name FROM information_schema.tables--",
        "' UNION SELECT column_name FROM information_schema.columns--",
        "' UNION SELECT schema_name FROM information_schema.schemata--",
        "' UNION SELECT version()--", "' UNION SELECT current_user()--",
        "' AND SLEEP(10)--", "' AND BENCHMARK(1000000,MD5('A'))--",
        "' AND 1=CONVERT(int, @@version)--", "' AND extractvalue(1,concat(0x7e,@@version))--",
        "' AND updatexml(1,concat(0x7e,@@version),1)--", "' OR 1=1-- -",
        "' OR 1=1#", "' OR 1=1/*", "'/**/OR/**/1=1--", "'/*!OR*/1=1--",
        "' UNIOn SELECT NULL--", "' Union Select NULL--",
        "' OR 'admin'='admin'--", "' OR 'admin'='admin'#",
    ]
    
    extreme_payloads = sql_payloads.get_sqli_payloads()
    
    if level == 'light':
        payloads = light_payloads
        mode_name = "LIGHT"
        mode_color = G
        params = ['id', 'page', 'user', 'q']
    elif level == 'medium':
        payloads = medium_payloads
        mode_name = "MEDIUM"
        mode_color = Y
        params = ['id', 'page', 'user', 'q', 'search', 'login', 'email']
    else:  # extreme
        payloads = extreme_payloads
        mode_name = "EXTREME"
        mode_color = R
        params = ['id', 'page', 'user', 'q', 'search', 'login', 'email', 'username', 'pass', 'pwd']
    
    print(f"\n{C}{'='*70}{RS}")
    print(f"{BR}{mode_color}{' ' * 20}SQL INJECTION SCANNER - {mode_name} MODE{RS}")
    print(f"{C}{'='*70}{RS}")
    
    target = get_target()
    
    print(f"{G}[*] Mode:{RS} {mode_color}{mode_name}{RS}")
    print(f"{G}[*] Payloads:{RS} {len(payloads)}")
    print(f"{G}[*] Parameters:{RS} {len(params)}")
    print(f"{G}[*] Started:{RS} {datetime.now().strftime('%H:%M:%S')}")
    print(f"{C}{'-'*60}{RS}")
    
    vulnerabilities = []
    total_tests = len(payloads) * len(params)
    tested = 0
    
    for param in params:
        for payload in payloads:
            tested += 1
            progress = (tested / total_tests) * 100
            sys.stdout.write(f"\r{Y}Progress:{RS} {progress:.1f}% ({tested}/{total_tests})")
            sys.stdout.flush()
            
            try:
                test_url = f"{target}?{param}={urllib.parse.quote(payload)}"
                response = requests.get(test_url, timeout=5, verify=False)
                
                sql_errors = ['sql', 'mysql', 'syntax error', 'database error', 
                             'unclosed quotation', 'odbc', 'driver', 'db2',
                             'oracle', 'sql server', 'postgresql', 'sqlite',
                             'you have an error', 'warning: mysql', 'mysqli',
                             'division by zero', 'column not found', 'table not found']
                
                if any(error in response.text.lower() for error in sql_errors):
                    vulnerabilities.append({
                        'param': param,
                        'payload': payload,
                        'url': test_url
                    })
                    print(f"\n{R}[!] SQLi Found! Param: {param} -> {payload[:40]}{RS}")
            except:
                pass
    
    print(f"\n\n{C}{'='*70}{RS}")
    print(f"{BR}{G}SCAN COMPLETE - {mode_name} MODE{RS}")
    print(f"{C}{'='*70}{RS}")
    print(f"{G}Tests:{RS} {total_tests}")
    print(f"{G}Vulnerabilities:{RS} {BR}{Y}{len(vulnerabilities)}{RS}")
    
    if vulnerabilities:
        print(f"\n{R}[!] SQL Injection Vulnerabilities Found:{RS}")
        print(f"{C}{'-'*80}{RS}")
        for i, v in enumerate(vulnerabilities, 1):
            print(f"\n{Y}[{i}]{RS} Parameter: {C}{v['param']}{RS}")
            print(f"    Payload: {Y}{v['payload']}{RS}")
            print(f"    URL: {M}{v['url']}{RS}")
        
        save = input(f"\n{Y}[?]{RS} Save results? (y/n): ").strip().lower()
        if save == 'y':
            filename = f"sqli_{mode_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                f.write(f"SQL Injection Scan Results\n")
                f.write(f"Target: {target}\n")
                f.write(f"Mode: {mode_name}\n")
                f.write(f"Date: {datetime.now()}\n")
                f.write(f"Total Tests: {total_tests}\n")
                f.write(f"Vulnerabilities Found: {len(vulnerabilities)}\n")
                f.write(f"{'-'*60}\n\n")
                for v in vulnerabilities:
                    f.write(f"Parameter: {v['param']}\n")
                    f.write(f"Payload: {v['payload']}\n")
                    f.write(f"URL: {v['url']}\n")
                    f.write(f"{'-'*40}\n")
            print(f"{G}[+]{RS} Saved to {BR}{filename}{RS}")
    else:
        print(f"\n{G}[+] No SQL injection vulnerabilities found{RS}")
    
    input(f"\n{C}Press Enter to continue...{RS}")

# ============================================================
# XSS SCANNER FUNCTIONS
# ============================================================

def test_xss_payload(url, payload, params):
    try:
        test_url = url + '?' + urllib.parse.urlencode(params)
        req = urllib.request.Request(test_url)
        req.add_header('User-Agent', 'Mozilla/5.0 (XSS Scanner)')
        response = urllib.request.urlopen(req, timeout=5)
        content = response.read().decode('utf-8', errors='ignore')
        
        if payload in content:
            return True
        return False
    except:
        return False

def scan_xss(url, level):
    print(f"\n{C}{'='*60}{RS}")
    print(f"{BR}{Y}XSS VULNERABILITY SCAN{RS}")
    print(f"{C}{'='*60}{RS}")
    print(f"{G}Target:{RS} {url}")
    print(f"{G}Mode:{RS} {Y}{level.upper()}{RS}")
    
    payloads = xss_payloads.get_payloads(level)
    print(f"{G}Total Payloads:{RS} {len(payloads)}")
    print(f"{G}Started:{RS} {datetime.now().strftime('%H:%M:%S')}")
    print(f"{C}{'-'*60}{RS}")
    
    vulnerabilities = []
    params = {'q': '', 'search': '', 'input': '', 'test': ''}
    total = len(payloads) * len(params)
    tested = 0
    
    for param in params:
        for payload in payloads:
            params[param] = payload
            tested += 1
            progress = (tested / total) * 100
            print(f"\r{Y}Progress:{RS} {progress:.1f}% ({tested}/{total}) - Testing {param} with {payload[:30]}...", end="", flush=True)
            
            try:
                if test_xss_payload(url, payload, params):
                    vulnerabilities.append({
                        'param': param,
                        'payload': payload,
                        'url': url + '?' + urllib.parse.urlencode(params)
                    })
                    print(f"\n{G}[!]{RS} XSS Found! Parameter: {C}{param}{RS} Payload: {Y}{payload[:50]}{RS}")
            except:
                pass
            params[param] = ''
            time.sleep(0.1)
    
    print(f"\n{C}{'-'*60}{RS}")
    print(f"{BR}{G}SCAN COMPLETED{RS}")
    print(f"{C}{'='*60}{RS}")
    print(f"{G}Total tests:{RS} {total}")
    print(f"{G}Vulnerabilities found:{RS} {BR}{Y}{len(vulnerabilities)}{RS}")
    
    if vulnerabilities:
        print(f"\n{BR}{R}VULNERABILITIES DETECTED:{RS}")
        print(f"{C}{'-'*80}{RS}")
        for i, vuln in enumerate(vulnerabilities, 1):
            print(f"\n{Y}[{i}]{RS} Parameter: {C}{vuln['param']}{RS}")
            print(f"    Payload: {Y}{vuln['payload']}{RS}")
            print(f"    URL: {M}{vuln['url']}{RS}")
    else:
        print(f"\n{G}[+]{RS} No XSS vulnerabilities found with {level} mode.")
    
    print(f"{C}{'='*60}{RS}")
    
    save = input(f"\n{Y}[?]{RS} Save results? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"xss_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"XSS Vulnerability Scan Results\n")
            f.write(f"Target: {url}\n")
            f.write(f"Mode: {level.upper()}\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"Total payloads tested: {len(payloads)}\n")
            f.write(f"Vulnerabilities found: {len(vulnerabilities)}\n")
            f.write(f"{'-'*60}\n")
            for vuln in vulnerabilities:
                f.write(f"Parameter: {vuln['param']}\n")
                f.write(f"Payload: {vuln['payload']}\n")
                f.write(f"URL: {vuln['url']}\n")
                f.write(f"{'-'*40}\n")
        print(f"{G}[+]{RS} Saved to {BR}{filename}{RS}")
    
    input(f"\n{C}Press Enter to continue...{RS}")

def xss_light():
    url = get_target()
    scan_xss(url, 'light')

def xss_medium():
    url = get_target()
    scan_xss(url, 'medium')

def xss_hard():
    url = get_target()
    scan_xss(url, 'hard')

def xss_extreme():
    url = get_target()
    print(f"\n{R}[!]{RS} {BR}Warning:{RS} Extreme mode uses 100+ advanced payloads and may take a while!")
    confirm = input(f"{Y}[?]{RS} Continue? (y/n): ").strip().lower()
    if confirm == 'y':
        scan_xss(url, 'extreme')
    else:
        print(f"{G}[+]{RS} Cancelled")
        input(f"\n{C}Press Enter to continue...{RS}")

def admin_panel_finder():
    clear()
    banner()
    print(f"\n{C}{'='*70}{RS}")
    print(f"{BR}{Y}{' ' * 20}ADMIN PANEL FINDER{RS}")
    print(f"{C}{'='*70}{RS}")
    
    target = get_target()
    if not target.endswith('/'):
        target += '/'
    
    print(f"\n{Y}[?]{RS} Select scan mode:")
    print(f"  {G}[1]{RS} Quick (100 random paths)")
    print(f"  {G}[2]{RS} Normal (500 paths)")
    print(f"  {G}[3]{RS} Full (All {admin_panels.get_panel_count()} paths)")
    print(f"  {G}[4]{RS} Custom (Enter your own wordlist file)")
    
    while True:
        mode = input(f"\n{Y}[?]{RS} Choose (1-4): ").strip()
        if mode in ['1', '2', '3', '4']:
            break
        print(f"{R}[!]{RS} Invalid choice")
    
    if mode == '1':
        wordlist = admin_panels.get_admin_panels()[:100]
    elif mode == '2':
        wordlist = admin_panels.get_admin_panels()[:500]
    elif mode == '3':
        wordlist = admin_panels.get_admin_panels()
    elif mode == '4':
        file_path = input(f"\n{Y}[?]{RS} Enter wordlist file path: ").strip()
        try:
            with open(file_path, 'r') as f:
                wordlist = [line.strip() for line in f if line.strip()]
            print(f"{G}[+]{RS} Loaded {len(wordlist)} paths from file")
        except:
            print(f"{R}[!]{RS} Could not load file, using default list")
            wordlist = admin_panels.get_admin_panels()
    
    print(f"\n{Y}[?]{RS} Enter max threads (default 50): ")
    try:
        threads = int(input().strip())
        if threads <= 0:
            threads = 50
    except:
        threads = 50
    
    print(f"\n{C}{'='*60}{RS}")
    print(f"{BR}{Y}SCANNING FOR ADMIN PANELS{RS}")
    print(f"{C}{'='*60}{RS}")
    print(f"{G}Target:{RS} {target}")
    print(f"{G}Paths to check:{RS} {len(wordlist)}")
    print(f"{G}Threads:{RS} {threads}")
    print(f"{G}Started:{RS} {datetime.now().strftime('%H:%M:%S')}")
    print(f"{C}{'-'*60}{RS}")
    
    found = []
    lock = threading.Lock()
    scan_queue = queue.Queue()
    
    for path in wordlist:
        scan_queue.put(path)
    
    def admin_worker():
        while not scan_queue.empty():
            try:
                path = scan_queue.get_nowait()
                test_url = target + path
                
                try:
                    start_time_req = time.time()
                    response = requests.get(test_url, timeout=5, allow_redirects=False)
                    elapsed = time.time() - start_time_req
                    
                    status = response.status_code
                    
                    if status in [200, 301, 302, 303, 307, 308]:
                        with lock:
                            found.append({
                                'url': test_url,
                                'status': status,
                                'size': len(response.content),
                                'time': elapsed
                            })
                            
                            status_color = G if status == 200 else Y
                            print(f"{G}[+]{RS} Found: {C}{test_url}{RS} {status_color}[{status}]{RS} {B}({len(response.content)} bytes){RS}")
                except:
                    pass
                scan_queue.task_done()
            except:
                break
    
    start_time = time.time()
    thread_list = []
    
    for _ in range(min(threads, len(wordlist))):
        t = threading.Thread(target=admin_worker)
        t.start()
        thread_list.append(t)
    
    while any(t.is_alive() for t in thread_list):
        scanned = len(wordlist) - scan_queue.qsize()
        progress = (scanned / len(wordlist)) * 100
        print(f"\r{Y}Progress:{RS} {progress:.1f}% ({scanned}/{len(wordlist)})  ", end="", flush=True)
        time.sleep(0.5)
    
    for t in thread_list:
        t.join()
    
    elapsed = time.time() - start_time
    
    print(f"\n{C}{'-'*60}{RS}")
    print(f"{BR}{G}SCAN COMPLETED{RS}")
    print(f"{C}{'='*60}{RS}")
    print(f"{G}Time:{RS} {elapsed:.2f}s")
    print(f"{G}Paths checked:{RS} {len(wordlist)}")
    print(f"{G}Found:{RS} {BR}{Y}{len(found)}{RS}")
    
    if found:
        print(f"\n{BR}{G}FOUND ADMIN PANELS:{RS}")
        print(f"{C}{'-'*80}{RS}")
        print(f" {BR}Status  URL{RS}")
        print(f"{C}{'-'*80}{RS}")
        for item in sorted(found, key=lambda x: x['status']):
            status_color = G if item['status'] == 200 else Y
            print(f" {status_color}{item['status']}{RS}   {C}{item['url']}{RS} {B}({item['size']} bytes){RS}")
    else:
        print(f"\n{Y}[!]{RS} No admin panels found")
    
    print(f"{C}{'='*60}{RS}")
    
    save = input(f"\n{Y}[?]{RS} Save results? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"admin_panels_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Admin Panel Scan Results\n")
            f.write(f"Target: {target}\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"Paths checked: {len(wordlist)}\n")
            f.write(f"Found: {len(found)}\n")
            f.write(f"{'-'*60}\n")
            for item in found:
                f.write(f"{item['status']} - {item['url']} ({item['size']} bytes)\n")
        print(f"{G}[+]{RS} Saved to {BR}{filename}{RS}")
    
    input(f"\n{C}Press Enter to continue...{RS}")

def subdomain_scanner():
    clear()
    banner()
    print(f"\n{C}{'='*70}{RS}")
    print(f"{BR}{Y}{' ' * 20}SUBDOMAIN SCANNER{RS}")
    print(f"{C}{'='*70}{RS}")
    
    domain = input(f"\n{Y}[?]{RS} Enter domain (example.com): ").strip().lower()
    if not domain:
        print(f"{R}[!]{RS} Domain cannot be empty")
        return
    
    domain = domain.replace('http://', '').replace('https://', '')
    if domain.startswith('www.'):
        domain = domain[4:]
    
    print(f"\n{Y}[?]{RS} Select scan mode:")
    print(f"  {G}[1]{RS} Quick (100 subdomains)")
    print(f"  {G}[2]{RS} Normal (500 subdomains)")
    print(f"  {G}[3]{RS} Full (All {subdomains.get_subdomain_count()} subdomains)")
    print(f"  {G}[4]{RS} Custom (Enter your own wordlist file)")
    
    while True:
        mode = input(f"\n{Y}[?]{RS} Choose (1-4): ").strip()
        if mode in ['1', '2', '3', '4']:
            break
        print(f"{R}[!]{RS} Invalid choice")
    
    if mode == '1':
        wordlist = subdomains.get_subdomains()[:100]
    elif mode == '2':
        wordlist = subdomains.get_subdomains()[:500]
    elif mode == '3':
        wordlist = subdomains.get_subdomains()
    elif mode == '4':
        file_path = input(f"\n{Y}[?]{RS} Enter wordlist file path: ").strip()
        try:
            with open(file_path, 'r') as f:
                wordlist = [line.strip() for line in f if line.strip()]
            print(f"{G}[+]{RS} Loaded {len(wordlist)} subdomains from file")
        except:
            print(f"{R}[!]{RS} Could not load file, using default list")
            wordlist = subdomains.get_subdomains()
    
    print(f"\n{Y}[?]{RS} Enter max threads (default 100): ")
    try:
        threads = int(input().strip())
        if threads <= 0:
            threads = 100
    except:
        threads = 100
    
    try:
        main_ip = socket.gethostbyname(domain)
        print(f"{G}[+]{RS} Main domain IP: {main_ip}")
    except:
        main_ip = None
        print(f"{Y}[!]{RS} Could not resolve main domain, continuing anyway...")
    
    print(f"\n{C}{'='*60}{RS}")
    print(f"{BR}{Y}SCANNING SUBDOMAINS{RS}")
    print(f"{C}{'='*60}{RS}")
    print(f"{G}Domain:{RS} {domain}")
    print(f"{G}Subdomains to check:{RS} {len(wordlist)}")
    print(f"{G}Threads:{RS} {threads}")
    print(f"{G}Started:{RS} {datetime.now().strftime('%H:%M:%S')}")
    print(f"{C}{'-'*60}{RS}")
    
    found = []
    lock = threading.Lock()
    scan_queue = queue.Queue()
    total = len(wordlist)
    start_time = time.time()
    
    for sub in wordlist:
        scan_queue.put(sub)
    
    def sub_worker():
        while not scan_queue.empty():
            try:
                sub = scan_queue.get_nowait()
                full_domain = f"{sub}.{domain}"
                
                try:
                    ip = socket.gethostbyname(full_domain)
                    
                    if ip != main_ip or main_ip is None:
                        with lock:
                            found.append({
                                'subdomain': full_domain,
                                'ip': ip
                            })
                            print(f"{G}[+]{RS} Found: {C}{full_domain}{RS} -> {Y}{ip}{RS}")
                    else:
                        with lock:
                            found.append({
                                'subdomain': full_domain,
                                'ip': ip,
                                'note': 'Same IP as main domain'
                            })
                            print(f"{Y}[!]{RS} Found: {C}{full_domain}{RS} -> {Y}{ip}{RS} (Same IP)")
                except socket.gaierror:
                    pass
                except:
                    pass
                
                scan_queue.task_done()
            except:
                break
    
    thread_list = []
    for _ in range(min(threads, len(wordlist))):
        t = threading.Thread(target=sub_worker)
        t.start()
        thread_list.append(t)
    
    while any(t.is_alive() for t in thread_list):
        scanned = total - scan_queue.qsize()
        progress = (scanned / total) * 100
        elapsed = time.time() - start_time
        if scanned > 0:
            eta = (elapsed / scanned) * (total - scanned)
            eta_str = f"{int(eta//60)}m {int(eta%60)}s"
        else:
            eta_str = "Calculating..."
        
        print(f"\r{Y}Progress:{RS} {progress:.1f}% ({scanned}/{total}) | {G}ETA:{RS} {eta_str}  ", end="", flush=True)
        time.sleep(0.5)
    
    for t in thread_list:
        t.join()
    
    elapsed = time.time() - start_time
    
    print(f"\n{C}{'-'*60}{RS}")
    print(f"{BR}{G}SCAN COMPLETED{RS}")
    print(f"{C}{'='*60}{RS}")
    print(f"{G}Time:{RS} {elapsed:.2f}s")
    print(f"{G}Subdomains checked:{RS} {len(wordlist)}")
    print(f"{G}Found:{RS} {BR}{Y}{len(found)}{RS}")
    
    if found:
        print(f"\n{BR}{G}FOUND SUBDOMAINS:{RS}")
        print(f"{C}{'-'*80}{RS}")
        print(f" {BR}Subdomain{' ' * 40}IP Address{RS}")
        print(f"{C}{'-'*80}{RS}")
        
        for item in sorted(found, key=lambda x: x['subdomain']):
            note = f" {Y}({item.get('note', '')}){RS}" if 'note' in item else ""
            print(f" {C}{item['subdomain']:50}{RS} {G}{item['ip']}{RS}{note}")
    else:
        print(f"\n{Y}[!]{RS} No subdomains found")
    
    print(f"{C}{'='*60}{RS}")
    
    save = input(f"\n{Y}[?]{RS} Save results? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"subdomains_{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Subdomain Scan Results\n")
            f.write(f"Domain: {domain}\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"Subdomains checked: {len(wordlist)}\n")
            f.write(f"Found: {len(found)}\n")
            f.write(f"{'-'*60}\n\n")
            for item in sorted(found, key=lambda x: x['subdomain']):
                f.write(f"{item['subdomain']} -> {item['ip']}\n")
                if 'note' in item:
                    f.write(f"  Note: {item['note']}\n")
        print(f"{G}[+]{RS} Saved to {BR}{filename}{RS}")
    
    input(f"\n{C}Press Enter to continue...{RS}")

def directory_bruteforcer():
    clear()
    banner()
    print(f"\n{C}{'='*70}{RS}")
    print(f"{BR}{Y}{' ' * 15}DIRECTORY BRUTEFORCER{RS}")
    print(f"{C}{'='*70}{RS}")
    
    target = get_target()
    if not target.endswith('/'):
        target += '/'
    
    print(f"\n{Y}[?]{RS} Select scan mode:")
    print(f"  {G}[1]{RS} Quick (100 random paths)")
    print(f"  {G}[2]{RS} Normal (500 paths)")
    print(f"  {G}[3]{RS} Full (All {directories.get_directory_count()} paths)")
    print(f"  {G}[4]{RS} Custom (Enter your own wordlist file)")
    
    while True:
        mode = input(f"\n{Y}[?]{RS} Choose (1-4): ").strip()
        if mode in ['1', '2', '3', '4']:
            break
        print(f"{R}[!]{RS} Invalid choice")
    
    if mode == '1':
        wordlist = directories.get_directories()[:100]
    elif mode == '2':
        wordlist = directories.get_directories()[:500]
    elif mode == '3':
        wordlist = directories.get_directories()
    elif mode == '4':
        file_path = input(f"\n{Y}[?]{RS} Enter wordlist file path: ").strip()
        try:
            with open(file_path, 'r') as f:
                wordlist = [line.strip() for line in f if line.strip()]
            print(f"{G}[+]{RS} Loaded {len(wordlist)} paths from file")
        except:
            print(f"{R}[!]{RS} Could not load file, using default list")
            wordlist = directories.get_directories()
    
    print(f"\n{Y}[?]{RS} Enter max threads (default 50): ")
    try:
        threads = int(input().strip())
        if threads <= 0:
            threads = 50
    except:
        threads = 50
    
    print(f"\n{Y}[?]{RS} Filter results:")
    print(f"  {G}[1]{RS} Show all status codes")
    print(f"  {G}[2]{RS} Only show 200 OK")
    print(f"  {G}[3]{RS} Only show 403 Forbidden")
    print(f"  {G}[4]{RS} Only show redirects (3xx)")
    
    while True:
        filter_choice = input(f"\n{Y}[?]{RS} Choose (1-4): ").strip()
        if filter_choice in ['1', '2', '3', '4']:
            break
        print(f"{R}[!]{RS} Invalid choice")
    
    print(f"\n{C}{'='*60}{RS}")
    print(f"{BR}{Y}SCANNING DIRECTORIES{RS}")
    print(f"{C}{'='*60}{RS}")
    print(f"{G}Target:{RS} {target}")
    print(f"{G}Paths to check:{RS} {len(wordlist)}")
    print(f"{G}Threads:{RS} {threads}")
    print(f"{G}Started:{RS} {datetime.now().strftime('%H:%M:%S')}")
    print(f"{C}{'-'*60}{RS}")
    
    found = []
    lock = threading.Lock()
    scan_queue = queue.Queue()
    total = len(wordlist)
    start_time = time.time()
    
    for path in wordlist:
        scan_queue.put(path)
    
    def dir_worker():
        while not scan_queue.empty():
            try:
                path = scan_queue.get_nowait()
                test_url = target + path
                
                try:
                    start_time_req = time.time()
                    response = requests.get(test_url, timeout=5, allow_redirects=False)
                    elapsed = time.time() - start_time_req
                    
                    status = response.status_code
                    
                    show = False
                    if filter_choice == '1':
                        show = True
                    elif filter_choice == '2' and status == 200:
                        show = True
                    elif filter_choice == '3' and status == 403:
                        show = True
                    elif filter_choice == '4' and 300 <= status < 400:
                        show = True
                    
                    if show:
                        with lock:
                            found.append({
                                'url': test_url,
                                'status': status,
                                'size': len(response.content),
                                'time': elapsed
                            })
                            
                            if status == 200:
                                status_color = G
                            elif 300 <= status < 400:
                                status_color = Y
                            elif 400 <= status < 500:
                                status_color = R
                            else:
                                status_color = C
                            
                            print(f"{status_color}[{status}]{RS} {C}{test_url}{RS} {B}({len(response.content)} bytes){RS}")
                except:
                    pass
                scan_queue.task_done()
            except:
                break
    
    thread_list = []
    for _ in range(min(threads, len(wordlist))):
        t = threading.Thread(target=dir_worker)
        t.start()
        thread_list.append(t)
    
    while any(t.is_alive() for t in thread_list):
        scanned = total - scan_queue.qsize()
        progress = (scanned / total) * 100
        elapsed = time.time() - start_time
        if scanned > 0:
            eta = (elapsed / scanned) * (total - scanned)
            eta_str = f"{int(eta//60)}m {int(eta%60)}s"
        else:
            eta_str = "Calculating..."
        
        print(f"\r{Y}Progress:{RS} {progress:.1f}% ({scanned}/{total}) | {G}ETA:{RS} {eta_str}  ", end="", flush=True)
        time.sleep(0.5)
    
    for t in thread_list:
        t.join()
    
    elapsed = time.time() - start_time
    
    print(f"\n{C}{'-'*60}{RS}")
    print(f"{BR}{G}SCAN COMPLETED{RS}")
    print(f"{C}{'='*60}{RS}")
    print(f"{G}Time:{RS} {elapsed:.2f}s")
    print(f"{G}Paths checked:{RS} {len(wordlist)}")
    print(f"{G}Found:{RS} {BR}{Y}{len(found)}{RS}")
    
    if found:
        print(f"\n{BR}{G}FOUND PATHS:{RS}")
        print(f"{C}{'-'*80}{RS}")
        print(f" {BR}Status  URL{RS}")
        print(f"{C}{'-'*80}{RS}")
        for item in sorted(found, key=lambda x: x['status']):
            if item['status'] == 200:
                status_color = G
            elif 300 <= item['status'] < 400:
                status_color = Y
            elif 400 <= item['status'] < 500:
                status_color = R
            else:
                status_color = C
            print(f" {status_color}{item['status']}{RS}   {C}{item['url']}{RS} {B}({item['size']} bytes){RS}")
    else:
        print(f"\n{Y}[!]{RS} No paths found")
    
    print(f"{C}{'='*60}{RS}")
    
    save = input(f"\n{Y}[?]{RS} Save results? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"directory_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Directory Bruteforce Results\n")
            f.write(f"Target: {target}\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"Paths checked: {len(wordlist)}\n")
            f.write(f"Found: {len(found)}\n")
            f.write(f"{'-'*60}\n")
            for item in found:
                f.write(f"{item['status']} - {item['url']} ({item['size']} bytes)\n")
        print(f"{G}[+]{RS} Saved to {BR}{filename}{RS}")
    
    input(f"\n{C}Press Enter to continue...{RS}")

def about():
    clear()
    banner()
    print(f"{C}{'='*70}{RS}")
    print(f"{BR}{Y}{' ' * 25}ABOUT{RS}")
    print(f"{C}{'='*70}{RS}")
    print(f"\n {BR}{C}Multi-Tool v3.0{RS}")
    print(f" {G}Complete Security Testing Suite{RS}")
    print(f"\n {BR}Features:{RS}")
    print(f"  {G}• Multi-threaded port scanning{RS}")
    print(f"  {G}• Service version detection{RS}")
    print(f"  {G}• XSS vulnerability scanning (4 modes){RS}")
    print(f"  {G}• Admin panel finder (600+ paths){RS}")
    print(f"  {G}• Subdomain scanner (1000+ subdomains){RS}")
    print(f"  {G}• Directory bruteforcer (1000+ directories){RS}")
    print(f"  {G}• SQL Injection scanner (Light/Medium/Extreme){RS}")
    print(f"  {G}• 100+ XSS payloads{RS}")
    print(f"  {G}• Progress tracking with ETA{RS}")
    print(f"  {G}• Save results to file{RS}")
    print(f"  {G}• Colorful terminal output{RS}")
    print(f"\n {BR}Author:{RS} {C}Iceman{RS}")
    print(f" {BR}Version:{RS} 3.0")
    print(f"\n{C}{'='*70}{RS}")
    input(f"\n{C}Press Enter to continue...{RS}")

def handle_port_scanner():
    while True:
        clear()
        banner()
        port_scanner_menu()
        choice = input().strip()
        
        if choice == "1":
            quick_scan()
        elif choice == "2":
            full_scan()
        elif choice == "3":
            custom_scan()
        elif choice == "4":
            break
        else:
            print(f"{R}[!]{RS} Invalid choice")
            time.sleep(1)

def handle_xss_scanner():
    while True:
        clear()
        banner()
        xss_scanner_menu()
        choice = input().strip()
        
        if choice == "1":
            xss_light()
        elif choice == "2":
            xss_medium()
        elif choice == "3":
            xss_hard()
        elif choice == "4":
            xss_extreme()
        elif choice == "5":
            break
        else:
            print(f"{R}[!]{RS} Invalid choice")
            time.sleep(1)

def main():
    while True:
        try:
            clear()
            banner()
            main_menu()
            
            choice = input().strip()
            
            if choice == "1":
                handle_port_scanner()
            elif choice == "2":
                full_scan()
            elif choice == "3":
                custom_scan()
            elif choice == "4":
                handle_xss_scanner()
            elif choice == "5":
                admin_panel_finder()
            elif choice == "6":
                subdomain_scanner()
            elif choice == "7":
                directory_bruteforcer()
            elif choice == "8":
                sql_injection_scanner()
            elif choice == "9":
                about()
            elif choice == "0":
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
