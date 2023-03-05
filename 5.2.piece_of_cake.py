def get_recipe_price(prices,optionals=None,**amount):
    sum=0
    if optionals==None:
        optionals=[]
    for i in prices:
        if i not in optionals:
            sum+=prices[i]*amount[i]/100
    return sum

print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(get_recipe_price({}))