# Profit or Loss
# Take Cost Price and Selling Price and determine profit, loss or no profit
def pol(cp,sp):
    if(cp==sp):
        print("No Profit and No Loss")
    elif(cp>sp):
        print("Loss")
    elif(cp<sp):
        print("Profit")

cp = int(input("Enter the cost price :"))
sp = int(input("Enter the selling price :"))

pol(cp,sp)