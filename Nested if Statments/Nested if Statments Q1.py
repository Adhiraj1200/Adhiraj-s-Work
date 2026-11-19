mood = input("Enter your mood:")
weather = input("Enter the weather:")
if mood == "happy":
    if weather == "sunny":
       print("Suggested Playlist: Pop Hits")
    if weather != "sunny":
       print("Suggested Playlist: Top Charts")
        
elif mood == "sad":
    if weather == "rainy":
       print("Suggested Playlist: Sad Acoustic")
    if weather != "sunny":
        print("Suggested Playlist: Top Charts")
        
elif mood == "Relaxed":
    print("Suggested Playlist: Chill Vibes")
    
else:
    print("Top Charts")

    
    
    
    
