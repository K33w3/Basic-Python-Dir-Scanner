#!/usr/bin/env python
import requests,time
import sys, argparse


def main(argv):
	print("""
 _______  __   __  _______  _______  _______  ______   
|  _    ||  | |  ||       ||       ||       ||    _ |  
| |_|   ||  | |  ||____   ||____   ||    ___||   | ||  
|       ||  |_|  | ____|  | ____|  ||   |___ |   |_||_ 
|  _   | |       || ______|| ______||    ___||    __  |
| |_|   ||       || |_____ | |_____ |   |___ |   |  | |
|_______||_______||_______||_______||_______||___|  |_|
		""")

	print("wordlist: ",args.wordlist)
	print("url: ",args.url)
	print("---------------------------------------")

	f = open(args.wordlist, 'r')
	f1 = f.read().splitlines()
	for line in f1:
		start = time.time()
		x = args.url.replace("BUZZ", line)
		y = requests.get(x)

		if(args.verb == True):
			if(y.status_code != 404):
				end = time.time()
				print(style.BOLD + x,"[", "Status: ",y.status_code, "Size: ", len(y.text), "Duration: ", end-start,"s","]"+style.END)
			else:
				end = time.time()
				print(x,"[", "Status: ",y.status_code, "Size: ", len(y.text), "Duration: ", end-start,"s","]")

		elif(y.status_code != 404):
			end = time.time()
			print(style.BOLD + x,"[", "Status: ",y.status_code, "Size: ", len(y.text), "Duration: ", end-start,"s","]"+style.END)


if __name__ == "__main__":
	
	class style:
		BOLD = '\033[1m'
		END = '\033[0m'
		Yellow = ''

	parser = argparse.ArgumentParser()
	parser.add_argument('-w', '--wordlist',
						default='0',
						dest='wordlist',
						help='Provide wordlist for fuzzing',
						required = True,
						type=str
						)
	parser.add_argument('-u', '--url',
						default='0',
						dest='url',
						help='Provide url to fuzz',
						required=True,
						type=str)
	parser.add_argument('-v', '--verbose',
						default='false',
						dest='verb',
						help='Give this argument if you want it to be a verbose output',
						action='store_true')
	#parser.add_argument('-b', '--buzz',
	#					default='0',
	#					dest='buzz',
	#					help='Provide url with keyword BUZZ to fuzz location',
	#					type=str)

	args = parser.parse_args()
	
	main(sys.argv[1:])