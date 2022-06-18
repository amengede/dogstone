## GUI Model classes

### Frame
A colored rectangle

#### class variables:
* center: np.Array(x,y)
* size: np.Array(w,h)
* bg_color: np.Array(r,g,b)

#### class functions:
* getters and setters for all variables

### Button
A colored rectangle with text

#### class variables:
* center: np.Array(x,y)
* size: np.Array(w,h)
* bg_color: np.Array(r,g,b)
* text: String
* fg_color: np.Array(r,g,b)
* highlight_color: np.Array(r,g,b)

#### class functions:
* inside(pos: tuple(x,y)) -> bool, indicates whether the given position is inside the button's rectangle
* getters and setters for all variables

### Label

#### class variables:
* center: np.Array(x,y)
* size: np.Array(w,h)
* text: String
* fg_color: np.Array(r,g,b)

#### class functions:
* getters and setters for all variables

### Slider
A label, bar and handle. The handle is normalized between 0 and 1. Bar's position is reflected by the slider's value.

#### class variables:
* bar_center: np.Array(x,y)
* handle_center: np.Array(x,y)
* bar_size: np.Array(w,h)
* handle_size: np.Array(w,h)
* bg_color: np.Array(r,g,b)
* handle_color: np.Array(r,g,b)
* highlight_color: np.Array(r,g,b)
* fg_color: np.Array(r,g,b)

#### class functions:
* inside(pos: tuple(x,y)) -> bool, indicates whether the given position is inside the handle
* getters and setters for all variables