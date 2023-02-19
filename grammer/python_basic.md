# Python 기본 문법

## 변수
"="를 이용해 변수를 할당할 수 있다.
ex) x = 5

## 자료형
다음과 같은 자료형이 있다.
- 숫자 (integers, floats)
- 문자(Strings)
- 리스트
- 딕셔너리
- Booleans(T/F)

## 연산자
다음과 같은 수학/논리적 연산자가 있다.
- 덧셈 (+)
- 뺄셈 (-)
- 곱셈 (*)
- 제곱수 (**)
- 나눗셈 (/)
- 몫 (//)
- 나머지 (%)

## 조건문
- `if`
- `else`
- `for` 반복문

## 함수
`def` 키워드를 이용해 고유의 함수(재사용할 수 있는 코드 모음)를 만들 수 있다.

## 모듈
`import` 를 이용해 파이썬 코드들을 모아 모듈을 만들 수도 있고, 타인이 만든 모듈을 가져와 사용할 수도 있다.

## 예외 처리
`try` 와 `except` 를 이용해 에러발생이나 예외 시 동작을 설정할 수 있다.

## 잊기 쉬운 함수
### Iteration
- enumerate
- zip
- reversed
- sorted
- map
- filter
- reduce

### 자료형 변환
- int : 숫자형
- float : 실수형
- str : 문자형
- list : 리스트
- tuple : 튜플
- dict : 딕셔너리
- set : 집합(중복불가, 변경 가능)
- frozenset : 집합(변경 불가)

### 수학적 함수
- abs
- divmod
- pow
- round
- sum
- min : 최솟값
- max : 최댓값

### 문자 조작
- len : 문자의 길이 출력
- str.upper : 대문자로 변경
- str.lower : 소문자로 변경
- str.strip
- str.replace
- str.split : 분리
- str.join

### 입출력
- print : 출력
- input : 값 입력
- open : 파일 열기
- file.read : 파일 읽기
- file.write : 파일 쓰기

### 파일과 폴더 관리
- os.getcwd
- os.chdir
- os.mkdir : 폴더 생성
- os.rmdir : 폴더 삭제
- os.listdir : 

### 예외 처리
- try
- except
- finally
- raise