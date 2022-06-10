
class renderer:
    """
        Manages an OpenGL context, renders stuff.
    """


    def __init__(self, width: int, height: int):
        """
            Creates a renderer, which can then be passed commands.

            Parameters:

                width: the width of the window
                height: the height of the window
        """

        pass

    def create_shaders(self) -> None:
        """
            Creates the shaders to be used.
        """

        pass

    def query_shader_locations(self) -> None:
        """
            Fetch the locations of uniforms ahead of time,
            so they can be reused cheaply.
        """

        pass

    def set_onetime_shader_data(self) -> None:
        """
            Some shader data only needs to be set once.
        """

        pass

    def create_assets(self) -> None:
        """
            Create any assets eg. Meshes and Materials which may be used
        """

        pass

    def render(self, renderables: dict[any]) -> None:
        """
            Render a given scene, as described in renderables

            Parameters:

                renderables: a dictionary describing the data to render. format
                will depend on the concrete instance of renderer being used.
        """

        pass

    def destroy(self) -> None:
        """
            Destroys the renderer, freeing its memory.
        """

        pass