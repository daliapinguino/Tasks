import pandas as pd
import os
import datetime
import xlrd



time_of_parsing = datetime.datetime.today().strftime('%Y-%m-%d')

df = pd.read_excel('CaseCountData.xlsx')
df.insert(1, 'State', 'Texas')
df.insert(4, 'Date', time_of_parsing)
df.to_csv('Texas_cases.csv')
os.remove('CaseCountData.xlsx')
