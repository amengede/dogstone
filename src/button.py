from typing import Sequence
import numpy as np

class Button:
    """
        A GUI element which can hold text and be pressed.
    """
    __slots__ = (
        "_center", "_size", "_bg_color", "_text", "_fg_color", "_highlight_color", "_command"
    )


    def __init__(
        self, center: Sequence[float], size: Sequence[float], bg_color: Sequence[float],
        text: str, fg_color: Sequence[float], highlight_color: Sequence[float], command: int
    ):
        """
            Constructs a new button

            Parameters:

                center: the (x,y) center of the button
                size: the (w,h) size of the button
                bg_color: the (r,g,b) color of the button
                text: the text on the button
                fg_color: the (r,g,b) color of the text
                highlight_color: the (r,g,b) color of the button
                when active (eg. has mouse focus)
                command: the signal to return on click
        """
        
        self._center = np.array(center + (0,), dtype=np.float32)
        self._size = np.array(size + (0,), dtype=np.float32)
        self._bg_color = np.array(bg_color, dtype=np.float32)
        self._text = text
        self._fg_color = np.array(fg_color, dtype=np.float32)
        self._highlight_color = np.array(highlight_color, dtype=np.float32)
        self._command = command
    
    def set_center(self, new_center: Sequence[float])->None:
        """
            Change the center of the button

            Parameters:

                new_center: the new center
            
            Returns:

                None
        """

        self._center = np.array(new_center, dtype=np.float32)
    
    def get_center(self)->np.array:
        """
            Get the center of the button
            
            Returns:

                np.array: a reference to the button's center (note: not a fresh copy!)
        """

        return self._center

    def set_size(self, new_size: Sequence[float])->None:
        """
            Change the size of the button

            Parameters:

                new_size: the new size
            
            Returns:

                None
        """

        self._size = np.array(new_size, dtype=np.float32)
    
    def get_size(self)->np.array:
        """
            Get the size of the button
            
            Returns:

                np.array: a reference to the button's size (note: not a fresh copy!)
        """

        return self._size
    
    def set_bg_color(self, new_bg_color: Sequence[float])->None:
        """
            Change the background color of the button

            Parameters:

                new_bg_color: the new background color
            
            Returns:

                None
        """

        self._bg_color = np.array(new_bg_color, dtype=np.float32)
    
    def get_bg_color(self)->np.array:
        """
            Get the background color of the button
            
            Returns:

                np.array: a reference to the frame's background color (note: not a fresh copy!)
        """

        return self._bg_color
    
    def set_text(self, new_text: str)->None:
        """
            Set the text of the button

            Parameters:

                new_text: the new text
            
            Returns:

                None
        """

        self._text = new_text
    
    def get_text(self):
        """
            Get the text contents of the button

            Returns:

                str: the text on the button
        """

        return self._text

    def set_fg_color(self, new_fg_color: Sequence[float])->None:
        """
            Change the foreground (text) color of the button

            Parameters:

                new_fg_color: the new foreground color
            
            Returns:

                None
        """

        self._fg_color = np.array(new_fg_color, dtype=np.float32)
    
    def get_fg_color(self)->np.array:
        """
            Get the foreground (text) color of the button
            
            Returns:

                np.array: a reference to the frame's foreground color (note: not a fresh copy!)
        """

        return self._fg_color
    
    def set_highlight_color(self, new_highlight_color: Sequence[float])->None:
        """
            Change the highlight (active) color of the button

            Parameters:

                new_bg_color: the new highlight color
            
            Returns:

                None
        """

        self._highlight_color = np.array(new_highlight_color, dtype=np.float32)
    
    def get_highlight_color(self)->np.array:
        """
            Get the highlight (active) color of the button
            
            Returns:

                np.array: a reference to the frame's highlight color (note: not a fresh copy!)
        """

        return self._highlight_color
    
    def get_command(self) -> int:
        """
            Get the command code for the button.

            Returns:

                int: The return action for the button. Defined in return_actions (config.py)
        """

        return self._command
    
    def set_command(self, new_command) -> None:
        """
            Set the command code for the button.

            Parameters:

                new_command: The return action for the button. Defined in return_actions (config.py)

            Returns:

                None
        """

        self._command = new_command
    
    def inside(self, position: Sequence[float]) -> bool:
        """
            Is the given position inside the button's bounding box?

            Parameters:

                position: the (x,y) position
            
            Returns:

                bool: whether the given position is inside the button
        """

        left = self._center[0] - self._size[0]
        right = self._center[0] + self._size[0]
        top = self._center[1] + self._size[1]
        bottom = self._center[1] - self._size[1]

        x = position[0]
        y = position[1]

        return x > left and x < right and y < top and y > bottom
