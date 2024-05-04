from PySide6.QtCore import Qt
from inter.design import *
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QVBoxLayout
import sys
import markdown2
from config import request_chat
import asyncio

class Main(QMainWindow, Ui_MainWindow):
    _clear_history = False

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btnSave.clicked.connect(self.save_config)
        self.btnLoad.clicked.connect(self.load_config)
        self.btnSend.clicked.connect(self.send_message)
        self.btnNewChat.clicked.connect(self.new_chat)

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


    def send_message(self, who=True):
        content = self.message.toPlainText()
        if content:
            self.create_block_message(content, True)
        
        # restaurando estado original
        if self._clear_history:
            self._clear_history = False

    def create_message(self, msg, who):
        # Criando uma label para representar a mensagem
        message_converted = self.convert_to_markdown(msg)
        text_message = f"You: {message_converted}" if who else f"ChatGPT: {message_converted}"
        message = QLabel(text_message)
        message.setStyleSheet("padding: 10px;")
        if not who:
            message.setStyleSheet("background-color: #424769; padding: 10px;")
        message.setWordWrap(True)
        return message

    def create_block_message(self, msg, who):
        # Criando uma mensagem
        mensagem = self.create_message(msg, who)
        self.layout_mensagens.addWidget(mensagem)
        self.message.setText("")

        if who:
            self.process_user_request(str(msg))
            

    def process_user_request(self, msg):
        response = request_chat(msg, self._clear_history)
        if response:
            self.create_block_message(str(response), False)


    def show_message(self, msg):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText(msg)
        message_box.exec()
        return


    def new_chat(self):
        # Limpa o layout removendo todos os widgets filhos
        for i in reversed(range(self.layout_mensagens.count())):
            widget = self.layout_mensagens.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        self._clear_history = True

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
