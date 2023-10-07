# 16s rDNA metagenome analysis
## I. 용어 정리
- 16s rDNA : 미생물이나 세균(archea) 등에서 많이 발견되는 16s(리보솜의 서브유닛의 한 종류) rRNA를 코딩하는 rDNA(리보솜 DNA)의 일부
- 16s rRNA : 16S라는 서브유닛을 구성하는 ribosomal RNA 
- metagenomics : 토양 환경 전체 샘플에서 추출된 유전물질에 대한 연구


## II. 분석전략
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

## III. 전처리
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