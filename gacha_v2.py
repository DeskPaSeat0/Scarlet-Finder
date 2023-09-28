import random

pilgrims = ["Dorothy", "Harran", "Isabel", "Modernia", "Noah", "Rapunzel", "Scarlet", "Snow White"]

all_SSRs = ["Admi", "Alice", "Aria", "Biscuit", "Blanc", "Brid", "Centi", "Cocoa", "Crow", "D", "Diesel", "Dolla", "Drake", "Emma", "Epinel",
            "Eunhwa", " Exia", "Folkwang", "Frima", "Guillotine", "Helm", "Jackal", "Julia", "Laplace", "Liter", "Ludmilla", "Maiden", "Mary",
            "Mast", "Maxwell", "Milk", "Miranda", "Nero", "Noir", "Noise", "Novel", "Pepper", "Poli", "Privaty", "Rosanna", "Rupee", "Sakura", 
            "Signal", "Soda", "Soline", "Sugar", "Vesti", "Viper", "Volume", "Yan", "Yulha", "Yuni"]

all_SRs = ["Delta", "Neon", "Rapi", "Ether", "Mihara", "N102", "Anis", "Belorta", "Mica"]

all_Rs = ["Soldier EG", "Soldier FA", "Soldier OW", "Product 08", "Product 12", "Product 23", "iDoll Flower", "iDoll Ocean", "iDoll Sun"]

#elysion_SSRs = ["Brid", "D", "Diesel", "Emma", "Eunhwa", "Guillotine", "Helm", "Maiden", "Mast", "Miranda", "Poli", "Privaty", "Signal", 
#                "Soline", "Vesti"]
#elysion_SRs = ["Delta", "Neon", "Rapi"]
#elysion_Rs = ["Soldier EG", "Soldier FA", "Soldier OW"]

#missilis_SSRs = ["Admi", "Centi", "Crow", "Drake", "Epinel", "Jackal", "Julia", "Laplace", "Liter", "Maxwell", "Pepper", "Yuni"]
# missilis_SRs = ["Ether", "Mihara", "N102"]
# missilis_Rs = ["Product 08", "Product 12", "Product 23"]

#tetra_SSRs = ["Alice", "Aria", "Biscuit", "Blanc", "Cocoa", "Dolla", "Exia", "Folkwang", "Frima", "Ludmilla", "Mary", "Milk", "Nero", 
#              "Noir", "Noise", "Novel", "Rosanna", "Rupee", "Sakura", "Soda", "Sugar", "Viper", "Volume", "Yan", "Yulha"]
# tetra_SRs = ["Anis", "Belorta", "Mica"]
# tetra_Rs = ["iDoll Flower", "iDoll Ocean", "iDoll Sun"]

#SSR Drop Rate = 4%
#SR Drop Rate = 43%
#R Drop Rate = 53%

#Pilgrim Drop Rate = 0.0625% x 8
#Regular SSR Drop Rate = 0.0673%
#Wishlisted SSR Drop Rate = 0.2333% x 15
#Regular SR Drop Rate = 4.7778%
#Regular R Drop Rate = 5.8889%

def general_pull():
    randRarity = round(random.uniform(0, 100), 4)
    
    if(randRarity >=0 and randRarity <= 4):
        
        randManufacturer = round(random.uniform(0, 4), 4)
        
        if(randManufacturer >= 0 and randManufacturer <= 0.5000):
            
            randPilgrim = random.randint(0, len(pilgrims) - 1)
            return pilgrims[randPilgrim]
            # print(f"You got a {pilgrims[randPilgrim]}")
            
        elif(randManufacturer > 0.5 and randManufacturer <= 4):
            randSSR = random.randint(0, len(all_SSRs) - 1)
            return all_SSRs[randSSR]
            # print(f"You got a {all_SSRs[randPilgrim]}")
            
    elif(randRarity > 4 and randRarity <= 44):
        
        randSR = random.randint(0, len(all_SRs) - 1)
        return all_SRs[randSR]
        # print(f"You got a {all_SRs[randSR]}")    
    
    elif(randRarity > 44 and randRarity <= 100):
        randR = random.randint(0, len(all_Rs) - 1)
        return all_Rs[randR]
        # print(f"You got a {all_Rs[randR]}")
        
        
def ten_pull():
    count = 0
    result = []

    while count < 10:
        pull = general_pull()
        result.append(pull)
        count += 1     

    # for i in range(0, len(result)):
    #     print(result[i])
        
    return result
    

def scarlet_finder():
    found = False
    count = 0
    
    while not found:
        list = ten_pull()
        count += 10
        
        if "Scarlet" in list:
            found = True
            
    print(f"It takes {count} pulls to get Scarlet")
    return True

scarlet_finder()



