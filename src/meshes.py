"""
    Various mesh classes
"""

import numpy as np
from OpenGL.GL import *

class ColoredQuad:
    """
        A basic 2D Rectangle. No color data (this is applied by uniforms)
        or texture coordinates.
        No size (this is applied by uniforms)
    """

    __slots__ = ("vertices", "vao", "vbo", "vertex_count")

    def __init__(self):
        """
            Create the vertices, vbo and vao of the mesh.
            vbo and vao have memory allocated, and must be freed
            on destruction.
        """

        self.vertices = (
            -1,  1,
            -1, -1,
             1, -1,

            -1,  1,
             1, -1,
             1,  1
        )

        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 6

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 8, ctypes.c_void_p(0))
    
    def destroy(self) -> None:
        """
            Free memory allocated by this mesh.
        """

        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))

class TexturedQuad:
    """
        A textured 2D Rectangle. No color data (this is applied by uniforms)
        No size (this is applied by uniforms)
    """

    __slots__ = ("vertices", "vao", "vbo", "vertex_count")

    def __init__(self):
        """
            Create the vertices, vbo and vao of the mesh.
            vbo and vao have memory allocated, and must be freed
            on destruction.
        """

        self.vertices = (
            -1,  1, 0, 1,
            -1, -1, 0, 0,
             1, -1, 1, 0,

            -1,  1, 0, 1,
             1, -1, 1, 0,
             1,  1, 1, 1
        )

        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 6

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 8, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 8, ctypes.c_void_p(0))
    
    def destroy(self) -> None:
        """
            Free memory allocated by this mesh.
        """

        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))
