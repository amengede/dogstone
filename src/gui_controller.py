from typing import Sequence
from config import *
import controller

class GUIController(controller.Controller):
    """
        GUI Controller class, extends Controller, has
        general GUI widgets.
    """

    def __init__(self) -> None:
        """
            Create a GUI controller.
        """

        self._frames = []
        self._buttons = []
        self._labels = []
        self._sliders = []
    
    def handle_mouse_click(self, mouse_position: Sequence[float]) -> int:
        """
            handles a mouse click at the given position, returns the next action
            to take, if any.

            Parameters:
                mouse_position: the (x,y) position where the click occurred.
            
            Returns:
                int: the next action to take, as per the return_action constants in config.py
        """

        for button in self._buttons:

            if button.inside(mouse_position):

                return button.get_command()
    
    def get_widgets(self) -> dict[int,list[object]]:
        """
            Get a dictionary of renderable objects for the viewcontroller.

            Returns:
                dict[int: list[object]]: a dictionary of renderable objects. Keys are the renderable_types
                constants from config.py, each key has an associated list of matching objects.
        """

        
        return {
            RENDERABLE_TYPE_FRAME: self._frames,
            RENDERABLE_TYPE_BUTTON: self._buttons,
            RENDERABLE_TYPE_LABEL: self._labels,
            RENDERABLE_TYPE_SLIDER: self._sliders,
        }
    
    def render(self, mouse_position: Sequence[float]) -> None:
        """
            Render the view controller

            Parameters:

                mouse_position: (x,y) position of the mouse, might be useful
                for some menu drawing.
        """

        self._renderer.render(self.get_widgets(), mouse_position)