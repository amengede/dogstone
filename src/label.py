from typing import Sequence
import numpy as np

class Label:
    """
        A GUI element which displays text
    """
    __slots__ = (
        "_center", "_start_pos", "_letter_size" "_text", "_fg_color"
    )


    def __init__(
        self, start_pos: Sequence[float], letter_size: Sequence[float], fg_color: Sequence[float],
        text: str
    ):
        """
            Constructs a new label

            Parameters:

                stat_pos: the start position of the text, text runs left to right.
                letter_size: the (w,h) size of each letter
                text: the text on the button
                fg_color: the (r,g,b) color of the text
        """
        
        self._start_pos = np.array(start_pos, dtype=np.float32)
        self._letter_size = np.array(letter_size, dtype=np.float32)
        self._text = text
        self._fg_color = np.array(fg_color, dtype=np.float32)
    
    def set_start_pos(self, new_start: Sequence[float])->None:
        """
            Change the start position of the label

            Parameters:

                new_start: the new start position
            
            Returns:

                None
        """

        self._start_pos = np.array(new_start, dtype=np.float32)
    
    def get_start_pos(self)->np.array:
        """
            Get the start position of the label
            
            Returns:

                np.array: a reference to the label's start position (note: not a fresh copy!)
        """

        return self._start_pos

    def set_size(self, new_size: Sequence[float])->None:
        """
            Change the size of the label

            Parameters:

                new_size: the new size
            
            Returns:

                None
        """

        self._size = np.array(new_size, dtype=np.float32)
    
    def get_size(self)->np.array:
        """
            Get the size of the label
            
            Returns:

                np.array: a reference to the label's size (note: not a fresh copy!)
        """

        return self._size
     
    def set_text(self, new_text: str)->None:
        """
            Set the text of the label

            Parameters:

                new_text: the new text
            
            Returns:

                None
        """

        self._text = new_text
    
    def get_text(self):
        """
            Get the text contents of the label

            Returns:

                str: the text on the label
        """

        return self._text

    def set_fg_color(self, new_fg_color: Sequence[float])->None:
        """
            Change the foreground (text) color of the label

            Parameters:

                new_fg_color: the new foreground color
            
            Returns:

                None
        """

        self._fg_color = np.array(new_fg_color, dtype=np.float32)
    
    def get_fg_color(self)->np.array:
        """
            Get the foreground (text) color of the label
            
            Returns:

                np.array: a reference to the frame's foreground color (note: not a fresh copy!)
        """

        return self._fg_color
    