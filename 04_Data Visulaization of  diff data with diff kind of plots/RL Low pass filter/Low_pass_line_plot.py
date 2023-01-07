from re import X
import pandas as pd
from seaborn.utils import get_color_cycle
output=pd.read_csv("Book1.csv")
# print(output)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="ticks",color_codes=True)


sns.lineplot(x="Freq" , y="Voltages", data=output , color="Blue")
plt.title("RL Low Pass Filter")
plt.show()

