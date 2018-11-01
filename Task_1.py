# Задача 1. (макс. 8 баллов)
# Скачайте датасет в .xlsx (Excel) "Археологические находки на реконструируемых улицах" с московского портала открытых данных :
# https://data.mos.ru/opendata/7702155262-arheologicheskie-nahodki-na-rekonstruiruemyh-ulitsah?pageNumber=2&versionNumber=2&releaseNumber=8
#
#     (2 балла) Загрузите датасет функцией pandas.read_excel(). Сколько было находок?
#     (1 балла) Добавьте в датафрейм колонки с годом и месяцем обнаружения (метод apply)
#     (1 балл) Выведете распределение количества находок по годам и отдельно по месяцам (метод value_counts())
#     (2 балла) Найдите находку с самым длинным описанием
#     (1 балл) Бонусный балл за интересные факты, которые можно почерпнуть из датасета с использованием pandas.

import pandas as pd
from datetime import datetime


pd.set_option('display.max_columns', None)
file = pd.read_excel('data-54581-2018-08-28.xlsx')
allFind = file['ID']
allFind = max(allFind.values)
print('Всего {} находок.'.format(allFind))
sp = file['DateOfDiscovery']
file['Year'] = sp.apply(lambda sp: datetime.strptime(sp, '%d.%m.%Y').year)
file['Month'] = sp.apply(lambda sp: datetime.strptime(sp, '%d.%m.%Y').month)
y = file['Year'].value_counts(sort=True)
m = file['Month'].value_counts(sort=True)
print('Уникальных значений в поле Year:\n', y)
print('Уникальных значений в поле Month:\n', m)
description = file['DescriptionOfFinding'].values
lenStr = []

for item in description:
    lenStr.append(len(item))

file['Len'] = lenStr
print(file['Len'].values.max(axis=0))

#print('index:', max(map(len, description['DescriptionOfFinding'])))


