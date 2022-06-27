from typing import Sequence
from config import *

class Controller:
    """
        General Controller class, supports event handling, updating
        and rendering. Has a renderer class of some kind, and model data,
        possibly simple or complex.
    """

    def handle_mouse_click(self, mouse_position):

        pass

    def update(self, mouse_position):

        pass

    def destroy(self) -> None:
        """
            destroy the view controller, freeing any allocated memory.
        """

        self._renderer.destroy()