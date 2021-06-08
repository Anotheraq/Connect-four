from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QComboBox
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import QSize, Qt
from itertools import chain
from GameLogic.ConnectFourLogic import ConnectFourClassic, ConnectFourPopOut
from Exceptions.ImpossibleMoveException import ImpossibleMoveException
import GameStateFrame


class MainFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = ConnectFourClassic()
        self.init_interface()
        self.connect_backend()

    def init_interface(self):
        self.set_font()
        self.set_window_properties()
        self.set_top_interface()
        self.set_drop_buttons()
        self.set_game_board()
        self.set_pop_buttons()

    def set_font(self):
        self.font = QFont("Calibri Light")
        self.font.setBold(True)

    def set_window_properties(self):
        self.setWindowTitle("Connect Four")
        self.setWindowIcon(QIcon('Images/main_frame_icon.png'))
        self.setFixedSize(QSize(610, 700))

        self.setCentralWidget(QWidget(self))
        self.central_layout = QVBoxLayout(self.centralWidget())

    def set_start_restart_button(self):
        self.font.setPointSize(20)
        self.start_restart_button = QPushButton(self.inface_widget)
        self.start_restart_button.setText("Start")
        self.start_restart_button.setFont(self.font)

    def set_mode_combo_box(self):
        self.game_mode_combo_box = QComboBox(self.inface_widget)
        self.game_mode_combo_box.addItem("Classic")
        self.game_mode_combo_box.addItem("PopOut")
        self.game_mode_combo_box.setFont(self.font)
        self.game_mode_combo_box.currentIndexChanged.connect(
            lambda *args: self.set_game_mode(self.game_mode_combo_box.currentText()))

    def set_game_state_label(self):
        self.font.setPointSize(17)
        self.game_state_label = QLabel(self.inface_widget)
        self.game_state_label.setFixedSize(QSize(200, 40))
        self.game_state_label.setText("Waiting for start...")
        self.game_state_label.setFont(self.font)
        self.game_state_label.setAlignment(Qt.AlignCenter)

    def set_top_interface(self):
        self.inface_widget = QWidget(self.centralWidget())
        self.central_layout.addWidget(self.inface_widget)
        self.inface_layout = QHBoxLayout(self.inface_widget)

        self.set_start_restart_button()
        self.inface_layout.addWidget(self.start_restart_button)
        self.set_mode_combo_box()
        self.inface_layout.addWidget(self.game_mode_combo_box)
        self.set_game_state_label()
        self.inface_layout.addWidget(self.game_state_label)

    def set_drop_buttons(self):
        self.top_controls_widget = QWidget(self.centralWidget())
        self.central_layout.addWidget(self.top_controls_widget)
        self.top_controls_layout = QHBoxLayout(self.top_controls_widget)
        self.create_drop_buttons()

    def set_game_board(self):
        self.board_widget = QWidget(self.centralWidget())
        self.central_layout.addWidget(self.board_widget)
        self.board_layout = QGridLayout(self.board_widget)
        self.board_layout.setVerticalSpacing(0)
        self.board_layout.setHorizontalSpacing(0)
        self.board_layout.setOriginCorner(Qt.BottomLeftCorner)
        self.render_board()

    def set_pop_buttons(self):
        self.bottom_controls_widget = QWidget(self.centralWidget())
        self.central_layout.addWidget(self.bottom_controls_widget)
        self.bottom_controls_layout = QHBoxLayout(self.bottom_controls_widget)
        self.create_pop_buttons()


    def set_game_mode(self, mode):
        '''Ustawia tryb gry na określony'''

        self.game_mode = mode
        if self.game_mode == "PopOut":
            self.game = ConnectFourPopOut()
        elif self.game_mode == "Classic":
            self.game = ConnectFourClassic()

    def create_drop_buttons(self):
        '''Tworzу 7 przycisków "drop" '''

        self.drop_buttons = []
        for i in range(7):
            self.drop_button = QPushButton(self.top_controls_widget)
            self.drop_buttons.append(self.drop_button)
            self.top_controls_layout.addWidget(self.drop_buttons[i])
            self.drop_buttons[i].setText("Drop")
            self.drop_buttons[i].setFont(self.font)
            self.drop_buttons[i].setEnabled(False)

    def create_pop_buttons(self):
        '''Tworzy 7 przycisków "pop" '''

        self.pop_buttons = []
        for i in range(7):
            self.pop_button = QPushButton(self.bottom_controls_widget)
            self.pop_buttons.append(self.pop_button)
            self.bottom_controls_layout.addWidget(self.pop_buttons[i])
            self.pop_buttons[i].setText("Pop")
            self.pop_buttons[i].setFont(self.font)
            self.pop_buttons[i].setEnabled(False)

    def render_board(self):
        '''Aktualizuje wygląd wizualny tablicy'''

        positions = list(chain.from_iterable([[(i, j) for j in range(7)] for i in range(6)]))
        for position in positions:
            self.render_field(position[0], position[1])

    def render_field(self, x, y):
        '''Aktualizuje wygląd pojedynczego pola planszy'''

        field = QLabel(self.board_widget)
        if self.game.get_board()[x][y] == 1:
            field.setPixmap((QPixmap("Images/red_cell.png")))
        elif self.game.get_board()[x][y] == 2:
            field.setPixmap((QPixmap("Images/yellow_cell.png")))
        else:
            field.setPixmap((QPixmap("Images/empty_cell.png")))
        self.board_layout.addWidget(field, x, y)

    def connect_backend(self):
        self.game_in_progress = False
        self.game_mode = self.game_mode_combo_box.currentText()

        self.start_restart_button.clicked.connect(self.start_restart_game)

        for drop_button, pop_button, column in zip(self.drop_buttons, self.pop_buttons, range(7)):
            drop_button.clicked.connect(lambda *args, column=column: self.drop_move(column))
            pop_button.clicked.connect(lambda *args, column=column: self.pop_move(column))

    def enable_buttons(self, enable):
        '''W zależności od parametru enable i trybu gry włącza lub wyłącza przyciski'''

        for pop, drop in zip(self.pop_buttons, self.drop_buttons):
            drop.setEnabled(enable)
            if enable:
                if self.game_mode == "PopOut":
                    pop.setEnabled(enable)
            else:
                pop.setEnabled(enable)

    def start_restart_game(self):
        '''Uruchamia grę, albo ją resetuje'''

        if self.game_in_progress:
            self.game_in_progress = False
            self.start_restart_button.setText("Start")
            self.game_state_label.setText("Waiting for start...")
            self.game_mode_combo_box.setEnabled(True)
            self.enable_buttons(False)
            self.game.reset()
            self.render_board()
        else:
            self.game_in_progress = True
            self.start_restart_button.setText("Restart")
            self.game_state_label.setText("Tura gracza " + str(self.game.current_player))
            self.game_mode_combo_box.setEnabled(False)
            self.enable_buttons(True)


    def move(move_func):
        '''Wrapper dla każdego ruchu podczas gry'''

        def wrapper(self, *args, **kwargs):
            try:
                move_func(self, *args, **kwargs)
                self.render_board()
            except ImpossibleMoveException:
                self.game_state_label.setText("Impossible move!")
        return wrapper

    @move
    def drop_move(self, column):
        '''Dodaje monete bieżącego gracza do określonej kolumny'''

        self.game.drop_move(column)
        if self.game.kto_wygral(self.game.current_player):
            self.game_state_label.setText("Wygrał gracz " + str(self.game.current_player))
            self.enable_buttons(False)
            game_state_frame = GameStateFrame.GameStateFrame(self.game.current_player)
            game_state_frame.show()
        elif self.game.is_board_full() and self.game_mode == "Classic":
            self.game_state_label.setText("Remis!")
            self.enable_buttons(False)
            game_state_frame = GameStateFrame.GameStateFrame(0)
            game_state_frame.show()
        else:
            self.game.change_turns()
            self.game_state_label.setText("Tura gracza  " + str(self.game.current_player))

    @move
    def pop_move(self, column):
        '''Zrzuca monete bieżącego gracza z określonej kolumny'''
        self.game.pop_move(column)
        if self.game.kto_wygral(self.game.current_player):
            self.game_state_label.setText("Wygrał gracz " + str(self.game.current_player))
            self.enable_buttons(False)
            game_state_frame = GameStateFrame.GameStateFrame(self.game.current_player)
            game_state_frame.show()
        elif self.game.kto_wygral(self.game.next_player):
            self.game_state_label.setText("Wygrał gracz " + str(self.game.next_player))
            self.enable_buttons(False)
            game_state_frame = GameStateFrame.GameStateFrame(self.game.next_player)
            game_state_frame.show()
        else:
            self.game.change_turns()
            self.game_state_label.setText("Tura gracza " + str(self.game.current_player))


if __name__ == "__main__":
    app = QApplication([])
    main_frame = MainFrame()
    main_frame.show()
    app.exec_()
