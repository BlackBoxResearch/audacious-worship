import streamlit as st
import pandas as pd

st.title("Nights of Fire 2025", anchor=False)
st.markdown("Friday 31st Jan - Sunday 2nd Feb 2025")

lineup, song_bank, run_sheet, dress_code = st.tabs(["Band Lineup", "Song Bank", "Run Sheet", "Dress Code"])

with lineup:
    st.subheader("Lineup", anchor=False)

    night_1, night_2, night_3 = st.columns(3)

    with night_1:
        st.markdown("**Friday 31st Jan:**")
        df = pd.DataFrame(
            {
            "Role": ["Vox 1", "Vox 2", "Vox 3", "Vox 4", "Vox 5", "Vox 6", "Vox 7", "MD", "Bass", "Drums", "Keys", "EG 1", "EG 2"],
            "Who": ["Matt B", "Lynn-Marie", "Mary", "Luke", "Rutendo", "Charlie", "Miah", "Ben", "Joe", "Reuben", "Joel", "Ben", "Tim"],
            }
        )

        st.dataframe(
            df,
            height=500,
            hide_index=True,
            use_container_width=True,
            on_select="ignore")

    with night_2:
        st.markdown("**Saturday 1st Feb:**")
        df = pd.DataFrame(
            {
            "Role": ["Vox 1", "Vox 2", "Vox 3", "Vox 4", "Vox 5", "Vox 6", "Vox 7", "MD", "Bass", "Drums", "Keys", "EG 1", "EG 2"],
            "Who": ["Matt B", "Lynn-Marie", "Mary", "Luke", "Rutendo", "Charlie", "Miah", "Ben", "Joe", "Reuben", "Joel", "Ben", "Gabe"],
            }
        )

        st.dataframe(
            df,
            height=500,
            hide_index=True,
            use_container_width=True,
            on_select="ignore")
        
    with night_3:
        st.markdown("**Sunday 2nd Feb:**")
        df = pd.DataFrame(
            {
            "Role": ["Vox 1", "Vox 2", "Vox 3", "Vox 4", "Vox 5", "Vox 6", "Vox 7", "MD", "Bass", "Drums", "Keys", "EG 1", "EG 2"],
            "Who": ["Matt B", "Lynn-Marie", "Mary", "Luke", "Rutendo", "Charlie", "Miah", "Ben", "Joe", "Reuben", "Joel", "Ben", "TBC"],
            }
        )

        st.dataframe(
            df,
            height=500,
            hide_index=True,
            use_container_width=True,
            on_select="ignore")
        
with song_bank:
    st.subheader("Song Bank", anchor=False)

    fast, slow = st.columns(2)

    with fast:
        st.markdown("**Fast Songs**")
        df = pd.DataFrame(
            {
            "Song": ["Vox 1", "Vox 2", "Vox 3", "Vox 4", "Vox 5", "Vox 6", "Vox 7", "MD", "Bass", "Drums", "Keys", "EG 1", "EG 2"],
            "Artist": ["Matt B", "Lynn-Marie", "Mary", "Luke", "Rutendo", "Charlie", "Miah", "Ben", "Joe", "Reuben", "Joel", "Ben", "Tim"],
            "Link": ["Matt B", "Lynn-Marie", "Mary", "Luke", "Rutendo", "Charlie", "Miah", "Ben", "Joe", "Reuben", "Joel", "Ben", "Tim"],
            }
        )

        st.dataframe(
            df,
            height=500,
            hide_index=True,
            use_container_width=True,
            on_select="ignore")

    with slow:
        st.markdown("**Slow Songs**")
        df = pd.DataFrame(
            {
            "Song": ["Vox 1", "Vox 2", "Vox 3", "Vox 4", "Vox 5", "Vox 6", "Vox 7", "MD", "Bass", "Drums", "Keys", "EG 1", "EG 2"],
            "Artist": ["Matt B", "Lynn-Marie", "Mary", "Luke", "Rutendo", "Charlie", "Miah", "Ben", "Joe", "Reuben", "Joel", "Ben", "Tim"],
            "Link": ["Matt B", "Lynn-Marie", "Mary", "Luke", "Rutendo", "Charlie", "Miah", "Ben", "Joe", "Reuben", "Joel", "Ben", "Tim"],
            }
        )

        st.dataframe(
            df,
            height=500,
            hide_index=True,
            use_container_width=True,
            on_select="ignore")
        
with run_sheet:
    st.subheader("Run Sheet", anchor=False)

with dress_code:
    st.subheader("Dress Code", anchor=False)

    st.image(image="a39dc0a6695910ae7a205def3b661c6f.jpg", use_container_width=True)
