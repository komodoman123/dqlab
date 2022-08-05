import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ast
from PIL import Image

st.title("Hollywood's most profitable stories")

st.header("Introduction")
st.write("Saya merasa heran karena selama ini Hollywood menilai atau menyiarkan kesuksesan sebuah film dengan pendapatan kotor. "
"Bagaimana dengan Profitabilitas, atau % dari anggaran yang dipulihkan? "
"Terutama di Amerika, di mana setiap film memiliki biaya marketing tidak yang kalah tinggi dengan biaya produksi."
" Jika kita menggunakan profitabilitas sebagai indeks, hasil yang ditunjukkan sangat berbeda." 
"Contoh pada 2007, misalnya, di mana film terlaris pada tahun tersebut adalah Pirates Of The Caribbean: At Worlds End." )
image = Image.open("imgs/poc_awe.jpg")
st.image(image)
st.write("Dengan keuntungan sebesar 9.6 milliar dollar yang ternyata hanya memulihkan 320% dari budget sebesar 300 juta dollar." 
" Tapi jika dilihat dari profitability, untuk film tahun 2007, manakah yang paling menguntungkan, bisakah anda menebak: ")

st.header("Most profitable on 2007")
col1,col2,col3=st.columns(3)

with col1:
	st.write("Spiderman 3")
	image = Image.open("imgs/sp3.jpg")
	st.image(image)
	tombol1=st.button("pilih spiderman 3")
	if tombol1==True:
	 st.write('Salah, ROI dari spiderman 3 adalah 300%')
	else:
	 st.write('')
with col2:
	st.markdown("Shrek the third")
	image = Image.open("imgs/shrek.jpg")
	st.image(image)
	tombol2=st.button("pilih Shrek the third")
	if tombol2==True:
	 st.write('Salah, ROI dari shrek the third adalah 500%')
	else:
	 st.write('')
with col3:
	st.write("Paranormal Activity")
	image = Image.open("imgs/pa.jpg")
	st.image(image)
	tombol3=st.button("pilih Paranormal Activity")
	if tombol3==True:
	 st.write('Betul, Paranormal Activity memiliki ROI sebesar 42000%')
	else:
	 st.write('')






st.header("Film dengan budget dan revenue tertinggi")
df=pd.read_csv('movies.csv')
top=df[['title','budget','revenue']]
top_budget=top.sort_values(by=['budget'],ascending=False)
s=top_budget.head(20)
s.head()
#st.dataframe(s)


s["budget"] = pd.to_numeric(s["budget"])
fig2, ax2 = plt.subplots(figsize = (10,10))
sns.set_color_codes('muted')
sns.barplot(x = 'revenue', y = 'title', data = s,
            label = 'revenue', color = 'b', edgecolor = 'w',ax=ax2)
sns.set_color_codes('bright')
sns.barplot(x = 'budget', y = 'title', data = s,
            label = 'Budget', color = 'y', edgecolor = 'w',ax=ax2)
ax2.set(xlabel='jumlah(miliar $)',title='Budget tertinggi')
ax2.legend(ncol = 2, loc = 'lower right')
sns.despine(left = True, bottom = True)
st.pyplot(fig2)

st.write("Film dengan budget tertinggi pada dataset ini merupakan Pirates of the Carribean: on Stranger Tides, yang membutuhkan 380 juta us dolla untuk diproduksi," 
" tapi biaya tersebut terbayarkan, karena film tersebut mendapatkan 1 miliar us dollar. di sisi lain The Lone Ranger mendapatkan 90 juta dollar dari biaya produksi sebesar 255 juta dollar."
" Sehingga budget besar tidak selalu berarti pendapatan besar. Film mana yang memiliki revenue paling tinggi?") 


top_revenue=top.sort_values(by=['revenue'],ascending=False)
r=top_revenue.head(20)
#st.dataframe(r)
fig3, ax3 = plt.subplots(figsize = (10,10))
sns.set_color_codes('muted')
sns.barplot(x = 'revenue', y = 'title', data = r,
            label = 'revenue', color = 'b', edgecolor = 'w',ax=ax3)
sns.set_color_codes('bright')
sns.barplot(x = 'budget', y = 'title', data = r,
            label = 'Budget', color = 'y', edgecolor = 'w',ax=ax3)
ax3.set(xlabel='jumlah(miliar $)',title='Revenue tertinggi')
ax3.legend(ncol = 2, loc = 'lower right')
sns.despine(left = True, bottom = True)
st.pyplot(fig3)

st.write("Film dengan reveue paling tinggi merupakan Avatar sebesar 2.8 miliar dolar. Jika dilihat hanya ada sedikit persimpangan diantara kedua chart diatas, budget yang tinggi tidak selalu berarti revenue yang tinggi")

st.header('Return on Investment (ROI)')
st.write("Berikut merupakan film dengan ROI(revenue/budget)tertinggi pada dataset.")

top1=df[['title','budget','revenue','prof']]
top_prob=top1.sort_values(by=['prof'],ascending=False)
p=top_prob.head(20)
st.dataframe(p)
fig4, ax4 = plt.subplots(figsize = (10,10))
sns.set_color_codes('muted')
sns.barplot(x = 'prof', y = 'title', data = p,
            label = 'profitability', color = 'b', edgecolor = 'w',ax=ax4)
ax4.set(xlabel='Persen',title='ROI tertinggi')
ax4.legend(ncol = 2, loc = 'lower right')
sns.despine(left = True, bottom = True)
st.pyplot(fig4)

st.write("The Blair Witch Project menempati posisi pertama, perlu diperhatikan juga beberapa film pada chart ini merupakan film horror, sepertinya film horror tidak mahal untuk dibuat dan terkadang menjadi cult classic dan memiliki banyak penggemar")

def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L
df['genres'] = df['genres'].apply(convert)
#=======================================================================
st.header("Genre")
st.write("Rata-rata revenue berdasarkan genre")
image = Image.open("imgs/p3.png")
st.image(image)
st.write("Rata-rata budget berdasarkan genre")
image = Image.open("imgs/p2.png")
st.image(image)
st.write("Rata-rata ROI berdasarkan genre")
image = Image.open("imgs/p1.png")
st.image(image)
st.write("ROI memang cukup tinggi untuk horror namun genre tersebut bukan genre safe yang mungkin ditunjukkan oleh rata-rata, dikarenakan oleh outlier seperti blair witch")
st.write("Secara umum, film yang menghasilkan revenue terbesar adalah film dengan budget yang signifikan, tetapi umumnya bukan yang paling banyak menghasilkan ROI. ")
st.write("Namun outlier seperti The Blair Witch Project bisa melawan tren dan menunjukkan bahwa film dengan budget yang lebih rendah dapat sukses besar dalam situasi yang tepat, sementara The Lone Ranger menunjukkan bahwa film dengan budget yang lebih tinggi masih bisa gagal.")









