
import streamlit as st
import streamlit.components.v1 as stc


import pandas as pd

HTML_BANNER = """
    <div style="background-color:#489e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Classic/Oldies 90s Movie Directory App </h1>
    </div>
    """


def main():


    menu = ["Home", "Search", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    stc.html(HTML_BANNER)

    df = pd.read_csv("classicmoviedictionary.csv")

    del df['sno']

    #Change Year to Datetime
    df['year'] = pd.to_datetime(df['year'])

    if choice == 'Home':
        st.subheader("Home")



        movies_title_list = df['title'].tolist()

        movie_choice = st.selectbox("Movie Title", movies_title_list)
        with st.expander('Movies DF', expanded=False):
            st.dataframe(df.head(10))

            # Filter
            img_link = df[df['title'] == movie_choice]['img_link'].values[0]
            title = df[df['title'] == movie_choice]['title'].values
            genre = df[df['title'] == movie_choice]['genres'].values


        c1, c2, c3 = st.columns([1, 2, 1])

        with c1:
            with st.expander("Title"):
                st.success(title)

        with c2:
            with st.expander("Image"):
                st.image(img_link, use_column_width=True)

        with c3:
            with st.expander("Genre"):
                st.write(genre)





    elif choice == "Search":
        st.subheader("Search Movies")

        with st.expander("Search By Year"):
            movie_year = st.number_input("Year", 1900, 2000)

            df_for_year = df[df['year'].dt.year == movie_year]
            st.dataframe(df_for_year)

        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            with st.expander("Title"):
                for t in df_for_year['title'].tolist():
                    st.success(t)

        with col2:
            with st.expander("Images"):
                for i in df_for_year['img_link'].tolist():
                    st.image(i, use_column_width=True)

        with col3:
            with st.expander("Genre"):
                for g in df_for_year['genres'].tolist():
                    st.write(g)







    else:
        st.subheader("About")
        st.text("Made By Rakshit Saxena")
        st.text("Cloud Computing, 2021")


if __name__ == '__main__':
    main()



