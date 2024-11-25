import base64
import streamlit as st
import info2
import random

def initialize_skins():
    if "finalList" not in st.session_state:
        info2.fortniteSkins()
        st.session_state.finalList = random.sample(info2.finalList, 10)
        st.session_state.skinsDict = info2.skinsDict  
    if "selectedRarity" not in st.session_state:
        st.session_state.selectedRarity = None
    if "selectedSkin" not in st.session_state:
        st.session_state.selectedSkin = None
if "generate_loadout_pressed" not in st.session_state:
    st.session_state.generate_loadout_pressed = False

if "ready_up_pressed" not in st.session_state:
    st.session_state.ready_up_pressed = False

def skinSelect():
    initialize_skins()
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="margin-bottom: 20px;">Fortnite Loadout Generator</h1>
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

        st.session_state.selectedSkin = st.selectbox("Pick a Fortnite Character", [" "] + st.session_state.finalList, key="skin_select")

    st.write("---")

    
    if st.button("Generate loadout!"):
        if st.session_state.selectedSkin:
            rarity, chapter, image = st.session_state.skinsDict[st.session_state.selectedSkin]
            st.session_state.selectedRarity = rarity
            st.session_state.generate_loadout_pressed = True
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="{image}" alt="{st.session_state.selectedSkin}" style="width: 300px; margin-top: 20px;">
                </div>
                """,
                unsafe_allow_html=True
                )
            st.write("---")
            if chapter == "1":
                st.write(f"Your skin is {st.session_state.selectedSkin}! They are a seasoned fighter from Chapter 1 who honed their skills during the early days of the iconic battle royale. Some of their favorite landmarks include POIs from the likes of Tilted Towers to Dusty Depot.")
            if chapter == "2":
                st.write(f"Your skin is {st.session_state.selectedSkin}! This fighter is from Chapter 2, and has experienced the game's evolution. They learned to adapt to changes like the introduction of vehicles and new mechanics.")
            if chapter == "3":
                st.write(f"Your skin is {st.session_state.selectedSkin}! They were introduced during Chapter 3, a pivotal time in Fortnite's history marked by the Unreal Engine 5 upgrade. This is when unique game changes like sliding and mantling changed the course of Fortnite as we know it. They were priveleged to explore iconic locations like the Daily Bugle and Sanctuary.")
            if chapter == "4":
                st.write(f"Your skin is {st.session_state.selectedSkin}! They are a fighter from Chapter 4 who stumbled through controversial game updates such as an original loot pool and a new map that blended futuristic and medieval aesthetics.")
            if chapter == "5":
                st.write(f"Your skin is {st.session_state.selectedSkin}! Your skin stands at the cutting edge of Fortnite. They were introduced in Chapter 5, where they competed on a map unlike any other.")
            st.write("---")
            st.write("Now that you have selected your Fortnite character, it's time to ready up for a solo match. However, you must be careful! Your landing spot directly affects your probabilty of achieving the coveted #1 Victory Royale. Good luck... and don't forget to thank the bus driver!")
    if st.session_state.generate_loadout_pressed:
        if st.button("Ready Up"):
            st.session_state.ready_up_pressed = True
            with open("APIFiles/battleBusAudio.mp3", "rb") as audio_file:
                audio_base64 = base64.b64encode(audio_file.read()).decode()
            st.markdown(
                f"""
                <audio id="battlebus-audio" autoplay>
                    <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
                </audio>
                <script>
                    const audioElement = document.getElementById('battlebus-audio');
                    audioElement.currentTime = 2;
                </script>
                """,
                unsafe_allow_html=True,
            )
            st.image("APIFiles/battlebusimage.jpg", caption="", use_column_width=True)
            st.markdown(
                """
                <p style="font-size: 18px; line-height: 1.6; margin-top: 20px; text-align: center;">
                    Please go to the Fortnite Simulator page to see how you fare in a solo match of Fortnite Battle Royale.
                </p>
                """,
                unsafe_allow_html=True,
            )
skinSelect()
