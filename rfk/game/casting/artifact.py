#from email import message
from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):


    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self.message = ""
    
    def get_message(self):
        """Gets the artifact's message.
        Returns:
            string: The message.
        """
        return self.message

    def set_message(self, message):
        """Updates the message to the given one.
        Args:
            message (string): The given message.
        """
        self.message = message