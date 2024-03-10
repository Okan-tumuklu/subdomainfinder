import socket

def check_host(host, port):
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            return True
    except (socket.timeout, socket.error):
        return False

def check_subdomains(domain, wordlist_path):
    with open(wordlist_path, "r") as wordlist_file:
        for subdomain in wordlist_file:
            subdomain = subdomain.strip() + "." + domain
            if check_host(subdomain, 80):
                print("[X] :", subdomain)

def main():
    try:
        target_domain = input("Hedef site örnk(google.com): ")
        wordlist = "wordlist.txt"
        check_subdomains(target_domain, wordlist)
    except KeyboardInterrupt:
        print("\n[!] Kullanıcı tarafından durduruldu.")

if __name__ == "__main__":
    print("""
    _________________________|
    |Sub-Domain-Finder       |
    |Coder By Okan.Tümüklü   |
    --------------------------
    \n""")
    main()
