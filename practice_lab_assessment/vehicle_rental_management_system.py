import csv
rentals=[
    {"id": 1, "vehicle": "Honda City", "type": "Car", "customer": "Rahul", "days": 4, "rate": 1800, "status": "Medium Rental"}
    ,{"id": 2, "vehicle": "Honda City", "type": "Car", "customer": "Rahul", "days": 4, "rate": 1800, "status": "Medium Rental"}
]
filename="rentals.csv"

def main():
    while True:
        choice=int(input("1 for save 2 for load."))
        
        match choice:
            case 1:
                save_to_csv()
            case 2:
                load_to_csv()
            
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
    print("loaded Successfully")
    if rentals:
        id_counter=max(r['id'] for r in rentals) + 1
        
if __name__=='__main__':
    main()