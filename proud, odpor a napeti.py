napeti = float(input("zadej hodnotu napětí"))
proud = float(input("zadej hodnotu proudu"))

odpor = napeti / proud 

print("hodnota odporu je", odpor,"ohmů")

#...............................................................

odpor = float(input("zadej hodnotu odporu"))
napeti = float(input("zadej hodnotu napeti"))

proud = napeti / odpor

print("hodnota proudu je", proud,"amperů")

#...............................................................

odpor = float(input("zadej hodnotu odporu"))
proud = float(input("zadej hodnotu proudu"))

napeti = odpor * proud 

print("hodnota napětí je", napeti,"voltů")
