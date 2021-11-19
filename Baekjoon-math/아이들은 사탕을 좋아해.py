T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    answer = 0

    for i in candy:
        answer += i // k

    print(answer)
