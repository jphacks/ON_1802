import urllib.request, json

if __name__ == '__main__':
    url = "http://127.0.0.1:5000/tasks/jafkl23kh45l"

    method = "DELETE"
    headers = {"Content-Type" : "application/json"}

    obj = {
        'user_id' : "jafkl23kh45l",
        'task_name' : '洗濯物をたたむ',
        }

    json_data = json.dumps(obj).encode("utf-8")

    # httpリクエストを準備してPOST
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
