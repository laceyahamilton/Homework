import streamlit as st 
import pandas as pd
import seaborn as sns
import numpy as np

st.title("A Guide To Chess")
df = pd.read_csv("games.csv")
st.image("chess.jpeg")
st.subheader("A brief overview of chess and what you can expect while learning.")
 
 #tabs
intro_tab, rules_tab, pieces_tab, gameplay_tab, endgame_tab, rating_tab, moves_tab, conclusion_tab = st.tabs(["Introduction", "Rules", "How The Pieces Move", "Gameplay", "How to Win", "How Ratings Work", "More on Gameplay", "Conclusion"])

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
    col1, col2 = st.columns([1, 1])
    with col1:
        st.pyplot(winner)
    with col2:
        st.write("Start of game setup: When the chess board is set up to start a game, half of the squares are occupied by the pieces while the middle 32 squares are left open for play.")
        st.image("setup.png")
        st.image("pieces.png")
with pieces_tab:
    st.write("Here is an overview of how each piece moves")
    col00, col01, col02, col03= st.columns([1, 1, 1, 1])
    with col00:
        st.write("King Movement")
        st.image("kingmove.png")
        st.write("Queen Movement")
        st.image("queenmove.png")
    with col01:
        st.write("Knight Movement")
        st.image("knightmove.png")
        st.write("Bishop Movement")
        st.image("bishopmove.jpg")
    with col02:
        st.write("Rook Movement")
        st.image("rookmove.png")
        st.write("Pawn Movement")
        st.image("pawnmove.png")
    with col03:
        st.write("Notation")
        st.write("How to write pieces - Capital letters are used for pieces as follows: K-King, Q-Queen, R-Rook, B-Bishop, N-Knight, P-Pawn (although, by convention, P is usually omitted from notation)")
        st.write("How to write move - To write a move, give the name of the piece and the square to which it moves. If a piece is captured, we include the symbol x for 'captures' before the destination square")
        st.write("Special Symbols - Special Symbols x: captures, 0-0: kingside castle, 0-0-0: queenside castle, +: check, #: checkmate,!: good move, ?: poor move,more !s and ?s can be added for emphasis.")


#dataset with just the top openings
df2 = df[df['opening_name'].map(df['opening_name'].value_counts()) > 200]

sns.set_palette("magma", n_colors = 10)
opening2 = sns.displot(df2, x="opening_name", hue="opening_name")
opening2 = opening2.set(xticklabels=[])
opening2 = opening2.set(title='Most Frequent Openings')
opening2 = opening2.set(xlabel='Opening Name')
opening2 = opening2.set(ylabel='Number of Plays')

df["opening_move"]=df["moves"].str.slice(0,2)
blackmoves = df[df["winner"]=="black"]
blackmoves = blackmoves[blackmoves['opening_name'].map(blackmoves['opening_name'].value_counts()) > 50]
blackturns = sns.displot(blackmoves, x="opening_move", hue="opening_move")

df["opening_move"]=df["moves"].str.slice(0,2)
whitemoves = df[df["winner"]=="white"]
whitemoves = whitemoves[whitemoves['opening_name'].map(whitemoves['opening_name'].value_counts()) > 47]
whiteturns = sns.displot(whitemoves, x="opening_move", hue="opening_move")

with gameplay_tab:
    st.write("There are three phases of the game: the opening, middlegame and endgame. The opening is where piece development occurs and sets the tone of the game as previously stated. The middlegame is the meat of the game where attacking and defense occurs; this is also a time where weaknesses in the opponent’s game can be spotted. The endgame is where final attacks and attempts to checkmate the king occur. Chess theory goes into a deep analysis of different approaches and techniques for each. There are around 1,300 named chess openings. Here, we can see top 10 openings that are the most frequently played.")   
    col3, col4 = st.columns([1, 1])
    with col3:
        choose = st.radio(
            "Choose Color",
            ["Top 10 Openings", "Top Openings Moves for White (White Wins)",
            "Top Openings Moves for Black (Black Wins)"])
        if choose == "Top 10 Openings":
            st.pyplot(opening2)
        if choose == "Top Openings Moves for White (White Wins)":
            st.pyplot(whiteturns)
        if choose == "Top Openings Moves for Black (Black Wins)":
            st.pyplot(blackturns)
    with col4:
    	st.image("openings.png")
    	st.caption("This image shows the complexity and similariy of different openings.")


#graphs


sns.set_palette("magma", n_colors = 4)

results = sns.displot(df, x="victory_status", hue="victory_status")
results = results.set(title='Distribution of Results')
results = results.set(xlabel='Victory Status')
results = results.set(ylabel='Count')
results = results._legend.remove()

with endgame_tab:
    st.write("There are 2 categories in which that game can end: win/lose and draw. There are 8 ways these two can happen. For win/lose, you can checkmate, resign, or timeout (run out of time). You can come to a draw by stalemate, agreement, repetition, 50 move-rule, and insufficient material. Here is the distribution of results from the dataset.")    
    col5, col6 = st.columns([1, 1])
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
	st.write("There is a rating system that indicates how good you are at the game. As you win and lose throughout your career, your rating will go up or down depending on the rating on the opponent and whether or not you won or lost. The highest ever rating achieved was by GM Magnus Carlsen with 2882 rating. Using the Elo rating system, there are 11 categories to be put into as seen below. Here is the distribution of those ratings in the dataset.")
	col7, col8 = st.columns([1, 1])
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

sns.set_palette("magma", n_colors = 11)
blackturn = sns.relplot(data=df, x="black_rating", y="turns", hue = "turns")
blackturn.set(title='Number of Turns by Black ranking')
blackturn.set(xlabel='Rankings')
blackturn.set(ylabel='Turn')

sns.set_palette("magma", n_colors = 11)
whiteturn = sns.relplot(data=df, x="white_rating", y="turns", hue = "turns")
whiteturn.set(title='Number of Turns by White ranking')
whiteturn.set(xlabel='Rankings')
whiteturn.set(ylabel='Turn')

with moves_tab:
    st.write("In the early 1800s, a competitive game tactic was to run the game out as long as possible to exhaust the opponent. Since then clocks have been used to avoid this. When each player moves, they will hit the clock and the opponent's time will start ticking and this will go back and forth with each turn. The time on each clock is set with an agreed time. Running out of time means forfeiting the game. The evolution of chess clocks have gone through pocketwatches, sand-timers, mechanical chess clocks and modern day digital chess clocks. With this time limit, there are only so many reasonable moves you can make within the time frame. The average number of moves in a game is 40 moves. Due to this, one may think that more experienced players may make less moves because they are thinking more efficiently and find checkmate quicker. But that is not the case. Here, we can see that the number of moves against the rating of the player has no apparent correlation.")
    col7, col8 = st.columns([1, 1])
    with col7:
        color1 = st.radio(
            "Choose Color",
            ["**White**", "**Black**"],
            key="color1")
        if color1 == "**White**":
            st.pyplot(whiteturn)
        if color1 == "**Black**":
            st.pyplot(blackturn)
    with col8:
        st.image("clock.jpeg")
        st.image("olderclock.png")
with conclusion_tab:
    st.write("You now know enough of the basics to start playing chess. You can join the young, the old and everyone in between and start building your chess skills. Have fun! :) ")
    st.image("enjoy.jpg")
    st.image("kidschess.jpg")



















