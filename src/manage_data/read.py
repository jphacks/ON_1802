import pandas as pd

def json_to_data(user_id):

    file_name = str(user_id) + '.json'
    df = pd.read_json(file_name)
    
    user_id = df['user_id'][0]
    task_name = df['task_name'][0]
    task_info = df['task_info'][0]
    time_limit = df['time_limit'][0]
    
    task_dict = {'user_id':user_id, 'task_name':task_name, 'task_info':task_info, 'time_limit':time_limit}
    
    return task_dict

# this is test
if __name__ == '__main__':
    user_id = 1
    task_data = json_to_data(user_id)
    print(task_data)
