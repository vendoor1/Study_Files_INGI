#ДЗ 1
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145934462, 331002651, 80345321, 67886011, 65273511, 1380004385]
for country, capital, population in zip(countries, capitals, population):
    print(f'{capital} is the capital of {country}, population equal {population} people.')
#ДЗ 2
def ignore_command(command):
    return any([i for i in command if i in ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']])


