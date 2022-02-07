#Read an XML document and convert the same into tabular csv using file file handling operation
import csv
class Problem4():
    def __init__(self,xmlFile):
        self.xmlFile=xmlFile

    def readXml(self):
        file = open(self.xmlFile, "r")
        self.fileContent = file.readlines()
        return self.fileContent

    def printXml(self):
        for i in self.fileContent:
            print(i)

    def createCsv(self):
        csvFile=open("problem4aOutput", 'w')
        writer=csv.writer(csvFile)
        columns=['book Id', 'author', 'title',"genre","price","publish_date","description"]
        writer.writerow(columns)
        each_row = []
        for i in self.fileContent:
            i = i.strip()
            if "<book id" in i:
                if len(each_row)!=0: writer.writerow(each_row)
                each_row=[]
                bookId= i.split('"')[1]
                each_row.append(bookId)
            else:
                for column_name in columns:
                    if column_name in i:
                        row_values=i.split('>')[1].split('<')[0]
                        each_row.append(row_values)

                #since description is in multi-line
                if i.startswith('<') != 1:
                        descr=i.split('<')
                        each_row[-1] += descr[0]
                        each_row.append(row_values)

obj=Problem4("problem4Input.xml")
obj.readXml()
#obj.printXml()
obj.createCsv()



