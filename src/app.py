from config import *

from menu_view_controllers import Controller

class App:
    """
        Takes user input and sends messages to view controller.
    """

    def __init__(self):
        """
            Create a new App, initializes pygame
        """

        pg.init()
        self._viewcontroller = None
    
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
                    return_action = self._viewcontroller.handle_mouse_click(pg.mouse.get_pos())
                    if return_action != RETURN_ACTION_NONE:
                        running = False
                
                self._viewcontroller.update(pg.mouse.get_pos())

                self._viewcontroller.render(pg.mouse.get_pos())
        
        return return_action
    
    def set_controller(self, new_controller: Controller) -> None:
        """
            Change the App's controller. The current controller is destroyed.

            Parameters:
                new_controller: the new controller for the app.
        """

        self._viewcontroller.destroy()
        self._viewcontroller = new_controller
    
    def destroy(self) -> None:
        """
            Destroy the App, calls pygame's destructor.
        """

        self._viewcontroller.destroy()
        pg.quit()