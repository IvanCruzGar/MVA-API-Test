import pandas as pd
import os
import numpy as np
import os

# The Report1 is created after ran the Pytest command
csv_file1 = 'Report2.csv'

# df1--docuemnto, df--columnas y filas
df1 = pd.read_csv(csv_file1)

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
df5 = df4.rename(columns={'id': 'ID', 'status': 'Result', 'message': 'Error_message', 'duration': 'Duration'})

# Relocate the index for the report
df6 = df5.set_index(['ID', 'Result', 'Error_message', 'Duration'])

df6['Description'] = 'Comparison between API and database'

# Creation for the newest Report
df6.to_csv("Test_results2.csv")

compare_results = "Test_results2.csv"
compare_vsts = os.getcwd() +  "\\csv\\compare_results.csv"

comp_r = pd.read_csv(compare_results)
comp_vsts = pd.read_csv(compare_vsts)

column_results = comp_r["ID"]
id = column_results.head()

column_vsts = comp_vsts["ID"]
id2 = column_vsts.head()

add_column = comp_vsts['TCS']
vsts = add_column.head()

if id.equals(id2):
    comp_r.drop('ID', inplace=True, axis=1)
    comp_r["ID"] = add_column
    relocate = comp_r.set_index(['ID', 'Result', 'Error_message', 'Duration'])
    print(relocate)
else:
    print("This is different table")

relocate.to_csv("Test_results2.csv")

