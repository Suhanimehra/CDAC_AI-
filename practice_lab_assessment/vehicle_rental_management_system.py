import csv
rentals=[]
filename="rentals.csv"
def save_to_csv():
    global filename
    with open(filename,mode='w',newline='') as file:
        fieldname=["id","vehicle","type","customer","days","rate","status"]
        
        writer=csv.DictWriter(file,fieldnames=fieldname)
        
        writer.writeheader()
        writer.writerows(rentals)
    print("saved")
    
def load_to_csv():
    with open(filename , mode='r',newline='') as file:
        reader=csv.DictReader(file)
        
        rentals=[]
        
        for row in reader:
            row['id']=int(row['id'])
            row['id']=int(row['id'])
            row['id']=int(row['id'])
            row['id']=int(row['id'])
            row['id']=int(row['id'])
            row['id']=int(row['id'])
            row['id']=int(row['id'])
            row['id']=int(row['id'])
            
            rentals.append(row)
    
    if rentals:
        id_counter=max(r['id'] for r in rentals) + 1