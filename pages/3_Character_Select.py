import streamlist as st
import info2
import pandas as pd

#Drop down select
def skinSelect():
    st.header("Select a Fortnite Character")
    st.image(info2.dropboximage, width = 300)
    selectedSkin = st.selectbox("Pick a Fortnite character", info.finalList, index = None)
    st.write("---")
skinSelect()
