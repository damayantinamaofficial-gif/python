prices = [100,678,1200,300,1000]

out = [price*10 for price in prices]
outwithcond = [price*10 for price in prices if price > 1000]
print(out,outwithcond)