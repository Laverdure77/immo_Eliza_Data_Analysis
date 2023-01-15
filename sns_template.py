import seaborn as sns
import matplotlib.pyplot as plt

# Style seaborn
sns.set_style("darkgrid")   # background

sns.set_context("talk")     # Bold scale, change scale

sns.set_palette(["#39A7D0","#36ADA4"])  # Custom color palette


# Graph

g = sns.catplot()   # FacetGrid (relplot and catplot)
type_of_g = type(g)
g.fig.suptitle("New Title", y=1.03) #FacetGrid
g.set_title("Average MPG Over Time") #AxesSubplot
g.set_titles("this is {col_name}")


g.set(xlabel="title",
    ylabel="title")
plt.xticks(rotation=90) #Facet and axis labels graphs


plt.show()