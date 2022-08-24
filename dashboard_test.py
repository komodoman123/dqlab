import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ast
from PIL import Image

st.title("Hollywood's most profitable stories")

st.header("Introduction")
st.write("Hollywood always grades or broadcasts the success of a film by their gross income." 
	"what if we look at it from the angle of Profitability, or % of Budget Recovered? Especially considering that hollywood film has such high printing and advertising costs,"
	"If you use Profitability as an index, it changes the view considerably." 
	"Take 2007, for example, where the biggest grossing film was Pirates Of The Caribbean: At Worlds End." )
image = Image.open("imgs/poc_awe.jpg")
st.image(image)
st.write("with a profit of 960 million dollars which recovered 320% of its budget. But the most profitable film of 2007 by far was…Can you guess? ")

st.header("Most profitable on 2007")
col1,col2,col3=st.columns(3)

with col1:
	st.write("Spiderman 3")
	image = Image.open("imgs/sp3.jpg")
	st.image(image)
	tombol1=st.button("spiderman 3")
	if tombol1==True:
	 st.write('False')
	else:
	 st.write('')
with col2:
	st.markdown("Shrek the third")
	image = Image.open("imgs/shrek.jpg")
	st.image(image)
	tombol2=st.button("Shrek the third")
	if tombol2==True:
	 st.write('False')
	else:
	 st.write('')
with col3:
	st.write("Paranormal Activity")
	image = Image.open("imgs/pa.jpg")
	st.image(image)
	tombol3=st.button("Paranormal Activity")
	if tombol3==True:
	 st.write('True')
	else:
	 st.write('')



st.header("Films with the highest budget and revenue")
df=pd.read_csv('movies.csv')
top=df[['title','budget','revenue']]
top_budget=top.sort_values(by=['budget'],ascending=False)
s=top_budget.head(20)
#s.head()
d2 = s.melt(id_vars="title", var_name="type")

#st.dataframe(d2)
#st.dataframe(df)
figg, axx = plt.subplots(figsize = (10,10))
axx = sns.barplot(x="value", y="title", hue="type", data=d2)
axx.set(ylabel="value", xlabel="Billion ($)")
axx.legend(loc = 'lower right')
st.pyplot(figg)


s["budget"] = pd.to_numeric(s["budget"])

st.write("The highest budget film in the dataset is Pirates of the Caribbean: On Stranger Tides, which cost \$380 million to make. It did pay off, though the film had a revenue of $1 billion from the box office.")
st.write("On the other hand, The Lone Ranger earned a paltry \$90 million revenue from its $255 million dollar budget.")
st.write("Therefore, high budgets don’t always translate to large amounts of money coming in. Which films had the highest revenues?")


top_revenue=top.sort_values(by=['revenue'],ascending=False)
r=top_revenue.head(20)
r2=r.melt(id_vars="title", var_name="type")
#st.dataframe(r)
figg2, axx2 = plt.subplots(figsize = (10,10))
axx2 = sns.barplot(x="value", y="title", hue="type", data=r2)
axx2.set(ylabel="value", xlabel="Billion ($)")
axx2.legend(loc = 'lower right')
st.pyplot(figg2)

st.write("The highest revenue film was Avatar, which made $2.8 billion. Interestingly, there is very little crossover between the two charts; high budgets don’t always translate to high revenues.")

st.header('Return on Investment (ROI)')
st.write("So, high budgets doesn't always give high revenues. Here are the films with the highest return on investment (revenue / budget) in the dataset.")

top1=df[['title','budget','revenue','prof']]
top_prob=top1.sort_values(by=['prof'],ascending=False)
p=top_prob.head(20)
#st.dataframe(p)
fig4, ax4 = plt.subplots(figsize = (10,10))
sns.set_color_codes('muted')
sns.barplot(x = 'prof', y = 'title', data = p,
            label = 'profitability', color = 'b', edgecolor = 'w',ax=ax4)
ax4.set(xlabel='Percentage',title='Highest ROI')
ax4.legend(ncol = 2, loc = 'lower right')
sns.despine(left = True, bottom = True)
st.pyplot(fig4)

st.write("Obviously, the major outlier here is The Blair Witch Project, which made \$250 million off its budget of $60 thousand. It’s worth noting that a number of other films in this list are also horror movies")

def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L
df['genres'] = df['genres'].apply(convert)
#=======================================================================
st.header("Genre")
st.write("Average revenue based on genre")
image = Image.open("imgs/p3.png")
st.image(image)
st.write("Average budget based on genre")
image = Image.open("imgs/p2.png")
st.image(image)
st.write("Average ROI based on genre")
image = Image.open("imgs/p1.png")
st.image(image)
st.write("In general, the films that make the most revenue are the ones with a significant budget, but generally not the most investment. ")
st.write("Yet outliers such as The Blair Witch Project buck the trend and demonstrate that even lower-budget films can be smash hits in the right circumstances, while The Lone Ranger shows that higher-budget films can still flop.")
st.write("Horror is on the top of ROI, and if we refer to the highest ROI chart, most of them are horror movies, it seems that they’re cheap to make and sometimes become cult classics.")
st.write("In fact, one of the production studio, blumhouse productions is adopting this strategy.")
st.write("they threw a few million dollars at each of these movies so they don't even need to have a huge hit for it to be profitable.")
image = Image.open("imgs/blum.png")
st.image(image)
st.write("And sometimes they do get a huge hit, aside from Paranormal Activity for example, blumhouse's insidious series, which im sure everyone is familiar with. Started with only a budget of \$1.5 million has now reached $539.4 million accross 4 movies with a fifth one in the making ")
image = Image.open("imgs/insidious.jpg")
st.image(image)
