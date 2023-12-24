from apyori import apriori
## Data 
market_data = [['T-Shirt','Pants','Jeans','Jersy','Socks','Basketball','Bottle','Shorts'],
 ['T-Shirt','Jeans'],
 ['Jersy','Basketball','Socks','Bottle'],
 ['Jeans','Pants','Bottle'],
 ['Shorts','Basketball','Pants'],
 ['Shorts','Jersy'],
 ['Basketball','T-Shirt'],
 ['Basketball','Jersy'],
 ]
association_rules = apriori(market_data, min_support=0.2, min_confidence=0.2, min_lift=2, max_length=2)
association_results = list(association_rules)
##print(association_results )
for product in association_results:
 #print(product) # ex. RelationRecord(items=frozenset({'Basketball', 'Socks'}), support=0.25, ordered_statistics=[OrderedStatistic(items_base=frozenset({'Basketball'}), items_add=frozenset({'Socks'}), confidence=0.5, lift=2.0), OrderedStatistic(items_base=frozenset({'Socks'}), items_add=frozenset({'Basketball'}), confidence=1.0, lift=2.0)])
 pair = product[0] 
 ##print(pair) ## ex. frozenset({'Basketball', 'Socks'})
 products = [x for x in pair]
 print(products) # ex. ['Basketball', 'Socks']
 print("Rule: " + products[0] + " →" + products[1])
 print("Support: " + str(product[1]))
 print("Confidence: " + str(product[2][0][2]))
 print("Lift: " + str(product[2][1][3]))
 print("==================================")