from typing import Sequence
import numpy as np

class Button:
    """
        A GUI element which can be clicked and slid to change a value
    """
    __slots__ = (
        "_bar_center", "_handle_center", "_bar_size", "_handle_size",
        "_bg_color", "_handle_color", "_highlight_color", "_fg_color"
    )


    def __init__(
        self, bar_center: Sequence[float],  handle_center: Sequence[float],
        bar_size: Sequence[float], handle_size: Sequence[float],
        bg_color: Sequence[float], fg_color: Sequence[float], highlight_color: Sequence[float]
    ):
        """
            Constructs a new slider

            Parameters:

                center: the (x,y) center of the button
                size: the (w,h) size of the button
                bg_color: the (r,g,b) color of the button
                text: the text on the button
                fg_color: the (r,g,b) color of the text
                highlight_color: the (r,g,b) color of the button
                when active (eg. has mouse focus)
        """
        
        self._bar_center = np.array(bar_center, dtype=np.float32)
        self._handle_center = np.array(handle_center, dtype=np.float32)

        self._bar_size = np.array(bar_size, dtype=np.float32)
        self._handle_size = np.array(handle_size, dtype = np.float32)

        self._bg_color = np.array(bg_color, dtype=np.float32)
        self._fg_color = np.array(fg_color, dtype=np.float32)
        self._highlight_color = np.array(highlight_color, dtype=np.float32)
    
    def set_bar_center(self, new_center: Sequence[float])->None:
        """
            Change the bar center of the slider

            Parameters:

                new_center: the new bar center
            
            Returns:

                None
        """

        self._bar_center = np.array(new_center, dtype=np.float32)
    
    def get_bar_center(self)->np.array:
        """
            Get the bar center of the slider
            
            Returns:

                np.array: a reference to the slider's bar center (note: not a fresh copy!)
        """

        return self._bar_center

    def set_handle_center(self, new_center: Sequence[float])->None:
        """
            Change the handle center of the slider

            Parameters:

                new_center: the new handle center
            
            Returns:

                None
        """

        self._handle_center = np.array(new_center, dtype=np.float32)
    
    def get_handle_center(self)->np.array:
        """
            Get the handle center of the slider
            
            Returns:

                np.array: a reference to the slider's handle center (note: not a fresh copy!)
        """

        return self._handle_center
    
    def set_bar_size(self, new_size: Sequence[float])->None:
        """
            Change the bar size of the slider

            Parameters:

                new_size: the new bar size
            
            Returns:

                None
        """

        self._bar_size = np.array(new_size, dtype=np.float32)
    
    def get_bar_size(self)->np.array:
        """
            Get the bar size of the slider
            
            Returns:

                np.array: a reference to the slider's bar size (note: not a fresh copy!)
        """

        return self._bar_size
    
    def set_handle_size(self, new_size: Sequence[float])->None:
        """
            Change the handle size of the slider

            Parameters:

                new_size: the new handle size
            
            Returns:

                None
        """

        self._handle_size = np.array(new_size, dtype=np.float32)
    
    def get_handle_size(self)->np.array:
        """
            Get the handle size of the slider
            
            Returns:

                np.array: a reference to the slider's handle size (note: not a fresh copy!)
        """

        return self._handle_size
    
    def set_bg_color(self, new_bg_color: Sequence[float])->None:
        """
            Change the background color of the slider

            Parameters:

                new_bg_color: the new background color
            
            Returns:

                None
        """

        self._bg_color = np.array(new_bg_color, dtype=np.float32)
    
    def get_bg_color(self)->np.array:
        """
            Get the background color of the slider
            
            Returns:

                np.array: a reference to the slider's background color (note: not a fresh copy!)
        """

        return self._bg_color
    
    def set_fg_color(self, new_fg_color: Sequence[float])->None:
        """
            Change the foreground (text) color of the slider

            Parameters:

                new_fg_color: the new foreground color
            
            Returns:

                None
        """

        self._fg_color = np.array(new_fg_color, dtype=np.float32)
    
    def get_fg_color(self)->np.array:
        """
            Get the foreground (text) color of the slider
            
            Returns:

                np.array: a reference to the slider's foreground color (note: not a fresh copy!)
        """

        return self._fg_color
    
    def set_highlight_color(self, new_highlight_color: Sequence[float])->None:
        """
            Change the highlight (active) color of the slider

            Parameters:

                new_bg_color: the new highlight color
            
            Returns:

                None
        """

        self._highlight_color = np.array(new_highlight_color, dtype=np.float32)
    
    def get_highlight_color(self)->np.array:
        """
            Get the highlight (active) color of the slider
            
            Returns:

                np.array: a reference to the frame's highlight color (note: not a fresh copy!)
        """

        return self._highlight_color
    
    def inside(self, position: Sequence[float]) -> bool:
        """
            Is the given position inside the slider's bounding box?

            Parameters:

                position: the (x,y) position
            
            Returns:

                bool: whether the given position is inside the button
        """

        left = self._handle_center[0] - self._handle_size[0]
        right = self._handle_center[0] + self._handle_size[0]
        top = self._handle_center[1] + self._handle_size[1]
        bottom = self._handle_center[1] - self._handle_size[1]

        x = position[0]
        y = position[1]

        return x > left and x < right and y < top and y > bottom

    def set_value(self, new_value: float) -> None:
        """
            Set the value for the slider

            Parameters:
                new_value: should be between 0 and 1
        """

        #value is encoded in the position of the handle, so set the position
        left_x_coord = self._bar_center[0] - self._bar_size[0] + self.handle_size[0]
        right_x_coord = (self._bar_center[0] + self._bar_size[0] - self.handle_size[0])
        new_handle_center = ((1 - new_value) * left_x_coord + new_value * right_x_coord, self.handle_size[1])
        self.set_handle_center(new_handle_center)
    
    def get_value(self) -> float:
        """
            Get the value for the slider

            returns:
                float: the value the slider is holding
        """

        #value is encoded in the position of the handle, so read the position
        left_x_coord = self._bar_center[0] - self._bar_size[0] + self.handle_size[0]
        right_x_coord = (self._bar_center[0] + self._bar_size[0] - self.handle_size[0])
        x_value = self._handle_center[0]
        offset = x_value - left_x_coord
        width = right_x_coord - left_x_coord
        
        return offset / width
