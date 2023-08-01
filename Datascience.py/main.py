import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# a = pd.Series(range(1,10))
# b = pd.Series(["I","would","like","use","python","and","pandas","for","data"],index=range(0,9))
# print(a,b)

start_date = "January,1, 2020"
end_date = "December, 31, 2020"
rang= pd.date_range(start_date,end_date)  # return a range with evenly separated times
print(f"Length is {len(rang)}.")

items_sold=pd.Series(np.random.randint(20,25,size=len(rang)),index=rang)
items_sold.plot(figsize=(8,5))
plt.show()