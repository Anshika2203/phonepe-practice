class PaymentGateway:
    def __init__(self):
        self.clients={}
        self.paymodes={}
        self.traffic_distribution={}

    def addClient(self, client_id):
        if client_id not in self.clients:
            self.clients[client_id] = {"paymodes": set()}
            print("Client added.")
        else:
            print("Client already exists.")

    def removeClient(self, client_id):
        if client_id in self.clients:
            del self.clients[client_id]
            print("Client Deleted.")
        else:
            print("Client does not exists.")
    
    def hasClient(self, client_id):
        return client_id in self.clients
    
    def listSupportedPaymodes(self, client_id=None):
        if client_id:
            if client_id in self.clients:
                return self.clients[client_id]["paymodes"]
            else:
                print("Client does not exist.")
        return self.paymodes
    
    def addSupportForPaymode(self, paymode, client_id=None):
        if client_id:
            if client_id in self.clients:
                self.clients[client_id]["paymodes"].add(paymode)
                print("Paymode added for client.")
            else:
                print("Client does not exist.")
        else:
            self.paymodes[paymode]=[]
            print("Paymode added globally.")

    def removePaymode(self, paymode, client_id=None):
        if client_id:
            if client_id in self.clients and paymode in self.clients[client_id]["paymodes"]:
                self.clients[client_id]["paymodes"].remove(paymode)
                print("Paymode removed for client.")
            else:
                print("Client or paymode does not exist.")
        else:
            if paymode in self.paymodes:
                del self.paymodes[paymode]
                print("Paymode removed globally.")
            else:
                print("Paymode does not exist.")
        
    def showDistribution(self):
        return self.traffic_distribution
    
    def makePayment(self, client_id, paymode, amount, bank):
        if client_id in self.clients and paymode in self.clients[client_id]["paymodes"]:
            print(f"Payment of {amount} processed for client '{client_id}' using {paymode} through bank '{paymode}'.")
        else:
            print("Payment failed. Either client or paymode is not suported.")

    def setTrafficDistribution(self, bank, percentage):
        self.traffic_distribution[bank]=percentage
        print(f"Traffic distribution for bank '{bank}' set to {percentage}%.")

    def switchTraffic(self, bank, new_percentage):
        if bank in self.traffic_distribution:
            self.traffic_distribution[bank]=new_percentage
            print(f"Traffic for bank '{bank}' update to {new_percentage}%.")
        else:
            print("Bank not found in distribution")    

pg=PaymentGateway()

pg.addClient("Flipkart")
pg.addClient("Amazon")

pg.addSupportForPaymode("UPI")
pg.addSupportForPaymode("Credit")

pg.addSupportForPaymode("Netbanking", "Flipkart")

pg.setTrafficDistribution("HDFC", 70)
pg.setTrafficDistribution("ICICI", 30)

pg.makePayment("Flipkart", "Netbanking", 1000, "HDFC")

print(pg.showDistribution())

pg.switchTraffic("HDFC", 50)