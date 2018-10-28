import pandas as pd

file_name = '1.json'
df = pd.read_json(file_name)

user_id = df['user_id'][0]
task_name = df['task_name'][0]
task_info = df['task_info'][0]
time_limit = df['time_limit'][0]

task_dict = {'user_id':user_id, 'task_name':task_name, 'task_info':task_info, 'time_limit':time_limit}
print(task_dict)
print(type(task_dict['time_limit']))

