import google.generativeai as genai
import info2
import streamlit as st
import random



genai.configure(api_key = "AIzaSyDWHcBKbkhlS8OxyKdHZFqn7v9d9CYfgiM")
model = genai.GenerativeModel("gemini-1.5-flash")

def initialize_items():
    if "finalBannerList" not in st.session_state:
        info2.fortniteBanners()
        st.session_state.finalBannerList = random.sample(info2.finalBannerList, 3)

    if "finalLocationList" not in st.session_state:
        info2.fortnitePOIS()
        st.session_state.finalLocationList = random.sample(info2.finalLocationList, 6)

    if "selectedSkin" not in st.session_state:
        st.session_state.selectedSkin = None
        
    if "selectedBanner" not in st.session_state:
        st.session_state.selectedBanner = None

    if "selectedLocation" not in st.session_state:
        st.session_state.selectedLocation = None

    if "selectedRarity" not in st.session_state:
        st.session_state.selectedRarity = None
initialize_items()

if "deploy_glider" not in st.session_state:
    st.session_state.deploy_glider = False

if "llmgenerate" not in st.session_state:
    st.session_state.llmgenerate = False

if "finalResponse" not in st.session_state:
    st.session_state.finalResponse = None

#Title Area
def titleFunc():
    st.title("Fortnite Battle Royale Simulator")
    st.write("---")

#Banner and LocationArea
def bannerandlocFunc():
    st.markdown(
        """
        <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 20px;">
            <div style="text-align: center;">
                <img src="{img1}" style="width: 175px; height: auto;" />
                <p style="margin-top: 10px; font-size: 16px;">1</p>
            </div>
            <div style="text-align: center;">
                <img src="{img2}" style="width: 175px; height: auto;" />
                <p style="margin-top: 10px; font-size: 16px;">2</p>
            </div>
            <div style="text-align: center;">
                <img src="{img3}" style="width: 175px; height: auto;" />
                <p style="margin-top: 10px; font-size: 16px;">3</p>
            </div>
        </div>
        """.format(
            img1=st.session_state.finalBannerList[0],
            img2=st.session_state.finalBannerList[1],
            img3=st.session_state.finalBannerList[2]
        ),
        unsafe_allow_html=True,
    )
    selectedImage = st.radio("Choose a banner:", ["1", "2", "3"]) 
    st.session_state.selectedBanner = int(selectedImage)

    st.image(info2.mapImage, use_column_width=True)
    locationResponse = st.radio("Select a landing spot:", st.session_state.finalLocationList)
    st.session_state.selectedLocation = locationResponse
bannerandlocFunc()


rarityList = ["Uncommon", "Rare", "Epic", "Legendary"]

rarityList = ["Uncommon", "Rare", "Epic", "Legendary"]
if st.button("Deploy your Glider!"):
    st.session_state.deploy_glider = True
    locationIndex = st.session_state.finalLocationList.index(st.session_state.selectedLocation)
    selectedBanner = st.session_state.selectedBanner
    selectedLocation = st.session_state.selectedLocation
    selectedRarity = st.session_state.selectedRarity   
    selectedSkin = st.session_state.selectedSkin
    if locationIndex == 0 or locationIndex == 3 and selectedBanner == 2 or selectedBanner == 3 and selectedRarity in ["Uncommon", "Epic", "Legendary"]:
        response = model.generate_content(
            f"Write a short description of a Fortnite character's events as they win a game of solo battle royale. The character’s skin is {selectedSkin}. They landed at {selectedLocation}. Write a short paragraph for each storm circle, describing the ways in which the character got eliminations or the loot that they found in chests and supply drops. Include details relevant to today's Fortnite meta, such as cranking 90's and grappling."
        ).text
    elif locationIndex == 1 and selectedBanner == 3 or selectedBanner == 1 and selectedRarity in ["Rare", "Uncommon"] or selectedRarity not in rarityList:
        response = model.generate_content(
            f"Write a short description of a Fortnite character's events as they place second in a game of solo battle royale. The character’s skin is {selectedSkin}. They landed at {selectedLocation}. Write a short paragraph for each storm circle, describing the ways in which the character got eliminations, the loot they found in chests and supply drops, and the way in which they were eliminated."
        ).text
    elif locationIndex == 2 or locationIndex == 4 and selectedBanner == 1 or selectedBanner == 2 and selectedRarity in ["Legendary", "Epic"] or selectedRarity not in rarityList:
        response = model.generate_content(
            f"Write a short description of a Fortnite character's events as they place top 15 but do not place within the top 2 in a game of solo battle royale. The character’s skin is {selectedSkin}. They landed at {selectedLocation}. Write a short paragraph for each storm circle, describing the ways in which the character got eliminations and the loot they found in chests and supply drops."
        ).text
    elif locationIndex == 5 and selectedBanner == 1 or selectedBanner == 3 and selectedRarity in ["Epic", "Rare", "Legendary"] or selectedRarity not in rarityList:
        response = model.generate_content(
            f"Write a short description of a Fortnite character's events as they were eliminated early in a solo battle royale. The character’s skin is {selectedSkin}. They landed at {selectedLocation}. Talk about how the character got a few eliminations, but was then quickly eliminated by another player."
        ).text
    else:
        response = model.generate_content(
            f"Write a short description of a Fortnite character's events as they place within the top 40 players not within the top 15 in a game of solo battle royale. The character’s skin is {selectedSkin}. They landed at {selectedLocation}. Write a short paragraph for each storm circle, describing the ways in which the character got eliminations or the loot they found in chests and supply drops."
        ).text
    st.write(response)
    
    st.title("Ask a question!")
    st.subheader("If you want to know more about the match, or just about Fortnite in general, type a question.")
    if st.session_state.deploy_glider:
        responsePrompt = st.text_input("Type here:")
        if st.button("Enter"):
            st.session_state.llmgenerate = True
            if responsePrompt.strip():
                st.session_state.finalRespons = model.generate_content(responsePrompt)
            else:
                st.session_state.finalResponse = "No question entered."
            if st.session_state.llmgenerate:
                st.write(st.session_state.finalResponse)
    if st.session_state.llmgenerate:
        st.write(st.session_state.finalResponse)
        st.write("---")

