# NUMPY
## 시작
```python
import numpy as np
```
## 배열
```python
arr = np.array([1, 2, 3, 'A', 'B'])
# 문자와 숫자가 포함된 배열을 만들 수 있음
arr = np.array([1, 2, 3], [4, 5, 6])
# 다차원의 배열도 만들 수 있음
```
```python
arr.min()  # 최소값
arr.max()  # 최대값
arr.mean()  # 평균
arr.argmax()  # 최대값의 위치(index)
arr.argmin()  # 최소값의 위치(index)
```
```python
arr = np.array([1, 2, 3], [4, 5, 6])
arr.ndim  # 2, 
arr.shape  # (2, 3), N*N의 배열인지
arr.dtype  # dtype('int32'), 데이터 타입
```
```python
arr = np.arange(6)
# (n)까지 나열 : array([0, 1, 2, 3, 4, 5])
arr.reshape(2, 3)
# N * N으로 재배열 : array([0, 1, 2], [3, ,4 5])
```
```python
arr = np.arange(6)
# array([0, 1, 2, 3, 4, 5])
arr.tolist()
# 리스트로 변경 : [0, 1, 2, 3, 4, 5]
```
```python
np.where(조건문, 거짓, 참)
# 조건문이 참이면 참 출력, 아니면 거짓
np.where(arr < 2, 1, 0)
# 2보다 크면 1, 아니면 0
df['age_over'] = np.where(df['aa'] < 2, 1, 0>)
# df라는 데이터프레임의 'age_aver'열을 생성하여 'aa'열의 값이 2보다 크면 1, 아니면 0을 입력
```
```python
np.log(n)
# 밑이 e인 자연로그
np.log2(n)
# 밑이 2인 로그
np.log10(n)
# 밑이 10인 상용로그
```