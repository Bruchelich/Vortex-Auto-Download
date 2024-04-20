import tkinter as tk
import pyautogui
import os
import time
import threading
import keyboard
import sys

# Get the directory of the current script
script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
client_download_button = os.path.join(script_dir, "client_download.png")
website_download_button = os.path.join(script_dir, "website_download.png")

class AutoDownloaderApp:
    def __init__(self, master):
        self.master = master
        master.title("AutoDownloader - Discord: Bruchelich")
        master.geometry("612x412")
        master.configure(bg="#333333")  # Set background color to darker gray

        button_font = ("Helvetica", 16, "bold")  # Font properties for button
        label_font = ("Helvetica", 12, "bold")   # Font properties for label

        self.click_button = tk.Button(master, text="Start", command=self.toggle_clicker, width=20, height=8, bg="red", fg="white", font=button_font)
        self.click_button.pack(pady=20)

        self.info_label = tk.Label(master, text='Pressing "Escape" pauses and continues the downloader', bg='#333333', fg='white', font=label_font)
        self.info_label.pack(pady=20, padx=20, side=tk.TOP, anchor="center")  # Centered information label

        self.running = False

        keyboard.on_press_key('esc', lambda event: self.toggle_clicker())

    def toggle_clicker(self):
        if self.running:
            self.pause_clicker()
        else:
            self.start_clicker()

    def start_clicker(self):
        self.click_button.config(text="Pause", bg="green")
        self.running = True
        self.auto_click_thread = threading.Thread(target=self.auto_click)
        self.auto_click_thread.start()

    def pause_clicker(self):
        self.click_button.config(text="Start", bg="red")
        self.running = False

    def auto_click(self):
        while self.running:
            if self.click_button.cget("text") == "Pause":
                if self.click_image(client_download_button):
                    continue

                if self.click_image(website_download_button):
                    continue

            # If no buttons were clicked, wait before checking again.
            time.sleep(1)

        print("\nPaused") # Only prints if used in terminal

    def click_image(self, image_path):
        try:
            button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.95)
            if button_location is not None:
                pyautogui.click(button_location)
                print(f"Clicked on {image_path}")
                return True
        
        except pyautogui.ImageNotFoundException:
            pass
        return False

def main():
    root = tk.Tk()
    app = AutoDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
