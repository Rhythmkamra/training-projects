import pywhatkit

def send_message(phone_number, message, time_hour, time_minute):
  """

  Args:
    phone_number: The phone number of the recipient.
    message: The message to send.
    time_hour: The hour of the scheduled time.
    time_minute: The minute of the scheduled time.
  """

  pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute)

if __name__ == "__main__":
  
  send_message("+91**********", "This is an automatic message.", 7, 30)
