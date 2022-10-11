"""
file doc
"""


class GString:
    def __init__(self, init=None) -> None:
        self.content = init

    def __del__(self):
        print("Deleted")

    def __sub__(self, str):
        for i in str:
            self.content = self.content.replace(i, "")
        return GString(self.content)

    def __str__(self) -> str:
        return self.content


g = GString("ABCDEFGabcdefg")
r = g - "Adg"

print(r)
