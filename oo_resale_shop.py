from typing import Dict, Union, Optional

class ResaleShop: 
    def __init__(self): #Create an inventory of computer objects for the shop
        self. inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
        itemID = 0

    def buy(self,computer: Dict[str, Union[str, int, bool]]): # Add computer to inventory
        global itemID
        itemID += 1 # increment itemID
        self.inventory[itemID] = computer #add computer to inventory
        return itemID
    
    def sell(self,item_id: int): #Remove computer from inventory
        if item_id in self.inventory: #find computer in inventory
            del self.inventory[item_id] #remove from inventory
            print("Item", self.item_id, "sold!")
        else: #if item id is invalid
            print("Item", self.item_id, "not found. Please select another item to sell.")
    
    def print_inventory(self): #Print a list of items in inventory
    # If the inventory is not empty
      if self.inventory:
        # For each item
         for item_id in self.inventory:
            # Print its details
             print(f'Item ID: {self.tem_id} : {self.inventory[self.item_id]}')
      else: #when there are no items in inventory 
        print("No inventory to display.")
    
    def refurbish(self,item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory: #if item can be found
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None: #if value is given for os update
                computer["operating_system"] = new_os # update details after installing new OS
        else: #when item id is invalid
            print("Item", item_id, "not found. Please select another item to refurbish.")