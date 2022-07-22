import hashlib
import sys
import re
import requests

def request_api_data(query_char):
    """
    Requests pwned passwords from website who's first 5 characters
    matches the first 5 characters of our hashed password.
    """
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}")
    return response

def get_password_leak_count(hashes, hash_to_check):
    ''' Checks if the user's password exists in response 
        and provieds the number of times it has been pwned'''
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for hash_, count in hashes:
        if hash_ == hash_to_check:
            return count    
    return 0

def pwned_api_check(password):
    """Check if password exists in APi repsonse"""
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return  get_password_leak_count(response,tail)

def main(password):
    count = pwned_api_check(password)
    if count:
        print(f'{password} was found {count}. Password is not secure')
    else:
        print(f'{password} was NOT found {count}. Password is secure')
    return 'Check completed'
print('Has your password been pawned?')

if __name__ == '__main__':
    user_password = input('Enter password to check!:\n')
    main(user_password)

