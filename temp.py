import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard

token = ""

session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token)
session.cookies.set("__Secure-1PSIDTS", "")
session.cookies.set("__Secure-1PSIDCC", "")

bard = Bard(token=token, session=session)

output = bard.get_answer("Halsizlik ifade eden 10 cümle yaz")

print(output)