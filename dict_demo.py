# Dictionary Example Accessing values

dict = {'Name': 'Kavya', 'Age': 7, 'Class': 'First'}        #Defined Dictionary with keys and values
print ("dict['Name']: ", dict['Name'] )                  #display Name
print ("dict['Age']: ", dict['Age'])                    #dispaly age
print("dict['Class']:", dict['Class'])

#dict = {'Name': 'Kavya', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8;             # update existing entry
dict['School'] = "DAV Public School";      # Add new entry
print("After modifying the dictionary the values are:")
print ("Age ", dict['Age'])
print ("School ", dict['School'])

print("Final Output")
print(dict)