import pandas as pd
import streamlit as st
import base64

def main():
    characters = pd.read_csv("./data/characters.csv")
    episodes = pd.read_csv("./data/episodes.csv")
    st.title('Simpsons Dataset Analysis')
    st.markdown("<style>body{background-color: yellow;}</style>", unsafe_allow_html=True)
    st.sidebar.markdown("<style>div[role='listbox'] ul{height: 150px;}</style>", unsafe_allow_html=True)
    menu = ["Introduction", "Data", "Networks"]
    choice = st.sidebar.selectbox("Menu", menu)
    st.sidebar.image("./img/homer.png", use_column_width=True)
    if choice == "Introduction":
    
        st.markdown("""
Computational Social Science - DTU 2024
                    
Lluís Llull - s237198    
## Introduction
                

The project is divided into three main parts, which can be switched in the sidebar. The parts are the following: 
- **Introduction**: A brief explanation of the project and the motivation behind it.
- **Data**: This part is focused on a general data analysis of the datasets. It includes the description of the datasets, some stats, and some plots.
- **Network**:The last part is focused on the network analysis and the study of the objectives of the project.

                    
## Motivation
### Why did you choose this project?
The Simpsons dataset excels for my research because it acts as a social mirror. It reflects societal norms and trends through humor, allowing to potentially identify biases and changing perspectives on inclusion (racism, homophobia) over its impressive three-decade run. Plus, the show's popularity makes the analysis engaging and attractive, sparking broader interest in social issues.

### What are the main objectives of the project?

- Network Analysis of the Simpsons
- Community Detection in Springfield
- Influence Propagation in Springfield
- Evolution of the Network, including inclusion and ideology
                    """)


    elif choice == "Data":
        def download_data(df, name):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # Convert dataframe to base64 encoding
            href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download '+name+' Dataset</a>'
            return href
        raw_dataset = pd.read_csv("./data/simpsons_ep-char.csv")
        

        st.markdown("""
        ## Data                    

        ### What is your dataset?

        We have one *raw dataset* (simpsons_ep-char.csv) where we have all the characters that appear in every episode, from that dataset we obtained the two definitive datasets  using techniques of web scrapping to the [*Simpsons Wiki*](https://simpsons.fandom.com/wiki/Simpsons_Wiki)
                            """)
        st.markdown(download_data(raw_dataset, 'Raw'), unsafe_allow_html=True)
       
        
        st.markdown("""
                    ### Episodes
                    ***episodes.csv*** ->  Every episode, with all the characters appearing, season, date of the episode, etc.
                    - *episode_id* -> Id of the episode
                    - *character_id* -> Character appearing in the episode
                    - *season* -> Season of the episode
                    - *year* -> Year of the episode

                    Example of the episodes dataset:
                    """)
        st.markdown(download_data(episodes, 'Episodes'), unsafe_allow_html=True)
        st.write(episodes.head())
        st.markdown("""
                    ### Characters
                    ***characters.csv*** -> All the characters with general information such as name, genre, first_appearance, married, etc,**
                    - *character_id* -> Id of the character
                    - *name* -> Name of the character
                    - *male* -> If True the character is a male, otherwise is a female
                    - *lgbt* -> If True the character is part of the LGTB collective
                    - *married* -> If True the character is married, otherwise is not
                    - *smoker* -> If True the character is a regular smoker, otherwise is not
                    - *first_appearance* -> Id of the first episode where appeared the character
                    - *voice_actor* -> Name of the real actor who puts voice to the character
                    - *num_apperanaces* -> If True the character is a male, otherwise is a Female
                    - *text* -> Short and general description of the character 
                    - *tokens* -> Tf-Idf obtained of the *text*. Applying, tokenization, removing stopwords, and stemming
                    
                    
                    Example of the characters dataset:

                    """)
        st.markdown(download_data(characters, 'Characters'), unsafe_allow_html=True)
        st.write(characters.sample(5))
        st.markdown("""
                    ### Brief Data Analysis
                    Stats of some attributes of the characters:
                    """)
        st.image("./img/data_analysis.png", caption='Data analysis', use_column_width=True)
        st.markdown("""
                    First appearances of the characters over the seasons:
                    """)
        st.image("./img/first_apperances.png", caption='Data analysis', use_column_width=True)
        st.markdown("""
                    Characteristics of the main characters:
                    """)
        st.image("./img/main_characters.png", caption='Main characters', use_column_width=True)

        

    elif choice == "Networks":

        # st.write("This is a simple Streamlit application")
        # season = range(26,1,-1)
        # choice = st.sidebar.selectbox("Season", season)

        st.markdown("""
                     ## Network evolution
                    
                    First of all, it is important to comment on how the networks have been **represented**. The main characters are depicted in light yellow, characters that appear only once are represented in blue, and all other characters are shown in a darker shade of yellow. Additionally, the names of the 10 most connected characters in the network have been listed.
                    
                    If we focus on the image, a priori, it is clearly observed how the **network grows**, one of the most outstanding points being the significant importance acquired by the **main characters** (Homer, Lisa, Marge, Bart and Maggie). Additionally, we can also see how the characters that appear only once (represented in blue) become almost **non-existent** in the last season, while in the first season they can still be visualized. Finally, the differences between more and less **connected characters** are accentuated.                    """)
        st.image("./img/evolution_network.png", caption='Evolution Network', use_column_width=True)
        st.markdown("""
                    Looking in more detail the the **Networks** generated every season, we can see that the network **undergoes expansion with each passing season**, as evidenced by the escalating count of nodes and edges. This growth is mirrored in the increasing average degree, reflecting heightened character interactions as the number of episodes rises. Conversely, metrics such as average clustering, average shortest path, and diameter demonstrate a remarkable degree of **onstancy**. This stability underscores the network's ability to maintain its fundamental properties despite substantial expansion over successive seasons.
                    """)
        net_props = pd.read_csv("./data/season_properties.csv")
        st.write(net_props)
        st.markdown("""
                    ## Smokers communities
                     We see here how the network is divided into **two main clusters**, one of smokers and the other of non-smokers. This division is consistent throughout the seasons, with the smokers' cluster **remaining relatively stable** in size and composition. The non-smokers' cluster, however, undergoes significant growth, reflecting the increasing number of characters who do not smoke.                   
                     
                    Let's see how the relations between the two groups, the smokers and no smokers. With the following stats, we can see that the characters in **the smoker's group tend to be more connected** to them than the characters in the no-smokers group. Not only that, but also in season 25 is reflected that the characters **tend to be connected more times **(higher weight in the graph). That makes sense, for example, there is the 'Mafia' example, where all the characters who belong the the Mafia are connected between them, and they are all smokers.


                     **Season 1 - Number of smokers: 17 & Number of not smokers: 45**

                     - Possible edges between smokers: 136.0 Actual edges between smokers: 44 (32.35%)
                     - Average weight between smokers 1.07
                     - Possible edges between not smokers: 990.0 Actual edges between not smokers: 204 (20.61%)
                     - Average weight between not smokers 1.22
                     - Possible edges between smokers and non smokers: 765 Actual edges between smokers and non smokers: 193 (25.23%)
                     - Average weight between smokers and not smokers 1.24                  
                     **Season 25 - Number of smokers: 38 & Number of not smokers: 324**                 
                     - Possible edges between smokers: 703.0 Actual edges between smokers: 324. (46.09%)
                     - Average weight among smokers 6.85
                     - Possible edges between not smokers: 52326.0 Actual edges between not smokers: 2154. (4.12%)
                     - Average weight between not smokers 3.88
                     - Possible edges between smokers and non smokers: 12312 Actual edges between smokers and not smokers: 1749. (14.21%)
                     - average weight between smokers and not smokers 5.35

                     To summarize, it is seen that smokers are very connected with other smokers. Not only connected with a greater quantity of smoker characters but also connected more times (higher weight in the graph). Here we see the difference in the Network through the seasons, where the smokers group is represented in red and the no-smokers group in yellow.
                    
                     Note: we consider smokers the characters that have smoked at some point in the series, so could happen for example that in season 1 the character has not smoked yet, but we consider the character as *a smoker*. Even this, I think that it is not a big problem because the characters (except the main ones) generally are constant and do not change their personality during the show.
                    """)

        st.image("./img/smokers.png", caption='Smokers clusters', use_column_width=True)

        st.markdown("""
                    ## Inclusion evolution
Analyzing the data on the first appearances and total appearances of **LGBT characters** across seasons, several patterns emerge. Initially, it's notable that there are instances of more first appearances of LGBT characters in **later seasons**. Also in the inaugural season, altough, this needs to be contextualized by considering the influx of new characters in the first season. 

Upon closer examination, of the second plot, it becomes evident that there is a **visual uptick in the frequency of total appearances of LGBT characters in later seasons** compared to earlier ones. There appears to be a discernible **trend towards an increased presence of LGBT characters** in later seasons, suggesting a potential awareness of the scriptwritters.                    """)
        st.image("./img/lgbtperseason.png", caption='LGBT evolution', use_column_width=True)


if __name__ == "__main__":
    main()