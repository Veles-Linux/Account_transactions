import json
from datetime import date

with open('operations.json') as f:
    templates = json.load(f)


def extend_operations():
    """Фунция вытаскиет все операции в статусе 'EXTEND'"""
    count = 0
    operations_list = []  # Список с подходящими под условия операциями
    for i in templates:
        if templates[count] == {}:  # Если нет данных, то пропускаем итерацию
            continue
        if templates[count]['state'] == 'EXECUTED':
            operations_list.append(templates[count])
            count += 1
    return operations_list


def sort_by_time():  # Остановился тут!
    """Функция сортирует даты операций, начиная с последней"""
    operations_list = extend_operations()
    sort_list = []  # Список с датами операций
    count = 0
    for i in operations_list:
        sort_list.append(operations_list[count]['date'])
        count += 1
    sort_list = (sorted(sort_list, reverse=True))
    return sort_list


def sort_by_operations():
    """Функция сортирует операции по датам"""
    work_list = []
    for i in sort_by_time():
        for k in extend_operations():
            if k['date'] == i:
                work_list.append(k)
    return work_list


def sort_five_operations():
    """Функция вытаскивает первые 5 операция"""
    return sort_by_operations()[0:5]


def card_encryption(card):
    """Функция скрывает номер карты"""
    card_number = card.split()[-1]
    private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    resault = (" ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)]))
    return resault


def chek_encryption(chek):
    """Функция скрывает номер счёта"""
    chek_number = chek.split()[-1]
    resault = '**' + chek_number[-4:]
    return resault


def date_operations_format(date_operations):
    """Функция показывает время в определённом формате"""
    date_operations = date_operations[0:10]
    thedate = date(year=int(date_operations[0:4]), month=int(date_operations[5:7]), day=int(date_operations[-2:]))
    date_formatted = thedate.strftime("%d.%m.%Y")  # День Месяц Год
    return date_formatted


def name_card(name):
    """Функция показывает имя счета/карты откуда/куда был совершен перевод"""
    name = ''.join(c if c.isalpha() else ' ' for c in name).split()
    return ' '.join(name)
