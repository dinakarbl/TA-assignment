# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




b = float(input("Enter your budget : "))
s = b
# dictionary to store product name, quantity, price with empty list as their values
a ={"pname":[], "quantity":[], "price":[]}

# converting dictionary to list
x = list(a.values())

# variable na value of "pname" from dictionary 'a'
n = x[0]

# variable qu value of "quantity" from dictionary 'a'
q = x[1]

# variable pr value of "price" from dictionary 'a'
p = x[2]


while True:
    ch = int(input("1.ADD\n2.EXIT\nEnter your choice : "))
        # check the budget is greater than zero and option selected
        # by user is 1 i.e. to add an item
    if ch == 1 and s>0:
        #input product name
        pn = input("Enter product name : ")
        # input quantity of product
        qu = input("Enter quantity : ")
        # input price of the product
        pr = float(input("Enter price of the product : "))

        if pr>s:
                # checks if price is less than budget
            print("\nBudget limit exceeded")
            continue

        else:
            # checks if product name already in list
            if pn in n:
                # find the index of that product
                i = n.index(pn)

                    # remove quantity from "quantity" index of the product
                q.remove(qu[i])

                    # remove price from "price" index of the product
                p.remove(p[i])

                    # insert new value given by user earlier
                q.insert(i, qu)

                    # insert new value given by user earlier
                p.insert(ind, pr)

                # subtracting the price from the budget and assign

                s = b-sum(p)

                print("\namount left", s)
            else:
                    # append value of in "pname", "quantity", "price"
                n.append(pn)
                q.append(qu)
                p.append(pr)

                    # after appending new value the sum in price
                    # as to be calculated
                s = b-sum(p)

                print("\namount left", s)

        # if budget goes zero print "NO BUDGET"
    elif s<= 0:
        print("\nNO BUDGET")
        break;
    else:
        break

# will print amount left in variable 's'
print("\nAmount left : Rs.", s)

# if the amount left equals to any amount in price list
for i in range(len(p)):
    if(p[i]<s):
        # then printing the name of the product which can buy
        print("\nWith amount left you can buy :", n[p.index(s)],",")

print("\n\n\nGROCERY LIST")
print("Product name\tQuantity\tPrice")

# print final grocery list
for i in range(len(n)):
    print("\t\t",n[i],"\t\t", q[i],"\t\t\t", p[i])


# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
