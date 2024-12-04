# Lab 3: Deep Learning for NLP with Sequence Models and Transformers
## Overview
This repository contains the implementation of Lab 3 for the Master's in Big Data program at the Faculty of Sciences and Techniques in Tangier. The objective of the lab is to develop and evaluate various deep learning models for natural language processing (NLP) tasks, focusing on classification and text generation. The lab leverages PyTorch to implement and fine-tune deep neural network architectures.

## Objectives
1. Scrape Arabic text data on a chosen topic and prepare a dataset with relevance scores (0-10).
2. Preprocess the data using NLP techniques (tokenization, stemming, lemmatization, stop-word removal, discretization, etc.).
3. Implement and evaluate sequence models for classification:
  - Recurrent Neural Networks (RNN)
  - Bidirectional RNNs (BiRNN)
  - Gated Recurrent Units (BiGRU)
  - Long Short-Term Memory Networks (LSTM)
4. Fine-tune a pre-trained GPT-2 model for text generation tasks.
5. Report and analyze the performance of all models using metrics like accuracy, BLEU, MSE, MAE, and R².
## Dataset
The Arabic text data was scraped using Python libraries (BeautifulSoup/Scrapy) from BBC Arabia. Each text sample was assigned a relevance score ranging from 0 to 10.

Example Dataset Format:
| Text | Score |
|-----------|--------|
| حرب اوكرانيا      | 2.5   |
|الحرب علي غزه عمليات للمقاومه بجباليا واسرائيل تعتقل بجنوب لبنان       | 1.1   |
|كيف قرا اهالي غزه اتفاق وقف اطلاق النار في لبنان       | 3.4   |
| ...       | ...    |

	


# Part 1: Classification Task
## Dataset
**Stories Dataset**
### 1. Requests and BeautifulSoup:
  - Fetches the HTML content from the website and parses it.
  - Finds all visible text using soup.find_all(text=True).

### 2. Arabic Text Filtering:
  - Uses a regular expression ([\u0600-\u06FF]+) to match Arabic Unicode characters only.
  - Collects and filters any visible Arabic text.

### 3. Saving to File:
  - Saves the extracted Arabic text into a file named kolalkotob_arabic_text.txt.
  - Each line in the file contains one segment of Arabic text.

### 4. Data Cleaning:
  - Use regular expressions to remove non-informative content like navigation menus, duplicated phrases, and filler text (e.g., "إذهب إلى المحتوى").
  - Keep only relevant sections containing actual news content or article summaries.

### 5. Normalization:
  - Normalize Arabic text by:
  - Unifying variations like "أ" and "إ" into "ا".
  - Removing diacritics if not necessary for the task.

### 6. Content Segmentation:
  - Group data by categories (e.g., "Politics," "Economy," "Sports").
  - For each article, extract only the headline, description, and possibly the timestamp.

### 7. Analysis Potential:
  - BBC Data:
    - Topics span international and regional news, making it suitable for topic modeling.
    - Good for sentiment analysis and stance detection related to global politics.

### 8. Topic Keywords:
  - You define relevant keywords for your chosen topic in TOPIC_KEYWORDS.

### 9. Relevance Score Calculation:
  - Uses cosine similarity between the text and the topic keywords to assign a relevance score.
  - Scores are scaled between 0 and 10.

### 10. CSV File Generation:
  - The script reads cleaned text from the file and writes it into a CSV file with two columns: Text and Score.

### 11. Result:
  - One CSV files (aljazeera_data.csv) with text and corresponding relevance scores.

## Preprocessing Pipeline
  - Tokenization
  - Stemming and Lemmatization
  - Stop-words removal
  - Discretization
## Model Architectures and Results
### 1. RNN
  - Training Loss over Epochs:
    [1.3796, 1.0687, 1.1039, 1.1509, 1.0052, 0.9054, 0.8388, 0.8316, 0.8853, 0.9201]
  - Metrics:
    - Training: MSE = 37.96, MAE = 2.0371, R² = -0.5011, Accuracy = 85.94%
    - Testing: MSE = 26.29, MAE = 1.5194, R² = -0.7279, Accuracy = 87.99%
### 2. BiRNN
  - Training Loss over Epochs:
    [0.9742, 0.5513, 0.4051, 0.3053, 0.2170, 0.1668, 0.1079, 0.0803, 0.0510, 0.0362]
  - Metrics:
    - Training: MSE = 0.5137, MAE = 0.0309, R² = 0.9797, Accuracy = 99.73%, BLEU = 0.9973
    - Testing: MSE = 6.523, MAE = 0.6926, R² = 0.5713, Accuracy = 90.11%, BLEU = 0.9011
### 3. BiGRU
  - Training Loss over Epochs:
    [1.0261, 0.5891, 0.4420, 0.3942, 0.2912, 0.2121, 0.1533, 0.1043, 0.0789, 0.0622]
  - Metrics:
    - Training: MSE = 0.0548, MAE = 0.0106, R² = 0.9978, Accuracy = 99.73%
    - Testing: MSE = 5.3958, MAE = 0.5901, R² = 0.6454, Accuracy = 90.46%
### 4. LSTM
  - Training Loss over Epochs:
    [1.1123, 0.6933, 0.5175, 0.3984, 0.3169, 0.2243, 0.1607, 0.1113, 0.0952, 0.0657]
  - Metrics:
    - Training: MSE = 0.7984, MAE = 0.0522, R² = 0.9684, Accuracy = 99.29%
    - Testing: MSE = 5.4629, MAE = 0.6007, R² = 0.6410, Accuracy = 90.81%

# Part 2: Transformer (Text Generation)
## Dataset
**Stories Dataset**
  - URL: [Kaggle - Stories Dataset](https://www.kaggle.com/datasets/shubchat/1002-short-stories-from-project-guttenberg)

## Model Implementation
  - Pre-trained GPT-2 model from pytorch-transformers.
  - Fine-tuned on the scraped Arabic text dataset.

## Results
  - Training Loss (Selected Batches, Epoch 1):
    Batch 10: 3.4116, Batch 50: 1.9235, Batch 100: 2.1501
  - Final Loss (Epoch 10):
    Batch 10: 1.7579, Batch 50: 1.3079, Batch 150: 1.0425

## Generated Story:
Once upon a time in a dystopian world, there was a man who was willing to sacrifice his own life for the betterment of mankind...

## Key Learnings
  - Familiarized with PyTorch for deep learning.
  - Enhanced understanding of sequence models and their comparative performance.
  - Learned how to preprocess Arabic text for NLP tasks.
  - Developed skills in fine-tuning transformer models for text generation.

## Tools and Libraries
  - Programming Languages: Python
  - Libraries: PyTorch, BeautifulSoup, Scrapy, Transformers
  - Development Platforms: Google Colab, Kaggle
  - Version Control: GitHub
