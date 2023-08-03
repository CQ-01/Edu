# Python 기본 문법

## 변수 할당
```py
x = 5
```

## 데이터타입
- 숫자
  - int : 정수
  - float : 실수
- 문자열(str)
  - `input()`으로 입력받으면 모두 문자열
- 리스트
  - `list = [a, b, c, d ...]`
  - 리스트 컴프리헨션
```py
# 1 부터 10,000까지 중 7의 갯수
str(list(range(1, 10001))).count('7')

sum([str(x).count('7') for x in range(1, 10001)])
```
- 딕셔너리
  - `dic = {a : 1, b : 2, c = 3}`
- 튜플
  - `tuple = (a, b, c, d ...)`
  - 수정이 안되므로 처음 지정할때 값을 다 넣기
  - `() + ()`로 list의 `.append`와 같은 결과
    - 한 가지 요소만 더할 경우 ` + (a,)` 콤마 넣기
- 불린
  - True / False

## 연산자
> 프로그래밍 언어의 시작 : 빠른 연산을 위해
### 산술연산자
- `+` : 덧셈, `+=` : a = a + 1
- `-` : 뺄셈, `-+` : a = a - 1
- `*` : 곱셈, `*=` : a = a * 1
- `**` : 거듭제곱, `**=` : a = a ** 1
- `/` : 나눗셈, `/=` : a = a / 1
- `//` : 몫, `//=` : a = a // 1
- `%` : 나머지, `%=` : a = a % 1

### 관계연산자
- `>` : 왼쪽이 크다
- `<` : 오른쪽이 크다
- `==` : 같다
- `!=` : 같지 않다
- `<=` : 오른쪽이 크거나 같다
- `>=` : 왼쪽이 크거나 같다

### 논리연산자
> 결과값이 True / False
- `and`(논리곱) : 둘다 참이어야 참
- `or`(논리합) : 둘중 하나만 참이어도 참
- `not`(논리부정) : 참이면 거짓, 거짓이면 참
- 멤버쉽연산자
  - `in`
  - `not in`

## 조건문, 반복문
- if문
```py
if 조건문1:
  실행문1
# 조건문이 참이면 실행문1 실행

elif 조건문2:
  실행문2
# 조건문1이 거짓이고, 조건문2가 참이면 실행문2 실행

else:
  실행문 3
# 조건문1, 2가 모두 거짓이면 실행문3 실행
```
### 주민번호로 정보얻기
```py
num = input('주민번호를 입력하세요 :').split('-')
if num[1][0] == '1' or num[1][0] == '3':
    sex = '남성'
elif num[1][0] == '2' or num[1][0] == '4':
    sex = '여성'
year = int(num[0][0:2])
if num[1][0] == '1' or num[1][0] == '2':
    year += 1900
elif num[1][0] == '3' or num[1][0] == '4':
    year += 2000
print(f'{year}년 {num[0][2:4]}월 {num[0][4:6]}일, {2023 - year + 1}세, {sex}')
```
### 자동주문머신
```py
coffee1_price = 2500
coffee2_price = 3000
coffee3_price = 3000

menu = f'''[커피 자동주문 머신 메뉴]
-----------------------
- 아메리카노 : {coffee1_price}원
- 카페라떼 : {coffee2_price}원
- 카푸치노 : {coffee3_price}원
-----------------------
원하시는 커피종류와 잔수를 입력하세요
'''

print(menu)
coffee1 = int(input('아메리카노 몇잔: '))
coffee2 = int(input('카페라떼   몇잔: '))
coffee3 = int(input('카푸치노   몇잔: '))

total = coffee1_price * coffee1 + coffee2_price * coffee2 + coffee3_price * coffee3
print(f'주문하신 총 가격은 {total}원 입니다.')

money = int(input('돈을 입력해주세요.'))
if total > money:
    print(f'돈이 {total - money}원 모자랍니다')
elif total == money:
    print('주문하신 음료 나왔습니다')
else:
    print(f'주문하신 음료와 함께 거스름돈 {money - total}원 돌려드리겠습니다')
```

## 함수
In Python, you can define your own functions using the `def` keyword. Functions are blocks of reusable code that can be called with specific arguments.

## 모듈
You can organize your Python code into reusable modules using the `import` statement.

## 예외처리
Python provides a mechanism for handling errors and exceptions using the `try` and `except` statements.

## 출력
### 포매팅
```py
print('덧셈 : %d + %d = %d' % (num1, num2, num1 + num2))
# %d 자리에 포매팅, d(십진수), b(이진수), s(문자열)...

print(f'덧셈: {num1} + {num2} = {num1 + num2}')
# f'string

print(f'덧셈: {num1} + {num2:>3} = {num1 + num2}')
# >n : n(자릿수), >(우측정렬), <(좌측정렬), ^(가운데정렬)
```
```py
print('%d' % 123)
>> 123
# 십진수로 포맷

print('%5d' % 123)
>>   123
# 십진수의 5자리로 포맷

print('%05d' % 123)
>> 00123
# 십진수의 5자리 빈칸 0으로 포맷

print('%f' % 123.45)
>> 123.450000
# 숫자 입력 없으면 소수 6째 자리까지 포맷

print('%7.1f' % 123.45)
>>   123.5
# 7자리에 소수 첫째줄까지

print('%7.3f' % 123.45)
>> 123.450
# 7자리에 소수 셋째줄까지
```

### escape 문자
이스케이프문자|역할|설명
|--|--|--|
|\n|새줄로 이동|enter|
|\t|다음탭 이동|tab|
|\b|뒤로 한칸 이동|backspace|
|`\\`|\출력|
|`\'`|'출력|
|`\*`|*출력|

### eval()
- 문자열을 숫자처럼 계산
```py
eval('3' + '4')
>> 7
```
### type이 tuple 인 이유?
```py
a = ''
b = 1
c = ['a', 'b', ['a', b], (a, 'c')]
for b in c:
  a = b
print(type(a))
```
### 인덱싱, 슬라이싱
- 데이터에 순서가 있어야 한다

```py
a = agriculture
a[1:3]
>> gr
# 인덱스 순서는 첫 글자가 0부터 시작, :뒤의 숫자 바로 전까지 출력

a = agriculture
a[1:3:-1]
>> rg
# 세 번째 숫자가 -1이 입력되면 거꾸로 출력

a = agriculture
a[-3:-1]
>> ur
# 오른쪽 끝에서 부터 -1 ~ 로 세어 출력하는 것도 가능
```
```py
print('%s' % 'Python')
>> Python

print('%10s' % 'Python')
>>     Python
# 10자리로 우측정렬한다
# 문자 간 공백이 있을 경우 공백을 사이에 두고 양측으로 정렬됨
```
```py
"I eat {0} apples".format(3)
>> "I eat 3 apples"

"I ate {0} apples. So, I'm {1}".format(10, 'full')
>> "I ate 10 apples. So, I'm full"
```
- 문자개수 세기
  - `count()`
- 위치 알려주기
  - `find()` : 없는 문자를 입력하면 -1 반환
  - `index()` : 없는 문자를 입력하면 에러 반환

- 문자열 관련 함수
  - `join()`
```py
a = "!"
a.join('파이썬')
'파!이!썬'
```

  - `upper()`, `lower()` : 대문자로, 소문자로
  - `strip()`, `lstrip()`, `rstrip()` : 전체 공백지우기, 왼쪽 오른쪽 공백 지우기
  - `replace()` : 문자열 바꾸기
  - `split()` : 문자열 나누기
    - `split()` 괄호 안의 문자가 없을 경우 리스트를 통으로 반환

### 단일문자와 정수간의 관계
- 문자 데이터를 변환할 국제적인 기준 : ASCII, UNICODE
- `chr()` : 정수 $\rightarrow$ 문자로 변환, `ord()` : 문자 $\rightarrow$ 정수로 변환

### 날짜
```py
import datetime
now = datetime.datetime.now()
# 현재 시각

now.strftime('지금 시각은 %Y년 %m월 %d일 %H시 %M분 %S초 입니다.')
# 시간 포맷하는 함수
```
## 외부 사이트에서 가져오기
```py
import urllib.request
import ssl

ctx = ssl._create_unverified_context()

#환율정보 페이지 불러오기
print("[환율정보 불러오기]")
URL = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8"
page = urllib.request.urlopen(URL, context=ctx)  
text = page.read().decode("utf8")  # 해당 페이지의 소스코드
# print(text)

#환율정보 가져오기: 기준시간 
searchText = 'class="grp_info"> <em>'
# 해당 유니크 텍스트의 가장 앞 부분의 위치를 찾음
where      = text.find(searchText)  #소스코드에서 해당 문자열의 시작위치
targetInfo = text[where+len(searchText):where+len(searchText)+16]
print(f'-환율기준시간: {targetInfo}')

#환율정보 가져오기: 달러
searchText = '<span>미국 <em>USD</em></span></a></th> <td><span>'
where      = text.find(searchText)
targetInfo = text[where+len(searchText):where+len(searchText)+8] 
print(f'-달러당: {targetInfo}')

#환율정보 가져오기: 유로
searchText = '<span>유럽연합 <em>EUR</em></span></a></th> <td><span>'
where      = text.find(searchText)
targetInfo = text[where+len(searchText):where+len(searchText)+8]
print(f'-유로: {targetInfo}')

#환율정보 가져오기: 위안
searchText = '<span>중국 <em>CNY</em></span></a></th> <td><span>'
where      = text.find(searchText)
targetInfo = text[where+len(searchText):where+len(searchText)+6] 
print(f'-위안: {targetInfo}')

#환율정보 가져오기: 엔화
searchText = '<span><em>JPY 100</em>일본 </span></a></th> <td><span>'
where      = text.find(searchText)
targetInfo = text[where+len(searchText):where+len(searchText)+6] 
print(f'-엔화: {targetInfo}')
```

## 관련 링크
[파이썬 자습서](https://docs.python.org/ko/3.10/tutorial/datastructures.html#list-comprehensions)