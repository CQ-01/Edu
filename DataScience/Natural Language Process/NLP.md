# I. Natural Language Processing
## 1. Preprocessing
- 자연어 학습을 위해 수집된 데이터에 대한 전처리 작업이 중요
- 토큰화(Tokenization)
  - sentence, word, chracter
  - stop words (내용전달에 의미없는 단어)
  - stemming, lemmatization
- Encoding(vectorization)
  - 정수 인코딩(Integer Encoding)
  - 원핫 인코딩(One-Hot Encoding)

### Tokenization
- 수집한 말뭉치(corpus)를 토큰 단위로 나누는 작업
  - 토큰 단위 : 의미를 가지는 크기
- 일반적으로 형태소 단위의 토큰화 수행
  - 형태소 : 의미를 가지는 가장 작은 말의 단위
- 단어 토큰화 : 단어를 기준으로 나눔
- 문장 토큰화 : 토큰의 단위가 문장
- 한국어의 경우 조사와 띄어쓰기 등으로 영어보다 토큰화가 어려움

### Encoding
- 정수 인코딩 : 단어를 고유한 정수로 매핑하는 방식(단어 각각에 고유한 정수를 인덱스로 부여)
- 원핫 인코딩 : 단어집합 크기의 벡터 차원으로 0, 1을 사용하여 표현하는 벡터

## 2. Language Model
- 언어(단어, 문장)에 존재하는 특징을 표현하기 위해 확률을 할당하는 것
- 문장이 적절한지, 말이 되는지 판단하기 위한 기준
  - P(승객이 버스에 탔다) vs P(승객이 버스에 태운다)
  - 나는 딥러닝을 ~P(배운다) vs P(어렵다) vs P(고친다) vs P(가르친다)
- Bag of Words
- n-gram
- TF_IDF

### Bag of Words
- 문장이 가지는 모든 단어를 문맥이나 순서를 무시하고 일괄적으로 빈도값을 부여해 특징을 추출
- 발생 빈도가 높을수록 중요한 단어로 인식
- 장점
  - 쉽고 빠른 구축
  - 예상보다 문장의 특징을 잘 반영함
- 단점
  - 언어의 특성상 자주 등장하는 단어에 높은 중요도를 부여
  - 단어의 순서를 고려하지 않아 문맥의미 반영 부족
  - 희소행렬(sparse metrix)을 생성하여 학습시간 및 성능에 부정적 영향
- BoW - Feature Vectorization
  - M * N 크기의 행렬(term-document matrix) 생성
  - M개의 문장이나 문서
  - N 종류의 단어

### n-gram
> N개의 단어를 활용하여 다음에 올 단어를 추출한다
- 1-gram(unigram), 2-gram(bigram), 3-gram(trigram)
- 단어 순서를 무시하는 BoW의 단점을 보완
- 문장 내 전체 단어를 고려하는 언어모델과 비교해 정확도가 낮음
- trade-off : N이 너무 작으면 문장 맥락 파악이 어렵고, 너무 크면 카운팅할 확률이 낮아 희소성 문제 대두

### TF-IDF(Term Frequency - Inverse Document Frequency)
> 단어마다 중요도를 고려하여 가중치를 준다
- TF(단어 출현빈도) * IDF(역 문서 빈도) = TF-IDF 가중치
  - TF : 특정문서에서 특정단어의 출현빈도
  - DF : 전체 문서 중 특정단어가 등장한 문서 개수
  - IDF : DF의 역수
  - 전체 문서에서 빈출되는 단어의 중요도는 낮고, 특정 문서에서만 빈출되는 단어의 중요도를 높게 판단

## 3. Simularity
> 단어나 문장을 벡터로 변환 후 유사도를 비교
- Euclidean Distance
- Cosine
  
### Euclidean Distance Similarity
> 벡터간의 거리를 계산하여 유사도를 측정
- ed1 = $\sqrt{(5 - 5)^2+(1 - 2)^2}$
- 거리가 짧을 수록 유사도가 높음

### Cosine Similarity
> 두 벡터간의 사잇각을 계산하여 유사도를 측정
- cos $\theta$ = $\frac{A\cdot B}{||A||\cdot||B||}$
- 사잇각이 작을수록 유사도 높음
- 벡터의 크기가 아닌 방향성 기반

## 4. Embedding
> 단어나 문장을 벡터로 변환 후 벡터공간으로 끼워넣는 것, 전이학습
- Word Embedding : 단어를 희소표현이 아닌 밀집표현으로 변환
  - 희소표현(Sparse Representation) : 대부분 값이 0으로 표현되어 공간낭비, 단어 의미 담지 못함
  - 밀집표현(Dense Representation) : 실수값을 사용하여 표현되는 지정된 차원의 밀집벡터
- One-Hot Vector vs Embedding Vector

||One_hot Vector|Embedding Vector|
|--|--|--|
|차원|고차원|저차원|
|구조|희소벡터|밀집벡터|
|표현방법|확정적|데이터로부터 학습|
|값의 타입|0, 1|실수|

- Encoding과의 차이점
  - Embedding : 토큰들을 벡터로 변환하는 과정
  - Encoding : Embedding된 벡터들을 Sentence Matrix로 변환하는 과정
  - 보통 Encoder에서 Embedding과 Encoding 모두 수행

### Word2vec
> 문장 내의 비슷한 위치에 있는 단어로부터 유사도 획득
- 각각의 벡터가 단어간 유사도를 반영한 값을 가짐
- One-Hot Encoding 및 TF-IDF 방식의 단점 보완
- CBOW(Continuous Bag of Words)
- Skip-gram

- CBOW : 주변에 있는 단어를 사용하여 중간에 있는 단어를 예측하는 방법
  - 윈도우를 이동(Sliding Window)하며 생성된 데이터로 임베딩 학습
- Skip-gram : 중간에 있는 단어를 사용하여 주변에 있는 단어를 예측하는 방법
  - 윈도우 크기만큼 주변단어를 사용하여 생성된 데이터로 임베딩 학습

- Word2Vec Model

- Word2Vec Embedding
20230419NLP

- Visualization

## 5. BERT vs GPT
- 최근 NLP 동향 : Transfer learning & Fine tuning
  
### BERT
- 다른 단어와의 관계를 통하여 임베팅 매트릭스 생성
- transformer self-attention 구조 사용

- Bidirectional Encoder Representations from Transformer
- 양방향에서 입력값을 받아 결과를 도출
  
### GPT
- OPENAI의 NLP 모델
- Maksed Language Model