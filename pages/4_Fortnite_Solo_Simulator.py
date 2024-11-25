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

    
    if "deploy_glider" not in st.session_state:
        st.session_state.deploy_glider = False
    
    if "llmgenerate" not in st.session_state:
        st.session_state.llmgenerate = False
    
    if "finalResponse" not in st.session_state:
        st.session_state.finalResponse = None
    
    if "responsePrompt" not in st.session_state:
        st.session_state.responsePrompt = ""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
initialize_items()


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
if st.button("Deploy your Glider!"):
    st.session_state.deploy_glider = True
    locationIndex = st.session_state.finalLocationList.index(st.session_state.selectedLocation)
    selectedBanner = st.session_state.selectedBanner
    selectedLocation = st.session_state.selectedLocation
    selectedRarity = st.session_state.selectedRarity   
    selectedSkin = st.session_state.selectedSkin
    if locationIndex == 0 or locationIndex == 3 and selectedBanner == 2 or selectedBanner == 3 and selectedRarity in ["Uncommon", "Epic", "Legendary"]:
        st.session_state.finalResponse = model.generate_content(
            f"Write a short description of a Fortnite character's events as they win a game of solo battle royale. The character’s skin is {selectedSkin}. They landed at {selectedLocation}. Write a short paragraph for each storm circle, describing the ways in which the character got eliminations or the loot that they found in chests and supply drops. Include details relevant to today's Fortnite meta, such as cranking 90's and grappling."
        ).text
    elif locationIndex == 1 and selectedBanner == 3 or selectedBanner == 1 and selectedRarity in ["Rare", "Uncommon"] or selectedRarity not in rarityList:
        st.session_state.finalResponse = model.generate_content(
            f"Write a short description of a Fortnite character's events as they place second in a game of solo battle royale. The character’s skin is {selectedSkin}. They landed at {selectedLocation}. Write a short paragraph for each storm circle, describing the ways in which the character got eliminations, the loot they found in chests and supply drops, and the way in which they were eliminated."
        ).text
    elif locationIndex == 2 or locationIndex == 4 and selectedBanner == 1 or selectedBanner == 2 and selectedRarity in ["Legendary", "Epic"] or selectedRarity not in rarityList:
        st.session_state.finalResponse = model.generate_content(
            f"Write a short description of a Fortnite character's events as they place top 15 but do not place within the top 2 in a game of solo battle royale. The character’s skin is {selectedSkin}. They landed at {selectedLocation}. Write a short paragraph for each storm circle, describing the ways in which the character got eliminations and the loot they found in chests and supply drops."
        ).text
    elif locationIndex == 5 and selectedBanner == 1 or selectedBanner == 3 and selectedRarity in ["Epic", "Rare", "Legendary"] or selectedRarity not in rarityList:
        st.session_state.finalResponse = model.generate_content(
            f"Write a short description of a Fortnite character's events as they were eliminated early in a solo battle royale. The character’s skin is {selectedSkin}. They landed at {selectedLocation}. Talk about how the character got a few eliminations, but was then quickly eliminated by another player."
        ).text
    else:
        st.session_state.finalResponse = model.generate_content(
            f"Write a short description of a Fortnite character's events as they place within the top 40 players not within the top 15 in a game of solo battle royale. The character’s skin is {selectedSkin}. They landed at {selectedLocation}. Write a short paragraph for each storm circle, describing the ways in which the character got eliminations or the loot they found in chests and supply drops."
        ).text
    st.write(st.session_state.finalResponse)

if st.session_state.finalResponse:
    st.write("---")
    st.subheader("Fortnite Chatbot")
    st.text_area("Chat History", value="\n".join(st.session_state.chat_history), height=300, disabled=True)

    st.session_state.responsePrompt = st.text_input("Ask a question about Fortnite or your simulation:")
    if st.button("Ask"):
        user_input = st.session_state.responsePrompt.strip()
        fortniteKeywords = fortniteKeywords = [
            "fortnite", "battle royale", "epic games", "victory royale", "storm", "circle", "loot",
            "weapons", "skins", "glider", "map", "chests", "supply drops", "emotes", "pickaxe", "build",
            "materials", "edit", "turbo build", "cranking 90s", "zone wars", "trios", "squads", "duos",
            "solo", "eliminations", "reboot card", "reboot van", "medkit", "bandages", "shield potion",
            "mini shield", "big shield", "slurp juice", "chug jug", "storm surge", "battle bus", "POI",
            "landing spot", "high ground", "low ground", "mid ground", "arena", "creative mode",
            "zero build", "gold bars", "NPCs", "mythic weapons", "legendary weapons", "epic weapons",
            "rare weapons", "uncommon weapons", "common weapons", "vaults", "keys", "chrome splash",
            "rift-to-go", "boogie bomb", "shockwave grenade", "bush camping", "sniping", "headshot",
            "AR", "assault rifle", "pump shotgun", "combat shotgun", "tactical shotgun",
            "heavy sniper", "bolt-action sniper", "pistol", "dual pistols", "rocket launcher",
            "grenade launcher", "minigun", "submachine gun", "SMG", "scar", "DMR", "hammer assault rifle",
            "twin mag SMG", "hunting rifle", "crossbow", "thermal scope", "lever-action shotgun",
            "tactical assault rifle", "stinger SMG", "striker pump", "charge shotgun", "lever-action rifle",
            "combat SMG", "rapid fire SMG", "plasma cannon", "pulse rifle", "shadow tracker",
            "primal shotgun", "primal rifle", "makeshift rifle", "makeshift shotgun", "makeshift SMG",
            "wildcard week", "fortnitemares", "chapter 4", "chapter 3", "chapter 2", "chapter 1",
            "seasons", "battle pass", "item shop", "V-Bucks", "challenges", "quests", "season XP",
            "milestones", "level up", "endgame", "victory crown", "sweats", "default skins", "OG skins",
            "renegade raider", "aerial assault trooper", "black knight", "john wick", "drift",
            "peely", "fishstick", "meowscles", "midas", "jules", "sky", "lynx", "man cake", "guff",
            "marvel skins", "dc skins", "star wars skins", "naruto skins", "ninja skin",
            "loserfruit skin", "lachlan skin", "bugha skin", "travis scott skin", "ariana grande skin",
            "thanos", "iron man", "spider-man", "gwen stacy", "mandalorian", "stormtrooper",
            "kylo ren", "lightsabers", "bounty hunters", "collabs", "fortnite concerts", "travis scott event",
            "marshmello event", "ariana grande event", "live event", "end event", "cube queen",
            "kevin the cube", "chrome tornado", "mecha team leader", "the foundation", "agent jones",
            "the imagined", "the origin", "the paradigm", "zero point", "island", "volcano",
            "tilted towers", "pleasant park", "retail row", "salty springs", "lazy lake",
            "sweaty sands", "steamy stacks", "craggy cliffs", "coral castle", "slurpy swamp",
            "weeping woods", "risky reels", "boney burbs", "catty corner", "dirty docks",
            "frenzy farm", "holly hedges", "misty meadows", "stealthy stronghold", "spire",
            "fortnite meta", "fortnite esports", "FNCS", "cash cup", "arena points", "creative maps",
            "deathrun", "box fights", "zone wars maps", "1v1 map", "edit course", "aim trainer",
            "fortnite tournaments", "custom matchmaking", "stream sniping", "spectating",
            "final circle", "storm phases", "reloading", "aim assist", "controller player",
            "keyboard and mouse", "PC player", "console player", "crossplay", "ping", "FPS",
            "graphics settings", "fortnite updates", "patch notes", "weekly updates", "content creators",
            "streamers", "ninja", "tfue", "clix", "bugha", "fresh", "typical gamer", "lachlan", "skin", 
        ]
        try:
            if not user_input:
                raise ValueError("Input cannot be empty. Please enter a question.")
        
            is_fortnite_related = any(keyword in user_input.lower() for keyword in fortniteKeywords)
        
            if is_fortnite_related:
                generated_scenario = st.session_state.finalResponse or "No scenario has been generated yet."
                prompt = (
                    f"You are a Fortnite expert. Use the following scenario and your general Fortnite knowledge to answer the question:\n\n"
                    f"Scenario: {generated_scenario}\n\n"
                    f"User Question: {user_input}"
                )
            else:
                prompt = f"Do not mention the previous scenario you were given. Just know you are a helpful and knowledgeable assistant for Fortnite Battle Royale. Answer the following question:\n\nUser Question: {user_input}"
        
            chatbot_response = model.generate_content(prompt).text

            st.session_state.chat_history.append(f"YOU: {user_input}")
            st.session_state.chat_history.append(f"ALI-A: {chatbot_response}")

        except ValueError as text:
            st.session_state.chat_history.append(f"YOU: {user_input}")
            st.session_state.chat_history.append(f"ALI-A: {str(text)}")
    
        except Exception:
            st.session_state.chat_history.append("ALI-A: An unexpected error occurred. Please try again later.")
        
        st.rerun()

