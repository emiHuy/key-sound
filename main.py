import sys
import key_sound_window as ksw
import key_sound_controller as ksc
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ksw.KeySoundWindow()
    window.show()
    controller = ksc.KeySoundController(window)
    controller._player.run()
    app.exec()