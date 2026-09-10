def process_dataset(dataset):
    
    parsed_data = list(map(
        lambda item: (
            item[0],
            float(item[1].split(":")[1].strip()),
            float(item[2].split(":")[1].strip())
        ),
        dataset
    ))

    
    filtered_data = filter(
        lambda item: item[1] <= 1000.0,
        parsed_data
    )

    
    mapped_data = list(map(
        lambda item: {
            "product": item[0],
            "price": item[1],
            "score": item[2]
        },
        filtered_data
    ))

    
    sorted_data = sorted(
        mapped_data,
        key=lambda item: item["score"],
        reverse=True
    )

    return sorted_data



data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]

print(process_dataset(data_input))
