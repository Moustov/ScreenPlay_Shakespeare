from canvas.screen import Screen
from canvas.screenplay import ScreenPlay


class Element (ScreenPlay):

    def __init__(self, name: str):
        super.__init__(self, name)
        pass

    def on_a(self, a_screen: Screen):
        pass
