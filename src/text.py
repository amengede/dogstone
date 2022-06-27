from config import *

class Font:

    def __init__(self):

         #some parameters for fine tuning.
        w = 55.55 / 1000.0
        h =  63.88 / 1150.0
        heightOffset = 8.5 / 1150.0
        margin = 0.014

        """
            Letter: (left, top, width, height)
        """
        self.letterTexCoords = {
            'A': (       w, 1.0 - h,                          w - margin, h - margin), 'B': ( 3.0 * w, 1.0 - h,                          w - margin, h - margin),
            'C': ( 5.0 * w, 1.0 - h,                          w - margin, h - margin), 'D': ( 7.0 * w, 1.0 - h,                          w - margin, h - margin),
            'E': ( 9.0 * w, 1.0 - h,                          w - margin, h - margin), 'F': (11.0 * w, 1.0 - h,                          w - margin, h - margin),
            'G': (13.0 * w, 1.0 - h,                          w - margin, h - margin), 'H': (15.0 * w, 1.0 - h,                          w - margin, h - margin),
            'I': (17.0 * w, 1.0 - h,                          w - margin, h - margin), 'J': (       w, 1.0 - 3.0 * h + heightOffset,     w - margin, h - margin),
            'K': ( 3.0 * w, 1.0 - 3.0 * h + heightOffset,     w - margin, h - margin), 'L': ( 5.0 * w, 1.0 - 3.0 * h + heightOffset,     w - margin, h - margin),
            'M': ( 7.0 * w, 1.0 - 3.0 * h + heightOffset,     w - margin, h - margin), 'N': ( 9.0 * w, 1.0 - 3.0 * h + heightOffset,     w - margin, h - margin),
            'O': (11.0 * w, 1.0 - 3.0 * h + heightOffset,     w - margin, h - margin), 'P': (13.0 * w, 1.0 - 3.0 * h + heightOffset,     w - margin, h - margin),
            'Q': (15.0 * w, 1.0 - 3.0 * h + heightOffset,     w - margin, h - margin), 'R': (17.0 * w, 1.0 - 3.0 * h + heightOffset,     w - margin, h - margin),
            'S': (       w, 1.0 - 5.0 * h + 2 * heightOffset, w - margin, h - margin), 'T': ( 3.0 * w, 1.0 - 5.0 * h + 2 * heightOffset, w - margin, h - margin),
            'U': ( 5.0 * w, 1.0 - 5.0 * h + 2 * heightOffset, w - margin, h - margin), 'V': ( 7.0 * w, 1.0 - 5.0 * h + 2 * heightOffset, w - margin, h - margin),
            'W': ( 9.0 * w, 1.0 - 5.0 * h + 2 * heightOffset, w - margin, h - margin), 'X': (11.0 * w, 1.0 - 5.0 * h + 2 * heightOffset, w - margin, h - margin),
            'Y': (13.0 * w, 1.0 - 5.0 * h + 2 * heightOffset, w - margin, h - margin), 'Z': (15.0 * w, 1.0 - 5.0 * h + 2 * heightOffset, w - margin, h - margin),

            'a': (       w,                     1.0 - 7.0 * h, w - margin, h - margin), 'b': ( 3.0 * w,         1.0 - 7.0 * h, w - margin, h - margin),
            'c': ( 5.0 * w,                     1.0 - 7.0 * h, w - margin, h - margin), 'd': ( 7.0 * w,         1.0 - 7.0 * h, w - margin, h - margin),
            'e': ( 9.0 * w,                     1.0 - 7.0 * h, w - margin, h - margin), 'f': (11.0 * w,         1.0 - 7.0 * h, w - margin, h - margin),
            'g': (13.0 * w,                     1.0 - 7.0 * h, w - margin, h - margin), 'h': (15.0 * w,         1.0 - 7.0 * h, w - margin, h - margin),
            'i': (17.0 * w,                     1.0 - 7.0 * h, w - margin, h - margin), 'j': (       w,      1.0 - 9.0 * h + heightOffset, w - margin, h - margin),
            'k': ( 3.0 * w,      1.0 - 9.0 * h + heightOffset, w - margin, h - margin), 'l': ( 5.0 * w,      1.0 - 9.0 * h + heightOffset, w - margin, h - margin),
            'm': ( 7.0 * w,      1.0 - 9.0 * h + heightOffset, w - margin, h - margin), 'n': ( 9.0 * w,      1.0 - 9.0 * h + heightOffset, w - margin, h - margin),
            'o': (11.0 * w,      1.0 - 9.0 * h + heightOffset, w - margin, h - margin), 'p': (13.0 * w,      1.0 - 9.0 * h + heightOffset, w - margin, h - margin),
            'q': (15.0 * w,      1.0 - 9.0 * h + heightOffset, w - margin, h - margin), 'r': (17.0 * w,      1.0 - 9.0 * h + heightOffset, w - margin, h - margin),
            's': (       w, 1.0 - 11.0 * h + 2 * heightOffset, w - margin, h - margin), 't': ( 3.0 * w, 1.0 - 11.0 * h + 2 * heightOffset, w - margin, h - margin),
            'u': ( 5.0 * w, 1.0 - 11.0 * h + 2 * heightOffset, w - margin, h - margin), 'v': ( 7.0 * w, 1.0 - 11.0 * h + 2 * heightOffset, w - margin, h - margin),
            'w': ( 9.0 * w, 1.0 - 11.0 * h + 2 * heightOffset, w - margin, h - margin), 'x': (11.0 * w, 1.0 - 11.0 * h + 2 * heightOffset, w - margin, h - margin),
            'y': (13.0 * w, 1.0 - 11.0 * h + 2 * heightOffset, w - margin, h - margin), 'z': (15.0 * w, 1.0 - 11.0 * h + 2 * heightOffset, w - margin, h - margin),

            '0': (       w, 1.0 - 13.0 * h, w - margin, h - margin), '1':  ( 3.0 * w,                1.0 - 13.0 * h, w - margin, h - margin),
            '2': ( 5.0 * w, 1.0 - 13.0 * h, w - margin, h - margin), '3':  ( 7.0 * w,                1.0 - 13.0 * h, w - margin, h - margin),
            '4': ( 9.0 * w, 1.0 - 13.0 * h, w - margin, h - margin), '5':  (11.0 * w,                1.0 - 13.0 * h, w - margin, h - margin),
            '6': (13.0 * w, 1.0 - 13.0 * h, w - margin, h - margin), '7':  (15.0 * w,                1.0 - 13.0 * h, w - margin, h - margin),
            '8': (17.0 * w, 1.0 - 13.0 * h, w - margin, h - margin), '9':  (       w, 1.0 - 15.0 * h + heightOffset, w - margin, h - margin),
            
            '.':  ( 3.0 * w,     1.0 - 15.0 * h + heightOffset, w - margin, h - margin), ',': ( 5.0 * w,     1.0 - 15.0 * h + heightOffset, w - margin, h - margin),
            ';':  ( 7.0 * w,     1.0 - 15.0 * h + heightOffset, w - margin, h - margin), ':': ( 9.0 * w,     1.0 - 15.0 * h + heightOffset, w - margin, h - margin),
            '$':  (11.0 * w,     1.0 - 15.0 * h + heightOffset, w - margin, h - margin), '#': (13.0 * w,     1.0 - 15.0 * h + heightOffset, w - margin, h - margin),
            '\'': (15.0 * w,     1.0 - 15.0 * h + heightOffset, w - margin, h - margin), '!': (17.0 * w,     1.0 - 15.0 * h + heightOffset, w - margin, h - margin),
            '"':  (       w, 1.0 - 17.0 * h + 2 * heightOffset, w - margin, h - margin), '/': ( 3.0 * w, 1.0 - 17.0 * h + 2 * heightOffset, w - margin, h - margin),
            '?':  ( 5.0 * w, 1.0 - 17.0 * h + 2 * heightOffset, w - margin, h - margin), '%': ( 7.0 * w, 1.0 - 17.0 * h + 2 * heightOffset, w - margin, h - margin),
            '&':  ( 9.0 * w, 1.0 - 17.0 * h + 2 * heightOffset, w - margin, h - margin), '(': (11.0 * w, 1.0 - 17.0 * h + 2 * heightOffset, w - margin, h - margin),
            ')':  (13.0 * w, 1.0 - 17.0 * h + 2 * heightOffset, w - margin, h - margin), '@': (15.0 * w, 1.0 - 17.0 * h + 2 * heightOffset, w - margin, h - margin)
        }

        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        image = pg.image.load("gfx/Inconsolata.png").convert_alpha()
        image_width,image_height = image.get_rect().size
        img_data = pg.image.tostring(image,'RGBA')
        glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,image_width,image_height,0,GL_RGBA,GL_UNSIGNED_BYTE,img_data)
        glGenerateMipmap(GL_TEXTURE_2D)
    
    def get_bounding_box(self, letter):

        if letter in self.letterTexCoords:
            return self.letterTexCoords[letter]
        return None
    
    def use(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D,self.texture)

    def destroy(self):
        glDeleteTextures(1, (self.texture,))

class TextLine:

    
    def __init__(self, initial_text, font, start_position, letter_size):

        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        self.start_position = start_position
        self.letter_size = letter_size
        self.build_text(initial_text, font)
    
    def build_text(self, new_text, font):

        self.vertices = []
        self.vertex_count = 0

        margin_adjustment = 0.96

        for i,letter in enumerate(new_text):

            bounding_box  = font.get_bounding_box(letter)
            if bounding_box is None:
                continue

            #top left
            self.vertices.append(
                self.start_position[0] - self.letter_size[0] + ((2 - margin_adjustment) * i * self.letter_size[0])
            )
            self.vertices.append(self.start_position[1] + self.letter_size[1])
            self.vertices.append(bounding_box[0] - bounding_box[2])
            self.vertices.append(bounding_box[1] + bounding_box[3])
            #top right
            self.vertices.append(
                self.start_position[0] + self.letter_size[0] + ((2 - margin_adjustment) * i * self.letter_size[0])
            )
            self.vertices.append(self.start_position[1] + self.letter_size[1])
            self.vertices.append(bounding_box[0] + bounding_box[2])
            self.vertices.append(bounding_box[1] + bounding_box[3])
            #bottom right
            self.vertices.append(
                self.start_position[0] + self.letter_size[0] + ((2 - margin_adjustment) * i * self.letter_size[0])
            )
            self.vertices.append(self.start_position[1] - self.letter_size[1])
            self.vertices.append(bounding_box[0] + bounding_box[2])
            self.vertices.append(bounding_box[1] - bounding_box[3])

            #bottom right
            self.vertices.append(
                self.start_position[0] + self.letter_size[0] + ((2 - margin_adjustment) * i * self.letter_size[0])
            )
            self.vertices.append(self.start_position[1] - self.letter_size[1])
            self.vertices.append(bounding_box[0] + bounding_box[2])
            self.vertices.append(bounding_box[1] - bounding_box[3])
            #bottom left
            self.vertices.append(
                self.start_position[0] - self.letter_size[0] + ((2 - margin_adjustment) * i * self.letter_size[0])
            )
            self.vertices.append(self.start_position[1] - self.letter_size[1])
            self.vertices.append(bounding_box[0] - bounding_box[2])
            self.vertices.append(bounding_box[1] - bounding_box[3])
            #top left
            self.vertices.append(
                self.start_position[0] - self.letter_size[0] + ((2 - margin_adjustment) * i * self.letter_size[0])
            )
            self.vertices.append(self.start_position[1] + self.letter_size[1])
            self.vertices.append(bounding_box[0] - bounding_box[2])
            self.vertices.append(bounding_box[1] + bounding_box[3])

            self.vertex_count += 6

        self.vertices = np.array(self.vertices, dtype=np.float32)

        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        offset = 0
        #position
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(offset))
        offset += 8
        #texture
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(offset))
    
    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1,(self.vbo,))