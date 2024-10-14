import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout

class MatrizApp(QWidget):
    def __init__(self, altura, largura):
        super().__init__()
        self.altura = altura
        self.largura = largura
        self.vagas = [[0 for _ in range(largura)] for _ in range(altura)]
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Matriz de Botões")
        self.layout = QGridLayout()

        self.buttons = [[None for _ in range(self.largura)] for _ in range(self.altura)]

        for i in range(self.altura):
            for j in range(self.largura):
                btn = QPushButton('0')
                btn.setStyleSheet("background-color: red;")
                btn.clicked.connect(lambda checked, row=i, col=j: self.button_click(row, col))
                self.layout.addWidget(btn, i, j)
                self.buttons[i][j] = btn

        reset_button = QPushButton('Reset')
        reset_button.clicked.connect(self.reset_matrix)
        self.layout.addWidget(reset_button, self.altura, 0, 1, self.largura)

        self.setLayout(self.layout)

    def change_state(self, row, col, state):
        self.buttons[row][col].setText(str(state))
        self.buttons[row][col].setStyleSheet("background-color: red;" if state == 1 else "background-color: green;")
        self.vagas[row][col] = state

    def button_click(self, row, col):
        txt = self.buttons[row][col].text()
        if txt == "0":
            self.change_state(row, col, 1)
        elif txt == "1":
            self.change_state(row, col, 0)

    def reset_matrix(self):
        for i in range(self.altura):
            for j in range(self.largura):
                self.change_state(i, j, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    altura = 3  # int(input("Altura: "))
    largura = 3  # int(input("Largura: "))
    matriz_app = MatrizApp(altura, largura)
    matriz_app.show()
    sys.exit(app.exec())
