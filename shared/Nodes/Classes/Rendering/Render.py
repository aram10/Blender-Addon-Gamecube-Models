from ...Node import Node


# Render
class Render(Node):
    fields = [
        ('toon_texture', 'Texture'),
        ('grad_texture', 'Texture'),
        ('terminator', 'uint'),
    ]
