import pandas as pd

def _chenge_dict_for_pandas(task_dict):
    
    for key, data in task_dict.items():
        task_dict[key] = [data]

    return task_dict

def data_to_csv(dict):

    task_dict = _change_dict_to_pandas(dict)
    file_name = str(dict['user_id']) + '.csv'
    df = pd.DataFrame(task_dict)
    df.to_csv(file_name)

    return 0
