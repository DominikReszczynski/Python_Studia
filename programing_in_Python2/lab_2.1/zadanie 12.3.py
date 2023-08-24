def metr (foots):
    footToMeters=foots*(0.3048)
    return footToMeters
def centimeter(foots):
    footToCentimeter=foots*(30.48)
    return footToCentimeter
def milimeters(foots):
    footToMilimeters=foots*(304.8)
    return footToMilimeters
def kilometers(foots):
    footsToKilometers = foots*0.0003048
    return footsToKilometers
foots=int(input("podaj ilość stup: "))
print("podana ilość stup to:", foots, "na milimetry to:",milimeters(foots),"na cm to:", centimeter(foots),"na m:", metr(foots),"na km:", kilometers(foots))