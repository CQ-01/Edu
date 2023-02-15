
T = int(input("테스트 케이스 갯수를 입력하세요 : "))
answer = 0


def array(c1, c2, c3, c4):
    for i in range(c1, c3 + 1):
        for j in range(c2, c4 + 1):
            return (i, j)

for test_case in range(1, T + 1):
    num_area = int(input("색칠할 영역의 갯수를 입력하세요 : "))
    for area in range(1, num_area + 1):
        color = b, c, d, e, f = list(map(int, input("색칠 정보를 입력하세요 : ").split()))
        if f == 1:
            array(color[0 : 4])
        if f == 2:
            blue = color[0 : 4]
