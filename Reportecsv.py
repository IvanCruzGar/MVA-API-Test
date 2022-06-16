import pandas as pd
import os
import numpy as np

# The Report1 is created after ran the Pytest command
csv_file1 = 'Report1.csv'
csv_file2 = 'Report2.csv'

# Merge files
merge_report = pd.concat(map(pd.read_csv, ['Report1.csv', 'Report2.csv']))
merge_report.to_csv('Report.csv', index=False)
csv_file = 'Report.csv'

# df1--docuemnto, df--columnas y filas
df1 = pd.read_csv(csv_file)

# Those are going to replace bcz are related from the Report1
replace_listp = ['passed']
replace_listf = ['failed']
replace_listid = ['ssqaapitest/']

# Regular expression `to_replace` with for loop with 'passed' and 'failed'
for i in replace_listp:
    df2 = df1.replace({'status': r'^({})'.format(i)}, {'status': 'Pass'}, regex=True)

for i in replace_listf:
    df3 = df2.replace({'status': r'^({})'.format(i)}, {'status': 'Fail'}, regex=True)

for i in replace_listid:
    df4 = df3.replace({'id': r'^({})'.format(i)}, {'id': ''}, regex=True)

# Rename column names
df5 = df4.rename(columns={'id': 'id', 'status': 'Result', 'message': 'Error_message', 'duration': 'Duration'})

# Relocate the index for the report
df6 = df5.set_index(['id', 'Result', 'Error_message', 'Duration'])

df6['Description'] = 'Comparison between API and database'

# Creation for the newest Report
df6.to_csv("Test_results.csv")

compare_results = "Test_results.csv"
compare_vsts = os.getcwd() + "\\csv\\compare_results.csv"

comp_r = pd.read_csv(compare_results)
comp_vsts = pd.read_csv(compare_vsts)

column_results = comp_r["id"]
id = column_results.head()

column_vsts = comp_vsts["id"]
id2 = column_vsts.head()

add_column = comp_vsts['TCS']
vsts = add_column.head()

if id.equals(id2):
    comp_r.drop('id', inplace=True, axis=1)
    comp_r["id"] = add_column
    relocate = comp_r.set_index(['id', 'Result', 'Error_message', 'Duration'])
    print(relocate)
else:
    print("This is different table")

relocate.to_csv("Test_results.csv")
