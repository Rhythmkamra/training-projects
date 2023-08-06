import pywhatkit

def send_whatsapp_message(phone_number, message, time_hour, time_minute):
  """Sends an automatic WhatsApp message to the specified phone number at the specified time.

  Args:
    phone_number: The phone number of the recipient.
    message: The message to send.
    time_hour: The hour of the scheduled time.
    time_minute: The minute of the scheduled time.
  """

  pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute)

if __name__ == "__main__":
  
  send_whatsapp_message("+91**********", "This is an automatic message.", 7, 30)
