from ...Node import Node


# Fog
class Fog(Node):
    fields = [
        ('type', 'uint'),
        ('adj', 'FogAdj'),
        ('start_z', 'float'),
        ('end_z', 'float'),
        ('color', '@RGBAColor'),
    ]

    def build(self, builder):
        pass
