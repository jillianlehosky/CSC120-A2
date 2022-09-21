class Computer: # Construct a Computer object
    def __init__(self,description, processor_type,hd_capacity,memory,os,
    year_made, price): # create a computer instance and store information about that computer
        self.description = description
        self.processor_type = processor_type
        self.hd_capacity = hd_capacity
        self.memory = memory
        self.os = os
        self.year_made = year_made
        self.price = price 
# I'm choosing to do keep all of my methods within the ResaleShop class. The only method here is a constructor.
    