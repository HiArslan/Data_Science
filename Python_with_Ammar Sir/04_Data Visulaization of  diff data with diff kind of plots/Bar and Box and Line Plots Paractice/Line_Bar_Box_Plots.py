# Import libraries and read data through csv
import pandas as pd
mydata=pd.read_csv("data_chilla.csv")
# print(mydata)

# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="ticks",color_codes=True)

# Import data
mydata=pd.read_csv("data_chilla.csv")
# Line_Plot
# sns.lineplot(x="Age", y="Duration_(min)", hue="Location" , data=mydata)
# plt.title("Line Plot of chilla_csv_file")
# plt.show()

sns.barplot(x="Gender" , y="Duration_(min)", hue="Location" , data=mydata , ci=True , order=(["Female","Male"]) , color="#c203fc" , palette="pastel")
plt.show()





