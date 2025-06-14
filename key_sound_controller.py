import key_sound_player as player

class KeySoundController:
    def __init__(self, view):
        self._view = view
        self._player = player.KeySoundPlayer()
        self._view.set_player(self._player)
        self.connect_signals()
        self._player.run()

    def connect_signals(self):
        self._view.theme_combobox.currentTextChanged.connect(self.handle_combobox)
        self._view.volume_slider.valueChanged.connect(self.handle_slider)

    def handle_combobox(self):
        self._player.set_theme(self._view.theme_combobox.currentText())
    
    def handle_slider(self):
        self._player.set_volume_adj_factor(self._view.volume_slider.value()/10)