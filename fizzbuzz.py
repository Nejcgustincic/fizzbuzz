izbrana_stevilka= int (raw_input("izberi stevilko do  100 "))

for i in range (1, izbrana_stevilka):

    if i % 3 == 0 and i % 5 == 0:
        print ("fizz buzz")
    elif i % 5 == 0:
        print ("buzz")
    elif i % 3 == 0:
        print ("fizz")
    else:
        print i
