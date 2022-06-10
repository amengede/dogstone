import shader_functions
from renderer import renderer
import meshes
from OpenGL.GL import *

class GUIRenderer(renderer):
    """
        Manages an OpenGL context, renders GUI widgets.
    """

    # slots: speeds up class (although not noticably, but why not!)
    __slots__ = (
        "width", "height", "colored_shader", "textured_shader",
        "colored_quad", "textured_quad", "font",
        "model_matrix_location", "color_data_location"
    )


    def __init__(self, width: int, height: int):
        """
            Creates a renderer, which can then be passed commands.

            Parameters:

                width: the width of the window
                height: the height of the window
        """

        self.width = width
        self.height = height

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glDisable(GL_DEPTH_TEST)

        self.create_shaders()
        self.create_assets()

    def create_shaders(self) -> None:
        """
            Creates the shaders to be used.
        """

        self.colored_shader = shader_functions.create_shader(
            filepath = "shaders/colored_2d"
        )

        self.textured_shader = shader_functions.create_shader(
            filepath = "shaders/textured_2d"
        )

    def query_shader_locations(self) -> None:
        """
            Fetch the locations of uniforms ahead of time,
            so they can be reused cheaply.
        """

        self.model_matrix_location = {
            "colored": None,
            "textured": None
        }

        self.color_data_location = {
            "colored": None,
            "textured": None
        }

        glUseProgram(self.colored_shader)
        self.model_matrix_location["colored"] = glGetUniformLocation(
            self.colored_shader, "model"
        )
        self.color_data_location["colored"] = glGetUniformLocation(
            self.colored_shader, "objectColor"
        )

        glUseProgram(self.textured_shader)
        self.model_matrix_location["textured"] = glGetUniformLocation(
            self.textured_shader, "model"
        )
        self.color_data_location["textured"] = glGetUniformLocation(
            self.textured_shader, "objectColor"
        )

    def create_assets(self) -> None:
        """
            Create any assets eg. Meshes and Materials which may be used
        """

        self.colored_quad = meshes.ColoredQuad()
        self.textured_quad = meshes.TexturedQuad()

    def render(self, renderables: dict[any], mouse_position: tuple[float, float]) -> None:
        """
            Render a given scene, as described in renderables

            Parameters:

                renderables: a dictionary describing the data to render. format
                will depend on the concrete instance of renderer being used.

                mouse_position: the (x,y) position of the mouse.
        """

        glClear(GL_COLOR_BUFFER_BIT)

        for frame in renderables["Frames"]:

            glUseProgram(self.colored_shader)
            #send color data
            #build model transform
            #draw
            pass
            
        for button in renderables["Buttons"]:

            glUseProgram(self.colored_shader)
            #choose color data for rectangle
            #build model transform for rectangle
            #draw rectangle
            glUseProgram(self.textured_shader)
            #send color data for text
            #build model transform for text
            #draw text
            pass
            
        for label in renderables["Labels"]:

            glUseProgram(self.textured_shader)
            #send color data for text
            #build model transform for text
            #draw text
            pass
        
        for slider in renderables["Sliders"]:

            glUseProgram(self.colored_shader)
            #send color data for bar
            #build model transform for bar
            #draw bar
            #choose color data for handle
            #build model transform for handle
            #draw handle
            glUseProgram(self.textured_shader)
            #send color data for text
            #build model transform for text
            #draw text
            pass

    def destroy(self) -> None:
        """
            Destroys the renderer, freeing its memory.
        """

        self.colored_quad.destroy()
        self.textured_quad.destroy()