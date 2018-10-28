import urllib.request, json

if __name__ == '__main__':
    url = "https://51c55c54.ngrok.io/tasks/jafkl23kh45l"
    method = "POST"
    headers = {"Content-Type" : "application/json"}

    # PythonオブジェクトをJSONに変換する
    obj = {
        'user_id' : "jafkl23kh45l",
        'task_name' : '洗濯物をたたむ',
        'task_info' : '洗濯物が溜まってきたのでそろそろ畳まないといけない',
        'time_limit' : {'year':2018, 'month':10, 'date':18}
        }

    json_data = json.dumps(obj).encode("utf-8")

    # httpリクエストを準備してPOST
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
