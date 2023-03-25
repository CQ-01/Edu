# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mjx6bhkICjGFOKsf2g6L4j0dpulapGRe
"""

import pandas as pd
import numpy as np



data = {
    "name" : ['철수', '영희', '동희','영수'],
    "age": [15, 12, 20, 35]
}

df = pd.DataFrame(data)
df

doc = {
    "name": '세종',
    "age":23
}

df = df.append(doc, ignore_index=True)

df['city'] = ['서울', '부산', '서울', '부산', '부산']
print(df)

cond = df['age'] > 20
print(df[cond])
print(df.iloc[-1, 0])

df.sort_values(by='age', ascending=False)

df['is_adult'] = np.where(df['age'] < 20, '청소년', '성인')
df

df['age'].describe()

df[df['city'] == '서울']['age'].mean()

df = pd.read_excel('종목데이터.xlsx')
df.head()

pd.options.display.float_format = '{:.2f}'.format
# 소수 둘째자리만 보이도록록

cond = df['change_rate'] > 0
df = df[cond]

cond = df['per'] > 0
df = df[cond]

df['close'] = df['per']* df['eps']
df['earning'] = df['marketcap'] / df['per']


cond = (df['pbr'] < 1) & (df['marketcap'] > 100000000) & (df['per'] < 20)
df = df[cond]

print(df.sort_values(by='marketcap', ascending = False))
print(df.describe())

import pandas as pd
import numpy as np

import yfinance as yf

company = yf.Ticker("TSLA")
company.info

name = company.info['shortName']
industry = company.info['industry']
marketCap = company.info['marketCap']
revenue = company.info['totalRevenue']

print(name, industry, marketCap, revenue)

df = company.recommendations
cond = df['Firm'] == 'JP Morgan'
df[cond]

company.news[0]['title']

name = company.info['shortName']
industry = company.info['industry]
marketcap = company.info['marketCap']
summary = company.info['long']
currentprice = company.info['currentprice']
targetprice = company.info['']

def add_company(code):
  company yf.Ticker(code)

df = pd.DataFrame()

codes = ['AAPL','ABNB','BIDU','FB','GOOG','MSFT','TSLA','PYPL','NFLX','NVDA']

for code in codes:
  print(code)
  try:
    row = add_company(code)
    df = df.append(row, ignore_index = True)
  except:
    print(f'error - {code}')

df

df.sort_values(by='eps', ascending=False)

import pandas as pd
import numpy as np
import yfinance as yf

company = yf.Ticker('TELA')
df = company.balance_sheet.loc[['Cash And Cash Equivalents']]
df.columns = ['2021','2020', '2019']

df['name'] = company.info['shortName']

new_df = df[['name','2021','2020']].copy()

new_df['diff'] = new_df['2021'] - new_df['2020']

new_df.reset_index(drop=True)