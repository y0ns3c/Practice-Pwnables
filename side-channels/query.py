from urllib import request

print("This program will request you for an address to a HTTP server.")
print("It will then make a HTTP GET request with a query string 'flag=$flag'")
print()

flag = "{flag_knOckknoCK}"

num = -1
addr = input("Input a HTTP server address: ").strip()

net_location, _, query = addr.partition('?')
net_location = net_location.split("://", 1)[-1]
url = f"http://{net_location}"
query = f"{query}&flag={flag}" if len(query) > 0 else f"flag={flag}"

print(f"Making GET request to {url}")
request.urlopen(f"{url}?{query}")
