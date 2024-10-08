import sys 

# 식당 수 
N = int(sys.stdin.readline())
# 식당 별 고객수
custs = list(map(int,sys.stdin.readline().rstrip().split()))
# 팀장 최대 검사 가능 인원수, 팀원 최대 검사 가능 인원수 
max_value_ldr, max_value_mbr = map(int,sys.stdin.readline().split())
ans = 0
for cust in custs:
    remain_ldr = (cust-max_value_ldr)
    if remain_ldr > 0:
        if remain_ldr > max_value_mbr:
            n_mbr = remain_ldr//max_value_mbr
            if remain_ldr % max_value_mbr == 0: 
                n = n_mbr + 1 # 팀원 수 + 리더 한명 
            else: 
                n = n_mbr + 2 # 팀원 수 +  리더 한명 + 나머지 팀원 한명 
        else:
            n = 2 # 리더 한명 팀원 한명 
    else:
        n = 1 # 리더 한명 
    ans+=n

print(ans)