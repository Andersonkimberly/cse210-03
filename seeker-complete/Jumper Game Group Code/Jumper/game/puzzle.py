import random

#Camila
#List of random words
#Word lengths
#Each word letter & index for each letter


class List:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new List of words.

        Args:
            self (Hider): An instance of Hider.
        """
        self._list = ["star","beach","countryside","meadow","rainforest","wilderness","flower"]
        self._word = ""
        self.random_word()
    def random_word(self):
        """Gets a hint for the seeker.
        
        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker."""
        random_index= random.randint(0,7)
        self._word= self._list[random_index]

    def get_word(self):
        """Whether or not the hider has been found.

        Args:
            
            
        Returns:
            """
        
        return self._word
        
    def watch_seeker(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        distance = abs(self._location - seeker.get_location())
        # self._distance.append(distance)