import csv
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Define keywords for your topic
TOPIC_KEYWORDS = ["غزة", "لبنان", "حرب", "إسرائيل", "السياسة", "وقف إطلاق النار"]

# Step 2: Function to calculate relevance score
def calculate_relevance_score(text, keywords):
    vectorizer = CountVectorizer().fit_transform([text, " ".join(keywords)])
    vectors = vectorizer.toarray()
    score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    return round(score * 10, 1)  # Scale score between 0-10

# Step 3: Create dataset
def create_dataset(input_file, output_csv, keywords):
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    # Open CSV for writing
    with open(output_csv, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Text", "Score"])  # Header row

        for line in lines:
            line = line.strip()
            if len(line) > 10:  # Ignore very short lines
                score = calculate_relevance_score(line, keywords)
                writer.writerow([line, score])
    
    print(f"Dataset saved to {output_csv}")

# Step 4: Generate the dataset
create_dataset("bbc_cleaned.txt", "aljazeera_data.csv", TOPIC_KEYWORDS)
