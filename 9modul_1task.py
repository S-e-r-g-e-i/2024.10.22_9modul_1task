# Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    dict_all_func = {}
    for i in functions:
        dict_all_func[i.__name__] = i(int_list)
    return dict_all_func


# Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
