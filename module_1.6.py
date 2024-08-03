my_dict = {'Lada': 1999,
           'Natasha': 1979,
           'Nikolay': 1974,
           'Varvara': 2023}
print("Dict:",  my_dict)
print("Existing value:", my_dict.get('Lada'))
print("Not existing value:", my_dict.get('Valeriay',
                  "Такого имени ещё не добавлено"))
my_dict.update({'Valeriay': 2028,
                'Vladislav': 2032})
print("Modified dictionary: ", my_dict)
a = my_dict.pop('Nikolay')
print("Deleted value:", a)
print(my_dict)
my_set = {1988, 1999, 2023, 1988,
          'apple', 'apple', 99.99, 99.99}
print("Set: ", my_set)
my_set.add(88.88)
my_set.add(11)
print("Modified set: ", my_set)
my_set.discard('apple')
print("Modified set:", my_set)
