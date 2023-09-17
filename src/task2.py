sum_of_even = 0
product_of_odd = 1

for number in range(21):
    if number % 2 == 0:
        sum_of_even += number
    else:
        product_of_odd *= number

# Виводимо результати
print(f'Сума усіх парних чисел: {sum_of_even}')
print(f'Добуток усіх непарних чисел: {product_of_odd}')
