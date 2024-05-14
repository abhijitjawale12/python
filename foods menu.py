

#FOOD MENU

data = input("which type of food you r looking for veg/non_veg:")
if data =="VEG":
        veg=input("which type of food u are looking for:")
        if veg =="sandwich":
            print("sandwich\n pavbhaji\n paneer masala\n paneer Tikka\n :")
        food = input("select any one menu to see detail:")
        if food == "pavbhaji":
            print(""" price:60rs\n extra pav:4rs Hotel GREEN LEAF (ulhasnagar)""")
        elif food =="Paneer Masala":
            print("price full:180rs \n half:90rs\n Hotel GREEN LEAF (ulhasnagar)")
        if food == "sandwich":
            print('price:100rs\n Hotel GREEN LEAF (ulhasnagar)')


if data== "NON_VEG":
    non_veg =input("which type of food u are looking for:")
    if veg =="chicken boneless biryani":
        print("chicken boneless biryani\n chicken sukha\n  :")
    food = input("select any one menu to see detail:")
    if food == "chicken boneless biryani":
        print(""" price:280rs\n half:140rs Hotel GREEN LEAF (ulhasnagar)""")
    if food == "chicken sukha":
        print(""" price:150rs (full)\n  half:75rs Hotel GREEN LEAF (ulhasnagar)""")
        
        
