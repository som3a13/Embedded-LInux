import requests

def request(url):
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        # print(data)
    else:
        print("Cant reach")
    return data
#Print dictionary items function
def dictPrint(dict_name):
    for keys,values in dict_name.items():
        print(f"{keys} : {values}")

#Public IP
my_ip=request("https://api.ipify.org/?format=json")

dictPrint(my_ip)

#Location for the ip we got
location=request(f"http://ip-api.com/json/{my_ip['ip']}")

dictPrint(location)