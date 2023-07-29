# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    rows = [int(i) for i in range(1, num_rows + 1)]
    columns = [int(i) for i in range(1, num_columns + 1)]
    print(*rows)
    for x in range(1, len(rows)):
        print(rows[x], end=' ')
        for y in range(1, len(columns)):
            print(operation(rows[x],columns[y]), end=' ')
        print()


print_operation_table(lambda x, y: x * y)
