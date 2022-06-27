import shader_functions
from renderer import renderer
import meshes
import material
import text
from config import *

class GUIRenderer(renderer):
    """
        Manages an OpenGL context, renders GUI widgets.
    """

    # slots: make life hard, let's ignore them!


    def __init__(self):
        """
            Creates a renderer, which can then be passed commands.

            Parameters:

                width: the width of the window
                height: the height of the window
        """

        glClearColor(PALETTE_BG[0], PALETTE_BG[1], PALETTE_BG[2], 1.0)
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.create_shaders()
        self.query_shader_locations()
        
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

        self.font = text.Font()
        self.text_mesh = text.TextLine("", self.font, (0,0), (0,0))

    def render(self, renderables: dict[any], mouse_position: tuple[float, float]) -> None:
        """
            Render a given scene, as described in renderables

            Parameters:

                renderables: a dictionary describing the data to render. format
                will depend on the concrete instance of renderer being used.

                mouse_position: the (x,y) position of the mouse.
        """

        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.colored_shader)
        glBindVertexArray(self.colored_quad.vao)
        for frame in renderables[RENDERABLE_TYPE_FRAME]:

            
            glUniform3fv(self.color_data_location["colored"], 1, frame.get_bg_color())

            model_transform = pyrr.matrix44.create_identity(dtype = np.float32)
            model_transform = pyrr.matrix44.multiply(
                m1 = model_transform,
                m2 = pyrr.matrix44.create_from_scale(scale = frame.get_size())
            )
            model_transform = pyrr.matrix44.multiply(
                m1 = model_transform,
                m2 = pyrr.matrix44.create_from_translation(vec = frame.get_center())
            )
            glUniformMatrix4fv(self.model_matrix_location["colored"], 1, GL_FALSE, model_transform)

            glDrawArrays(GL_TRIANGLES, 0, self.colored_quad.vertex_count)
            
        for button in renderables[RENDERABLE_TYPE_BUTTON]:

            glUseProgram(self.colored_shader)
            glBindVertexArray(self.colored_quad.vao)
            if button.inside(mouse_position):
                color = button.get_highlight_color()
            else:
                color = button.get_bg_color()
            glUniform3fv(self.color_data_location["colored"], 1, color)

            model_transform = pyrr.matrix44.create_identity(dtype = np.float32)
            model_transform = pyrr.matrix44.multiply(
                m1 = model_transform,
                m2 = pyrr.matrix44.create_from_scale(scale = button.get_size())
            )
            model_transform = pyrr.matrix44.multiply(
                m1 = model_transform,
                m2 = pyrr.matrix44.create_from_translation(vec = button.get_center())
            )
            glUniformMatrix4fv(self.model_matrix_location["colored"], 1, GL_FALSE, model_transform)

            glDrawArrays(GL_TRIANGLES, 0, self.colored_quad.vertex_count)

            glUseProgram(self.textured_shader)
            glUniform3fv(self.color_data_location["textured"], 1, button.get_fg_color())

            model_transform = pyrr.matrix44.create_identity(dtype=np.float32)
            glUniformMatrix4fv(self.model_matrix_location["textured"], 1, GL_FALSE, model_transform)

            center = button.get_center()
            size = button.get_size()
            self.text_mesh.start_position = (center[0] - size[0]/1.2, center[1])
            self.text_mesh.letter_size = (size[0]/ 6, size[1] / 2)
            self.text_mesh.build_text(button.get_text(), self.font)
            
            glBindVertexArray(self.text_mesh.vao)
            self.font.use()
            glDrawArrays(GL_TRIANGLES, 0, self.text_mesh.vertex_count)
        
        glUseProgram(self.textured_shader)
        for label in renderables[RENDERABLE_TYPE_LABEL]:

            glUniform3fv(self.color_data_location["textured"], 1, label.get_fg_color())

            model_transform = pyrr.matrix44.create_identity(dtype=np.float32)
            glUniformMatrix4fv(self.model_matrix_location["textured"], 1, GL_FALSE, model_transform)

            self.text_mesh.start_position = tuple(label.get_start_pos())
            self.text_mesh.letter_size = tuple(label.get_size())
            self.text_mesh.build_text(label.get_text(), self.font)
            
            glBindVertexArray(self.text_mesh.vao)
            self.font.use()
            glDrawArrays(GL_TRIANGLES, 0, self.text_mesh.vertex_count)
        
        for slider in renderables[RENDERABLE_TYPE_SLIDER]:

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
            
        pg.display.flip()

    def destroy(self) -> None:
        """
            Destroys the renderer, freeing its memory.
        """

        self.colored_quad.destroy()
        self.textured_quad.destroy()

        self.font.destroy()
        self.text_mesh.destroy()