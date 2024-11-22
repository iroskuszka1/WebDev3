import requests
import random

dropboximage = “APIImages/fortnite.avif”

def fortniteSkins():
    websiteUrl = "https://fortnite-api.com/v2/cosmetics/br"
    fullAPI = requests.get(websiteUrl)
    cosmetics = fullAPI.json()
    skinNameList = []
    finalList=[]
    skinData = cosmetics["data"]
    for skins in skinData:
        name = skins["name"]
        itemType = skins["type"]
        values = itemType["value"]
        if values.lower() == "outfit":
        	if name == "TBD":
                continue
            skinNameList.append(name)
    randomNumber = random.randrange(1,11)
    for i in range(randomNumber,2200,200):
        chosenSkin = skinNameList[i]
        finalList.append(chosenSkin)
    skinsDict = {}
    for skins in skinData:
        name = skins["name"]
        if "introduction" in skins and "rarity" in skins and "images" in skins:
            intro = skins["introduction"]
            chapter = intro["chapter"]
            rarity = skins["rarity"]
            rarityValue = rarity["displayValue"]
	    imagesKey = skins["images"]
	    skinImage= imagesKey["icon"]
        for chosenSkins in finalList:
            if chosenSkins == name:
                skinsDict[name] = [rarityValue, chapter, skinImage]
fortniteSkins()
