
#I'm at a restaurant
# if (I want meat)
#    { I order a steak
#        }
#otherwise if(I want pasta)
#      { I order spaghetti & meatballs }
#Otherwise
#   { I order a salad. }

is_male = True
is_tall = False

if is_male and is_tall:
    print("YEP both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not (is_tall) and(is_male):
    print("You aren't short male")
else:
    print("NO")