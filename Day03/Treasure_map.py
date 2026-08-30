def coordinates():
    
    coords=[[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
    
    
    
    valid=[coord for coord in coords if coord[0]>1 and coord[1]>0]
    # valid = [[x, y] for x, y in coords if x > 0 and y > 0]

               
    print(valid)
coordinates()