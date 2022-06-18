"""
    Helper function for compiling and linking shaders
"""

from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.GL import GL_VERTEX_SHADER, GL_FRAGMENT_SHADER

def create_shader(filepath) -> int:
    """
        reads source code for the given filepath (both .vert and .frag files),
        compiles and links. Allocates memory, the created shader must be destroyed.

        Parameters:
            
            filepath: the file to read. everything up the file extension
        
        Returns:
            The index of the created shader.
    """

    with open(f"{filepath}.vert", "r") as f:
        vertex_src = f.readlines()
    
    with open(f"{filepath}.frag", "r") as f:
        fragment_src = f.readlines()
    
    return compileProgram(
        compileShader(vertex_src, GL_VERTEX_SHADER),
        compileShader(fragment_src, GL_FRAGMENT_SHADER)
    )