import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard

token = "egjHFD-wgl29I288FzOF_p2nYDcM5Svp1_nQV0SCRmyW9-w-P9AdK6yMVrg1i6hmHvY89Q."

session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token)
session.cookies.set("__Secure-1PSIDTS", "sidts-CjIBPVxjSu3Y0TuLhlNk1FD3_Fq0Z4aZMCaKizVgIiuIZqLdu11yVhR1OiM_mIjM7G680hAA")
session.cookies.set("__Secure-1PSIDCC", "ABTWhQHK8U_zViWx9L9y6pQVNy79JT1r8Mrqqm2vizOv61zdekSpCVr48mrJZLBELLjr9_IpMsCQ")

bard = Bard(token=token, session=session)

output =  bard.get_answer("Halsizlik ifade eden 10 cümle yaz")

print(output)