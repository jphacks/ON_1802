import pandas as pd

def json_to_data(user_id):

    path = './data/'
    file_name = str(user_id) + '.json'
    df = pd.read_json(path + file_name)

#     print(df)
    
    user_id = [x for x in df['user_id']]
    task_name = [x for x in df['task_name']]
    task_info = [x for x in df['task_info']]
    time_limit = [x for x in df['time_limit']]
    
    task_dict = {'user_id':user_id, 'task_name':task_name, 'task_info':task_info, 'time_limit':time_limit}
    
    return task_dict

# this is test
if __name__ == '__main__':
    user_id = 1
    task_data = json_to_data(user_id)
    print(task_data)
