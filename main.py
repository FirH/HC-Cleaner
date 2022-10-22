import streamlit as st
st.title("""Hackerrank Cleaner""")

st_input = st.text_input("Masukkan username hackerrank")
hc_input = st.text_input("Masukkan data hackerrank (CTRL+A) ")
usernames = st_input.split(" ")
removal = ['PREPARENEW', 'CERTIFY', 'COMPETE', 'Search', 'All', 'Contests', 'Generic', '2022', 'Leaderboard', 'AllFriendsFilter', 'by', 'Type', 'username', 'to', 'compare', 'Compare', 'Rank', 'User', 'Score', 'Time', 'Interview', 'Prep', '|', 'Blog', '|', 'Scoring', '|', 'Environment', '|', 'FAQ', '|', 'About', 'Us', '|', 'Support', '|', 'Careers', '|', 'Terms', 'Of', 'Service', '|', 'Privacy', 'Policy', '|']
str_input = [x for x in [x for x in hc_input.split(" ") if x.strip()] if x not in removal]

for user in usernames :
    if(user in str_input) : 
        style = f"""<p style="font-family:Arial; 
                    background-color : white; 
                    color : black">
                    {str_input[str_input.index(user)+1]}</style>
                    </BR></p>"""
        st.markdown(style, unsafe_allow_html=True)
    else :
        style = """<p style="font-family:Arial; 
                    background-color : white; 
                    color : black; ">Nan</style>
                    </BR></p>"""
        st.markdown(style, unsafe_allow_html=True)
