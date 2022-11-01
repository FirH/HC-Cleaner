import streamlit as st
st.title("""HackerRank Cleaner""")
st.write(
"""
<style>

div[class*="stTextInput"] label {
  font-size: 20px;
}

</style>
""", unsafe_allow_html=True
)

@st.cache
unused_words = ['PREPARENEW', 'CERTIFY', 'COMPETE', 'Search', 'All', 'Contests', 'Generic', 'Leaderboard', 'AllFriendsFilter', 'by', 'Type', 'username', 'to', 'compare', 'Compare', 'Rank', 'User', 'Score', 'Time', 'Interview', 'Prep', 'Blog', 'Scoring', 'Environment', 'FAQ', 'About', 'Us', 'Support', 'Careers', 'Terms', 'Of', 'Service', 'Privacy', 'Policy', '|']
usernames = (st.text_input("Masukkan username HackerRank")).split(" ")
leaderboard_data = [x for x in [x for x in (st.text_input("Masukkan seluruh isi page leaderboard HackerRank (CTRL+A) ")).split(" ") if x.strip()] if x not in unused_words]

for user in usernames :
    if(user in leaderboard_data) : 
        st.markdown(f"""<p style="font-family:Arial; 
                    background-color : white; 
                    color : black";>
                    {leaderboard_data[leaderboard_data.index(user)+1]}</style>
                    </p>""", unsafe_allow_html=True)
    else :
        st.markdown("""<p style="font-family:Arial; 
                    background-color : white; 
                    color : black; ">0</style>
                    </p>""", unsafe_allow_html=True)
