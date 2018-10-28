import urllib.request

url = 'http://127.0.0.1:5000/tasks/jafkl23kh45l'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = res.read().decode("utf-8")
    print(body)
