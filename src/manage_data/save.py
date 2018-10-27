import pandas as pd

def _change_dict_for_pandas(task_dict):
    
    for key, data in task_dict.items():
        task_dict[key] = [data]

    return task_dict

def data_to_csv(dict):

    file_name = str(dict['user_id']) + '.csv'
    task_dict = _change_dict_for_pandas(dict)
    df = pd.DataFrame(task_dict)
    df.to_csv(file_name)

    return 0

if __name__ == '__main__':
    task_dict = {
        'user_id' : 1,
        'task_name' : '洗濯物をたたむ',
        'task_info' : '洗濯物が溜まってきたのでそろそろ畳まないといけない',
        'time_limit' : {'year':2018, 'month':10, 'date':18}
    }
    
    data_to_csv(task_dict)
