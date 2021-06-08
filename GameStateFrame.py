from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, Qt


class GameStateFrame(QDialog):
    def __init__(self, game_state):
        super().__init__()
        self.set_font()
        self.set_window_properties()
        self.set_window_widgets(game_state)

    def set_font(self):
        self.font = QFont("Calibri Light")
        self.font.setBold(True)

    def set_window_properties(self):
        self.setWindowTitle(" ")
        self.setWindowIcon(QIcon('Images/dialog_frame_icon.png'));
        self.setFixedSize(QSize(150, 100))
        self.setModal(True)
        self.central_widget = QWidget(self)
        self.central_layout = QVBoxLayout(self.central_widget)


    def set_close_button(self):
        self.close_button = QPushButton(self.central_widget)
        self.central_layout.addWidget(self.close_button)
        self.close_button.setText("Close")
        self.close_button.setFont(self.font)
        self.close_button.clicked.connect(lambda: self.accept())

    def set_window_widgets(self, game_state):
        self.game_state_label = QLabel(self.central_widget)
        self.central_layout.addWidget(self.game_state_label)

        if game_state != 0:
            self.game_state_label.setText("Wygrał gracz " + str(game_state))
        else:
            self.game_state_label.setText("Remis!")
        self.font.setPointSize(15)
        self.game_state_label.setFont(self.font)
        self.central_layout.setAlignment(self.game_state_label, Qt.AlignHCenter)

        self.set_close_button()


