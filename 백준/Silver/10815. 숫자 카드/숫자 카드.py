n = int(input())
my = list(map(int, input().strip().split()))
my_dict = {mine: None for mine in my}
m = int(input())
yours = map(int, input().split())
for y in yours:
    if y in my_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')
