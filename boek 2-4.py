# Christel van Haren, geschreven op 12-9-2019.
# Boek opdracht 4 'Total Purchase', bladzijde 126.
# Dit programma laat zien wat de totale prijs is en
# wat de btw van die prijs is.

a = "2.56"
b = "3.64"
c = "2.94"
d = "5.94"
e = "8.46"

total = float(a)+float(b)+float(c)+float(d)+float(e)
tax = (total)*0.07

print("De totale prijs is", total)
print("En de btw van die prijs is", tax)
