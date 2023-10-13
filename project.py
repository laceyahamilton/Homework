import streamlit as st 
import pandas as pd
import seaborn as sns
import numpy as np

st.set_page_config(layout="wide")
st.title("A Guide To Chess")
df = pd.read_csv("games.csv")
st.image("chess.jpeg")
st.subheader("A brief overview of chess and what you can expect while learning.")
 
 #tabs
intro_tab, rules_tab, gameplay_tab, endgame_tab, rating_tab = st.tabs(["Introduction", "Rules", "Gameplay", "How to Win", "How Ratings Work"])

with intro_tab:
    st.write("What is chess? – Chess is one of the oldest played board games by humans. Played on a checkered board and each player playing with pieces of contrasting colors. Each player takes turns moving a piece with the goal of checkmating the King. This means a position where the King cannot evade capture.")
    st.image("tournament.jpeg")

sns.set_palette("magma", n_colors = 3)
st.set_option('deprecation.showPyplotGlobalUse', False)

winner = sns.displot(df, x="winner", hue="winner")
winner = winner.set(title='Distribution of Wins')
winner = winner.set(xlabel=' ')
winner = winner.set(ylabel='Number of Wins')
winner = winner._legend.remove()

with rules_tab:
    st.write("Each player has 16 pieces with 6 different types: King, Queen, 2 Rooks, 2 Bishops, 2 Knights, and 8 Pawns. White is always the first to move. This rule gives the misconception that white has an advantage since they can set the tone for the game first. Based on the analysis below, there may be some truth to that.")   
    col1, col2 = st.columns([1, 2])
    with col1:
        st.pyplot(winner)
    with col2:
    	st.image("pieces.png")

#dataset with just the top openings
df2 = df[df['opening_name'].map(df['opening_name'].value_counts()) > 200]
sns.set_palette("magma", n_colors = 10)

openings = sns.displot(df2, x="opening_name", hue="opening_name")
openings = openings.set(xticklabels=[])
openings = openings.set(title='Most Frequent Openings')
openings = openings.set(xlabel='Opening Name')
openings = openings.set(ylabel='Number of Plays')


with gameplay_tab:
    st.write("There three phases of the game: the opening, middlegame and endgame. The opening is where piece development occurs and sets the tone of the game as previously stated. The middlegame is the meat of the game where attacking and defense occurs, this is also a time where weaknesses in the opponent’s game can be spotted. The endgame is where final attacks and attempts to checkmate the king occur. Chess theory goes into a deep analysis of different approaches and techniques for each. There are around 1,300 named chess openings. Here we can see top 10 openings that are the most frequently played.")   
    col3, col4 = st.columns([2, 1])
    with col3:
    	st.pyplot(openings)
    with col4:
    	st.image("openings.png")
    	st.caption("This image shows the complexity and similarities of different openings.")


#graphs


sns.set_palette("magma", n_colors = 4)

results = sns.displot(df, x="victory_status", hue="victory_status")
results = results.set(title='Distribution of Results')
results = results.set(xlabel='Victory Status')
results = results.set(ylabel='Count')
results = results._legend.remove()

with endgame_tab:
    st.write("There are 2 categories in which that game can end: win/lose and draw. There are 8 ways these two can happen. For win/lose, you can checkmate, resign, or timeout (run out of time). You can come to a draw by stalemate, agreement, repetition, 50 move-rule, insufficient material. Here is the distribution of results from the dataset.")    
    col5, col6 = st.columns([1, 2])
    with col5:
    	st.pyplot(results)
    with col6:
    	st.image("stalemate.png")
    	st.caption("This is an example of a stalemate.")

white_conditions = [
    (df['white_rating'] >= 2700),
    (df['white_rating'] >= 2500) & (df['white_rating'] < 2700),
    (df['white_rating'] >= 2400) & (df['white_rating'] < 2500),
    (df['white_rating'] >= 2300) & (df['white_rating'] < 2400),
    (df['white_rating'] >= 2200) & (df['white_rating'] < 2300),
    (df['white_rating'] >= 2000) & (df['white_rating'] < 2200),
    (df['white_rating'] >= 1800) & (df['white_rating'] < 2000),
    (df['white_rating'] >= 1600) & (df['white_rating'] < 1800),
    (df['white_rating'] >= 1400) & (df['white_rating'] < 1600),
    (df['white_rating'] >= 1200) & (df['white_rating'] < 1400),
    (df['white_rating'] < 1200)
    
]

values = ['World Championship Contenders','Grand Masters', 'International Masters'
               ,'FIDE Masters', 'FIDE Candidate Masters/National Masters',
               'Candidate Masters/Experts(USA)', 'Class A', 'Class B', 'Class C', 
                'Class D', 'Novices']

black_conditions = [
    (df['black_rating'] >= 2700),
    (df['black_rating'] >= 2500) & (df['black_rating'] < 2700),
    (df['black_rating'] >= 2400) & (df['black_rating'] < 2500),
    (df['black_rating'] >= 2300) & (df['black_rating'] < 2400),
    (df['black_rating'] >= 2200) & (df['black_rating'] < 2300),
    (df['black_rating'] >= 2000) & (df['black_rating'] < 2200),
    (df['black_rating'] >= 1800) & (df['black_rating'] < 2000),
    (df['black_rating'] >= 1600) & (df['black_rating'] < 1800),
    (df['black_rating'] >= 1400) & (df['black_rating'] < 1600),
    (df['black_rating'] >= 1200) & (df['black_rating'] < 1400),
    (df['black_rating'] < 1200)
    
]

df['white_ranking'] = np.select(white_conditions, values)
df['black_ranking'] = np.select(black_conditions, values)

sns.set_palette("magma", n_colors = 11)

whiteranking = sns.displot(df, x="white_ranking", hue="white_ranking")
whiteranking.set(xticklabels=[])
whiteranking.set(title='Rankings Who Played White')
whiteranking.set(xlabel=' ')
whiteranking.set(ylabel='Count')

sns.set_palette("magma", n_colors = 11)
blackranking = sns.displot(df, x="black_ranking", hue="black_ranking")
blackranking.set(xticklabels=[])
blackranking.set(title='Rankings Who Played Black')
blackranking.set(xlabel=' ')
blackranking.set(ylabel='Count')


with rating_tab:
	st.write("There is a rating system that indicates how good you are at the game. As you win and lose throughout your career, your rating will go up or down depending on the rating on the opponent and whether or not you won or lost. The highest ever rating achieved was by GM Magnus Carlsen with 2882 rating. Using the Elo rating system, there are 11 categories to be put into as seen below")
	col7, col8 = st.columns([2, 1])
	with col7:
		color = st.radio(
    		"Choose Color",
    		["**White**", "**Black**"])
		if color == "**White**":
			st.pyplot(whiteranking)
		if color == "**Black**":
			st.pyplot(blackranking)
	with col8:
		st.image("rankings.jpeg")
		st.caption("List of Categories")



















