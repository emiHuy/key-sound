from PySide6.QtWidgets import QMainWindow, QGridLayout, QLabel, QComboBox, QWidget, QSlider
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QFont
from utils import resource_path

class KeySoundWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KeySound")
        self.setFixedSize(QSize(350, 200))
        self.setWindowIcon(QIcon(resource_path("assets/images/key-sound-icon.png")))

        font = QFont("Segoe UI", 11)

        # sound theme label
        self._theme_label = QLabel("Sound theme:")
        self._theme_label.setFixedSize(180, 15)
        self._theme_label.setFont(font)

        # sound theme combobox
        self.theme_combobox = QComboBox()
        self.theme_combobox.setFixedSize(180, 30)
        self.theme_combobox.addItem(QIcon(resource_path("assets/images/minecraft.jpg")), "Minecraft")
        self.theme_combobox.addItem(QIcon(resource_path("assets/images/super-mario-bros.png")), "Super Mario Bros.")
        self.theme_combobox.addItem(QIcon(resource_path("assets/images/animal-crossing.jpg")), "Animal Crossing")
        self.theme_combobox.setFont(font)

        # volume label
        self._volume_label = QLabel("Volume: ")
        self._volume_label.setFixedSize(180, 15)
        self._volume_label.setFont(font)

        # volume combo box
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(10)
        self.volume_slider.setValue(10)
        self.volume_slider.setTickInterval(1)
        self.volume_slider.setTickPosition(QSlider.NoTicks)
        self.volume_slider.setFixedSize(180, 15)
        self.volume_slider.setFont(font)

        # create layout and add components to layout
        layout = QGridLayout()
        layout.addWidget(self._theme_label, 0, 0, alignment=Qt.AlignBottom)
        layout.addWidget(self.theme_combobox, 1, 0)
        layout.addWidget(self._volume_label, 2, 0, alignment=Qt.AlignBottom)
        layout.addWidget(self.volume_slider, 3, 0, alignment=Qt.AlignTop)

        # add layout to window (central)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def set_player(self, player):
        self._player = player

    def closeEvent(self, event):
        if hasattr(self, "_player"):
            self._player.end()
        event.accept()