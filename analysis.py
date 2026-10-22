
import csv
import statistics

# Read the sample dataset
with open("sample_data.csv", newline="", encoding="utf-8-sig") as file:
    first_line = file.readline()
    file.seek(0)

    delimiter = ";" if first_line.count(";") > first_line.count(",") else ","
    reader = csv.DictReader(file, delimiter=delimiter)

    # Remove extra spaces from column names
    reader.fieldnames = [name.strip() for name in reader.fieldnames]
    data = [
        {key.strip(): value.strip() for key, value in row.items()}
        for row in reader
    ]

# Extract numerical variables
ages = [int(row["Age"]) for row in data]
study_hours = [float(row["Study_Hours"]) for row in data]
scores = [float(row["Statistics_Score"]) for row in data]

# Calculate descriptive statistics
print("STATISTICAL COMPUTING RESULTS")
print("-----------------------------")
print("Number of students:", len(data))
print("Mean age:", round(statistics.mean(ages), 2))
print("Mean study hours:", round(statistics.mean(study_hours), 2))
print("Mean statistics score:", round(statistics.mean(scores), 2))
print("Median statistics score:", statistics.median(scores))
print("Standard deviation:", round(statistics.stdev(scores), 2))
print("Minimum score:", min(scores))
print("Maximum score:", max(scores))
