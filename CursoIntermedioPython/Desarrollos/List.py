
from contextlib import nullcontext

class Element:
    content = ""

    def __init__(self, content) -> None:
        self.content = content
    
    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content


class MyList:

    def __init__(self, size) -> None:
        self.index = 0
        self.element = [None] * size;

    def get_index(self):
        return self.index

    def add(self, element):
        self.element[self.index] = element
        self.index += 1

    def update(self, index, element):
        self.element[index] = element

    def forList(self):
        for i in self.element:
            print(i.get_content())

    def print(self):
        return print(self.element.__str__)

class Main:

    def run():
        element1 = Element("Object 1")
        list = MyList(3)
        list.add(element1)
        element2 = Element("Object 2")
        element3 = Element("Object 3")
        list.add(element2)
        list.add(element3)
        list.update(0, element3)
        list.forList()
        list.print()


    if __name__ == "__main__":
        run()