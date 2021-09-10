import graphene


def str_to_enum(name):
    return name.replace(" ", "_").replace("-", "_").upper()


# transform a list of choices in graphql enum type
def to_enum(enum_cls, *, type_name=None, **options) -> graphene.Enum:
    type_name = type_name or (enum_cls.__name__ + "Enum")
    enum_data = [(str_to_enum(code.upper()), code) for code, name in enum_cls.CHOICES]
    return graphene.Enum(type_name, enum_data, **options)