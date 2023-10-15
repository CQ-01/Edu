# I. 바이오 인포매틱스 개요
## 필요 지식
- 통계(수리통계, 회귀분석, R)
- 컴공(이산수학, 데이터)
- 바이오(분자생물학, 유전학)

## 하는 일
- 도구 : R, Python
- 항암 표적물질 발굴
- 기본 유전체 표준 Reference 제작

## 실무
- PCR ~ NGS
- 한양대 융합생명공학등 융합학부가 늘어나는 추세
- 방대한 분량을 혼자 다 배울 수는 없기에; 휴먼 네트워크가 중요
- 마크로젠, 테라젠, DNA링크, 휴앤바이옴(미생물 쪽)

# II. 분자 생물학 기초
## 1. Central Dogma
### DNA
> 생명체의 설계도
- 하나의 세포당 1 copy 존재한다
- 이중나선의 안정적 구조, A, G, C, T 염기서열로 구성
- 복제 중 오류 발생 시 repair 기작이 발달
  - mutation 발생 시 암 발생
- 전체 DNA 중 3~5%만 실제 RNA 및 단백질로 발현된다(=exome)
- DNA 영역을 전체 sequencing 하는 WGRS
- 실제 코딩이 진행되는 영역만을 시퀀싱하는 WES
- 특정 타깃만을 시퀀싱하는 Target sequencing
- cDNA : 한번 전사되었던 RNA를 DNA로 되돌림 (실험 등 목적으로 RNA를 안정적으로 유지하기 위함)
  - coding되지 않은 DNA서열이 존재하지 않음
  - 현대의 sequencer가 ATGC 서열만 해독 가능하기 때문에 활용
  
### RNA
> 단백질의 중간과정으로 여겨졌으나 자체적으로 효소로 작용하는 등 특이기능 연구 중
- A, G, C, U의 염기서열로 구성, 단일가닥으로 존재하여 불안정한 구조
- 단백질로 전환이 되는 mRNA, 염기서열과 일치하는 단백질을 옮기는 tRNA, 리보솜을 구성하는 rRNA 등
- 하나의 DNA 서열로부터 여러개의 RNA transcript가 생겨날 수 있다
  - RNA 성숙과정에서 엑손들의 배치 순서 및 포함여부 결정
- RNA maturation : pre-mRNA에서 인트론 서열이 제거되는 과정
- mRNA는 RNA maturation 완료 후 3' end 쪽에 poly-A tail이 capping 된다(RNA 분해효소 기능 억제)
- transcription factor(TF) 단백질, RNA polymerase 단백질이 전사를 돕는다
  - RNA 연구 시 굉장히 중유하게 고려해야할 요소
- miRNA : dicer protein과 결합하여 스스로와 상보적인 서열을 가지는 RNA 서열을 절단함으로서 발현 조절

### Protein
> 최종적으로 생체 내 현상을 매개하는 분자단계
- 세 개의 RNA 서열로부터 아미노산 서열을 합성(codon)
- mRNA에 리보솜이 결합하여 상보적인 tRNA가 배달하는 아미노산들이 하나의 가닥으로 조립됨

### Insight
- DNA는 특정한 조건이 아닌 이상 일정한 수를 유지하며, 생체 과정을 매개할 때 양이 변화하는 것은 RNA, Protein
- RNA나 Protein의 발현량이 변화했다
- 분자 단계의 발현량 변화가 최종적으로 어떠한 표현형(눈에 보이는 형질)의 변화로 이어진다

### genome 사이즈
  - 인간 : 30억 Base Pair(염기의 수)
  - genome 사이즈가 크다고 고등동물임을 뜻하는 것은 아님
  - 자이언트 세콰이어나 아홀로틀 샐러맨더는 인간의 몇배에 달하는 BP

### 단일염기다형성(SNP)
  - 하나의 염기가 다른 염기로 대체되며 나타나는 변이
  - 모노모피즘 : 특정 염기 위치에서 대체로 모든 개체가 동일한 염기를 가짐

# III. 데이터 분석 과정
## 1. EDA
> 탐색적 데이터 분석, 데이터를 처음 접하는 사람들이 데이터의 구조와 패턴을 파악하기 위해 사용, 견적을 내는 일
- 획득한 데이터에 대해 critic한 태도를 유지

### EDA의 대상
- 일변량(Univariate)
  - EDA를 통해 한 번에 파악하려는 변수가 1개
  
- 다변량 변수
  - EDA를 통해 한 번에 파악하려는 변수가 여러 개
  - 변수들 간의 관계를 보는 것이 주요 목적

### EDA의 종류
- 시각화(Graphic) : 차트 혹은 그림 등을 이용해 데이터 확인, 데이터를 한 눈에 파악 용이
- 비시각화(Non-Graphic) : 주로 summary statistics 활용, 정확한 데이터값 파악 용이

### EDA의 유형
- 일변량 비시각화(Uni - Non Graphic)
  - 주어진 데이터의 분산(distribution)을 확인하는 것이 주목적
  - 수치형 자료라면 summary statistics를 주로 활용한다.
  - 범주형 자료라면 발생(occurence), 빈도(frequency), 탭화(tabulation)

- 일변량 시각화(Uni - Graphic)
  - 주어진 데이터를 전체적으로 살펴보는 것이 주목적
  - Histogram, pie chart, stem-leaf plot, boxplot, QQplot..
  - 값들이 다양하다면 binning, tabulation 등 활용 가능
  
- 다변량 비시각화(Multi - Non Graphic)
  - 변수간 관계(relationship)를 확인하는 것이 주목적
  - cross-tabulation, cross-statistics(correlation, covariance) 등 활용
  - 범주형 데이터는 행과 열을 바꾸는 cross-tabulation 적용가능
  - 수치형 데이터는 cross statistics 활용가능
  
- 다변량 시각화(Multi - Graphic)
  - 범주형과 수치형은 boxplot, stacked bar, parallel coordinate, heatmap
  - 수치형끼리는 scatter plot 등
  
- Negative control : 분석이 올바르게 수행되었다면 이 값이 반드시 나오지 않음
- Positive control : 분석이 올바르게 수행되었다면 이 값이 반드시 도출됨
- bulk RNA-seq $\rightarrow$ scRNA-seq

## 2. NGS
- 이전에는 700~1000개 base pair 밖에 읽을 수 없었음
- downstream analysis : 시퀀싱 과정이 편해짐에 따라 중요도 가중
  - 시퀀싱데이터 해석할 수 있을 뿐만 아니라 생물학적 통찰을 찾을 수 있는 사람
- 실제 작용하는 건 RNA, 단백질이나 DNA ~ RNA 서열만 읽을 수 있음
- biological replicate 우선, technical replicate 차선
- fastq : 151bp 염기서열
- normalization은 필수, 연구자들 사이에 합의가 이루어짐
- NGS 데이터 생산은 점점 쉬워지나, 적합한 분석을 할 줄 아는 것은 더 어려워진다

## RNA-seq
### 순서
- 시퀀싱
  
- raw reads(fastq)
  - 시퀀싱으로 읽은 서열정보 raw data
  - 151bp를 하나의 reads로 하여 6M ~ 10M개 정도의 reads 수를 확보해야
  
- Alignment
  - 참조 서열에 mapping 하는 작업
  - 참조서열 정보가 없는 경우 DNA-seq을 통해 참조서열 구축
  
- Quantification
  - gene_expression.xlsx파일 등 ; Quantification 완료된 상태
  - align을 마치고 mapping된 reads를 count
  - 특정 유전자 영역에 매핑된 reads의 수를 의미하며, 유전자의 발현값으로 분석하기 위해서는 반드시 생산량을 고려하여 정규화(normalization) 과정이 필요

- Down-stream analysis

### 부가설명
- Tuxedo Protocol
  > 전반적인 워크플로우에 사용되는 툴 들의 이름이 턱시도와 관련된 이름들이라서

- Normalization
  - R/FPKM
  - TPM
  - TMM

- 약점 : RNA가 많이 발현된다고 반드시 Protein이 많이 발현되는 것은 아니다

DEG분석
  edgeR

  input을 specific하게 지정하기
  bioinfo 파이프 라인 >> 사용되는 툴 사이의 인풋과 아웃풋을 맞추는 것이 절반?
  차등발현 유전자가 어떠한 pathway(기능, 표현형?)와 연관이 있는가

### pathway 분석론
- 1세대 pathway 분석 방법론
  - GSEA, DAVID
  - ORA : 직관적으로 p-value높은 것이 연관성이 있다고 판단
- 2세대 pathway 분석 방법론
  - 내가 뽑은 차등발현유전자가 아슬아슬하게 발현시키는 경우 p-value가 크게 나오나 실제 연관되는 것보다 과장되어 pathway와 연관되어 있다고 결론지어질 가능성이 있는데, 2세대는 발현량을 같이 고려해서 pathway와 연관시키기 때문에 상대적으로 데이터의 왜곡이 발생할 가능성을 낮추는 방법이다.
  - GSEA, 널리 사용되어 2세대 방법론을 GSEA라고 칭하는 경우도
  - 한 눈에 봤을 때 직관성은 떨어지나 읽는 방법만 알아 놓으면 해석하기 편한 방법이다.
  - 데이터 포매팅이 약간 필요해서 손이 들어가긴 하나 그에 비해 얻을 수 있는 것이 많아 universial하게 사용됨
- 3세대 pathway
  - 단점 : 데이터 포매팅이 어렵고 리소스를 많이 차지한다. 추가적으로 정의해야 할 요소들이 많다
  - 장점 : 메타데이터(분석조건)을 굉장히 다원화 시킬 수 있다. 여러가지 변량 간의 연관도 등
  - 네트워크 애널리시스 : pathway 사이에 network를 연결해준다. 온갖 방법론에 따른 툴들이 즐비함.

- 세대로 구분하나, 차 세대가 이전세대를 완벽히 커버하는 것은 아님

- 분자생물학과 전반적인 워크플로우
  - BI, 하이브리드 직종으로 컴퓨터사이언스, 생물학적 인사이트 중 어느곳에 중점을 두어야 하는가
  - Technician vs Scientist, 당연히 생물학적 인사이트에 중점을 두어야 한다
  - 컴퓨터사이언스는 보조할 수 있는 수단들이 많다.

## 분석 논문
- 논리전개 방식을 알아두기
- 논문 리뷰

## GEO 활용 RNA-Seq
- 같은 샘플을 가지고 실험했기 때문에 결과가 크게 다르면 안 됨
- EDA과정 : histogram, scatter plot, box plot을 확인해 데이터간의 전반적인 분포확인
- DEG분석 : edgeR

## GSEA
> 2세대 pathway analysis

### 과정
- Gene expression data(.gct)
- phenotype data(.cls)
- DB 파일을 다운로드 받아왔을 때도 구조 확인하는 버릇
- Gene Set Database(.gmt)
- Ranked Gene Lists(.rnk)

### 단점
- data prep과정이 번거롭다
- 데이터를 분석하는데에 있어 비직관적이다
- 스크립트를 통한 자동화 불가능

## fGESA
> fast Gene Set Enrichment Analysis
- GSEA 방법론 자체는 우수하나 프로그램의 단점이 많음
- bioconductor tool중 40번째로 많이 사용됨

어느 유전자나 단백질이 어떤 상황에서 많이 발현되느냐?

## DB
### GEO

### TCGA
- GDC를 통해
- GEO보다 양질의 데이터
- 암정복에 대한 단서는 이미 TCGA에 올라와 있을 것이다

## 새로운 방법론
- RNA-Seq based
  
### scRNA-Seq
- 암에 걸렸다고 가정하면 어느 세포는 정상세포이고, 어느 세포는 암세포일 것인데 기존 mRNA-Seq은 전체 세포를 하나의 데이터로 만들어 분석하나, single cell RNA-Seq은 세포 하나별 데이터를 보존하여 섬세한 결과를 도출 가능
- RNA Seq보다 비직관적

### Spatial transcriptomics
> 세포의 실제 위치에 따라 발현되는 유전자의 차이를 구분

### Multiomic Analysis    
> genomics(DNA) + transcriptomics(RNA) + proteomics(Protein)

## Cloud Computing
|on-premises|cloud computing|
|--|--|
|높은 초기 투자 비용|사용한 만큼만 지불|
|한정된 용량|유연한 용량|
|많은 공수 및 소요시간|적은 노력 및 소요시간|

# Question
- 시퀀싱 과정에서 염기서열들이 무작위로 뒤섞이는데 본래의 위치를 찾는 방법?

### 10x
파이프라인 제공(cell ranger)
count : alignment, filtering, barcode counting, UMI counting
실험 방법이 다르니 
10x barcode : 셀들을 분류, UMI : PCR 개발
unique molecular index : PCR로 뻥튀기 된 상태에서 실제 샘플 값을 확인하는 방법

### result structure
- matrix
  - filtered_bc_matrix : 어느정도(10x에서 정한) 검증된 분자만 검출
    - 세포 사멸 단계를 연구하는데 10x에서 사멸 직전 세포로 판단해 필터링 당한다면?
  - raw_feature_bc_matrix : 필터링 하지 않음
- bam
  - .bam : 바이너리 파일로 용량 최적화
  - fastq 파일 자체를 bam파일로 만들기도 함
- summary
  - summary.html

### seurat
> scRNA-seq전용 R 패키지

### 카운트 매트릭스
- 4*4*4*4 하면 capa 확인이 된다? 10만 개 이상은 퀄리티가 좋지 않다?
- barcode.tsv : 셀 번호
- feature.tsv : 유전자 번호
- matrix.mtx : 전체 통계

### 실습
- min.feature(100) : sum 최소가 100
- assign(a, b) : a안의 변수를 b에 할당한다
- , add.cell.id = c('ctrl', 'stim') : 머지할 때 cell id 뒤에 이름 추가
- log10, UMI / QC(퀄리티 컨트롤)하기 위한 정보? 

### QC(퀄리티 컨트롤)
> 분석하기 위해 최적화된 세포들만 남겨놓는다
- 목적 : 셀타입 identification 정확하게 하기 위함
- UMI count per cell : 셀당 분자
  - 적을 때 : 진짜 적은 것(사멸 중) or 잘못 매핑된 것
  - 많을 때 : 잘못 매핑된 것 or 실제 많이 발현이 되는 것
  - 이봉그래프는 안 좋은 샘플, 두번째 봉에 있는 것들을 분석
  - 복잡도??

### Normalization(정규화)
- FP control :
- depth를 맞추는 방법(sequencing depth normalization)
  - 5'에서 150bp 시퀀싱하는 방법 vs 3'에서 하는 방법
- total count 
- scTransform : 지수를 만들어 정규화를 돕는다, 세포 phase에 따라 발현 유전자가 달라질 수도 있는 등

### Integeratino

### 클러스터링
- PCA : 군집 분석

T-SNE : 글로벌 스탠타드를 유지해야 할 때, 각각의 발현값을 보고 싶을 때
UMAP

### Dimplot

## Target Panel
- WGS : depth를 얼마만큼 해독을 해야 하나? 30x 이상(homo hetero변화 잡기 위해)
WES : 희귀한 돌연변이들을 잡기 위해서는 ~60000x 까지 해봐야
팩바이오 장비 > 시퀄

- splice accept : 스플라이소좀이 gt at서열을 인지해 intron 제거
WGS : 
- 긴 사이즈를 depth 있게 확인하기 어려움(mutation은 WES가 유리)
- genome 전반적으로 구조적인 변이를 보기는 좋음

- germline mutation : 선천적 돌연변이(생식세포 돌연변이)
- somatic mutation : 후천적 돌연변이(체세포 돌연변이)

- somatic mutation call
  - single nucleotide variant
  - short indels
  - structual variant
  - copy number(copyno)

- 영향주는 요인
  - 세포분열
  - 노화
- 환경
  - aflatoxin

- Exome/target capture
  - 미리 exome과 상보적인 RNA서열들을 만들어 놓은 뒤 자성을 띄게 한다
  - 자석으로 RNA서열과 결합한 exome들을 가져와 seq

- Exome/target analysis pipeline
- PCR duplication : 동일한 서열들은 PCR로 증폭된 같은 서열들로 bias를 줄 수 있기 때문에 정리

### Padigree(가계도)
- 상염색체 우성유전
- 상염색체 열성유전

NCBI >> ClinVar
- variant DB

- 돌연변이의 종류
  - missense mutation : 서열이 바뀌어 아미노산이 달라짐 
  - nonsense mutation : 스탑 코돈 유발
  - silent mutation : 코드는 바뀌었으나 영향x
  - frameshift mutation : 염기서열 해독이 하나씩 밀림

|종류|기호|
|--|--|
|coding DNA|c.|
|genomic DNA|g.|
|mito DNA|m.|
|RNA|r.|
|Protein|p.|

- NM number : RNA식별 번호

- ACMG 가이드라인 한번 읽어 볼 것

- 관련 DB
  -dbSNP, ExAC, ClinVar, 1000 genome project, OMIM

- 액체 생검

- 병리사 : 백정이다, 암 protein조직을 작게 썰어 파라핀(촛농)에 심어 놓는다
최소 시료량 : 슬라이드4 micron 10장, DNA > 100ng, 4cc EDTA tube 1개
- NGS < 암을 정복하기 위해 

- TIL(tumor-infiltrating lymphocyte) vs immune desert : 종양에 면역세포가 모여있는지 여부

- immuno therapy : 종양에 면역세포가 많이 모여있는지 아닌지 여부에 따라, 돌연변이 양이 많은지 적은지 여부에 따라 치료방법이 달라져야 한다

- 면역항암제, 마이크로바이옴, 알츠하이머
- 장 환경이 뇌와 연관되어 있다 ; 장내 미생물
- 미생물이 약이 된다

- 혈액이나 타액에는 cell이 많아 host cell의 DNA가 많이 나온다, 분변에는 bacteria들이 많이 나옴

- 벼 조차 4만개의 유전자를 보유하는데 인간은 2만개에, life cycle에 많이 관여하는 것은 2천개 뿐. 나머지는 체내의 미생물의 역할로 보완
- 미생물이 많이 서식하는 곳 : 피부, 소화계(구강~항문), 호흡계, 장
  외래 인자에 항상 노출되는 곳에 미생물들이 존재한다(defense 목적)

## 프로바이오틱스
- 유산균과 probiotics가 일치하는 개념은 아니다
- prebiotics : 프로바이오틱스의 먹이
- synbiotics : 프리바이오틱스 + 프로바이오틱스
- 정확한 용량, 구체적인 효능 등 입증 후에 건강기능식품 등록
- 홍삼(사포닌) 바로 다음 시장이 프로바이오틱스

## 미생물시장
- 체중 70kg 성인의 장내미생물 무게는 약 200g
- 인간의 세포수와 체네 세균수가 거의 비슷함
- 95%의 세균은 대장에 존재
- 산업화 시대로 넘어가며 이로운 미생물 감소(alpha diversity)
- 임신했을 때 환경에 따라 아이들의 건강이 결정
- 자연분만: 질내 유익균 도포
- 사춘기 시기 장내 세균총의 변화
- 인종이 아니라 식단이 중요한 역할을 한다(동남아에서 이민 온지 6~9개월만에 서구화 장내환경 구성)
- 강원도와 제주도 외 한국의 장내 미생물 비중이 비슷하다
- FMD(단식모방식단) : 제한된 음식을 먹음으로서 몸은 단식한다고 느끼면서 세포에 영양분 공급을 지속
- 미생물의 주기적인 조절로 비만예방
- 제왕절개로 출산할 경우 질내 분비물 아기에 도포함으로서 자연분만 효과
- 산모의 분변 성분을 아기에게 먹임
- 장내 미생물을 분석하여 
- 제철과일 100%, 냉동과일 70%


박사를 빨리 하자
파이썬 하나만 파자

## fastq
- read 끝에 붙는 것이 adapter
- read 사이에 위치한 것이 inner distance
- adapter를 제외한 것이 insert size
- adapter를 포함한 것이 fragment size

## 돌연변이
### 돌연변이의 종류
- Point mutation : DNA내의 한 개의 염기서열이 바뀜
- Gene amplification : 유전자가 증폭되어 중복서열이 발생
- Chromosomal translocation : 염색체 간의 부분이나 완전한 DNA조각이 이동
- Local DNA rearrangement : DNA내의 일부 영역이 추가/제거 되거나 이동
- Insertional mutagensis : 다른 생물에서 기원한 DNA가 삽입됨

## GWAS
> Genome wide association study
- 유전자 영역을 전체적으로 커버하는 연관성 분석
- 통계적인 유의수준(p-value 0.05 미만)
- 10년대에 GWAS 연구 전성기가 왔으나..
- GWAS + 기능연구가 결합되어야 좋은 학술지에 실릴 수 있게 됨
- 이후 total omics분야를 요구받는 시대

### 유전지표(Marker)
변경시 의미가 바뀌는 것?

### Polymorphosm
- mutation : 1% 미만 존재
- polymorphism : 1% 이상 유지되는 변이서열

SNP들이 할 수 있는 설명률이 떨어짐
intron이나 intergenic발 변이라서 원인변이인지 알 수 없는
association간의 통계적 관계가 있다면 그것까지 분석은 불가