from GREED.casting.player import Player


class Gemstone(Player):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Gemstone is to provide a message about its value
    and adjust points.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the artifact's message. Adjust points
        
        Returns:
            string: The message.
        """
        
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message