#from email import message
from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):


    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self.points = 0
    
    def get_points(self):
        """Gets the artifact's message.
        Returns:
            string: The message.
        """
        return self.points

    def set_points(self, points):
        """Updates the message to the given one.
        Args:
            message (string): The given message.
        """
        self.point = points