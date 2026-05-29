class Seat:

    def __init__(self):
        """
        Here, the object Seat is created. 
        self.free refers whether the seat is occupied or not. It is not occupied in the beining, therefore the deaful 
        self.free = True. 
        self.occupant is the parameter where the name of seated person.
        """
        self.free = True
        self.occupant = ""
    
    def set_occupant(self,name):
        """
        Function that will show the person who is sitting. 

        name refers to the occupant's name, who is sitting on the spot. 
        """
        if self.free:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        """"
        Function that will remove the occupant and return the seat as free
        """
        previous_occupant = self.occupant
        self.occupant = ""
        self.free = True
        return previous_occupant
    
    def __str__(self):
        """
        To show that when the seat is taken, it shows who is seated, as a full sentence. 
        """
        return f"{self.occupant} is seated"
    

class Table:
    def __init__(self, capacity = 4):
        """
        Here, the object Table is created. 
        The default of capacity is 4 since there are 4 seats per table in our situation.

        self.seats is a list, so for each seat in the range of 4, we create a loop to add Seat objects in self.seats. 
        """
        self.capacity = capacity
        self.seats = []
        for i in range(capacity):
            self.seats.append(Seat())

    def has_free_spot(self):
        """
        Function that will perform to check whether there is a free spot in a table.
        We start from the loop for each seat in the list self.seats. If the Seat object in self.seats is Ture, 
        it refers that there is at least one free spot in the table" 
        """
        for seat in self.seats:
            if seat.free:
                return True    
        return False 

    def assign_seat(self, name):
        """
        Function that will perform to add the name of the person in the table. 
        We start from the loop for each seat in the list self.seats. If the seat is free, 
        we assign a person to a free seat in a table.
        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False  

    def left_capacity(self):
        """
        Function that will count how many free spots are left in the table. 
        The default of left_seats is started from 0. We start from the loop for each seat in the list self.seats. If the seat is free, 
        we add +1 to left_seats. The maximum value depends on the table capacity. 
        """
        left_seats = 0
        for seat in self.seats:
            if seat.free:
                left_seats += 1 
        return left_seats
    
    def __str__(self):
        """
        c
        """
        result = ""
        for seat in self.seats:
            result += str(seat) + "\n"
        return result
    

seat = Seat()
seat.set_occupant("Nick")

print(seat.occupant)
print(seat)

my_table = Table()

# has_free_spot() 
print("Empty spot？", my_table.has_free_spot())

# test left_capacity()
print("How many free spots?？", my_table.left_capacity())

# assign names
my_table.assign_seat("Anna")
my_table.assign_seat("Dan")
my_table.assign_seat("Gaetan")

# testing again
print("How many free spots？", my_table.left_capacity())  
print("Still have empty spot？", my_table.has_free_spot())  

# adding extra name
my_table.assign_seat("Guillermo")

# full seats
print("Still have empty spot？", my_table.has_free_spot())  
print("How many free spots？", my_table.left_capacity())  #

# trying to add one more person
result = my_table.assign_seat("Gunay")
print("Able to add？", result)  

print(my_table)
