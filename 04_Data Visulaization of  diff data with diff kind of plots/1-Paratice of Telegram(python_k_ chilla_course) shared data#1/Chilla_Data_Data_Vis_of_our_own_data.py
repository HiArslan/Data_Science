# Step-1 Import libraraies
import pandas as pd
# Step-2 Import data from file
chilla = pd.read_csv("data_chilla.csv")
# print(chilla) #There must not be any spaces in data 

# Step-3 Import libraraies
import matplotlib.pyplot as plt
import seaborn as sns

# Step-4 Set theme
sns.set_theme(style="ticks",color_codes=True)

# Step-5 Import data
chilla = pd.read_csv("data_chilla.csv")

# Step-6 plot of two variables with title

sns.countplot(x="Gender" , hue="Age" , data=chilla )
plt.title("Age of People who are doing chilla course")
plt.show() 

# Step-7 plot of one variable (In countplot we can only use one axis either x or y with hue)

sns.countplot(x="Location", data=chilla)
plt.title("Age of People who are doing chilla course")
plt.show()



