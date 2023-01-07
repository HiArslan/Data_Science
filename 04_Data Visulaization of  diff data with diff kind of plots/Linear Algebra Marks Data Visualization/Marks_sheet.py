import pandas as pd
marks_sheet = pd.read_csv("Pdf.csv")
# print(marks_sheet)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks", color_codes=True)
marks_sheet = pd.read_csv("Pdf.csv")
#Countplot
sns.countplot(x="Quiz_1",hue="Quiz_2",data=marks_sheet,color="salmon",
palette="pastel")
plt.show()

#Barplt
sns.barplot(x="Quiz_1",y="Quiz_2",data=marks_sheet,color="salmon",
palette="pastel" , ci=None)
plt.show()

#Boxplot
sns.boxplot(x="Quiz_1",y="Quiz_2",data=marks_sheet,color="salmon",
palette="pastel",dodge=True)
plt.show()
