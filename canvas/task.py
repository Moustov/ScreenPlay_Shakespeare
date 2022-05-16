from canvas.action import Action
from canvas.actor import Actor
from canvas.screenplay import ScreenPlay


class Task (ScreenPlay):
    def __init__(self, name: str):
        super.__init__(self, name)
        self.made_of = []

    def made_up_of(self, an_actor: Actor):
        pass
