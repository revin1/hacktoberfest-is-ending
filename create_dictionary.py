def create_dictionary():
     list_1 = ['Ten', 'Twenty', 'Thirty']
     list_2 = [10, 20, 30]
     dictionary = dict()
     for i in range(len(list_1)):
         dictionary[list_1[i]] = list_2[i]
     print(dictionary)
     
create_dictionary()
