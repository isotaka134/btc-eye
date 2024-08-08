import requests
from colorama import Fore, Style, init
import os

init(autoreset=True)

def print_banner():
    banner = r"""
     .S_SSSs    sdSS_SSSSSSbs    sSSs          sSSs   .S S.     sSSs  
.SS~SSSSS   YSSS~S%SSSSSP   d%%SP         d%%SP  .SS SS.   d%%SP  
S%S   SSSS       S%S       d%S'          d%S'    S%S S%S  d%S'    
S%S    S%S       S%S       S%S           S%S     S%S S%S  S%S     
S%S SSSS%P       S&S       S&S           S&S     S%S S%S  S&S     
S&S  SSSY        S&S       S&S           S&S_Ss   SS SS   S&S_Ss  
S&S    S&S       S&S       S&S           S&S~SP    S S    S&S~SP  
S&S    S&S       S&S       S&S           S&S       SSS    S&S     
S*S    S&S       S*S       S*b           S*b       S*S    S*b     
S*S    S*S       S*S       S*S.          S*S.      S*S    S*S.    
S*S SSSSP        S*S        SSSbs         SSSbs    S*S     SSSbs  
S*S  SSY         S*S         YSSP          YSSP    S*S      YSSP  
SP               SP                                SP             
Y                Y                                 Y              

ISOTAKA NOBOMARO ===> location: MA ===> IG: isotaka.nobomaro	                                                                  
    """
    
    print(f"{Fore.RED}{banner.center(os.get_terminal_size().columns)}")

def get_bitcoin_info(wallet_address, option):
   
    url = f"https://blockchain.info/rawaddr/{wallet_address}"

    try:
        response = requests.get(url)
        data = response.json()

        balance = data.get('final_balance', 0) / 1e8  
        total_received = data.get('total_received', 0) / 1e8  
        total_sent = data.get('total_sent', 0) / 1e8  
        transactions = len(data.get('txs', []))  
        wallet_link = f"https://www.blockchain.com/btc/address/{wallet_address}"

        if option == "1":
            print(f"{Fore.GREEN}[*] Balance: {balance} BTC")
        elif option == "2":
            print(f"{Fore.GREEN}[*] Total Sent: {total_sent} BTC")
        elif option == "3":
            print(f"{Fore.GREEN}[*] Total Received: {total_received} BTC")
        elif option == "4":
            print(f"{Fore.GREEN}[*] Number of Transactions: {transactions}")
        elif option == "5":
            print(f"{Fore.GREEN}[*] Wallet Web Link: {wallet_link}")
        else:
            print(f"{Fore.RED}[*] Invalid option.")

    except Exception as e:
        print(f"{Fore.RED}[*] Error retrieving data: {e}")

def main():
    print_banner()  

    print(f"\n{Fore.BLUE}Enter the Bitcoin wallet address:")
    wallet_address = input("> ")

    while True:
        print(f"\n{Fore.BLUE}Choose an option:")
        print(f"1. {Fore.BLUE}Balance")
        print(f"2. {Fore.BLUE}Total Sent")
        print(f"3. {Fore.BLUE}Total Received")
        print(f"4. {Fore.BLUE}Number of Transactions")
        print(f"5. {Fore.BLUE}Wallet Website Link")
        print(f"6. {Fore.BLUE}Exit")
        
        option = input("> ")

        if option == "6":
            print(f"{Fore.GREEN}[*] Exiting program.")
            break

        print(f"{Fore.GREEN}{'-'*40}")
        get_bitcoin_info(wallet_address, option)
        print(f"{Fore.GREEN}{'-'*40}")

if __name__ == "__main__":
    main()
