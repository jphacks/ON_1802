import pandas as pd
import os

def json_to_data(user_id):

    path = './data/'
    file_name = str(user_id) + '.json'
    if os.path.isfile(path + file_name):
        df = pd.read_json(path + file_name)

        task_list = []
        for _, task in df.iterrows():
            user_id = task['user_id']
            task_name = task['task_name']
            task_info = task['task_info']
            time_limit = task['time_limit']

            task_dict = {'user_id':user_id, 'task_name':task_name, 'task_info':task_info, 'time_limit':time_limit}

            task_list.append(task_dict)
        return task_list
    else:
        return False

# this is test
if __name__ == '__main__':
    user_id = 1
    task_data = json_to_data(user_id)
    print(task_data)
