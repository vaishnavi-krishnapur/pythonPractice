#Patients visits from file to dict
class Problem7():
    def get_patient_visits_dict(self,fileName):
        dict1={}
        fileObj = open(fileName, "r")
        fileContent = fileObj.readlines()
        #print(fileContent)
        for i in fileContent:
            #print(i)
            name= i.split()[1]
            if name in dict1:
                dict1[name] += 1
            else:
                dict1[name] =1
        return dict1

obj = Problem7()
print(obj.get_patient_visits_dict("Problem7_input.txt"))




