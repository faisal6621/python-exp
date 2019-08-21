from xml.etree import ElementTree
from xml.etree.ElementTree import Element


def main():
    tree: ElementTree = ElementTree.parse("sample.xml")
    root: Element = tree.getroot()
    for row in root:  # type: Element
        for column in row:  # type: Element
            print(column.attrib['name'], column.text, sep=' -> ', end='\t')
    print()


main()
