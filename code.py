from datetime import datetime


class Item:
    def __init__(self, name, price_per_unit):
        self.name = name
        self.price_per_unit = price_per_unit


class Supermarket:
    def __init__(self, name):
        self.name = name
        self.items = {
            'rice': Item ( 'rice', 30 ),
            'sugar': Item ( 'sugar', 40 ),
            'salt': Item ( 'salt', 10 ),
            'oil': Item ( 'oil', 100 ),
            'panner': Item ( 'panner', 200 )
        }
        self.cart = []

    def display_items(self):
        print ( "\nAvailable items:" )
        for item_name, item in self.items.items ():
            print ( f"{item.name:6} rs {item.price_per_unit}/kg or liter" )

    def add_to_cart(self, item_name, quantity):
        if item_name in self.items:
            item = self.items[item_name]
            self.cart.append ( (item, quantity) )
        else:
            print ( f"Sorry, {item_name} is not available." )

    def calculate_total(self):
        total = sum ( item.price_per_unit * quantity for item, quantity in self.cart )
        gst = total * 0.05
        final_amount = total + gst
        return total, gst, final_amount

    def generate_bill(self, customer_name):
        if not self.cart:
            print ( "No items in the cart to generate a bill." )
            return

        total, gst, final_amount = self.calculate_total ()
        print ( "\n" + "*" * 30 + " Supermarket " + "*" * 30 )
        print ( "*" * 32 + " Bill " + "*" * 32 )
        print ( f"Name: {customer_name} " + "-" * 30 + f" Date: {datetime.now ()}" )
        print ( "-" * 80 )
        print ( f"{'sno':<10}{'items':<10}{'quantity':<10}{'price':<10}" )
        for i, (item, quantity) in enumerate ( self.cart, start=1 ):
            price = item.price_per_unit * quantity
            print ( f"{i:<10}{item.name:<10}{quantity:<10}{price:<10}" )
        print ( "-" * 80 )
        print ( f"{'TotalAmount:':<70} Rs {total}" )
        print ( f"{'gst amount':<70} Rs {gst}" )
        print ( f"{'final amount':<70} Rs {final_amount}" )
        print ( "-" * 80 )
        print ( " " * 50 + "Thanks for visiting" )
        print ( "-" * 80 )


def main():
    name = input ( ">Enter your name: " )
    supermarket = Supermarket ( name )

    option = int ( input ( "For list of items press 1: " ) )
    if option == 1:
        supermarket.display_items ()

    while True:
        inp1 = int ( input ( "If you want to buy press 1 or 2 for exit: " ) )
        if inp1 == 2:
            break
        if inp1 == 1:
            item_name = input ( "Enter your item: " ).strip ().lower ()
            quantity = int ( input ( "Enter quantity: " ) )
            supermarket.add_to_cart ( item_name, quantity )
        else:
            print ( "You entered wrong number" )

    inp = input ( "Can I bill the items (yes or no): " ).strip ().lower ()
    if inp == "yes":
        supermarket.generate_bill ( name )


if __name__ == "__main__":
