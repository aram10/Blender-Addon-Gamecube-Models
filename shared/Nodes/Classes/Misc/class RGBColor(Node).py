from ...Node import Node
from ..Colors import Color


# RGB Color
class RGBColor(Node, Color):
    is_cachable = False
    fields = [
        ('red', 'uchar'),
        ('green', 'uchar'),
        ('blue', 'uchar'),
        ('padding', 'uchar')
    ]

    def loadFromBinary(self, parser):
        super().loadFromBinary(parser)

        self.alpha = 0xFF