import test_sender
import test_timer
from multiprocessing import Process
from datetime import datetime


if __name__ == '__main__':
    # а теперь запускаем проверку в отдельном потоке
    p1 = Process(target=test_sender.main)
    p1.start()
    tm = int(datetime.now().strftime(' %H'))
    if tm != 1 and tm != 2 and tm != 3 and tm != 4 and tm != 5 and tm != 6:
        p2 = Process(target=test_timer.main)
        p2.start()

