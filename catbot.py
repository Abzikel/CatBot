# Created by Abzikel on 21/09/2024
import sys
import random
import time
import threading
import pyautogui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

class CatBot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Labels and text fields to insert the time intervals
        self.min_send_label = QLabel("Min Envio (ms)")
        layout.addWidget(self.min_send_label)
        self.min_send_entry = QLineEdit(self)
        self.min_send_entry.setText("200")
        layout.addWidget(self.min_send_entry)

        self.max_send_label = QLabel("Max Envio (ms)")
        layout.addWidget(self.max_send_label)
        self.max_send_entry = QLineEdit(self)
        self.max_send_entry.setText("300")
        layout.addWidget(self.max_send_entry)

        self.min_wait_label = QLabel("Min Espera (s)")
        layout.addWidget(self.min_wait_label)
        self.min_wait_entry = QLineEdit(self)
        self.min_wait_entry.setText("12.5")
        layout.addWidget(self.min_wait_entry)

        self.max_wait_label = QLabel("Max Espera (s)")
        layout.addWidget(self.max_wait_label)
        self.max_wait_entry = QLineEdit(self)
        self.max_wait_entry.setText("25")
        layout.addWidget(self.max_wait_entry)

        # Button Start/Stop
        self.button = QPushButton("Iniciar", self)
        self.button.clicked.connect(self.toggle_sending)
        layout.addWidget(self.button)

        # Status label
        self.status_label = QLabel("Detenido", self)
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.setWindowTitle('Cat Bot')
        self.is_running = False
        self.stop_thread = False
        self.thread = None

        self.show()

    def closeEvent(self, event):
        # Stop program and kill thread on window close
        self.is_running = False
        self.stop_thread = True
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1)
        event.accept()

    def validate_input(self):
        try:
            min_send = float(self.min_send_entry.text())
            max_send = float(self.max_send_entry.text())
            min_wait = float(self.min_wait_entry.text())
            max_wait = float(self.max_wait_entry.text())

            if min_send > max_send:
                raise ValueError("El mínimo de envío debe ser menor o igual al máximo.")
            if min_wait > max_wait:
                raise ValueError("El mínimo de espera debe ser menor o igual al máximo.")
            return min_send, max_send, min_wait, max_wait
        except ValueError as e:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error en la validación")
            error_dialog.setText("Ingresar solamente números decimales")
            error_dialog.exec_()
            return None

    def send_message(self, min_send, max_send, min_wait, max_wait):
        while self.is_running:
            if self.stop_thread:
                break

            # Wait 5 seconds
            for _ in range(50):  
                if self.stop_thread:
                    break
                time.sleep(0.1) 

            if self.stop_thread:
                break

            # Write the word "cat" using pyautogui
            pyautogui.write("cat")

            # Wait a random time before sending the message
            send_delay = random.uniform(min_send, max_send) / 1000
            for _ in range(int(send_delay * 10)):
                if self.stop_thread:
                    break
                time.sleep(0.1)

            pyautogui.press("enter")

            # Wait for a random time before sending the next message
            wait_delay = random.uniform(min_wait, max_wait)
            for _ in range(int(wait_delay * 10)):
                if self.stop_thread:
                    break
                time.sleep(0.1)

        self.toggle_fields(True)

    def toggle_sending(self):
        if not self.is_running:
            # Validar entrada
            validation = self.validate_input()
            if not validation:
                return
            min_send, max_send, min_wait, max_wait = validation

            # Run the thread to send the messages
            self.is_running = True
            self.stop_thread = False
            self.status_label.setText("Corriendo...")
            self.button.setText("Detener")

            # Hide text fields
            self.toggle_fields(False)

            self.thread = threading.Thread(target=self.send_message, args=(min_send, max_send, min_wait, max_wait))
            self.thread.start()
        else:
            # Stop sending messages
            self.is_running = False
            self.stop_thread = True
            if self.thread and self.thread.is_alive():
                self.thread.join(timeout=1) 
            self.status_label.setText("Detenido")
            self.button.setText("Iniciar")
            self.toggle_fields(True)

    def toggle_fields(self, visible):
        # Show and hide the text fields depending if the program is running or not
        self.min_send_label.setVisible(visible)
        self.min_send_entry.setVisible(visible)
        self.max_send_label.setVisible(visible)
        self.max_send_entry.setVisible(visible)
        self.min_wait_label.setVisible(visible)
        self.min_wait_entry.setVisible(visible)
        self.max_wait_label.setVisible(visible)
        self.max_wait_entry.setVisible(visible)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CatBot()
    sys.exit(app.exec_())
