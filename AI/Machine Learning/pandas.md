# PANDAS
## 시작하기
```python
import pandas as pd
pd.__version__
```
## 파일 불러오기
```python
df = pd.read_csv('file.csv')
# 파일에 저장된 데이터 읽어오기
# txt파일의 경우 특정 구분자로 구분된 데이터는 sep인자에 명시하여 불러올 수 있음
# tap으로 구분시 : sep = '\t'
df = pd.read_csv('file.csv', encoding='cp949')
# 한글파일 인코딩 에러 시
df = pd.read_csv('file.csv', dtype = ({'column' : 'str'}))
# 불러오면서 특정 칼럼의 type 변경 가능
```
```python
df = pd.read_excel('file.xlsx')
# 엑셀파일 불러오기
df = pd.read_excel('file.xlsx', sheet_name = 0)
# 시트순번을 입력해 특정 시트만 불러올 수 있음
df = pd.read_excel('file.xlsx', sheet_name = 'first_sheet')
# 시트명을 입력해 특정 시트만 불러올 수 있음
```
```python
df.head(n)
# 첫 n개 row를 출력한다. n 미입력시 5개 출력
df.tail(n)
# 마지막 n개 row를 출력한다. n 미입력시 5개 출력
df.len()
# 데이터프레임에 사용하면 row개수를 반환
```
## 데이터프레임 생성
```python
df = pd.DataFrame({'carat' : [1, 11]. 'depth' : [60, 61]}, index = ['a','b'])
# 컬럼명 : 'carat', 'depth'
# row 인덱스 : 'a', 'b'
# row 인덱스명 생략 가능
df = df[0:1]
# 0행만 슬라이싱해서 df생성
dic = df.to_dict()
# 데이터프레임 딕셔너리로 만들기
# 값 입력 쉽게하기 위해
df = pd.DataFrame(dic)
# 딕셔너리를 다시 데이터프레임으로 만들기
```
## 기초
### 함수 및 메서드
```python
df['cut'].min()  # 최소값
df['cut'].max()  # 최대값
df['cut'].mean()  # 평균값
df['cut'].var()  # 분산
df['cut'].std()  # 표준편차
df['cut'].skew()  # 왜도(분포의 비대칭도)
df['cut'].kurt()  # 첨도(정규분포 기준 뾰족한 정도)
df['cut'].idxmin()  # 최소값의 위치
df['cut'].idxmax()  # 최대값의 위치
df['cut'].count()  # 개체 수
df['cut'].quantile(q = 0.25)  # 1사분위수
```
### 속성(attribute)
```python
df.ndim  # 객체의 차원
df.shape  # 각 차원의 길이(N * N)
df.dtypes  # 전 컬럼의 dtype
df.columns  # 컬럼명
pd.Series(df.columns)  # 컬럼명에 인덱스 붙이기(0, 1, 2)
df.info()  # 데이터타입, 결측치 등의 정보
df.describe()  # 각종통계량 정보(브라이틱스 stastics summary)
```
### astype
```python
df.astype(str)
# df내 타입을 전부 str로 변경
df.astype({'col1' : 'int32', 'col2' : 'int64'})
# 특정 컬럼만 변경
df = pd.read_csv('3.csv', dtype = ({'jumin7' : 'str'}))
# 파일 데이터를 불러올 때 데이터타입 변경 가능
```
### value_counts
```python
df['col1'].value_counts()
# 데이터들의 빈도 출력
df['col1'].value.counts(dropna = False)
# NaN값의 개수도 같이 출력, True가 default
```
### nunique
```python
df = df['col1'].nunique().reset_index()
# 컬럼 내 몇개의 고유값이 있는지 파악
```
## 데이터 변환
### 결측치
```python
df.isna(), df.isnull()
# 결측값 확인
df.notna(), df.notnull()
# 결측 아닌 값 확인
df.isna().sum()
# 결측치 갯수(column)
df.isna().sum(axis=1)
# 결측치 개수(row) 
```
```python
df.dropna()
# 결측치 제거
df.dropna(how = 'any')
# 한 값이라도 결측치가 있는 레이블을 삭제, default
df.dropna(how = 'all')
# 모든 값이 결측치인 레이블만 삭제
df.dropna(subset = ['col1','col2','col3'])
# 3개 변수에 대해 결측치삭제
```
```python
df.filna({'행정구역':'서울','국가':'대한민국'})
# 결측치를 해당값으로 채움
df.filna({'확진자' : df['확진자'].mean()})
# 결측치를 평균값으로 채움
```
```python
# 결측치 채운 값을 원본에 적용하기
df.filna({'행정구역' : '서울', '국가' : '대한민국', '확진자' : df['확진자'].mean()}, inplace=True)
df['Cabin'] = df['Cabin'].filna('C000')
df['Age'] = df['Age'].filna(df['Age'].mean())
```
### 삭제
```python
df = df.drop(columns = ['A', 'C'])
# 컬럼 별로 drop
df = df.drop(['A', 'C'], axis = 1)
# axis = 1을 이용해 컬럼별로 drop가능
df = df.drop(index = [1, 4, 5])
# 1, 4, 5행 drop
```
```python
df = df[['Line_No','Station_ID']].drop_duplicates()
# 이중리스트, 컬럼에서 중복데이터 삭제
df = df.drop_duplicates(subset=['date','time','trans_id','item'])
# 컬럼에서 중복 데이터 삭제
```
### 인덱스 설정
```python
df = df.reset_index()
# 현재 인덱스를 자료열로 편입, 인덱스는 기본값으로 설정됨(0, 1, 2, 3...)
df = df.reset_index(drop=True)
# 현재 인덱스를 버리고, 인덱스는 기본값으로 설정
df = df.set_index('col1')
# 특정 열을 인덱스로 지정, 기존 인덱스 사라짐
```
### 인덱싱/필터링
```python
df = df['col1']
# series 객체 반환
df = df[['col1']]
# DataFrame 객체 반환
df = df[0:1]
# 0행만 슬라이싱(머신러닝시 다용)
```
```python
df = df.iloc[:3, 0:2]
# 위치기반 필터링
df = df.iloc[[1, 3, 5], [0, 3]]
# 행, 컬럼 리스트 구조
df = df.iloc[:,[1,2,7]]
# 1,2,7번 컬럼만 필터
```
```python
df = df.loc[:,['A','B','C']] # 명칭기반 필터링
df = df.loc[:2, 'petal_width']
# 한 개 컬럼일때 리스트 구조[] 없이 직접 입력
df = df.loc[:2, ['sepal_length', 'petal_width']]
# 두개 이상 컬럼으로 리스트 구조 입력
df = df.loc[:2, 'petal_width':]
# 인덱스 ~ 2, 컬럼 'petal_width' 부터~
df = df.loc[:2, :'petal_width']
# 인덱스 ~ 2, 컬럼 ~ 'petal_width'까지
df = df.loc[df['BMI'] >  0, ] # 값중 > 0 를 필터
df = df.loc[df['Segmentation'].isin(['A', 'D']), ].reset_index(drop = True)
# 값중 A,D 컬럼 내 값을 필터
df = df.loc[df['Item'].isin(df_10['index']),]
# 값중 df_10 'index' 컬럼내 값을 필터
df = df.loc[(df['Pregnancies']== 0) & (df['BMI'] > 0),]
# and 아니고 &, 두 조건을 만족하는 값만 필터
df = df.loc[(health['BP_HIGH'] > hi) | (health30['BP_HIGH'] < low), ]
## or 아니고 | 사용, 두 조건 중 하나 만족하는 값 모두 필터
df = df[df2['Admit']=='Admitted']
df = df[df['condition'] != -1]
# ==, != 논리연산자로 필터
df = df[df['Count']>50].sort_values('Mean', ascending = False)
# 'Mean'컬럼 값 내림차순 정렬
df = df.query('Pregnancies== 0')
# query로 필터링
```
### group by
```python
df = df.groupby(['cut','color'])[['price','carat']].mean().reset_index()
# 'cut', 'color'컬럼별로 구분한 'price','carat' 컬럼의 mean값, [[ ]] 주의
df = df.groupby(['cut','clarity'])['price'].mean().reset_index()
df = df.groupby('Line_No')['Station_ID'].nunique().reset_index()
# 구분자가 단수일 경우 []필요 없음
```
### agg(다중통계량)
```python
df = df.groupby(['pet','color'])['breed_yn'].agg(['mean', 'min', 'max', 'count', 'size']).reset_index()
# 'pet', 'color'컬럼 별로 구분한 'breed_yn'컬럼의 다중통계량
df = df.groupby(['pet']).agg({'Age':'max', 'SibSp':'sum', 'Fare':'mean'}).reset_index()
# 컬럼 별로 다른 통계량 지정
df = df.groupby(['pet']).agg(Aeg_Cnt=('Age', 'count'), Age_Mean=('Age', 'mean'), Fare_Max=('Fare', 'max'))
# 동일 컬럼 다른 agg 혼합
```
### sort
```python
df = df.sort_values('lift', axis=0, ascending=False)
# 'lift' 컬럼 기준 내림차순 정렬
df = df.sort_values(['Station_ID','variable'], ascending=[False,True])
# 'Station_ID' 는 dscending,'variable'은 ascending 
```
### crosstab
```python
df = pd.crosstab(dia['cut'],dia['clarity'], normalize = True).round(2)
df = pd.crosstab(dia['cut'],dia['clarity'], normalize = 1).round(2)  # normalize = 1 컬럼기준으로 %
df = pd.crosstab(dia['cut'],dia['clarity'], normalize = 0).round(2)  # normalize = 1 행기준으로 %
df = pd.crosstab(dia['cut'],dia['clarity'],values = dia['price'],aggfunc = pd.Series.mean)
```
### 값 변경
```python
df['Sex'] = df['Sex'].replace('male', 'Man')
# Sex의 모든 male값을 Man으로 변경
df['Sex'] = df['Sex'].replace({'male':'Man', 'female':'Woman'})
# Sex의 모든 male값을 Man, 모든 female값을 Woman으로 변경
df['Cabin'] = df['Cabin'].replace(np.nan, 'C001')
# 결측치를 C001로 변경

tmp2 = np.where(tmp<7, tmp, 2*tmp)
# np.where 괄호 안의 조건에 따라 변경


df_2014_2015 = df_mart_year_cnt_pivot.loc[(df_mart_year_cnt_pivot[2014] > 0) & (df_mart_year_cnt_pivot[2015] <= 0),]
# '' 미포함하여 구문 작성 가능
```
### Datetime
```python
# 컬럼내 datetime 값을 YY, MM, DD 로 바꾸기
# 컬럼내 datetime에서 원하는 값만 필터링 하기
                                                                                           
df['ymd']=df['date_column'].apply(pd.to_datetime)
# 
df['ymd']=pd.to_datetime(df['date_column'], format='%Y/%m/%d, %H:%M:%S')
# 연/월/일, 시:분:초 포맷으로 날짜변환
df['yy']=df.ymd.dt.year
# 연(4자리 숫자)
df['mm']=df['ymd'].dt.month
# 월(숫자)
# bike.ymd.dt vs bike['ymd'].dt 두 가지 포맷이 다 가능
df['dd']=df.ymd.dt.day
# 일(숫자)
df['hour']=df.ymd.dt.hour
# 시(숫자)
df['wd']=df.ymd.dt.weekday
# 요일(숫자) (Monday=0, Sunday=6)
df['wd']=df.ymd.dt.day_name()
# 요일 이름(문자), 메소드라 ()필요함 주의 
df['wd']=df.ymd.dt.dt.month_name()
# 월 이름(문자), 메소드라 ()필요함 주의 
df['Datetime'] = pd.to_datetime(df['Datetime'], format='%m/%d/%Y, %H:%M:%S')
# 연/월/일, 시:분:초 포맷적용
df['D'] = (pd.to_datetime('31-08-2021',format = '%d-%m-%Y') - pd.to_datetime(df01['Dt_Customer'],format = '%d-%m-%Y')).dt.days
# 날짜 수 계산시 추천
df['stand_ym'] = df['date'].apply(lambda x: x[0:4]+x[5:7])
# 2001-03-04을 200103으로 만들기 lamda 함수 사용)
df['birth_yr'] = df['jumin7'].apply(lambda x: '19' + x[0:2]).astype(int) # 주민번호로 년도 만들기
df['Duration_Customer'] = df['Dt_Customer'].apply(lambda x:  (datetime.datetime.strptime('2021-08-31','%Y-%m-%d') - datetime.datetime.strptime(x,'%d-%m-%Y')).days)

(datetime.datetime.strptime('2021-08-31','%Y-%m-%d')-datetime.datetime.strptime('2021-08-30','%Y-%m-%d')).days # row별로는 실행 가능
* strptime은 문자열을 날짜로, strftime은 날짜를 문자열로 변환 주의:strptime은 Series 단위로 실행불가, row단위로 실행 <- lambda 사용
```
### 변수
```python
[파생변수 생성]
df['Sex_cd'] = (df['Sex'] == 'M') + 0    # 파생변수 값이 1,0일대 유용 
df['ratio'] = df['price'] / df['carat']
df['Age'] = (df['Age']//10) * 10  # 나이대 생성

[파생변수 조건문 map 활용] # map dict 안에 없어 mapping되지 않는 값은 null값으로 변경됨 주의
df['BP_cd'] = df['BP'].map({'LOW' : 0 , 'NORMAL' : 1 , 'HIGH' : 2})   # 3개중 선택, 

[변수명 변경]
df = df.rename(columns = {'Sepal_Length': 'SL'}) # 기존 컬럼명 Sepal_Length'를 'SL' 로 바꾼다
df.columns = ['SL', 'SW', 'PL', 'PW', 'Species'] # 기존 컬럼명을 'SL', 'SW', 'PL', 'PW', 'Species'로 바꾼다
df.columns.values[0] = 'Sepal_Length' # 위 df.columns = ['SL', 'SW', 'PL', 'PW', 'Species']의 0번째 'SL'을 'Sepal_Length'로 변경

[concat]
pd.concat([bike_1,bike_2], axis = 1)
df = pd.concat([df.loc[:,['Year_Month', 'Station_ID']],df.loc[:,'H01':'H24']], axis=1) # [ ] 주의

[merge]
pd.merge(left=df_A, right=df_B, how = 'inner', left_on='member', right_on='name')

[melt]
elec_melt=elec.melt(id_vars=['YEAR','MONTH','DAY'])

[pivot]
df = df.pivot_table(values='cnt', index='ID', 
                    columns='Item',  aggfunc='max', fill_value=0)
                                                                    
[shift] # 시계열, 브라이틱스 add lead lag, row방향 한칸 이동 
df['mean_dow_1'] = df['mean_dow'].shift(1)    # mean_dow 열을 row방향으로 한 칸 이동

[dummy]
df = pd.get_dummies(data = df, columns = ['season']).drop_first = True # 기존 df에 더미변수 생성, but 기존 컬럼 삭제
df_dum = pd.get_dummies(df['pet_category'], drop_first=True, prefix='pet_ca') # dummy 변수만 생성
df = pd.concat([df, df_dum],axis=1) # 기존 df와 df_dum을 concat, 더미변수 원래 컬럼으로 groupby 해야할때 편리
                                                                    
[cut, 변수 등급화]
pd.cut(arr, bins = [0,4,6,10], right=True, labels=['a','b','c']) # right=True면 right포함, False면 미포함
df['Na_K_gr'] = pd.cut(df['Na_to_K'], bins = [0, 9, 19, 29, 39],
       labels = ['Lv1', 'Lv2', 'Lv3','Lv4']) # labels 은 bins보다 1개 작아야 한다
```