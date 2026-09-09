import csv
import json


def process_student_records(input_csv_path, output_json_path):
    records = []

    with open(input_csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["score"] = float(row["score"])
            records.append(row)
            
    if not records:
        summary = {
            "total_students": 0,
            "average_score": 0,
            "top_scorer": None,
            "course_counts": {}
        }

    else:
        total_students = len(records)

        
        average_score = round(
            sum(record["score"] for record in records) / total_students,
            2
        )

        
        top_student = max(records, key=lambda record: record["score"])

        top_scorer = {
            "name": top_student["name"],
            "score": top_student["score"]
        }

        
        course_counts = {}

        for record in records:
            course = record["course"]
            course_counts[course] = course_counts.get(course, 0) + 1

        summary = {
            "total_students": total_students,
            "average_score": average_score,
            "top_scorer": top_scorer,
            "course_counts": course_counts
        }

    
    with open(output_json_path, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)



if __name__ == "__main__":
    process_student_records("students.csv", "summary.json")
    print("Student summary created successfully.")