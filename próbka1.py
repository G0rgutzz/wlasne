import calendar
import time

kalendarz = calendar.month(2025, 11)
localtime = time.asctime(time.localtime(time.time()))
print("Twoja strefa czasowa: UTC%s" % (round(time.altzone/3600)))
print(localtime)
print(kalendarz)
