import json
from datetime import date

with open('operations.json') as f:
    templates = json.load(f)


def operations(templates):
    count = 0
    operations_list = []  # Список с подходящими под условия операциями
    time_operations = []  # Список с временем операций. В дальнейшем будет сортироваться
    for i in templates:
        if templates[count] == {}:  # Если нет данных, то пропускаем итерацию
            continue
        if templates[count]['state'] == 'EXECUTED':
            time_operations.append(templates[count]['date'])
            operations_list.append(templates[count])
            count += 1
    time_operations = sorted(time_operations, reverse=True)  # Отсортированный список по времени
    time_operations = time_operations[0:5]  # Первые 5 успешных операций

    operations_list_sorted = []
    for i in time_operations:
        for k in operations_list:
            if i == k['date']:
                operations_list_sorted.append(k)

    return operations_list_sorted

def output_operations(operations_list_sorted):
    for i in range(5):  # Рабочая версия
        thedate = date.fromisoformat(operations_list_sorted[i]['date'][0:10])  # Показывает время транзакции
        time = f'{thedate.day}.{thedate.month}.{thedate.year}'

        descript = operations_list_sorted[i].get('description')
        card_from = operations_list_sorted[i].get('from')
        chek_to = operations_list_sorted[i].get('to')
        amount_sum = operations_list_sorted[i].get('operationAmount', ['amount'])

        print(time, descript)
        card_from_number = card_from_name = card_from
        chek_to_number = chek_to_name = chek_to

        if card_from == None:
            card_from = ''

        else:
            line = card_from
            numbers = ''.join(c if c.isdigit() else ' ' for c in line).split()
            numbers = ''.join(numbers)

            card_number = numbers
            private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
            chunks, chunk_size = len(private_number), len(private_number) // 4
            card_from_number = ((" ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])))

            chek_to_number = '**' + chek_to_number[-4:]

            line = card_from_name
            card_from_name = ''.join(c if c.isalpha() else ' ' for c in line).split()
            card_from_name = ''.join(card_from_name)

            line = chek_to_name
            chek_to_name = ''.join(c if c.isalpha() else ' ' for c in line).split()
            chek_to_name = ''.join(chek_to_name)
        if card_from == '':
            chek_to_name = '**' + chek_to_name[-4:]
            print(f'-> {chek_to_name}')  # Откуда и куда перевод
            print(amount_sum['amount'], amount_sum['currency']['name'])  # Сумма и валюта
            print()
        else:
            print(f'{card_from_name} {card_from_number} -> {chek_to_name} {chek_to_number}')
            print(amount_sum['amount'], amount_sum['currency']['name'])  # Сумма и валюта
            print()


# print(output_operations(operations(templates)))
