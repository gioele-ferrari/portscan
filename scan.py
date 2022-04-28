import ipaddress
import pyfiglet
import socket
import re
import os
from colorama import Fore, Back, init

init(autoreset = True)

# Define delle porte min e max e pattern di input
port_min = 0
port_max = 65536
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Header del programma
ascii_banner = pyfiglet.figlet_format("PORT SCANNER", font = "slant")
clear = lambda: os.system('cls')
clear()
print(Fore.LIGHTGREEN_EX + '-' * 75)
print('\n' + Fore.LIGHTGREEN_EX + ascii_banner)
print(Fore.LIGHTGREEN_EX + '-' * 75)
open_ports = []
# Inserimento ip per lo scan
while True:
    ip_to_scan = input('> Inserisci un indirizzo per lo scan: ')
    try:
        ip_address_check = ipaddress.ip_address(ip_to_scan)
        break
    except:
        print(Fore.LIGHTYELLOW_EX + '! Indirizzo non valido.')

# Inserimento delle porte 
while True:
    # Spieghiamo all'utente come usare il programma
    print(Fore.LIGHTCYAN_EX + '# Inserisci il range di porte su cui fare lo scan nel formato <int>-<int>')
    port_range = input('> Inserisci le porte: ')
    # Nel caso inserissimo port - port invece di port-port il programma funziona ugualmente
    port_range_validation = port_range_pattern.search(port_range.replace(" ", ""))
    # Nal caso sia andato tutto bene prendiamo la porta min e max grazie al pattern impostato
    if port_range_validation:
        port_min = int(port_range_validation.group(1))
        port_max = int(port_range_validation.group(2))
        break
# Stampa le informazioni riguardo allo scan
print('-' * 75)
print(Fore.LIGHTGREEN_EX + f'+ Scanning IP: {ip_to_scan} Port Min: {port_min} Port Max: {port_max}')
print('-' * 75)
# Proviamo a verificare ogni porta nel range
for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # 0.5 secondi permette di dare abbastanza tempo per verificare la connessione 
            s.settimeout(0.5)
            s.connect((ip_to_scan, port))
            # Nel caso sia aperta, aggiunge all'array
            open_ports.append(port)
    except:
        pass
# Se ci sono porte aperte, le mostra altrimenti invia un 'errore'
if len(open_ports):
    for port in open_ports:
        print(Fore.LIGHTGREEN_EX + f'+ Port {port} is open.')
else:
    print(Fore.LIGHTRED_EX + f'@ No port open in the range')