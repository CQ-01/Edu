# 16s rDNA metagenome analysis
- 16s rDNA : 미생물이나 세균(archea) 등에서 많이 발견되는 16s(리보솜의 서브유닛의 한 종류) rRNA를 코딩하는 rDNA(리보솜 DNA)의 일부
- 16s rRNA : 16S라는 서브유닛을 구성하는 ribosomal RNA 
- metagenomics : 토양 환경 전체 샘플에서 추출된 유전물질에 대한 연구


## I. 분석전략
### 1. 시퀀싱 방법
- A. 환경 샘플 내의 박테리아에서 Community DNA를 추출
- B-1. 16s rRNA PCR
    - PCR 증폭 > 16s rRNA 시퀀싱 > 서열 비교
- B-2. Metagenomics
    - 시퀀싱 library > high-throughput sequencing으로 빠르게 시퀀싱 후 조립

    ||16s rDNA gene PCR|Whole metagenome|
    |--|--|--|
    |키메라 DNA|O|X|
    |비용|낮음|보통|
    |Covered community|알려진 종|모두|
    |계통 분류|O|O|
    |기능 주석|X|O|
    |플랫폼|454, illumina MiSeq|illumina HiSeq|

### 2. Metagenomic 데이터 분석 전략
- 16s rDNA 유전자 PCR
    - A. 시퀀싱
    - B. 낮은 퀄리티나 chimeric reads 제거
        - C-1. OTU 계산
            - D. Alpha Diversity(특정 지역이나 환경 내에서 미생물의 다양성을 측정)
<br></br>            
        - C-2. 계통 프로파일(RDP, NCBI)
            - D-1. Beta Diversity()
            - D-2. 미생물구조 비교


## II. 전처리
### 1. 전처리 방법
- 시퀀싱(MiSeq 이용)
- Adapter 제거(CutAdapt v1.11)
- paired end reads 병합(FLASH v1.2.11)
    - fastq 파일은 양쪽에서 읽은 paired end 두개의 파일로 나온다
- QC(SICKLE v1.2.11)
- 키메라 시퀀스 제거(ChimeraSlayer r20110519)

### 2. 시퀀싱 QC
![SeqQC image](/img/SeqQC.png)
- &ge; Q30 : 전체 염기서열 중 Q30(정확도 99.9%)을 넘는 염기의 비율
- &ge; Q20 : 전체 염기서열 중 Q20(정확도 99%)을 넘는 염기의 비율

### 3. 전처리 결과
![결과 image](/img/PreproResult.png)
- No. of Reads : QC 이후 reads 수
- No. of Bases : QC 이후 염기서열 수
- Removed chimera reads : 키메라 시퀀스가 제거된 후 reads 수
- Removed chimera reads(%) : 전체 시퀀스 대비 키메라 시퀀스가 제거된 reads의 비율
- Removed chimera bases : 키메라 시퀀스가 제거된 염기 수


## III. OTU와 Alpha Diversity
### 1. OTU와 Alpha Diversity 계산방법
- A. 전처리 된 시퀀스
- B. OTU 계산
    - Qiime에서 pick de novo OTUs(DB 없이 97%이상 유사도 끼리 OTU)
- C. Alpha Diversity 계산
    - Shannon 지수(생물 다양성 지수)

### 2. OTU와 Alpha Diversity 계산
![](/img/OTU%20AD%20계산.png)
- No, of Reads : 전처리 된 reads 수
- OTUs : Qiime을 이용해 97%의 유사도를 통해 클러스터링된 시퀀스로 결정된다
- Alpha Diversity : 각 샘플의 alpha diversity를 측정하기 위해 shannon지수를 사용해 OTU를 분석했다.

## IV. 계통 프로파일링
### 1. 계통 프로파일링 방법
- A. 전처리된 시퀀스
    - B-1(속 분석). 계통 프로파일링(RDP classifier v.2.11)
        - C. 계통 할당과 krona plot(krona Tools v.2.7)
        - D. Beta Diversity 계산(Bray-Curtis 거리)

    - B-2(종 분석). 클러스터링
        - C. 계통 프로파일링(NCBI)
        - D. 계통 할당과 krona plot(krona Tools v.2.7)
            - krona plot : 원형 그래프로 분류학적 계층구조를 시각화하는 그래프
        - E. Beta Diversity 계산

### 2. 계통 프로파일링
- RDP
    ![](img/RDP%20taxpro.png)
- NCBI
    ![](img/NCBI%20taxpro.png)

### 3. Beta Diversity
- RDP
    ![](img/RDP%20beta.png)
- NCBI
    ![](img/NCBI%20beta.png)

## V. 데이터 구조
### 1. 전처리
- [sample].preprocessed.fasta
- Preprocessing.summary.xls

### 2. OTU와 Alpha Diversity
- [sample]_97_OTUs.txt
- OTUs_AlphaDiversity_Shannon_index.xls

### 3. 계통 프로파일링
#### RDP
- [sample]
    - [sample].rdp.krona.html
    - [sample].tax
- RDP.Taxonomy.[taxon rank].xls
- RDP.Taxonomy.[taxon rank].xls.betadiversity.PCAPlot.png
- RDP.Taxonomy.[taxon rank].xls.betadiversity.xls
- RDP.Taxonomy.[taxon rank].xls.heatmap.png
- RDP.Taxonomy.[taxon rank].xls.MDSPlot.png

#### NCBI
- [sample]
    - [sample].ncbi.krona.html
    - [sample].ncbi.krona.html.files
    - [sample].ncbi.taxonomy.Annotation.xls
- NCBI.Taxonomy.[taxon rank].xls
- NCBI.Taxonomy.[taxon rank].xls.betadiversity.PCAPlot.png
- NCBI.Taxonomy.[taxon rank].xls.betadiversity.xls
- NCBI.Taxonomy.[taxon rank].xls.heatmap.png
- NCBI.Taxonomy.[taxon rank].xls.MDSPlot.png