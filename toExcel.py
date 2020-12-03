import pandas as pd 
import sqlalchemy
import os; os.chdir('/Users/eason/Desktop/statistics/final-project')

engine  = sqlalchemy.create_engine('mysql+pymysql://root:breaking0203@localhost:3306/stats_final_project_2020')

df = pd.read_sql_table("towed_bike", engine, index_col='id')

df.to_excel('./src/datas.xlsx', 'towed_bike')