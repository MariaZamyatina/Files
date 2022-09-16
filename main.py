cook_book = {}
dish_ingredients = {}

with open('recipes.txt') as file:
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

# Нужно написать функцию,
# которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда.
dishes = input('Введите блюда через запятую: ').split(', ')
person_count = int(input('Введите количество персон: '))


def get_shop_list_by_dishes(dishes, person_count):
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


pprint.pprint(get_shop_list_by_dishes(dishes, person_count), sort_dicts=False)


