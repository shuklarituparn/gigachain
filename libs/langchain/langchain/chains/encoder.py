from json import JSONEncoder

from langchain.schema import BaseDocumentTransformer


class AliasJSONEncoder(JSONEncoder):
    """
    Класс помогающий нам кодировать не сериализуемые объекты,
    такие как BaseDocumentTransformer, в JSON, с помощью вспомогательных функций
    """

    def default(self, o):
        from langchain.document_transformers.serializers import serialize_transformer

        if isinstance(o, BaseDocumentTransformer):
            return serialize_transformer(o)
        else:
            return super().default(o)
