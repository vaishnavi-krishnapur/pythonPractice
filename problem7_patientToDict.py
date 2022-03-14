#Patients visits from file to dict
class problem7():
    def get_patient_visits_dict(self,fileName):
        dict1={}
        fileObj = open(fileName, "r")
        fileContent = fileObj.readlines()
        #print(fileContent)
        for i in fileContent:
            #print(i)
            if len(i.split()) < 2:
                raise IndexError("invalid details in input file")
            name= i.split()[1]
            if name in dict1:
                dict1[name] += 1
            else:
                dict1[name] =1
        fileObj.close()
        return dict1

obj = problem7()
print(obj.get_patient_visits_dict("Problem7_input.txt"))




