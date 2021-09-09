from django.db import models

from . import Color, PieceType


class Piece(models.Model):
    color = models.CharField(max_length=20, choices=Color.CHOICES)
    piece_type = models.CharField(max_length=20, choices=PieceType.CHOICES)

    def __str__(self):
        return str(self.piece_type)
