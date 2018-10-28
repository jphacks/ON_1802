import pandas as pd
import os

import read

def _change_dict_for_pandas(task_dict):
    
    for key, data in task_dict.items():
        task_dict[key] = [data]

    return task_dict

def data_to_json(dict):
    """
    task_dict = {
        'user_id' : 1,
        'task_name' : '洗濯物をたたむ',
        'task_info' : '洗濯物が溜まってきたのでそろそろ畳まないといけない',
        'time_limit' : {'year':2018, 'month':10, 'date':18}
    }
    """
    path = './data/'
    file_name = str(dict['user_id']) + '.json'

    if os.path.isfile(path + file_name):
        
        exist_tasks = read.json_to_data(dict['user_id'])
        df = pd.DataFrame(columns=['user_id', 'task_name', 'task_info', 'time_limit'])
        for task in exist_tasks:
            df = df.append(task, ignore_index=True)
#         print(df)
        task_dict = pd.Series(dict)
#         print(task_dict)
        new_tasks = df.append(task_dict, ignore_index=True)
#         print(new_tasks)
        new_tasks.to_json(path + file_name)
        
    else:
        
        task_dict = _change_dict_for_pandas(dict)
        df = pd.DataFrame(task_dict)
        df.to_json(path + file_name)

    return 0

# test
if __name__ == '__main__':
    task_dict = {
        'user_id' : 1,
        'task_name' : '洗濯物をたたむ',
        'task_info' : '洗濯物が溜まってきたのでそろそろ畳まないといけない',
        'time_limit' : {'year':2018, 'month':10, 'date':18}
    }
    
    data_to_json(task_dict)
