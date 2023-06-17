def search_number(lst, num):
    for i in lst:
        if i == num:
            return True
    return False

# Ejemplo de uso
lst = [1, 2, 3, 4, 5]
num = 4
print(search_number(lst, num))