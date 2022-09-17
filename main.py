######### Задание 1 ##########
print('Задание №1')
print()
cook_book = {}
dish_ingredients = {}

with open('recipes.txt', encoding='utf8') as file:
    for line in file:

        list_dict = []
        dish = line.strip()
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            ingredients = file.readline()
            ingredient_name, quantity, measure = ingredients.split(" | ")
            dish_ingredients = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
            list_dict.append(dish_ingredients)
        cook_book[dish] = list_dict
        file.readline()

import pprint

pprint.pprint(cook_book, width=100, sort_dicts=False)

##### Задание 2 ########
print()
print('Задание №2')

dishlist = {'1': 'Омлет', '2': 'Утка по-пекински', '3': 'Запеченный картофель', '4': 'Фахитос'}
dishesinput = input(f'Меню: \n 1: Омлет\n 2: Утка по-пекински\n 3: Запеченный картофель\n 4: Фахитос\n '
                    f'Укажите номера блюд через запятую: ').split(',')
person_count = int(input('Введите количество персон: '))
dishes = []
for i in range(len(dishesinput)):
    if int(dishesinput[i]) < 0 or int(dishesinput[i]) > 4:
        print(f'Блюда под номером {dishesinput[i]} нет')
        continue

    dishes.append(dishlist[dishesinput[i]])


def get_shop_list_by_dishes(dishes, person_count):
    """
    :param dishes: блюда из меню
    :param person_count: количество персон
    :return: словарь с названием ингридиентов и их количество.
    """
    dict_dishes = {}
    for dish in dishes:
        if dish not in cook_book.keys():

            print(cook_book.keys())
            return print(f'В списке блюд нет блюда {dish}')
        else:
            for ingredient in cook_book.get(dish):
                if ingredient['ingredient_name'] not in dict_dishes:
                    dict_dishes[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                  'quantity': int(
                                                                      ingredient['quantity']) * person_count}
                else:
                    dict_dishes[ingredient['ingredient_name']]['quantity'] += (
                            int(ingredient['quantity']) * person_count)

    return dict_dishes


print(f'\n Список ингридиентов: \n')
pprint.pprint(get_shop_list_by_dishes(dishes, person_count), sort_dicts=False)

##### Задание 3 ######
print()
print('Задание 3')


def new_text(file1, file2, file3, file4):
    dict_files = {'1': file1, '2': file2, '3': file3}

    # dict_files = {'1': '1.txt', '2': '2.txt', '3': '3.txt'}
    dict_files_length = {}

    for v in dict_files.values():
        file = open(v, encoding='utf8')
        length = len(file.readlines())
        dict_files_length[length] = v

        result_file = file4
        result_file = open(result_file, 'a', encoding='utf8')  # result_file = open('result.txt', 'a', encoding='utf8')

    for i in range(len(dict_files_length)):
        result_file.writelines(str(dict_files_length[sorted(dict_files_length)[i]]) + '\n')
        result_file.write(str(sorted(dict_files_length)[i]))
        result_file.write('\n' + open(dict_files_length[sorted(dict_files_length)[i]], encoding='utf8').read() + '\n')
    print()
    print(f'Текст из файлов записан в {file4}')


new_text('1.txt', '2.txt', '3.txt', 'result.txt')
