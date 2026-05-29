
# If you are planning to run only the openspace.py, it is necessary to adjust the way of importing the file. 
# from table import Table : since openspace.py and table.py locate in the same folder 'utils'
from utils.table import Table
import random
class OpenSpace:
    def __init__(self, n_of_tables = 6):
        """Here, the object OpenSpace is created.
        The default of the number of tables is 6 since there are 6 tables in Openspace in our scenario. 
        
        self.tables is a list , for tables in the range of 6, we create a loop to add table object in self.tables.
        """
        self.tables = []
        for i in range(n_of_tables):
            self.tables.append(Table())

    def organize(self,names):
        """ 
        Fuction that will randomly assign people to seats in the OpenSpace.
        
        First, We shuffle the list of names to ensure random seating.
        
        Then, for each person in the list, we loop through the tables in self.tables.
        
        For each table, we will assign a seat using the assign_seat() method.
        
        If a seat is successfully assigned, we move to the next person.
        
        If no table has an availabe seat, the function returns False, 
        meaning that not everyone could be seated.
        
        If all people are successfully seated, the function returns True.
        """

        random.shuffle(names)
        for name in names:
            seated = False
            for table in self.tables:
                success = table.assign_seat(name)
                if success: 
                    seated = True
                    break
            if not seated:
                return False
        return True
    
         
    def display(self):
        """
        Function will display the seating arrangement of the OpenSpace . 
        
        It iterates over each table in self.tables and prints a numbered label for each table.

        Then for each table, it loops through the seats and prints the occupant of each seat. 
        """
        count = 1
        for table in self.tables:
            print("Table :", count)
            for seat in table.seats:
                print(seat.occupant)
            print()
            count += 1

    

    def __str__(self):
        """
        Method that returns a full string representation of the openspace.
        
        We loop through each table in the list self.tables and build a string that includes the table number and the occupants.
        
        For each table, str(table) converts the table into a string by calling __str__ method of the table class,
        which includes its seats and occupants.
        
        The final result is a formatted string showing all tables and their assigned seats.
        """
        count = 1
        result = ""
        for table in self.tables:
            result += f"Table {count}\n"
            result += str(table) + "\n"
            count += 1
        return result
    
    def store(self, filename):
        """
        Fucntion will write the seating arrangement of the OpenSpace to a file.
        
        It opens the given filename in write mode and writes string representation of 
        the OpenSpace using str(self).
        """
        with open(filename,"w") as file:
            file.write(str(self))

