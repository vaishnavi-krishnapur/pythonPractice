#Read an XML document and convert the same into tabular csv using XMLTree

from xml.etree import ElementTree
import csv
class Problem4b():
    def __init__(self,xmlFile):
        self.xmlFile=xmlFile

    def readXml(self):
        self.fileContent = ElementTree.parse(self.xmlFile)

    def createCsv(self):
        csvFile = open("problem4bOutput", 'w', encoding='utf-8')
        writer = csv.writer(csvFile)
        columns = ['book Id', 'author', 'title', "genre", "price", "publish_date", "description"]
        writer.writerow(columns)

        xml=self.fileContent
        root = xml.getroot()
        #print(root.tag)
        for book in root:
            book_id = book.attrib['id']
            #print(book_id)
            author = book.find("author")
            title = book.find("title")
            genre = book.find("genre")
            price = book.find("price")
            publish_date = book.find("publish_date")
            description = book.find("description")
            csv_line=[book_id, author.text,title.text, genre.text, price.text,  publish_date.text, description.text]

            writer.writerow(csv_line)

obj=Problem4b("problem4Input.xml")
obj.readXml()
obj.createCsv()



