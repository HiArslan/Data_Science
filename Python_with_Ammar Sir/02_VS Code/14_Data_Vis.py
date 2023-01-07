import matplotlib.pyplot as plt
#Steps involved in data visualization
# Step-1 Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Step-2 set a theme
sns.set_theme(style="ticks",color_codes=True)

# Step-3 Import data set we can also import our own data
kashti = sns.load_dataset("titanic")
# print(kashti) #To print whole data of titanic
 
# Step-4 Plot basic graph with 1variable (Countplt)
# p= sns.countplot(x="sex" , data=kashti)
# plt.show()

# Step-5 Plot basic graph with two variables (Countplt) Hue=color in python
p= sns.countplot(x="sex" , data=kashti , hue="class")
plt.show()

# Step-6 Plot basic graph with two variables with titles (Countplt) Hue=color in python 
p= sns.countplot(x="sex" , data=kashti , hue="class")
p.set_title("Baba Ammar ka Countplot for kashti")
plt.show()

