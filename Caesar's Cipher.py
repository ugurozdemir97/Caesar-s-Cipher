from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from caesar import Screen
import sys
import source


# ------------------------------------- ALPHABET AND NUMBERS TO USE ------------------------------------------ #

alphabet_lower = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı",
                          "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r",
                          "s", "ş", "t", "u", "ü", "v", "w", "x", "y", "z"]
alphabet_upper = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I",
                  "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "Q", "R",
                  "S", "Ş", "T", "U", "Ü", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# ------------------------------------- MAIN APP ------------------------------------------ #

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        # ---------- SETUP ----------- #

        self.shift = None
        self.text = None
        self.saved = ""
        self.shift = 10
        self.direction = "Encode"
        self.ui = Screen()
        self.setWindowIcon(QtGui.QIcon('cipher.png'))
        self.ui.setupUi(self)

        # ---------- Add functionality to all the widgets ----------- #

        self.ui.horizontalSlider.valueChanged.connect(self.ui.label_2.setNum)
        self.ui.horizontalSlider.valueChanged.connect(self.key)
        self.ui.textEdit.setPlaceholderText("Type Here...")
        self.ui.pushButton.clicked.connect(self.translate)
        self.ui.radioButton.toggled.connect(self.encrypt)
        self.ui.radioButton_2.toggled.connect(self.encrypt)
        self.ui.actionNew.triggered.connect(self.clear)
        self.ui.actionSave_2.triggered.connect(self.save)
        self.ui.actionOpen_2.triggered.connect(self.open)
        self.ui.textEdit.setAcceptRichText(False)
        self.ui.actionCopy_2.triggered.connect(self.ui.textEdit.copy)
        self.ui.actionCut_2.triggered.connect(self.ui.textEdit.cut)
        self.ui.actionPaste_2.triggered.connect(self.ui.textEdit.paste)
        self.ui.actionAbout_2.triggered.connect(self.about)

    # --------------- NEW FILE -------------- #

    def clear(self):  # If text is saved, clear it, if not saved ask first.
        if self.ui.textEdit.toPlainText() != self.saved:
            msg = QMessageBox()
            answer = msg.question(self, "Are you sure?", "You have unsaved text? Do you want to continue?",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if answer == QMessageBox.Yes:
                self.ui.textEdit.clear()
                self.saved = ""
            else:
                pass
        else:
            self.ui.textEdit.clear()
            self.saved = ""

    # --------------- SAVE FILE -------------- #

    def save(self):
        name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                        "Text Files (*.txt);;All Files (*)")
        with open(name, 'w') as file:
            file.write(self.ui.textEdit.toPlainText())
        self.saved = self.ui.textEdit.toPlainText()

    # --------------- OPEN FILE -------------- #

    def open(self):  # If not saved, ask to open a new file first
        if self.ui.textEdit.toPlainText() != self.saved:
            msg = QMessageBox()
            answer = msg.question(self, "Are you sure?", "You have unsaved text? Do you want to continue?",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if answer == QMessageBox.Yes:
                path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                                "Text documents (*.txt);All files (*.*)")
                if path:
                    with open(path, 'r') as f:
                        text = f.read()
                    self.ui.textEdit.setPlainText(text)
                    self.saved = text
            else:
                pass
        else:
            path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                            "Text documents (*.txt);All files (*.*)")

            if path:
                with open(path, 'r') as f:
                    text = f.read()
                self.ui.textEdit.setPlainText(text)
                self.saved = text

    # --------------- ABOUT -------------- #

    @staticmethod
    def about():
        msg = QMessageBox()
        msg.setWindowTitle("Caesar's Cipher")
        msg.setText("This program allows you to encrypt and decrypt your text with Caesar's method."
                    "\n                                            Written by Uğur Özdemir in 2022.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # --------------- DECODE & ENCODE -------------- #

    def encrypt(self):
        enc = self.sender()
        if enc.isChecked():
            self.direction = enc.text()
            self.ui.pushButton.setText(self.direction)

    # --------------- SHIFTING -------------- #

    def key(self):
        self.shift = self.ui.horizontalSlider.value()  # How much letter will be shifted

    # --------------- CIPHERING -------------- #

    def translate(self):
        self.text = self.ui.textEdit.toPlainText()
        shift = int(self.shift) % 32
        number_shift = int(self.shift) % 10
        cipher_sentence = ""

        # ----------------- ENCODE ------------------ #

        if self.direction == "Encode":
            for i in range(len(self.text)):
                if self.text[i] in alphabet_lower:
                    for letters in range(len(alphabet_lower)):
                        if alphabet_lower[letters] == self.text[i]:
                            index = letters - shift
                            cipher_sentence += alphabet_lower[index]
                elif self.text[i] in alphabet_upper:
                    for letters in range(len(alphabet_upper)):
                        if alphabet_upper[letters] == self.text[i]:
                            index = letters - shift
                            cipher_sentence += alphabet_upper[index]
                elif self.text[i] in numbers:
                    for n in range(len(numbers)):
                        if numbers[n] == self.text[i]:
                            number = n - number_shift
                            cipher_sentence += numbers[number]
                else:
                    cipher_sentence += self.text[i]
            self.ui.textEdit.setPlainText(cipher_sentence)

        # ----------------- DECODE ------------------ #

        elif self.direction == "Decode":
            for i in range(len(self.text)):
                if self.text[i] in alphabet_lower:
                    for letters in range(len(alphabet_lower)):
                        if alphabet_lower[letters] == self.text[i]:
                            index = letters + shift
                            if index > 31:
                                no = index - 32
                                cipher_sentence += alphabet_lower[no]
                            else:
                                cipher_sentence += alphabet_lower[index]
                elif self.text[i] in alphabet_upper:
                    for letters in range(len(alphabet_upper)):
                        if alphabet_upper[letters] == self.text[i]:
                            index = letters + shift
                            if index > 31:
                                no = index - 32
                                cipher_sentence += alphabet_upper[no]
                            else:
                                cipher_sentence += alphabet_upper[index]
                elif self.text[i] in numbers:
                    for n in range(len(numbers)):
                        if numbers[n] == self.text[i]:
                            number = n + number_shift
                            if number > 9:
                                index_no = number - 10
                                cipher_sentence += numbers[index_no]
                            else:
                                cipher_sentence += numbers[number]
                else:
                    cipher_sentence += self.text[i]
            self.ui.textEdit.setPlainText(cipher_sentence)


# ------------------------------------- RUN APPLICATION ------------------------------------------ #

def application():
    win = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(win.exec_())


application()

