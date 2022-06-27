from config import *
from app import App
import load_menu_controller
import menu_controller


"""
    Dogstone: An exciting Project.

    Main function.
"""

def main():
    
    app = App()
    app.set_controller(menu_controller.MenuController())
    result = app.main_loop()
    while result != RETURN_ACTION_QUIT:

        if result == RETURN_ACTION_OPEN_MENU:
            app.set_controller(menu_controller.MenuController())

        elif result ==RETURN_ACTION_START_GAME:
            print("start game!")
        
        elif result == RETURN_ACTION_OPEN_LOAD_MENU:
            app.set_controller(load_menu_controller.LoadMenuController())
            
        elif result == RETURN_ACTION_OPEN_OPTIONS_MENU:
            pass
            #app.set_controller(OptionsMenuController())

        elif result == RETURN_ACTION_LOAD_GAME_ONE:
            print("Load game one!")
        
        elif result == RETURN_ACTION_LOAD_GAME_TWO:
            print("Load game two!")
        
        elif result == RETURN_ACTION_LOAD_GAME_THREE:
            print("Load game three!")
        
        else:
            break

        result = app.mainloop()
    
    app.destroy()

if __name__ == "__main__":

    main()