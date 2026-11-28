from speech import speak, listen
from commands import process_command

print("Jarvis is in standby...")

running = True

while running:
    command = listen()

    if command and "hey jarvis" in command:
        print("Wake word detected!")
        speak("Yes, how can I help you?")

        user_command = listen()

        if user_command:
            print("Command received:", user_command)
            running = process_command(user_command)

    if not running:
        break

