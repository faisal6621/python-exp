from xml.etree import ElementTree


def main():
    tree = ElementTree.parse("sample.xml")
    root = tree.getroot()
    for row in root:
        for column in row:
            print(column.attrib['name'], column.text, sep=' -> ', end='\t')
        print()


main()
