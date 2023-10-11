import requests

# Logo
logo = """
░██████╗██╗░░░██╗██████╗░
██╔════╝██║░░░██║██╔══██╗
╚█████╗░██║░░░██║██████╦╝
░╚═══██╗██║░░░██║██╔══██╗
██████╔╝╚██████╔╝██████╦╝
╚═════╝░░╚═════╝░╚═════╝░
"""

def ip_lookup(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data

def print_ip_info(ip_info):
    print(f"Ville: {ip_info.get('city', 'N/A')}")
    print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
    print(f"Location: {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}")
    print(f"Longitude: {ip_info.get('loc', 'N/A')}")
    print(f"Latitude: {ip_info.get('loc', 'N/A').split(',')[0]}")
    print(f"Altitude: {ip_info.get('altitude', 'N/A')}")

def main():
    print(logo)
    while True:
        print("Options:")
        print("1. Rechercher une adresse IP")
        print("2. Quitter")
        choice = input("Choisissez une option: ")

        if choice == '1':
            ip_address = input("Entrez une adresse IP: ")
            try:
                ip_info = ip_lookup(ip_address)
                print_ip_info(ip_info)
            except Exception as e:
                print(f"Erreur: {e}")
        elif choice == '2':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir 1 ou 2.")

if __name__ == "__main__":
    main()