import random

def one_pull():
    pull = random.randint(1, 100)
    #Rare Pulls
    if pull <= 53:
        specific = round(random.uniform(1, 53), 4)
        if specific <= 5.8889:
            NIKKE = "Product 08"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 5.8889 and specific <= 11.7778:
            NIKKE = "Product 12"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 11.7778 and specific <= 17.6667:
            NIKKE = "Product 23"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 17.6667 and specific <= 23.5556:
            NIKKE = "Soldier EG"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 23.5556 and specific <= 29.4445:
            NIKKE = "Soldier FA"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 29.4445 and specific <= 35.3334:
            NIKKE = "Soldier OW"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 35.3334 and specific <= 41.2223:
            NIKKE = "iDoll Sun"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 41.2223 and specific <= 47.1112:
            NIKKE = "iDoll Ocean"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 47.1112 and specific <= 53.0000:
            NIKKE = "iDoll Flower"
            #print(f"You got {NIKKE}!")
            return NIKKE
              
    #Super Rare Pulls
    elif pull > 53 and pull <= 96:
        specific = round(random.uniform(53.0001, 96.0000), 4)
        if specific <= 57.7778:
            NIKKE = "Rapi"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 57.7778 and specific <= 62.5556:
            NIKKE = "Neon"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 62.5556 and specific <= 67.3334:
            NIKKE = "Anis"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 67.3334 and specific <= 72.1112:
            NIKKE = "Mica"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 72.1112 and specific <= 76.8890:
            NIKKE = "Belorta"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 76.8890 and specific <= 81.6668:
            NIKKE = "Ether"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 81.6668 and specific <= 86.4446:
            NIKKE = "Delta"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 86.4446 and specific <= 91.2224:
            NIKKE = "Mihara"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 91.2224 and specific <= 96.0000:
            NIKKE = "N102"
            #print(f"You got {NIKKE}!")
            return NIKKE     
    
    elif pull > 96 and pull <= 100:
        specific = round(random.uniform(96.0001, 100.0000), 4)
        #################################################
        #Elysion
        #################################################
        if specific > 96.0000 and specific <= 96.0674:
            NIKKE = "Diesel"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.0674 and specific <= 96.1347:
            NIKKE = "Miranda"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.1347 and specific <= 96.2019:
            NIKKE = "Vesti"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.2019 and specific <= 96.2692:
            NIKKE = "Emma"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.2692 and specific <= 96.3365:
            NIKKE = "Privaty"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.3365 and specific <= 96.4038:
            NIKKE = "Poli"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.4038 and specific <= 96.4711:
            NIKKE = "Eunhwa"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.4711 and specific <= 96.5384:
            NIKKE = "Helm"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.5384 and specific <= 96.6057:
            NIKKE = "Brid"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.6057 and specific <= 96.6730:
            NIKKE = "Soline"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.6730 and specific <= 96.7403:
            NIKKE = "Guillotine"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.7403 and specific <= 96.8076:
            NIKKE = "Maiden"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.8076 and specific <= 96.8749:
            NIKKE = "Signal"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.8749 and specific <= 96.9422:
            NIKKE = "D"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 96.9422 and specific <= 97.0096:
            NIKKE = "Mast"
            #print(f"You got {NIKKE}!")
            return NIKKE
        #################################################
        #Missilis
        #################################################
        elif specific > 97.0096 and specific <= 97.0768:
            NIKKE = "Centi"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.0768 and specific <= 97.1441:
            NIKKE = "Epinel"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.1441 and specific <= 97.2114:
            NIKKE = "Maxwell"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.2114 and specific <= 97.2787:
            NIKKE = "Liter"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.2787 and specific <= 97.3460:
            NIKKE = "Pepper"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.3460 and specific <= 97.4133:
            NIKKE = "Laplace"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.4133 and specific <= 97.4806:
            NIKKE = "Julia"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.4806 and specific <= 97.5479:
            NIKKE = "Drake"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.5479 and specific <= 97.6152:
            NIKKE = "Crow"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.6152 and specific <= 97.6825:
            NIKKE = "Admi"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.6825 and specific <= 97.7498:
            NIKKE = "Yuni"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.7498 and specific <= 97.8172:
            NIKKE = "Jackal"
            #print(f"You got {NIKKE}!")
            return NIKKE
        #################################################
        #Tetra
        #################################################
        elif specific > 97.8172 and specific <= 97.8845:
            NIKKE = "Alice"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.8845 and specific <= 97.9518:
            NIKKE = "Rupee"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 97.9518 and specific <= 98.0191:
            NIKKE = "Frima"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.0191 and specific <= 98.0864:
            NIKKE = "Mary"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.0864 and specific <= 98.1537:
            NIKKE = "Ludmilla"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.1537 and specific <= 98.2210:
            NIKKE = "Biscuit"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.2210 and specific <= 98.2883:
            NIKKE = "Noise"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.2883 and specific <= 98.3556:
            NIKKE = "Milk"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.3556 and specific <= 98.4229:
            NIKKE = "Yulha"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.4229 and specific <= 98.4902:
            NIKKE = "Folkwang"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.4902 and specific <= 98.5575:
            NIKKE = "Sakura"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.5575 and specific <= 98.6248:
            NIKKE = "Volume"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.6248 and specific <= 98.6921:
            NIKKE = "Sugar"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.6921 and specific <= 98.7594:
            NIKKE = "Exia"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.7594 and specific <= 98.8267:
            NIKKE = "Blanc"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.8267 and specific <= 98.8940:
            NIKKE = "Noir"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.8940 and specific <= 98.9613:
            NIKKE = "Dolla"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 98.9613 and specific <= 99.0286:
            NIKKE = "Viper"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.0286 and specific <= 99.0959:
            NIKKE = "Soda"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.0959 and specific <= 99.1632:
            NIKKE = "Yan"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.1632 and specific <= 99.2305:
            NIKKE = "Novel"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.2305 and specific <= 99.2978:
            NIKKE = "Coco"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.2978 and specific <= 99.3651:
            NIKKE = "Aria"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.3651 and specific <= 99.4324:
            NIKKE = "Rosanna"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.4324 and specific <= 99.4998:
            NIKKE = "Neru"
            #print(f"You got {NIKKE}!")
            return NIKKE
        
        #################################################
        #Pilgrim
        #################################################
        elif specific > 99.4999 and specific <= 99.5625:
            NIKKE = "Scarlet"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.5625 and specific <= 99.6250:
            NIKKE = "Rapunzel"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.6250 and specific <= 99.6875:
            NIKKE = "Snow White"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.6875 and specific <= 99.7500:
            NIKKE = "Noah"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.7500 and specific <= 99.8125:
            NIKKE = "Isabel"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.8125 and specific <= 99.8750:
            NIKKE = "Harran"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.8750 and specific <= 99.9375:
            NIKKE = "Modernia"
            #print(f"You got {NIKKE}!")
            return NIKKE
        elif specific > 99.9375 and specific <= 100.0000:
            NIKKE = "Dorothy"
            #print(f"You got {NIKKE}!")
            return NIKKE
        
def ten_pull():
    result = []
    
    for i in range(10):
        each_pull = one_pull()
        result.append(each_pull)
    
    #for j in result:
        #print(j, end=", ")
        
    return result
        
def scarlet_finder():
    found = False
    count = 0
    
    while not found:
        list = ten_pull()
        count += 10
        
        if "Scarlet" in list:
            found = True
            
    print(f"It takes {count} amount of pulls to get Scarlet")
    return True
        
#ten_pull()

scarlet_finder()

print()