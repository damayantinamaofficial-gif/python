from .price import cal_total
from .inventory import check_stock

print(cal_total(1000,3))
print(check_stock(6))
print(check_stock(-6))