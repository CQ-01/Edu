# Python 기본 문법

## 변수
In Python, you can assign values to variables using the equal sign (=). For example:
x = 5

## 데이터타입
Python has several built-in data types, including:
- 숫자 (integers, floats)
- 문자열
- 리스트
- 딕셔너리
- 불린

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

## 포매팅
```py
print('덧셈 : %d + %d = %d' % (num1, num2, num1 + num2))
# %d 자리에 포매팅, d(십진수), b(이진수), s(문자열)...

print(f'덧셈: {num1} + {num2} = {num1 + num2}')

print(f'덧셈: {num1} + {num2:>3} = {num1 + num2}')
```