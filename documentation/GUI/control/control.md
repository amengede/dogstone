## GUI Control classes

### App
Runs the program, has a reference to a controller class. Initializes its controller, then calls
its mainloop and reacts based on that mainloop's return value.

### GUIController(Controller)
Owns widgets and handles mouse movement and click events

#### class variables:
* frames: List\[[Frame](../model/model.md)\]
* buttons: List\[[Button](../model/model.md)\]
* labels: List\[[Label](../model/model.md)\]
* sliders: List\[[Slider](../model/model.md)\]

#### class functions:
* handle_mouse()->void, handles any mouse position-related logic
* handle_mouse_click()->void, handles any mouse click-related logic
* main_loop()->return_action, starts the main loop, upon completion, returns the appropriate action to take

### MenuController(GUIController)
Controller class specific to the starting menu

### LoadMenuController(GUIController)
Controller class specific to the loadgame menu

### OptionsMenuController(GUIController)
Controller class specific to the options menu