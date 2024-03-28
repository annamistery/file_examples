try:
    f = open('example_text.txt')
except:
    print('Ошибка открытия файла')
else:
    f.close()
    print('(Очистка: Закрытие файла)')        