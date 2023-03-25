from matplotlib import pyplot as plt

# User prompts for the graph
print("Please input the $ amount for sales of each month")

jan_amt = float(input("January: "))
feb_amt = float(input("February: "))
mar_amt = float(input("March: "))
apr_amt = float(input("April: "))
may_amt = float(input("May: "))
jun_amt = float(input("June: "))
jul_amt = float(input("July: "))
aug_amt = float(input("August: "))
sep_amt = float(input("September: "))
oct_amt = float(input("October: "))
nov_amt = float(input("November: "))
dec_amt = float(input("December: "))

# Define lists to be used for x-axis and y-axis
monthlist = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
amtlist = [jan_amt, feb_amt, may_amt, apr_amt, may_amt, jun_amt, jul_amt, aug_amt, sep_amt, oct_amt, nov_amt, dec_amt]


# Graph processing
x = monthlist
y = amtlist
plt.plot(x, y)
plt.title("Yearly Sales Trend")
plt.xlabel("Month")
plt.ylabel("$ Amount")
plt.show()

