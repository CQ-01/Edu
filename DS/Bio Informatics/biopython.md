## 라이브러리 설치
```py
!pip install biopython==1.77
```
## Bio.Seq 활용
```py
from Bio.Seq import Seq

dna = Seq('ATGCATGC')
# seq 객체화

mrna = dna.trancribe()
# RNA 전사

ptn = mrna.translate()
# 단백질 번역
ptn = mrna.translate(to_stop=True)
# 종결코돈에서 종료하기

comp_seq = dna.complement()
# 상보적 서열 만들기
rvs_comp_seq = dna.reverse_complement()
# 역상보적 서열 만들기
```

## 코돈 테이블
```py
from Bio.Data import CodonTable
codon_table = CodonTable.unambiguous_dna_by_name['Standard']
# 인간 코돈 테이블
codon_table2 = CodonTable.unambiguous_dna_by_name['Vertebrate Mitochondrial']
# 미토콘드리아 코돈 테이블
```

## Bio.SeqUtils 활용
```py
from Bio.Seq import Seq
from Bio.SeqUtils import molecular_weight

seq1 = Seq('ATGCAGTAG')
print(molecular_weight(seq1))
# 서열의 무게 계산

from Bio.SeqUtils import six_frame_translations
print(six_frame_translations(seq1))
# 가능한 모든 번역 구하기

from Bio.SeqUtils import MeltingTemp as mt
print(mt.Tm_Wallace(seq1))
# 이중나선 분리 온도

from Bio.SeqUtils import seq1
essential_amino_acid_3 = "LeuLysMetValIleThrTrpPhe"
print(seq1(essential_amino_acid_3))
# 아미노산 서열 기호를 약자로 변환

from Bio.SeqUtils import seq3
essential_amino_acid_1 = "LKMVITWF"
print(seq3(essential_amino_acid_1))
# 아미노산 약자를 서열 기호로 변환
```