from pyray import *

class Score:
    """
    displays score in the top left of the screen and sets
    the text
    attributes:
        self.value: sets initial score at 0
        self.colour: sets score board color
    """
    def __init__(self):
        super().__init__()
        self.value = 0
        self.color = (255,0,0)

    def display_score(self):
        #displays the current score on score board
        draw_text(f"Score: {self.value}", 20, 20, 25, self.color)

    def update_score(self, points):
        #updates the score according to objects caught
        self.value += points