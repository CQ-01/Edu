# MARKDOWN
## 1. 마크다운이란?
- 텍스트 기반의 경량 마크업* 언어
- .md 확장자를 가지고, 개발과 관련된 많은 문서는 마크다운 형식으로 작성
- 문서화의 토대

## 2. 마크다운의 특징
- 문법과 관리가 쉬움
- 지원가능한 플랫폼이 다양함
- 표준이 없음
- 모든 HTML 마크업 기능을 대신하지는 못함
- 역할에 맞는 마크다운 문법을 사용해야 함

## 3. 마크다운 문법
### 제목(Heading)
```bash
# 제목 1
## 제목 2
### 제목 3
#### 제목 4
#### 제목 5
###### 제목 6
```
- 최대 6개 중첩
  

### 목록 (List)
- 순서 있는 목록 : `1., 2., 3.` 
- 순서 없는 목록 : `1, *, +`
- 들여쓰기 : `tab`
- 내어쓰기 : `shift + tab`

### 강조 (Emphasis)
- 기울임 : `*글자*` or `_글자_`
- 굵게 : `**글자**` or `__글자__`
- 취소선 : `~~글자~~`

### 코드 (Code)
```bash
인라인코드 : `코드`
블록 코드 : ```python + 코드 ```
```
- 내부의 코드가 실행되지 않음
### 링크 (Links)
- `[표시할문자](이동할주소)`

### 이미지 (Image)
- `![대체텍스트](이미지주소)`
  - 이미지를 정상적으로 불러오지 못했을때 대체텍스트를 표시

### 인용 (Blockquote)
- `> + 문구`
> 문구
- 최대 6개 중첩 가능

### 표 (Table)
```bash
|칼럼1|칼럼2|칼럼3|
|---|---|---|
|내용|내용|내용|
|내용|내용|내용|
|내용|내용|내용|
```
|칼럼1|칼럼2|칼럼3|
|---|---|---|
|내용|내용|내용|
|내용|내용|내용|
|내용|내용|내용|

### 수평선 (Horizontal Rule)
- `- * _` 3번 이상 연속 작성
```bash
---
***
___
```
---
***
___

### **특수문자**
>'$ $' 사이에 입력하기

#### 수학기호

|사용법|반환|
|--|--|
|\ge|$\ge$|
|\le|$\le$|
|\cap|$\cap$|
|\cup|$\cup$|
|\times|$\times$|
|\div|$\div$|
|_{5}\mathrm{C}_{3}|$_{5}\mathrm{c}_{3}$|
|_{5}\mathrm{P}_{3}|$_{5}\mathrm{P}_{3}$|
|P(A ,B)|$P(A, B)$|

#### 그리스 문자
|사용법|반환|
|--|--|
|\alpha|$\alpha$|
|\beta|$\beta$|
|\gamma|$\gamma$|
|\delta|$\delta$|
|\omega|$\omega$|

#### 화살표
|사용법|반환|
|--|--|
|\uparrow|$\uparrow$|
|\downarrow|$\downarrow$|
|\rightarrow|$\rightarrow$|
|\leftarrow|$\leftarrow$|
|\Uparrow|$\Uparrow$|
|\Downarrow|$\Downarrow$|
|\Rightarrow|$\Rightarrow$|
|\Leftarrow|$\Leftarrow$|
|\leftrightarrow|$\leftrightarrow$|

#### 지수
|사용법|반환|
|--|--|
|2^{10}|$2^{10}$|
|2_{10}|$2_{10}$|
|2^{_3^2}|$2^{_3^2}$|

#### 글씨색상 변경
|사용법|반환|
|--|--|
|\<span style="color : red">red\</span>|<span style="color : red">red</span>|
|\<span style="background-color:red">red\</span>|<span style="background-color:red">bg_red</span>|