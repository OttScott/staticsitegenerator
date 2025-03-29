from enum import Enum

class TextType(Enum):
    NORMAL = "NORMAL"
    BOLD   = "BOLD"
    ITALIC = "ITALIC"
    CODE   = "CODE"
    LINK   = "LINK"
    IMAGE  = "IMAGE"

class TextNode:
    def __init__(self, text: str, text_type: TextType=TextType.NORMAL, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, value):
        if self.text != value.text:
            return False
        if self.text_type != value.text_type:
            return False
        if self.url != value.url:
            return False
        return True
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.name}, {self.url})"

        