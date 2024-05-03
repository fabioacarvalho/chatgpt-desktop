from PySide6.QtCore import Qt
from inter.design import *
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QVBoxLayout
import sys
import markdown2

class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btnSave.clicked.connect(self.save_config)
        self.btnLoad.clicked.connect(self.load_config)
        self.btnSend.clicked.connect(self.send_message)

        try:
            self.load_file()
        except FileNotFoundError as e:
            pass
        
        self.set_block_messages()


    def convert_to_markdown(self, value):
        html = markdown2.markdown(value)
        return html
    

    def set_block_messages(self):
        # Criando o widget que conterá todas as mensagens
        self.widget_mensagens = QWidget()
        self.layout_mensagens = QVBoxLayout(self.widget_mensagens)
        self.scrollArea.setWidget(self.widget_mensagens)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)


    def send_message(self):
        content = self.message.toPlainText()
        if content:
            self.create_block_message(content)


    def create_message(self, value):
        # Criando uma label para representar a mensagem
        who = self.name.text() if self.name.text() else "You"
        message_converted = self.convert_to_markdown(value)
        message = QLabel(f"You: {message_converted}")
        message.setWordWrap(True)
        return message
    

    def create_block_message(self, msg):
        # Criando uma mensagem
        mensagem = self.create_message(msg)
        self.layout_mensagens.addWidget(mensagem)


    def show_message(self, msg):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText(msg)
        message_box.exec()
        return

    def save_config(self):
        with open('configs.txt', "w") as file:
            api_key = self.apiKey.text()
            url = self.url.text()
            name = self.name.text()

            if api_key or name:
                content = f"{api_key},{url},{name}\n"
                file.write(content)
                self.show_message("Settings save with success")
            else:
                self.show_message("Please set your 'Name' and 'API_Key'")

    def load_file(self):
        with open("configs.txt", "r") as file:
            if file:
                content = file.readline()
                if content:
                    self.apiKey.setText(str(content.split(',')[0]))
                    self.name.setText(str(content.split(',')[2]))

    def load_config(self):
        try:
            self.load_file()
        except FileNotFoundError as e:
            self.show_message("File not found. Put the file together this applicatrion or create a new.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()