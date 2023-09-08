### EDA(탐색적 데이터 분석)
- 시각화
- 비시각화

시각적 인지, 수용능력
기계 중심의 $\rightarrow$ 관점 사람에 대한 이해
 ### NUMPY
 - C언어로 구현되어 고성능의 수치계산을 위해 제작
 - 벡터 및 행렬 연산에서 매우 편리한 기능 제공
 - array 구조
   - ndarray의 약자
   - 스칼라 : 하나의 숫자 데이터
   - 벡터 : 1D array(데이터 레코드)
   - 행렬 : 2D array
 - `np.array()` : 튜플 형태로 받음
 - `np.arange()` : 
 - `np.linspace()` : 
 - `np.shape` : 
 - `np.reshape` : 
 - `np.ndim` : 
 - `.T` : 행렬 서로 바꿈
 - 인덱싱 슬라이싱
   - `arr[N, M]` : N행 M열'
   - `arr[N : M]` : N부터 MEL

### PANDAS
> 데이터프레임
- 세로줄, 열(column) : 속성
- 가로줄, 행(row) : 정보

fillna
replace
describe
axis
sort_values
at
concat
copy
mean
isnull
gruopby

### Matplotlib
- plt.axis([x1, x2, y1, y2])
  - x1 ~ x2, y1 ~ y2
- plt.title() : 제목
- 
- plt.grid() : 기준선 생성
- plt.xlabel : x축 제목
- plt.ylabel : y축 제목
- plt.legend() : 범례
- plt.xlim([x, y]) : x축의 범위 x ~ y
- plt.ylim([x, y]) : y    "
- plt.show() : figure 보이게 함

### Folium
- 