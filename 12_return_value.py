# fungsi dengan return value


def kuadrat(arg):
    total = arg ** 2
    print('Nilai kuadrat dari', arg, ' = ', total)
    return total


a = kuadrat(5)
print(a)
print('=' * 68)

# fungsi dengan return value dan multiple argument


def kali(arg1, arg2):
    hasil = arg1 * arg2
    print(arg1, '*', arg2, '=', hasil)
    return hasil


b = kali(2, 5)


def tambah(arg1, arg2):
    hasil = arg1 + arg2
    print(arg1, '+', arg2, '=', hasil)
    return hasil


c = tambah(5, 5)

d = c * b
e = kali(4, 2) + tambah(5, 5) % kuadrat(2)
f = c + b + a

print(c, '+', b, '+', a, '=', f)
print(d)
