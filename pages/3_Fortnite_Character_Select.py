import streamlit as st
import info2
import pandas as pd5
import random

def initialize_skins():
    if "finalList" not in st.session_state:
        info2.fortniteSkins()
        st.session_state.finalList = random.sample(info2.finalList, 10)
        st.session_state.skinsDict = info2.skinsDict  

def skinSelect():
    initialize_skins()
    
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="margin-bottom: 20px;">Fortnite Character Select</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="text-align: center;">
            <h2 style="margin-bottom: 20px;">Select a Fortnite character:</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(info2.dropboximage, width=300)

        selectedSkin = st.selectbox("Pick a Fortnite Character", [" "] + st.session_state.finalList, key="skin_select")

    st.write("---")

    
    if st.button("Generate loadout!"):
        for skinItems in info2.skinsDict:
            rarity, chapter, image = info2.skinsDict[skinItems]
            if selectedSkin == skinItems:
                st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="{image}" alt="{selectedSkin}" style="width: 300px; margin-top: 20px;">
                </div>
                """,
                unsafe_allow_html=True
                )
                st.write("---")
                if chapter == "1":
                    st.write(f"Your skin is {selectedSkin}! They are a seasoned fighter from Chapter 1 who honed their skills during the early days of the iconic battle royale. Some of their favorite landmarks include POIs from the likes of Tilted Towers to Dusty Depot.")
                if chapter == "2":
                    st.write(f"Your skin is {selectedSkin}! This fighter is from Chapter 2, and has experienced the game's evolution. They learned to adapt to changes like the introduction of vehicles and new mechanics.")
                if chapter == "3":
                    st.write(f"Your skin is {selectedSkin}! They were introduced during Chapter 3, a pivotal time in Fortnite's history marked by the Unreal Engine 5 upgrade. This is when unique game changes like sliding and mantling changed the course of Fortnite as we know it. They were priveleged to explore iconic locations like the Daily Bugle and Sanctuary.")
                if chapter == "4":
                    st.write(f"Your skin is {selectedSkin}! They are a fighter from Chapter 4 who stumbled through controversial game updates such as an original loot pool and a new map that blended futuristic and medieval aesthetics.")
                if chapter == "5":
                    st.write(f"Your skin is {selectedSkin}! Your skin stands at the cutting edge of Fortnite. They were introduced in Chapter 5, where they competed on a map unlike any other.")
                st.write("---")
                st.write("Now that you have selected your Fortnite character, it's time to ready up for a solo match. However, you must be careful! Your landing spot directly affects your probabilty of achieving the coveted #1 Victory Royale. Good luck... and don't forget to thank the bus driver!")
skinSelect()
