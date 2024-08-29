# Task 1: Keyword Highlighter
# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", 
# and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords 
# in uppercase so they stand out.

reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", 
           "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", 
           "The product was average. Nothing extraordinary about it."]
words_to_find = ["good", "excellent", "bad", "Poor", "average"]

for review in reviews:
    for word in words_to_find:
        review = review.replace(word, word.upper())
    print(review)

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
positive_counts = []
negative_counts = []
def word_count():
    for review in reviews:
        review_lower = review.lower()
        for word in positive_words:
            positive_count = review_lower.count(word)
            positive_counts.append(positive_count)
        for word in negative_words:
            negative_count = review_lower.count(word)
            negative_counts.append(negative_count)
    return f"Positive words: {sum(positive_counts)}; Negative words: {sum(negative_counts)}"
            
print(word_count())

# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

for review in reviews:
    summary = review[:30]
    last_space = summary.rfind(' ')
    if last_space == -1:
        print(f"{summary}...")
    else:
        print(f"{summary[:last_space]}...")