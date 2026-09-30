"""
    Author: Ahmad Taka
    Date: Ahmad Taka
    Description: CAN bus debugger
"""
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.config import Config

import serial
import threading
from datetime import datetime

SCANNER = serial.Serial('COM11', baudrate=115200,timeout=0.032)
# # Setting size to resizable
Config.set('graphics', 'resizable', 1)
class KhanLogger(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.event = None

    def my_callback(self, dt):
        raw_line = SCANNER.readline()
        line = raw_line.decode('utf-8').replace('\n', '')
        now = datetime.now().strftime("%H:%M:%S")
        if line == "":
            return
        final_line = now + " --> " + line
        print(final_line)
        self.ids.can_list.add_widget(Label(text=final_line, size=(100, 30), ))
    
    def start_serial(self):
        print("Starting... ")
        self.event = Clock.schedule_interval(self.my_callback, 1 / 60.)
    def stop_serial(self):
        print("Stopping... ")
        if self.event is not None:
            self.event.cancel()
       
    def clear_log(self):
        print("Clearing... ")
        self.ids.can_list.clear_widgets()

class KhanApp(App):

    def build(self):
        return KhanLogger()

def handle_app():
    KhanApp().run()
   
def handle_serial():
    scanner = serial.Serial('COM11', 115200)
    print("Starting Serial ...")
    while SERIAL_OPEN:
        raw_line = scanner.readline()
        line = raw_line.decode('utf-8').replace('\n', '')
        now = datetime.now().strftime("%H:%M:%S")
        final_line = now + " --> " + line
        print(final_line)
    
        
        
def main():
    print("STARTING APP.....")
    
    app = threading.Thread(target=handle_app)
    serial = threading.Thread(target=handle_serial)

    app.start()
    serial.start()

    app.join()
    serial.join()

if __name__ == '__main__':
   handle_app()