def playlist():
    
    playlist=["Inception", "The Matrix", "Interstellar"]
    
    new_movie = input("Enter a movie to add to the playlist: ")
    
    if new_movie not in playlist:
        playlist.append(new_movie)
        
    else:
        print(f"{new_movie} is already in the playlist.")
        
    playlist=sorted(playlist)
    
    print("Alphabetically sorted playlist is: ", playlist)

playlist()