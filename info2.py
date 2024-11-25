import requests
import random

dropboximage = "APIFiles/fortnitecover.jpg"
mapImage = "APIFiles/map_en.png"

finalList = []
skinsDict = {}
def fortniteSkins():
    websiteUrl = "https://fortnite-api.com/v2/cosmetics/br"
    fullAPI = requests.get(websiteUrl)
    cosmetics = fullAPI.json()
    skinNameList = []
    skinData = cosmetics["data"]
    for skins in skinData:
        name = skins["name"]
        itemType = skins["type"]
        values = itemType["value"]
        if values == "outfit":
            if name == "TBD" or name == "null":
                continue
            else:
                skinNameList.append(name)


    randomNumber = random.randrange(0,200)
    for i in range(randomNumber,2000,200):
        chosenSkin = skinNameList[i]
        finalList.append(chosenSkin)
    for skins in skinData:
        name = skins["name"]
        if "introduction" in skins and "rarity" in skins and "images" in skins:
            intro = skins["introduction"]
            chapter = intro["chapter"]
            rarity = skins["rarity"]
            rarityValue = rarity["displayValue"]
            imagesKey = skins["images"]
            if "icon" in imagesKey:
                skinImage = imagesKey["icon"]
            elif "smallIcon" in imagesKey:
                skinImage = imagesKey["smallIcon"]
        for chosenSkins in finalList:
            if chosenSkins == name:
                skinsDict[name] = [rarityValue, chapter, skinImage]

    print(finalList)
    print(skinsDict) 
print(fortniteSkins())

finalBannerList = []
def fortniteBanners():
    global finalBannerList
    websiteUrl = "https://fortnite-api.com/v1/banners"
    fullAPI = requests.get(websiteUrl)
    cosmetics = fullAPI.json()

    bannerList = []
    bannerData = cosmetics["data"]
    for banners in bannerData:
        name = banners["name"]
        if "images" in banners:
            imagesKey = banners["images"]
            if "icon" in imagesKey:
                image = imagesKey["icon"]
        bannerList.append(image)
    
    finalBannerList = []
    ranNum = random.randrange(0,251)
    for i in range(ranNum,753,250):
        chosenBanner = bannerList[i]
        finalBannerList.append(chosenBanner)
    
print(fortniteBanners())


finalLocationList = []
def fortnitePOIS():
    global finalLocationList
    websiteUrl = "https://fortnite-api.com/v1/map"
    fullAPI = requests.get(websiteUrl)
    locations = fullAPI.json()

    mapData = locations["data"]
    pois = mapData["pois"]
    poiList = []
    for locations in pois:
        name = locations["name"]
        poiList.append(name)

    ranNum3 = random.randrange(0,13)
    for i in range(ranNum3,78,13):
        chosenLocation = poiList[i]
        if chosenLocation[0] == "??" or chosenLocation[0] == "?":
            finalLocationList.append("Mystery")
        else:
            finalLocationList.append(chosenLocation)

print(fortnitePOIS())
