import pandas as pd
import read

def task(user_id, task_name):

    path = './data/'
    try:
        exist_tasks = read.json_to_data(user_id)
            
    except:
        return 'data is not found.'
        
    df = pd.DataFrame(columns=['user_id', 'task_name', 'task_info', 'time_limit'])
    for task in exist_tasks:
        df = df.append(task, ignore_index=True)

#     print(exist_tasks)
    # タスクを削除する処理
    df = df.drop(df[df['task_name'] == task_name].index)
    df.to_json(path + user_id + '.json')
    
#     print(read.json_to_data(user_id))
    
    return True

if __name__ == '__main__':
    test_user_id = '1'
    test_task_name = '洗濯物をたたむ'
    print(task(test_user_id, test_task_name))

