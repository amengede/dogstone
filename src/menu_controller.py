from config import *
import gui_controller
import frame
import label
import button

class MenuController(gui_controller.GUIController):
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

        self._labels.append(label.Label(
            start_pos = (0.0, 0.8),
            letter_size = (0.05, 0.05),
            text = "Dogstone",
            fg_color = PALETTE_LIGHT
        ))

        self._buttons.append(button.Button(
            center = (-0.2, 0.6),
            size = (0.35, 0.1),
            bg_color = PALETTE_BG,
            text = "New Game",
            fg_color = PALETTE_ORANGE,
            highlight_color = PALETTE_LIGHT,
            command = RETURN_ACTION_START_GAME
        ))

        self._buttons.append(button.Button(
            center = (-0.2, 0.2),
            size = (0.35, 0.1),
            bg_color = PALETTE_BG,
            text = "Load Game",
            fg_color = PALETTE_ORANGE,
            highlight_color = PALETTE_LIGHT,
            command = RETURN_ACTION_OPEN_LOAD_MENU
        ))

        self._buttons.append(button.Button(
            center = (-0.2, -0.2),
            size = (0.35, 0.1),
            bg_color = PALETTE_BG,
            text = "Options",
            fg_color = PALETTE_ORANGE,
            highlight_color = PALETTE_LIGHT,
            command = RETURN_ACTION_OPEN_OPTIONS_MENU
        ))

        self._buttons.append(button.Button(
            center = (-0.2, -0.6),
            size = (0.35, 0.1),
            bg_color = PALETTE_BG,
            text = "Exit",
            fg_color = PALETTE_ORANGE,
            highlight_color = PALETTE_LIGHT,
            command = RETURN_ACTION_QUIT
        ))