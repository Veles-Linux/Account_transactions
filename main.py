import utils

operations_list = utils.extend_operations()  # Получили все операции со статусом 'EXTEND'
sort_list_time = utils.sort_by_time()  # Получили отсортированные даты операций
sort_operations_list = utils.sort_by_operations()  # Получили список операция по датам
five_operations = utils.sort_five_operations()  # Получили 5 последних операций

for i in five_operations:
    print(utils.date_operations_format(i['date']), i['description'])
    if i['description'] == 'Открытие вклада':
        print(utils.name_card(i['to']), utils.chek_encryption(i['to']))
        print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
        print()
    else:
        print(utils.name_card(i['from']), utils.card_encryption(i['from']), '->', utils.name_card(i['to']),
              utils.chek_encryption(i['to']))
        print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
        print()
