import pandas as pd
import numpy as np
data=pd.read_csv("chilla_data_2.csv")
# print(data)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="ticks",color_codes=True)
#Lineplot
plt.figure(figsize=(12,8))
sns.lineplot(x="Age",y="Qualification_completed",hue="field_of_study",data=data,palette="pastel")
plt.title("Python_chilla_Data_Vis_2_CSV",size=20,weight="bold") #Size for fonnt amd weight for bold
plt.show()

#Barplot In barplots both x and y axis must be numberic
plt.figure(figsize=(12,8))
sns.barplot(x="Age", y="Height in cm? Freelancer- (Float)" , hue="Blood group " , data=data ,ci=None)
plt.title("Python_chilla_Data_Vis_2_CSV",size=20,weight="bold") 
plt.show()


# plt.figure(figsize=(12,8))
sns.boxplot(x="Age",y="Your Weight in kg? (float)",data=data,dodge=True,showmeans=True,
meanprops={"marker":"*","markersize":"15" ,"markeredgecolor":"yellow"}) #meanprops are used to change mean style and showmeans toshow the mean of each box
plt.title("Python_chilla_Data_Vis_2_CSV",size=20,weight="bold") 
plt.show()


import plotly.express as px
fig = px.scatter(data, x="Age", y="Your Weight in kg? (float)")
fig.add_hline(y=0.9)
fig.add_vrect(x0=0.9, x1=2)
fig.show()