import pynotifier
import psutil
import time
from plyer import notification

battery=psutil.sensors_battery()
percent=battery.percent
print(percent)


battery=psutil.sensors_battery()
percent=battery.percent
print(percent)
notification.notify(title = "Battery Percentage",message=str(percent) + "% percent remaining" ,timeout=2)

# pynotifier.Notification(title = "Battery Percentage",message=str(percent) + "% percent remaining" ,timeout=2)
time.sleep(5)
