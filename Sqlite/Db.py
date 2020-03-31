import pandas as pd
import xlrd
import sqlite3
import csv
from csv import reader
from csv import writer
import os
import datetime

print('Please, enter the date in format (e.g.2020/03/20): ')
time = input()

wb = xlrd.open_workbook('covid-data-template.xlsx')
sheet_name = wb.sheet_names()
for ii in sheet_name:
    sh = wb.sheet_by_name(ii)

for li in sheet_name:
    data_xlsx = pd.read_excel('covid-data-template.xlsx', li)
    data_xlsx.to_csv(li + " covid-data-template.csv", encoding='utf-8')

    df = pd.read_csv(li + " covid-data-template.csv")
    df['Date'] = time
    df.to_csv(li + ' covid-data-template.csv')

    df['State'] = li
    df.to_csv(li + " covid-data-template.csv", index=False)

    df['Batch'] = + 1
    df.to_csv(li + " covid-data-template.csv", index=False)

    df = pd.read_csv(li + ' covid-data-template.csv')['Batch']

    con = sqlite3.connect(li + " Sql.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE t (State, County, Cases, Deaths, Source, Date, Batch);")
    # use your column names here

    with open(li + ' covid-data-template.csv', 'r') as fin:

        # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i['State'], i['County'], i['Cases'], i['Deaths'], i['Source'], i['Date'], i['Batch']) for i in dr]

    cur.executemany("INSERT INTO t (State, County, Cases, Deaths, Source, Date, Batch) VALUES (?, ?, ?, ?, ?, ?, ?);",
                    to_db)
    con.commit()

    con.execute('SELECT * FROM t')
    for row in cur:
        print(row)
    con.close()
    os.remove(li + ' covid-data-template.csv')
