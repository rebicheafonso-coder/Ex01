# ex04.py
algo = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('Está em maiúsculas? ', algo.isupper())