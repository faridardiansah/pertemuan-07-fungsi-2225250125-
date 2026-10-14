def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(jumlah_n(1))
print(jumlah_n(5))
print(jumlah_n(10))
print(jumlah_n(100))

# Menggunakan rumus n(n+1)/2
def rumus_jumlah(n):
    return n * (n + 1) / 2

print(rumus_jumlah(1))
print(rumus_jumlah(5))
print(rumus_jumlah(10))
print(rumus_jumlah(100))