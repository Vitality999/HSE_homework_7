# (2 балла) Загрузите датасет функцией pandas.read_excel(). Сколько всего площадок?
# (1 балл) Pandas сокращает количество выводимых столбцов, если их слишком много.
# Выполните pd.set_option('display.max_columns', None) , чтобы выводить всегда все колонки.
# (1 балл) Сколько площадок останется, если удалить строчки, у которых хотя бы 1 значение пропущено (функция pandas.dropna())?
# Почему столько?
# (2 балла) Выведите все бесплатные площадки, приспособленные для инвалидов
# (1 балл) Какие типы покрытия бывают на площадках (метод unique() у колонки)?
#  Какое покрытие самое популярное, самое непопулярное (метод value_counts())?
# (1 балл) Сколько всего районов, в которых расположены площадки (метод .nunique() у колонки).
# Какой район имеет наибольшее количество площадок?

sp_pl = pd.read_excel("data-25342-2018-08-17.xlsx" )
col = sp_pl.columns.values
print(col)
cnt = sp_pl['global_id'].count()
print(cnt)

pd.set_option('display.max_columns',None)
 print(sp_pl['Email'])

dr_sp_pl = sp_pl.dropna()
cnt_del = len(dr_sp_pl.index)
print('Count: ',cnt_del)

print(sp_pl[(sp_pl['DisabilityFriendly'] != 'не приспособлен') & (sp_pl['Paid'] =='бесплатно')])

print(sp_pl['SurfaceTypeSummer'].unique())
print(sp_pl['SurfaceTypeSummer'].value_counts().max())

print(sp_pl['District'].nunique())