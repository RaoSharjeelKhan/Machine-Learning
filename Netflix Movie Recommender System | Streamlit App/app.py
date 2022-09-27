import numpy as np
import pandas as pd
import streamlit as st
import pickle

st.markdown(
   f"""
   <style>
    .stApp {{
             background: url("https://images.unsplash.com/photo-1606937295547-bc0f668595b3");
             background-size: cover
         }}
    </style>
         """,
         unsafe_allow_html=True
     )


st.title('Movie Recommender System')
df=pd.read_csv('DataFrame.csv')
selected_movie_name = st.selectbox(
    "",
    df['title'].values
)

cos_sim=pickle.load(open('similarity.pkl','rb'))


	

df['lower']=df['title'].apply(lambda x: x.lower())
titles_list =df['lower'].tolist()
Slct=selected_movie_name.lower()
index_of_the_movie = df.index[df.lower == Slct].tolist()
idx=index_of_the_movie[0]
sim_mov= list(enumerate(cos_sim[idx]))
#Sort the movies in descending order
similar_movies = sorted(sim_mov, key = lambda x:x[1], reverse = True) 

#Displaying the Similar Movies

print(" Top Ten Recommended movies \n")

i = 1
recommended_movies=[]
for mov in similar_movies:
  index = mov[0]
  title = df[df.index==index]['title'].values[0]
  movies=[]
  if (i<11):
    recommended_movies.append(title)   
    i+=1
Dic={'RECOMMENDED MOVIES':recommended_movies}
D=pd.DataFrame(Dic)
if st.button('Recommend'):
    st.dataframe(D,height=400,width=900)
	#st.text_area(label="RECOMMENDED MOVIES:", value=D, height=350)

