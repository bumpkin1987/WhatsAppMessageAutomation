# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import pywhatkit


def send_message(date, group_identity):
    # added a few minutes to allow processing the request
    nowish = datetime.datetime.utcnow() - datetime.timedelta(hours=4) + datetime.timedelta(minutes=5)
    current_time = nowish.strftime("%H:%M:%S")

    after_hours_start = '13:01:00'
    after_hours_end = '23:59:00'

    whats_app_msg = f"Files for {date} have been sent to dropbox"
    if after_hours_start < current_time < after_hours_end:
        print('Sending WhatsApp message after hours of job completion')
        pywhatkit.sendwhatmsg_to_group(group_identity,
                                       whats_app_msg, 
                                       int(current_time[0:2]),
                                       int(current_time[3:5]),
                                       wait_time=20)
        print(current_time)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hey')
    group_id = 'DMezCEJbXxL8OGg8q4OljH'
    phone_number = "+16142707567"
    month_date = "06-10-2021"

    send_message(month_date, group_id)

