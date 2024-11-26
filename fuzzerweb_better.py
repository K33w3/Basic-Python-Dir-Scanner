#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import time
import requests

BOLD = "\033[1m"
END = "\033[0m"


def scan_urls(wordlist, url):
    with open(wordlist, "r") as file:
        content = file.read().splitlines()

        for line in content:
            start = time.time()
            x = f"{url}/{line}"
            y = requests.get(x)
            end = time.time()

            if y.status_code != 404:
                status_message = f"{BOLD}{x} [ Status: {y.status_code} | Size: {len(y.text)} | Duration: {end - start:.2f} s ]{END}"
            else:
                status_message = f"{x} [ Status: {y.status_code} | Size: {len(y.text)} | Duration: {end - start:.2f} s ]"

            print(status_message)


def main():
    if len(sys.argv) < 2:
        print("Usage: fuzzerweb_better.py <wordlist> <URL>")
        sys.exit()

    try:
        wordlist = sys.argv[1]
        url = sys.argv[2].rstrip("/")
    except IndexError:
        print("Please ensure all arguments are correctly specified.")
        sys.exit()

    print(
        """
 _______  __   __  _______  _______  _______  ______   
|  _    ||  | |  ||       ||       ||       ||    _ |  
| |_|   ||  | |  ||____   ||____   ||    ___||   | ||  
|       ||  |_|  | ____|  | ____|  ||   |___ |   |_||_ 
|  _   | |       || ______|| ______||    ___||    __  |
| |_|   ||       || |_____ | |_____ |   |___ |   |  | |
|_______||_______||_______||_______||_______||___|  |_|
        """
    )

    print(f"Wordlist: {wordlist}")
    print(f"Url: {url}")
    print("------" * 4)

    scan_urls(wordlist, url)


if __name__ == "__main__":
    main()
