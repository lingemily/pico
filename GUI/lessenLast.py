import requests

url = "https://blynk.cloud/external/api/update?token=cMMyYQdf4AuBzJyc1Th5A_PPYehHX8dj&v0=0"

response = requests.requests("GET",url)
if response.status_code == 200:
    print(response.json())


