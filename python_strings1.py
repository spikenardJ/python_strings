# Question 1: Product Review Analysis

# Task 1: Keyword Highlighter

print()
print("Reviews w/ Highlighted Keywords:")
def keyword_highlighter():
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
        ]
    keywords = ["good", "excellent", "bad", "poor", "average"]
    
    for review in reviews:
        for keyword in keywords:
            if keyword in review:
                print(review.replace(keyword, keyword.upper()))
            elif keyword.capitalize() in review:
                print(review.replace(keyword.capitalize(), keyword.upper()))

keyword_highlighter()


# Task 2: Sentiment Tally

print()
print("Positive & Negative Word Count:")
def word_tally(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    for review in reviews:
        for positive_word in positive_words:
            if positive_word in review:
                positive_count += 1
            elif positive_word.capitalize() in review:
                positive_count += 1
        for negative_word in negative_words:
            if negative_word in review:
                negative_count += 1
            elif negative_word.capitalize() in review:
                negative_count += 1
    return positive_count, negative_count

reviews = [
    "This product is really good. I'm impressed with its quality.",
            "The performance of this product is excellent. Highly recommended!",
            "I had a bad experience with this product. It didn't meet my expectations.",
            "Poor quality product. Wouldn't recommend it to anyone.",
            "The product was average. Nothing extraordinary about it."
            ]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
positive_count, negative_count = word_tally(reviews, positive_words, negative_words)

print(f"Their are {positive_count} positive reviews, and {negative_count} negative reviews.")


# Task 3: Review Summary

print()
print("Review Summaries:")
def review_summary():
    reviews = [
            "This product is really good. I'm impressed with its quality.",
            "The performance of this product is excellent. Highly recommended!",
            "I had a bad experience with this product. It didn't meet my expectations.",
            "Poor quality product. Wouldn't recommend it to anyone.",
            "The product was average. Nothing extraordinary about it."
            ]
    for review in reviews:
        if review[30] == " ":
            print(f"{review[0:31]}", end="...")
        else:
            print(f"{review[0:32]}", end="...")
        print()
review_summary()