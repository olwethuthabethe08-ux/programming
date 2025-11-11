import africastalking

username = "YOUR_USERNAME"
api_key = "YOUR_API_KEY"
africastalking.initialize(username, api_key)

sms = africastalking.SMS

def send_africastalking_sms(recipient_number, message):
    try:
        response = sms.send(message, [recipient_number])
        print(f" Message sent successfully: {response}")
    except Exception as e:
        print(f" Error sending message: {e}")

send_africastalking_sms("+27601234567", "Hi Student, your grade for Data Science 500 has been updated: 85%.")
send_africastalking_sms("+27601234567", "Reminder: Information Systems 511 Exam is tomorrow at 9 AM.")
send_africastalking_sms("+27601234567", "URGENT: Please contact the admin office regarding the Student immediately.")
