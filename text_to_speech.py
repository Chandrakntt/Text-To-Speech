#!/usr/bin/env python3
"""
Text-to-Speech Generator
A Python program that converts text to speech using pyttsx3 library.
"""

import pyttsx3
import sys
from pathlib import Path


class TextToSpeech:
    """A class to handle text-to-speech conversion."""
    
    def __init__(self, rate=150, volume=0.9):
        """
        Initialize the TextToSpeech engine.
        
        Args:
            rate (int): Speech rate (words per minute). Default is 150.
            volume (float): Volume level (0.0 to 1.0). Default is 0.9.
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # Get available voices
        self.voices = self.engine.getProperty('voices')
    
    def set_voice(self, voice_id=0):
        """
        Set the voice for speech synthesis.
        
        Args:
            voice_id (int): Index of the voice. Default is 0 (usually male voice).
        """
        if voice_id < len(self.voices):
            self.engine.setProperty('voice', self.voices[voice_id].id)
        else:
            print(f"Voice ID {voice_id} not available. Using default voice.")
    
    def set_rate(self, rate):
        """Set the speech rate (words per minute)."""
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume):
        """Set the volume level (0.0 to 1.0)."""
        if 0.0 <= volume <= 1.0:
            self.engine.setProperty('volume', volume)
        else:
            print("Volume must be between 0.0 and 1.0")
    
    def list_voices(self):
        """Display available voices."""
        print("\nAvailable Voices:")
        for idx, voice in enumerate(self.voices):
            print(f"{idx}. {voice.name} (ID: {voice.id})")
        print()
    
    def speak(self, text):
        """
        Convert text to speech and play it.
        
        Args:
            text (str): The text to convert to speech.
        """
        if not text.strip():
            print("Error: No text provided.")
            return
        
        print(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def save_to_file(self, text, filename):
        """
        Convert text to speech and save it to a file.
        
        Args:
            text (str): The text to convert to speech.
            filename (str): The output file path (should end with .mp3 or .wav).
        """
        if not text.strip():
            print("Error: No text provided.")
            return
        
        try:
            self.engine.save_to_file(text, filename)
            self.engine.runAndWait()
            print(f"Audio saved to: {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")


def main():
    """Main function to demonstrate the TextToSpeech class."""
    
    # Create TextToSpeech object with custom rate and volume
    tts = TextToSpeech(rate=150, volume=0.9)
    
    print("=" * 60)
    print("Python Text-to-Speech Generator")
    print("=" * 60)
    
    # List available voices
    tts.list_voices()
    
    # Example 1: Speak simple text
    print("Example 1: Speaking simple text...")
    tts.speak("Hello! This is a text to speech example.")
    print()
    
    # Example 2: Change voice and speak
    print("Example 2: Changing voice...")
    if len(tts.voices) > 1:
        tts.set_voice(1)
        tts.speak("This is a different voice speaking the same text.")
        tts.set_voice(0)  # Reset to default
    print()
    
    # Example 3: Change speech rate
    print("Example 3: Adjusting speech rate...")
    tts.set_rate(100)  # Slower
    tts.speak("This is slower speech.")
    tts.set_rate(200)  # Faster
    tts.speak("This is faster speech.")
    tts.set_rate(150)  # Reset to default
    print()
    
    # Example 4: Save to file
    print("Example 4: Saving speech to file...")
    tts.save_to_file("Welcome to the text to speech generator!", "output.mp3")
    print()
    
    print("=" * 60)
    print("Demo completed!")
    print("=" * 60)


def interactive_mode():
    """Interactive mode for custom text input."""
    tts = TextToSpeech(rate=150, volume=0.9)
    
    print("\n" + "=" * 60)
    print("Interactive Text-to-Speech Mode")
    print("=" * 60)
    
    tts.list_voices()
    
    while True:
        print("\nOptions:")
        print("1. Speak text")
        print("2. Save to file")
        print("3. Change voice")
        print("4. Change rate")
        print("5. Change volume")
        print("6. List voices")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            text = input("Enter text to speak: ").strip()
            if text:
                tts.speak(text)
        
        elif choice == '2':
            text = input("Enter text to save: ").strip()
            filename = input("Enter filename (e.g., output.mp3): ").strip()
            if text and filename:
                tts.save_to_file(text, filename)
        
        elif choice == '3':
            tts.list_voices()
            try:
                voice_id = int(input("Enter voice ID: ").strip())
                tts.set_voice(voice_id)
                print("Voice changed successfully!")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == '4':
            try:
                rate = int(input("Enter speech rate (50-300 WPM): ").strip())
                tts.set_rate(rate)
                print("Rate changed successfully!")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == '5':
            try:
                volume = float(input("Enter volume (0.0-1.0): ").strip())
                tts.set_volume(volume)
                print("Volume changed successfully!")
            except ValueError:
                print("Invalid input. Please enter a number between 0.0 and 1.0.")
        
        elif choice == '6':
            tts.list_voices()
        
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Uncomment the line below to run in interactive mode
    interactive_mode()
    
    # Run demo mode
    main()