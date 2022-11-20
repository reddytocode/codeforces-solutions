# https://codeforces.com/problemset/problem/1759/A
# title: A. Yes-Yes?


n = int(input())

no_yes = ["YES", "Yess", "se"]
allowed = "Yes"*20

def solution(s):
    if s in allowed:
        return "YES"
    return "NO"


for _ in range(n):
    s = input()
    print(solution(s))

