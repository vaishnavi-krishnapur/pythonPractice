class Problem8():
    def __init__(self):
        self.converted_appointments=[]

    def convert_to_24_hour_time(self, time):
        dict_convert={'12AM' : 0, '1AM' : 1, '2AM': 2, '3AM' : 3, '4AM' : 4, '5AM':5, '6AM' : 6,
                       '7AM' : 7, '8AM' : 8, '9AM' : 9, '10AM' : 10, '11AM' : 11, '12PM' : 12 ,
                       '1PM' : 13, '2PM' : 14, '3PM' : 15, '4PM' : 16, '5PM' : 17, '6PM' : 18,
                       '7PM' : 19, '8PM' : 20, '9PM' : 21 , '10PM' : 22, '11PM' : 23, '12PM': 24}
        return dict_convert[time]

    def appoitmentsList(self, fileName):
        file= open(fileName, 'r')
        fileContent= file.read()
        self.converted_appointments =[]
        for i in fileContent.split():
            self.converted_appointments.append(self.convert_to_24_hour_time(i))
        return self.converted_appointments

    def booking_appoitment(self):
        print("Please input a time when you're available or DONE when finished:")
        available_timings =[]
        input_time=input()
        while input_time != "DONE" :
            available_timings.append(self.convert_to_24_hour_time(input_time))
            print("Please input a time when you're available or DONE when finished:")
            input_time = input()
        available_timings.sort()
        print(available_timings)
        for i in available_timings:
            if i not in self.converted_appointments:
                print("your appointment is scheduled for ", i , "o'clock")
                break


obj=Problem8()
obj.convert_to_24_hour_time('1PM')
obj.appoitmentsList('Problem8_input.txt')
obj.booking_appoitment()

