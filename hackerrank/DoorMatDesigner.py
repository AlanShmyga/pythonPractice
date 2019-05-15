filler = "-"
cell = '.|.'
n, m = map(int,input().split())

for i in range(0, n//2):
    design = f"{cell * i}" + cell + f"{cell * i}"
    print(design.center(m, filler))

print('WELCOME'.center(m, filler))

for i in range(n//2, 0, -1):
    design = f"{cell * (i-1)}.|.{cell * (i-1)}"
    print(design.center(m, filler))

