weather = (1,0,0,1,1,1,0)

sunny = 0
rainy = 0

for i in range(0, len(weather)):
    
    if(weather[i] == 0):
        rainy = rainy + 1
        
    else:
        sunny = sunny + 1
        
if(sunny > rainy): 
    print("Gooooodddd weather")
    
else:
    print("Baaadddddd weather") 