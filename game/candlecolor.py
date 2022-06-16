from .price import price
from datetime import datetime
import time


p1 = float(price)
time.sleep(10)
from .price2 import price2
p2 = float(price2)
p3 = float( p1 - p2)

if p3 > 0 :
    candlecolor = 'red'
elif p3 < 0 :
    candlecolor = 'green'
        
elif p3 == 0 :
    candlecolor = 'green'

    
 