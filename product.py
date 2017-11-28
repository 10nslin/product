class Products(object):
    def  __init__(self, price, item_name, weight, brand, status = "for sale" ):
        self.price = price      
        self.item_name = item_name
        self.weight = weight
        self.brand = brand      
        self.status = status 
        self.tax = .06

  
    def sell(self):
        self.status = "Sold"
        return self
   
    def productReturn(self):
      
        if self.status == "Defective":
            self.price = 0
        elif self.status == "like new":
            self.status = "For Sale"
        elif self.status == "open box":
            self.status = "Used"
            self.price -=  self.price * .20
        return self

    def display_all(self):
        print 'Price: $',self.price
        print 'Item Name:',self.item_name 
        print 'Weight:',self.weight,"lbs"
        print 'Brand:',self.brand 
        print 'Total Amount: ${:,.2f}'.format(self.price + self.price * self.tax)
        print 'Status',self.status
        print ''
        return self

product1= Products(20, "Book", 5, 'Coding')
product1.sell().display_all()

product2= Products(35, "Pocket Knife", 2.1, 'Swiss', "open box")
product2.productReturn().display_all()

product3= Products(45, "Video Game", 2.1, 'Xbox', "defective")
product3.productReturn().display_all()

product4= Products(45, "Video Game", 2.1, 'Xbox', "like new")
product4.productReturn().display_all()

