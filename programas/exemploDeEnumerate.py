# l = [5, 9, 13]
# x = 0
# for e in l:
#     print(f"[{x}] {e}")
#     x += 1
# L = [5, 9, 13]
# for x, e in enumerate(L):
#     print(f"[{x}] {e}")

L = [5, 9, 13]
for z in enumerate(L):
    x, e = z
    print(f"Valor de z: {z}")
    print(f"[{x}] {e}")
