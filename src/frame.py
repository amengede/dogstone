from typing import Sequence
import numpy as np

class Frame:
    """
        A GUI element which can hold other elements.
        Essentially a colored rectangle.
    """
    __slots__ = ("_center", "_size", "_bg_color")


    def __init__(self, center: Sequence[float], size: Sequence[float], bg_color: Sequence[float]):
        """
            Constructs a new frame

            Parameters:

                center: the (x,y) center of the frame
                size: the (w,h) size of the frame
                bg_color: the (r,g,b) color of the frame
        """
        
        self._center = np.array(center + (0,), dtype=np.float32)
        self._size = np.array(size + (0,), dtype=np.float32)
        self._bg_color = np.array(bg_color, dtype=np.float32)
    
    def set_center(self, new_center: Sequence[float])->None:
        """
            Change the center of the frame

            Parameters:

                new_center: the new center
            
            Returns:

                None
        """

        self._center = np.array(new_center, dtype=np.float32)
    
    def get_center(self)->np.array:
        """
            Get the center of the frame
            
            Returns:

                np.array: a reference to the frame's center (note: not a fresh copy!)
        """

        return self._center

    def set_size(self, new_size: Sequence[float])->None:
        """
            Change the size of the frame

            Parameters:

                new_size: the new size
            
            Returns:

                None
        """

        self._size = np.array(new_size, dtype=np.float32)
    
    def get_size(self)->np.array:
        """
            Get the size of the frame
            
            Returns:

                np.array: a reference to the frame's size (note: not a fresh copy!)
        """

        return self._size
    
    def set_bg_color(self, new_bg_color: Sequence[float])->None:
        """
            Change the background color of the frame

            Parameters:

                new_bg_color: the new background color
            
            Returns:

                None
        """

        self._bg_color = np.array(new_bg_color, dtype=np.float32)
    
    def get_bg_color(self)->np.array:
        """
            Get the background color of the frame
            
            Returns:

                np.array: a reference to the frame's background color (note: not a fresh copy!)
        """

        return self._bg_color
