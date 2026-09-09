import csv
import json


def convert_log_file(input_log_path, output_csv_path, output_json_path):
    records = []

    
    with open(input_log_path, "r", encoding="utf-8") as file:

        for line in file:
            line = line.strip()

            
            if not line:
                continue

            parts = [part.strip() for part in line.split("|")]

            timestamp = parts[0]
            user_id = parts[1]
            endpoint = parts[2]
            status_code = int(parts[3])

            record = {
                "timestamp": timestamp,
                "user_id": user_id,
                "endpoint": endpoint,
                "status_code": status_code
            }

            records.append(record)
    
    fieldnames = [
        "timestamp",
        "user_id",
        "endpoint",
        "status_code"
    ]

    with open(output_csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(records)

    
    with open(output_json_path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)


if __name__ == "__main__":
    convert_log_file(
        "server_access.log",
        "access_records.csv",
        "access_records.json"
    )

    print("Log conversion completed successfully.")