#!/usr/bin/env python
import sys
import time
import requests
import argparse


def main(argv):
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

    print(f"Wordlist: {args.wordlist}")
    print(f"Url: {args.url}")
    print("---------------------------------------")

    with open(file=args.wordlist, mode="r") as file:
        f1 = file.read().splitlines()
        for line in f1:
            start = time.time()
            x = f"{args.url}/{line}"
            y = requests.get(x)
            end = time.time()

            if y.status_code != 404 or args.verb:
                if y.status_code != 404:
                    status_message = f"{style.BOLD}{x}\t[ Status: {y.status_code} | Size: {len(y.text)} | Duration: {end - start:.2f} s ]{style.END}"
                else:
                    status_message = f"{x}\t[ Status: {y.status_code} | Size: {len(y.text)} | Duration: {end - start:.2f} s ]"

                print(status_message)


if __name__ == "__main__":

    class style:
        BOLD = "\033[1m"
        END = "\033[0m"
        Yellow = ""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-w",
        "--wordlist",
        default="0",
        dest="wordlist",
        help="Provide wordlist for fuzzing",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-u",
        "--url",
        default="0",
        dest="url",
        help="Provide url to fuzz",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default="false",
        dest="verb",
        help="Give this argument if you want it to be a verbose output",
        action="store_true",
    )
    args = parser.parse_args()

    main(sys.argv[1:])
