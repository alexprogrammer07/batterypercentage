# Importing modules
from plyer import notification
import psutil
import time


def notify(text, icon):
    """
    Function that sends a desktop notification to the user
    :param text: A message that is to be displayed to the user
    :param icon: Image to show to the user in notification
    :return: None
    """
    notification.notify(
        app_name="Notify",
        app_icon=fr"IconPacks\{icon}",
        title="Battery",
        message=text,
        timeout=15)


if (__name__ == '__main__'):
    # Runs if the program is run and not imported as module

    battery = psutil.sensors_battery()  # Determining battery state
    percent = battery.percent  # getting battery percent

    charging = battery.power_plugged  # Getting charging status

    seconds = battery.secsleft  # Estimated total seconds remaining

    hour_left = time.strftime("%H", time.gmtime(seconds))  # Estimated hours remaining
    minute_left = time.strftime("%M", time.gmtime(seconds))  # Estimated minutes remaining

    if percent <= 40 and not charging:  # If else block begins
        notify(f"{str(percent)}% Remaining. Please feed me as soon as possible! \nI will die in {hour_left} hours "
               f"and {minute_left} minutes", "low.ico")

    elif charging and percent > 80:notify(f"{str(percent)}% Remaining. I have finished eating! \nI will not be hungry for {hour_left} hours " f"and {minute_left} minutes!", "80.ico")

    elif charging and percent < 50:notify(f"{str(percent)}% Remaining. I am feeling happy! \nYou are feeding me!", "charge.ico")  # Send notification if triggers

    elif charging and percent > 95:notify(f"{str(percent)}% Remaining. I am not hungry! \nI can last {hour_left} hours and {minute_left}"f" minutes!", "full.ico")

    elif percent < 25 and not charging: notify(f"{str(percent)}% Remaining. I am very Hungry \nI will die in {hour_left} hours and {minute_left}"f" minutes!", "0.ico")
