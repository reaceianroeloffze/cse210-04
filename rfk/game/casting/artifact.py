from game.casting.actor import Actor


class Artifact(Actor):
    """    
    The responsibility of an Artifact is to provide a score to the player.

    Attributes:
        _score (string): The score when colliding with an artifact.
    """
    def __init__(self):
        super().__init__()
        self._score = 0
        
    def get_score(self):
        """Gets the artifact's score.
        
        Returns:
            string: The score.
        """
        return self._score
    
    def set_score(self, score):
        """Updates the score to the given one.
        
        Args:
            score (string): The given score.
        """
        self._score = score