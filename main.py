import streamlit as st
st.write("""Hackerrank Cleaner""")

st_input = st.text_input("Masukkan username hackerrank")
hc_input = st.text_input("Masukkan data hackerrank (CTRL+A) ")
usernames = st_input.split(" ")
removal = ['PREPARENEW', 'CERTIFY', 'COMPETE', 'Search', 'All', 'Contests', 'Generic', '2022', 'Leaderboard', 'AllFriendsFilter', 'by', 'Type', 'username', 'to', 'compare', 'Compare', 'Rank', 'User', 'Score', 'Time', 'Interview', 'Prep', '|', 'Blog', '|', 'Scoring', '|', 'Environment', '|', 'FAQ', '|', 'About', 'Us', '|', 'Support', '|', 'Careers', '|', 'Terms', 'Of', 'Service', '|', 'Privacy', 'Policy', '|']
str_input = hc_input.split(" ")
str_input = [x for x in str_input if x.strip()]
str_input = [x for x in str_input if x not in removal]

for user in usernames :
    if(user in str_input) : 
        out = str_input[str_input.index(user)+1]
        htmlstr = f"""<p style = 'background-color: rgb(255,255,255,1);
                        color: rgb(0,0,0,1);'>
                        {out}</style>
                        <BR></p>"""
        st.markdown(htmlstr, unsafe_allow_html=True)
    else :
        out = "Nan"
        htmlstr = f"""<p style = 'background-color: rgb(255,255,255,1);
                        color: rgb(0,0,0,1);'>
                        {out}</style>
                        <BR></p>"""
        st.markdown(htmlstr, unsafe_allow_html=True)