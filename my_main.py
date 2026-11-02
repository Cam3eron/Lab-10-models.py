# my_main.py
# Author: Cameron McGraw

from my_assistant import AppointmentHelper
from my_tool import AppointmentBook

OPEN_TIMES = {
    "monday": "9:00 am and 2:30 pm",
    "wednesday": "11:00 am",
    "friday": "none",
}

appointment_book = AppointmentBook(OPEN_TIMES)
helper = AppointmentHelper(
    "Robin",
    "You help clients of Bayside Tax Help find an open appointment time.",
    appointment_book,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")