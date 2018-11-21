def count():
    """Функция для расчета рейтинга"""
    r, experts, k = float(input('Оценка покупателей = ')), float(input('Оценка экспертов = ')), float(input('Количество покупателей = '))
    m = 0.02*k//r+0.01
    if 1 <= r <= 10 and 1 <= experts <= 10:
        rating = r-(r-experts//(k+1)**m)
        print(rating)
    else:
        while r > 10 or experts > 10:
         print('Введены некорректные данные.Попробуйте еще раз.')
         r , experts, k = float(input('Оценка покупателей = ')), float(input('Оценка экспертов = ')), float(input('Количество покупателей= '))
        while r < 1 or experts < 1:
         print('Введены некорректные данные.Попробуйте еще раз.')
         r , experts, k = float(input('Оценка покупателей = ')), float(input('Оценка экспертов = ')), float(input('Количество покупателей= '))
        while 1 <= r <= 10 and 1 <= experts <= 10:
         rating = r-(r-experts//(k+1)**m)
         print(rating)
         break


def main():
 """Функция для вызова функции count"""
print('Введите значения:')
count()

