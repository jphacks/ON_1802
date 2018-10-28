import urllib.request

url = 'https://51c55c54.ngrok.io/tasks/jafkl23kh45l'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = res.read().decode("utf-8")
    print(body)
