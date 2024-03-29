#version 330

layout (location = 0) in vec2 vertexPos;

uniform mat4 model;

void main() {
    gl_Position = model * vec4(vertexPos, 0.0, 1.0);
}