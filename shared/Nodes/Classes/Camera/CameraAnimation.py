from ...Node import Node


# Camera Animation
class CameraAnimation(Node):
    fields = [
        ('animation', 'Animation'),
        ('eye_position_animation', 'WObject'),
        ('interest_animation', 'WObject'),
    ]