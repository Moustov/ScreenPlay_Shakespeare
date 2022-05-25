from canvas.element import Element


class Screen:
    def __init__(self, name: str):
        super.__init__(self, name)
        self.elements_on_the_screen = []

    def add_element(self, name: str, element: Element):
        """
        registers some new ability to this actor
        :param element: an Element object
        :param name: name of the ability
        :param action: the object associated to the ability
        :return:
        """
        self.elements_on_the_screen.append({"name": name, "what": element})