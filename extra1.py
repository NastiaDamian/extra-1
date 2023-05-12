
# Задача 1
countries = ["Ukrainian", "French", "Bulgarian", "Norwegian", "Latvian"]
# початковий список
print(countries)
# список в алфавітному порядку
print(sorted(countries))
# список в зворотньому порядку
print(sorted(countries, reverse=True))
# список відсортований на місці за спаданням
countries.sort(reverse=True)
print(countries)

# Задача 2

numbers = 2, -1, 9, 6
sum_num = sum(map(int, numbers))
print(sum_num)

# Задача 3

cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
cities_so = ', '.join(cities[:-1]) + ' and ' + cities[-1]
print(cities_so)

# Задача 4
numbers = 1, 2, 3, 4, 5
numbers_list = [int(num) for num in numbers]
reversed_list = numbers_list.copy()
reversed_list.reverse()
reversed_number = int(''.join(map(str, reversed_list)))
print(reversed_number)

# Задача 5
oceans = ['Atlantic', 'Pacific', 'Indian', 'Arctic']
oceans.remove('Arctic')
print(oceans)