from config import *
import gui_controller
import frame
import button

class LoadMenuController(gui_controller.GUIController):
    """
        Represents the out-of-game menu.
    """


    def __init__(self):
        """
            Create a menu.
        """

        super().__init__()
        
        self.create_widgets()

        
    def create_widgets(self) -> None:
        """
            Construct the various widgets for the menu.
        """


        self._frames.append(
            frame.Frame(
                center = (-0.2,0),
                size = (1.4, 1.8),
                bg_color = PALETTE_BLUE
            )
        )

        self._buttons.append(button.Button(
            center = (-0.2, 0.6),
            size = (0.35, 0.1),
            bg_color = PALETTE_BG,
            text = "Slot 1",
            fg_color = PALETTE_ORANGE,
            highlight_color = PALETTE_LIGHT,
            command = RETURN_ACTION_LOAD_GAME_ONE
        ))

        self._buttons.append(button.Button(
            center = (-0.2, 0.2),
            size = (0.35, 0.1),
            bg_color = PALETTE_BG,
            text = "Slot 2",
            fg_color = PALETTE_ORANGE,
            highlight_color = PALETTE_LIGHT,
            command = RETURN_ACTION_LOAD_GAME_TWO
        ))

        self._buttons.append(button.Button(
            center = (-0.2, -0.2),
            size = (0.35, 0.1),
            bg_color = PALETTE_BG,
            text = "Slot 3",
            fg_color = PALETTE_ORANGE,
            highlight_color = PALETTE_LIGHT,
            command = RETURN_ACTION_LOAD_GAME_THREE
        ))

        self._buttons.append(button.Button(
            center = (-0.2, -0.6),
            size = (0.35, 0.1),
            bg_color = PALETTE_BG,
            text = "Back",
            fg_color = PALETTE_ORANGE,
            highlight_color = PALETTE_LIGHT,
            command = RETURN_ACTION_OPEN_MENU
        ))