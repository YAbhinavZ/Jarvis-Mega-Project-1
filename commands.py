import webbrowser
from speech import speak

def process_command(command):

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "stop jarvis" in command or "exit" in command:
        speak("Goodbye!")
        return False

    else:
        speak("Sorry, I don't know that command yet.")

    return True