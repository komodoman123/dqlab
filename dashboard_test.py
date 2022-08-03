import streamlit as st
import lorem
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from numerize.numerize import numerize

st.set_page_config(layout="wide")
st.write("ayy lmao")

"AAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH"


st.markdown("yeeeehaw")
st.markdown("------------")

st.title("The title")
st.subheader("The subheader")
st.write("uhhhhhhhhhhhhhhhhhhhhhhh")

st.code("import streamlit as st")
st.write(lorem.paragraph())

df=pd.read_csv('store.csv')
st.dataframe(df)
#df[['Orderdate', 'Sales']].set_index
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')

st.title("aie")
st.dataframe(df)
df


st.metric("Total Sales", 1000,10)

st.metric("Total Profit", "$ 10M","-2.3%")

st.title("Charting")

freq=st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'))

sales=df[['Order Date', 'Sales']].set_index('Order Date').resample(freq).sum()

met1,met2,met3 = st.columns(3)
with met1:
	st.metric(
		"Total Sales", numerize.numerize(df['Sales'].sum())
		)
with met2:
	st.metric("Total Order", df['Order ID'].nunique())
with met3:
	st.metric("Number of Customers", df['Customer ID'].nunique)

cap1,cht1=st.columns([1,4])
with cap1:
	st.write(lorem.paragraph())

with cht1:
	st.line_chart(
		sales
	)

fig1,ax1=plt.subplots(figsize=(10,10))
sns.scatterplot(
	data=df,
	x='Sales',
	y='Profit',
	ax=ax1
	)
st.pyplot(fig1)

st.title("Input")
tombol1=st.button("tekan tombol")
st.write(tombol1)

jurusan=st.selectbox(
	"Pilih jurusan kamu",
	("Mat", "Fis", "Kim")
)
st.write("Kamu memilih: ", jurusan)

st.title("Image")
img=Image.open("1641979644627.png")
st.image(img, caption="the fellowship of bengis")

st.title("Kolom")
col1,col2,col3=st.columns(3)

with col1:
	st.write(lorem.paragraph())
with col2:
	st.write(lorem.paragraph())
with col3:
	st.write(lorem.paragraph())

