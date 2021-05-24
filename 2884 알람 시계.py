H, M = map(int, input().split())

re_setting = H * 60 + M - 45
H = re_setting // 60
M = re_setting % 60
if H < 0:
    H = 23

print(f"{H} {M}")