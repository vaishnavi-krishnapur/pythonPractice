class Problem12():
    def __init__(self):
        pass
    def get_genre_data(self, filenames) :
        genere_data={}
        for i in filenames:
            file=open(i,'r')
            content=file.read()
            content= content.splitlines()
            genre=content[0]
            dict_values=[]
            for i in content[1:]:
                value=tuple(i.split(','))
                dict_values.append(value)
            genere_data[genre] = dict_values
        return genere_data

    def get_author_data(self,genere_data):
        author_data = {}
        for genres in genere_data:
            for articles in genere_data[genres]:
                author=articles[1]
                if author not in author_data:
                    author_data[author]=[(articles[0],articles[2],genres)]
                else:
                    author_data[author].append((articles[0],articles[2],genres))
        return author_data


fileNames=['prob12_input_opinions.txt','prob12_input_arts.txt']
obj=Problem12()
genere_data = obj.get_genre_data(fileNames)
print(genere_data)
print(obj.get_author_data(genere_data))

