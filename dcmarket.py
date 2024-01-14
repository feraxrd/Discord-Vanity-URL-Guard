import requests # discord.gg/dcmarket
import time # discord.gg/dcmarket
from colorama import init, Fore, Style # discord.gg/dcmarket
from termcolor import colored # discord.gg/dcmarket

init()

green = Fore.GREEN # discord.gg/dcmarket
blue = Fore.BLUE # discord.gg/dcmarket
red = Fore.RED # discord.gg/dcmarket
yellow = Fore.YELLOW # discord.gg/dcmarket
reset = Style.RESET_ALL # discord.gg/dcmarket

def check_url(token, server_id, url):
    headers = {"Authorization": token}
    
    while True:
        response = requests.get(f"https://discord.com/api/v9/invites/{url}?with_counts=true&with_expiration=true", headers=headers) # discord.gg/dcmarket
        
        if response.status_code == 200:
            print(colored(f"URL mevcut sunucuda: {url}", 'yellow')) # discord.gg/dcmarket
        else:
            print(colored(f"URL sunucuda bulunmuyor: {url}", 'red')) # discord.gg/dcmarket 
            print(colored("Eski URL geri yüklendi.", 'green')) # discord.gg/dcmarket 
            restore_url(token, server_id, url) # discord.gg/dcmarket
        
        time.sleep(1) # discord.gg/dcmarket

def restore_url(token, server_id, url): 
    headers = {"Authorization": token} # discord.gg/dcmarket
    
    data = {"code": url} # discord.gg/dcmarket
    response = requests.patch(f"https://discord.com/api/v9/guilds/{server_id}/vanity-url", headers=headers, json=data) # discord.gg/dcmarket
    
    if response.status_code == 200:
        print(colored(f"Eski URL başarıyla geri yüklendi: {url}", 'green')) # discord.gg/dcmarket
    else:
        print(colored(f"Malesef Eski URL geri yüklenemedi: {url}", 'red')) # discord.gg/dcmarket

def main():
    token = input(colored("Token'i girin: ", 'blue')) # discord.gg/dcmarket
    server_id = input(colored("Sunucu ID'sini girin: ", 'blue')) # discord.gg/dcmarket
    url = input(colored("Kontrol edilecek URL'yi girin: ", 'blue')) # discord.gg/dcmarket
    
    check_url(token, server_id, url) # discord.gg/dcmarket

if __name__ == "__main__": 
    main() # discord.gg/dcmarket
