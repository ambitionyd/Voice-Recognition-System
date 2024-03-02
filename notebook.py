import speech_recognition as sr
from gtts import gTTS
import pygame
import pyautogui
import webbrowser
import os

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None

def respond(response_text):
    print("Response:", response_text)
    tts = gTTS(text=response_text, lang='en')
    current_directory = os.getcwd()
    output_file = os.path.join(current_directory, "response.mp3")
    print("Output file:", output_file)
    tts.save(output_file)
    print("Response audio saved successfully.")
    pygame.mixer.init()
    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()
    print("Response audio playback started.")
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    print("Response audio playback finished.")


def main():
    print("Main function started.")
    while True:
        command = listen_for_command()

        triggerKeyword = "bologna"

        if command:
             # Insert code to list tasks here
            if "Hi" in command:
                respond("Namaste, How may i help you today")
            elif "add a task" in command:
                respond("Sure, what is the task")
            elif "list tasks" in command:
                respond("Sure. Your tasks are:")   

            elif "take a screenshot" in command:
                pyautogui.screenshot("screenshot.png")
                respond("I took a screenshot for you.")
            elif "open chrome" in command:
                respond("Opening Chrome.")
                webbrowser.open("http://www.chrome.com")
            elif "open youtube" in command:
                respond("okay, let's go to youtube")
                webbrowser.open("http://www.youtube.com")    
            elif "exit" in command:
                respond("Goodbye!, have a nice day")
                break
            else:
                respond("Sorry, I'm not sure how to handle that command.")

if __name__ == "__main__":
    main()
