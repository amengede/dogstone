from typing import Tuple
from config import *

import controller

class App:
    """
        Takes user input and sends messages to view controller.
    """

    def __init__(self):
        """
            Create a new App, initializes pygame
        """

        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.OPENGL | pg.DOUBLEBUF)
        self._viewcontroller = None
    
    def get_mouse_position(self) -> Tuple[float]:
        """
            Transforms the mouse's position from pygame to OpenGL
            coordinates.

            Returns:
                the (x,y) position of the mouse.
        """

        mouse_pos = pg.mouse.get_pos()
        half_width = SCREEN_WIDTH / 2.0
        half_height = SCREEN_HEIGHT / 2.0
        x = (mouse_pos[0] - half_width)/half_width
        y = -(mouse_pos[1] - half_height)/half_height
        return (x,y)
    
    def main_loop(self) -> int:
        """
            Starts the main loop for the current viewcontroller,
            at the conclusion of the main loop, returns a return_action
            constant

            Returns:
                int: the action to take next, as per config.py
        """

        running = True
        return_action = RETURN_ACTION_NONE

        while running:

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    return_action = RETURN_ACTION_QUIT
                    running = False
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    return_action = self._viewcontroller.handle_mouse_click(self.get_mouse_position())
                    if return_action != RETURN_ACTION_NONE:
                        running = False
                
                self._viewcontroller.update(self.get_mouse_position())

                self._viewcontroller.render(self.get_mouse_position())
        
        return return_action
    
    def set_controller(self, new_controller: controller.Controller) -> None:
        """
            Change the App's controller. The current controller is destroyed.

            Parameters:
                new_controller: the new controller for the app.
        """

        if self._viewcontroller is not None:
            self._viewcontroller.destroy()
        self._viewcontroller = new_controller
    
    def destroy(self) -> None:
        """
            Destroy the App, calls pygame's destructor.
        """

        if self._viewcontroller is not None:
            self._viewcontroller.destroy()
        pg.quit()