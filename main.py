# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import pywhatkit

def send_message(month_date, phone_number):
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=4)
    current_time = now.strftime("%H:%M:%S")

    after_hours_start = '13:01:00'
    after_hours_end = '23:59:00'

    whats_app_msg = f"Files for {month_date} have been sent to dropbox"
    if current_time > after_hours_start and current_time < after_hours_end:
        print('Sending WhatsApp message after hours of job completion')
        pywhatkit.sendwhatmsg_instantly(phone_number, whats_app_msg)
        # pywhatkit.sendwhatmsg_to_group(group_id: str, message: str, time_hour: int, time_min: int, wait_time: int = 20,
        #                  print_wait_time: bool = True, tab_close: bool = False)
        print(current_time)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hey')
    phone_number = "+16142707567"
    month_date = "06-10-2021"
    send_message(month_date, phone_number)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
