import datetime
from tasks import cpu_bound


def main():

    a = cpu_bound.delay(1) # Я хочу выполнять его не здесь, а в приложении celery
    b = cpu_bound.delay(2) # Мне нужно запустить это приложение
    c = cpu_bound.delay(3) # Пишу delay чтобы исполнялось в селери
    d = cpu_bound.delay(4) # Теперь это - асинхронный результат async result

    return [a.get(), b.get(), c.get(), d.get()]


start = datetime.datetime.now()
print(main())
print(datetime.datetime.now() - start)