import random

#Camila
#List of random words
#Word lengths
#Each word letter & index for each letter


class List:
    """Contains a list of words that will be chosen at random. 
    
    The responsibility of List is to generate a random word.
    
    Attributes:
        _list (List[str]): list of words to be chosen at random.
        _word (str): The chosen word from the list.
    """

    def __init__(self):
        """Constructs a new List of words.

        Args:
            self (List): An instance of list.
        """
        self._list = ["star","beach","countryside","meadow","rainforest","wilderness","flower"]
        self._word = ""
        self.random_word()
    def random_word(self):
        """Selects a random word from the list
        
        Args:
            self (List): An instance of List.
        
        Returns:
            string: Word from the list"""
        random_index= random.randint(0,7)
        self._word= self._list[random_index]

    def word_to_list(self):
        list_of_letters= list(self.word)

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