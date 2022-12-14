# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

X = int (input ('Введите X: '))
Y = int (input ('Введите Y: '))
Z = int (input ('Введите Z: '))
left = not (X or Y or Z)
right = (not X) and (not Y) and (not Z)
def is_statement(left, right):
    if left == right:
        print(f"Утверждение истинно")
    else:
        print(f"Утверждение ложно")
print (is_statement (left,right))