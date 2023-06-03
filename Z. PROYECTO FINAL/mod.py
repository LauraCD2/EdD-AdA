#Suponga que a y b son n´umeros enteros, donde a ≡ 11( mod 19) y b ≡ 3( mod 19). 
# Encuentre el n´umero entero c, 0 ≤ c ≤ 18 tal que: c ≡ 13a( mod 19)
a = 11 % 19
b = 3 % 19
c = 13 * a % 19
print(c)

# c≡ 8b( mod 19)
c = 8 * b % 19
print(c)
 
#c ≡ 2a^2 + 3b^2 ( mod 19)
c = (2 * a**2 + 3 * b**2) % 19
print(c)

#Determine x tal que 11 · x ≡ 1( mod 113)
for x in range(113):
    if 11 * x % 113 == 1:
        print(x)
        break
    # Explique por qu´e el valor de x que encontr´o es el ´unico que satisface la congruencia.
    # Porque 11 y 113 son primos relativos, es decir, no tienen factores comunes.
    # Por lo tanto, el valor de x es el inverso multiplicativo de 11 en Z113.
    # PASO A PASO: por teorema de bezout.
    # 113 = 11 * 10 + 3
    # 11 = 3 * 3 + 2
    # 3 = 2 * 1 + 1
    # 1 = 3 - 2 * 1
    # 1 = 3 - (11 - 3 * 3) * 1
    # 1 = 4 * 3 - 11
    # 1 = 4 * (113 - 11 * 10) - 11
    # 1 = 4 * 113 - 51 * 11
    