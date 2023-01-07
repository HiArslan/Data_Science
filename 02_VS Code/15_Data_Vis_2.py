import seaborn as sns
import matplotlib.pyplot as plt
from seaborn.rcmod import set_theme
sns.set_theme(style="ticks",color_codes=True)
data_set=sns.load_dataset("titanic")
# print(data_set)

#Lineplot
# plt.figure(figsize=(15,10))
# sns.lineplot(x="survived",y="fare",hue="class",data=data_set)
# plt.xlim(0.5)
# plt.title("Titanic survived people graph against their fare",size=20,weight="bold")
# plt.show()

#Barplot
# plt.figure(figsize=(15,10))
sns.barplot(x="sex",y="survived",hue="embark_town",data=data_set,ci=True)
plt.xlim(0.5)
plt.title("Titanic survived people graph against their sex",size=20,weight="bold")
plt.show() 


