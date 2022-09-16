cook_book = {}
dish_ingredients = {}

with open('recipes.txt',encoding = 'utf8') as file:
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


dishlist = {'1':'Омлет','2':'Утка по-пекински','3':'Запеченный картофель','4':'Фахитос'}
dishesinput = input(f'\n 1: Омлет\n 2: Утка по-пекински\n 3: Запеченный картофель\n 4: Фахитос\n '
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

print()
pprint.pprint(get_shop_list_by_dishes(dishes, person_count), sort_dicts=False)

count_list = []
file1 = open('1.txt',encoding='utf8')
#count_file1 =
count_list.append(len(file1.readlines()))


file2 = open('2.txt',encoding='utf8')
#count_file2 = len(file2.readlines())
count_list.append(len(file2.readlines()))

file3 = open('3.txt',encoding='utf8')
#count_file3 = len(file3.readlines())
count_list.append(len(file3.readlines()))

file_result = open('result.txt',encoding='utf8')

print(sorted(count_list))





