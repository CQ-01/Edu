# Javascript 기본논리
## 변수
```bash
 a = 1
 let a = 1
 var a = 1
 const a = 1

 var season = ["봄", "여름", "가을", "겨울"]
 # 인덱스 기능 사용가능
```

# 연산자
```bash
/ : 나눈 몫
% : 나눈 나머지
++ : 1증가
-- : 1감소

+= : 더한 값을 할당
-+ : 뺀 값을 할당
*= : 곱한 값을 할당
/= : 나눈 값을 할당
%= : 나머지 값을 할당

== : 내용이 서로 같으면 true
=== : 내용이 서로 같고 자료형도 같으면 true
!= : 서로 같지 않으면 true
!== : 서로 같지 않거나 자료형이 같지 않으면 true
```

## 함수
```bash
# 유형 1
function function_name(x) {
    let answer 2*x + 6;
    return answer;
}
# 유형 2
function_name = (x) => {
    let answer = 2*x + 6;
    return answer;
}
# 유형 3
((x) => {return 2*x + 6})(x값 입력)
```
- 입출력값이 없어도 동작(코드 묶기 위한 용도)
## 조건문
```javascript
if (money>5000) {
    console.log("택시를 탄다")
} else if (money > 2000) {
    console.log("버스를 탄다")
} else {
    console.log("걸어간다")
}
console
```
## 반복문
```javascript
for (let i = 0; i < 10; i++>) {
    console.log("나무찍기" + i)
}
```