#version 330

uniform vec3 objectColor;

out vec4 fragmentColor;

void main() {
    fragmentColor = vec4(objectColor, 1.0);
}