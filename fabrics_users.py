import pandas as pd

#Загрузка исходной таблицы
data= pd.read_excel('C:\\Users\\admin\\Downloads\\real_xsml.xlsx')
data.head(10)

#Cохранение индексов компаний в отдельную таблицу

data['company_id'].to_csv('company_id.csv', index=False)



# Исключение столбцов с числовыми данными
columns_to_exclude = ['tz_count', 'tz_price_one', 'tz_price_part','tz_count_pers', 'tz_min_part', 'tz_obraz_zak','company_id']
raw_data = data.drop(columns=columns_to_exclude)

# Вычисление суммы по строкам в новом DataFrame, сщхранение в таблицу
row_sums = raw_data.sum(axis=1)

row_sums.to_csv('row_sums.csv', index=False)

merged_table = pd.concat([companies, row_sums])
merged_table.head()


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize = (5,3))
sns.displot(merged_table['options'], bins = 30)
plt.xlabel('Количество опций')
plt.ylabel('Количество фабрик')
plt.show()



#Список пользователей

users = pd.read_excel('/content/drive/MyDrive/Стажировки_ИИ/Сажировка_производители/Реестр закупок с описанием.xlsx')
users.head()


import re

email_pattern = r'Email:\s*(.*)'

# Применяем регулярное выражение к колонке 'text' и записываем результат в новую колонку 'email'
users['email'] = users['Описание'].str.extract(email_pattern)

# Выводим первые несколько строк DataFrame users для проверки результата
print(users.head())

# Замена пустых ячеек на адрес админа
users['email'].fillna('admin@tpktrade.ru', inplace = True)

# Сохранение DataFrame в Excel файл
users.to_excel('users_email.xlsx', index=False)  # Если не нужно сохранять индексы

# Подсчет количества уникальных адресов электронной почты
unique_emails_count = users['email'].nunique()

print("Количество уникальных адресов электронной почты:", unique_emails_count)

