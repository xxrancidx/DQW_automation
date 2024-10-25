import PySimpleGUI as sg
import pyautogui
import threading
import time

class AutoClicker:
    def __init__(self):
        self.running = False
        self.setup_gui()
    
    def setup_gui(self):
        layout = [
            [sg.Button('開始', key='-START-'), sg.Button('停止', key='-STOP-', disabled=True)]
        ]
        self.window = sg.Window('Auto Clicker', layout)
    
    def start_clicking(self):
        self.running = True
        while self.running:
            pyautogui.click()
            time.sleep(1)  # 1秒間隔
    
    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == '-START-':
                self.window['-START-'].update(disabled=True)
                self.window['-STOP-'].update(disabled=False)
                threading.Thread(target=self.start_clicking, daemon=True).start()
            elif event == '-STOP-':
                self.running = False
                self.window['-START-'].update(disabled=False)
                self.window['-STOP-'].update(disabled=True)

if __name__ == '__main__':
    auto_clicker = AutoClicker()
    auto_clicker.run()
