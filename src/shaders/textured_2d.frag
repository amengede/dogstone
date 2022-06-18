#version 330

in vec2 fragmentTexCoord;

uniform vec3 objectColor;
uniform sampler2d material;

out vec4 fragmentColor;

void main() {
    fragmentColor = vec4(objectColor, 1.0) * texture(material, fragmentTexCoord);
}