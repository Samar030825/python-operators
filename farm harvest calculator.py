field1 = 120
field2 = 85
field3 = 150
field4 =  95
field5 = 110

total = field1 + field2 + field3 + field4 + field5
average = total/5

print("total harvest:" , total)
print("average:", average )

price_per_kg = 15
earnings = total * price_per_kg
print("total earnings: Rs" , earnings )

bags = total//25
leftover = total%25

print("Full bags packed :", bags)
print("leftover bags :" , leftover , "kg")

last_year = 500
print("Better than last year ? : " , total>last_year)
print("Same as the last year ? :" , total == last_year)
print("Atleast as good as last year ?:" , total>=last_year)

total += 30
print("After bonus crop", total , "Kg")

total -= 15
print("After seed reserve", total , "Kg")

bags = total//5
print("Final bags packed:", bags)
