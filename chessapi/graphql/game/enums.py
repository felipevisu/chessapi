from ...graphql.core.enums import to_enum
from ...game import Color, PieceType


ColorEnum = to_enum(Color, type_name="ColorEnum")
PieceTypeEnum = to_enum(PieceType, type_name="PieceTypeEnum")