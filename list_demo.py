#List Data type Demonstration
lst = ["NIT","IIT", "Thapar Enginering College"]
lst1 = [1,2,3,4,5]
print(lst[0])       #print Zeroth location
print(lst[2])       #print Second location
lst[2] = "REC"      #Replace Existing location data to REC
print(lst)          #It will print the complete list
lst.append("SRM University")          #Add at end of the List
print(lst)          #it shows the modified list
lst.insert(1,"College of Engg.")  #Inserting data between the location
print(lst)
print(lst1)

