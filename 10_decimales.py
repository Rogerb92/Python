x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

#format(y, ".2g") le da formato pero solo usa 2 digitos
y_str = format(y, ".2g")
##! forma de pasar un float a str para comparar
print(y_str)
print(y_str == str(x))

print('*' * 10)

#abs es valor absoluto
tolerance = 0.0001
print(abs(x - y) < tolerance)