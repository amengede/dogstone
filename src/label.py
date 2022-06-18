from typing import Sequence
import numpy as np

class Label:
    """
        A GUI element which displays text
    """
    __slots__ = (
        "_center", "_size", "_text", "_fg_color"
    )


    def __init__(
        self, center: Sequence[float], size: Sequence[float], fg_color: Sequence[float],
        text: str
    ):
        """
            Constructs a new label

            Parameters:

                center: the (x,y) center of the button
                size: the (w,h) size of the button
                text: the text on the button
                fg_color: the (r,g,b) color of the text
        """
        
        self._center = np.array(center, dtype=np.float32)
        self._size = np.array(size, dtype=np.float32)
        self._text = text
        self._fg_color = np.array(fg_color, dtype=np.float32)
    
    def set_center(self, new_center: Sequence[float])->None:
        """
            Change the center of the label

            Parameters:

                new_center: the new center
            
            Returns:

                None
        """

        self._center = np.array(new_center, dtype=np.float32)
    
    def get_center(self)->np.array:
        """
            Get the center of the label
            
            Returns:

                np.array: a reference to the label's center (note: not a fresh copy!)
        """

        return self._center

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
    