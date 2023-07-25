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
  - list = []
  - 리스트 컴프리헨션
```py
# 1 부터 10,000까지 중 7의 갯수
str(list(range(1, 10001))).count('7')

sum([str(x).count('7') for x in range(1, 10001)])
```
- 딕셔너리
  - dic = {a : 1, b : 2, c = 3}
- 튜플
  - tuple = {}
- 불린
  - True / False

## 연산자
Python supports various mathematical and logical operators, such as:
- 덧셈 (+)
- 뺄셈 (-)
- 곱셈 (*)
- 나눗셈 (/)
- 몫 (//)
- 나머지 (%)

## 반복문
Python provides several control flow statements to control the flow of execution in a program, including:
- `if`
- `else`
- `for` loops

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
# >n 자릿수
```
```py
print('%d' % 123)
>> 123

print('%5d' % 123)
>>   123

print('%05d' % 123)
>> 00123

print('%f' % 123.45)
>> 123.450000

print('%7.1f' % 123.45)
>>   123.5

print('%7.3f' % 123.45)
>> 123.450

print('%s' % 'Python')
>> Python

print('%10s' % 'Python')
>>     Python
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

## 관련 링크
[파이썬 자습서](https://docs.python.org/ko/3.10/tutorial/datastructures.html#list-comprehensions)