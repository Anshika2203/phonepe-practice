class FullfilmentService:
    def __init__(self):
        self.inventory = {}
    
    def addInventory(self, productId, amount):
        if productId in self.inventory:
            self.inventory[productId]+=amount
        else:
            self.inventory[productId]=amount
        return f"Added '{amount}' units of product '{productId}' to the invertory."

    def removeInventory(self, productId):
        if productId not in self.inventory:
            return f"Product '{productId}' not exist in invertory."
        if self.inventory[productId]==0:
            return f"Product '{productId}' is out of stock."
        self.inventory[productId]-=1
        return f"Removed 1 unit of product '{productId}' from the inventory."
    
    def viewInventory(self):
        if not self.inventory:
            return "Inventory is empty."
        views="Inventory view:\n"
        for productId, amount in self.inventory.items():
            views+=f"productId: {productId}, Quantity: {amount}\n"
        return views
    
if __name__=="__main__":
    service=FullfilmentService()

    print(service.addInventory("p1", 10))
    print(service.addInventory("p2", 5))
    print(service.viewInventory())
    print(service.removeInventory("p1"))
    print(service.viewInventory())
    print(service.removeInventory("p3"))
    print(service.removeInventory("p2"))
    print(service.viewInventory())