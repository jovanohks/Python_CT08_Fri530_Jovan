"""
============================================================
Q2. Review Text Analysis
============================================================
You are given a text file containing customer reviews.
The program must analyse the reviews and generate a rating.

Program Requirements:
- Read the contents of the file "reviews.txt"
- Count the total number of characters in the file
- Count how many reviews contain "good"
- Count how many reviews contain "bad"
- Calculate the percentage of good reviews
- Determine the overall rating:
    70% and above → Positive
    40% to 69% → Mixed
    Below 40% → Negative
- Save the results into "review_results.txt" and also print the results to the console

Note:
- The counting must be case-insensitive
- The percentage must be rounded to 2 decimal places
- If there are no valid reviews, the percentage should be 0

Print and save the result in this format:
    Review Text Analysis
    ------------------------------
    Total Characters: <number>
    Good Reviews: <number>
    Bad Reviews: <number>
    Percentage of Good Reviews: <value>%
    Overall Rating: <rating>

============================================================
"""

# ============================================================
# Step 1: Read file contents
# ============================================================
import os

with open("reviews.txt", "r") as file:
    reviews=file.readlines()
with open("reviews.txt","r") as file:
    lines=file.read()

    


# ============================================================
# Step 3: Count characters and good or bad reviews
# ============================================================
good_reviews=0
bad_reviews=0
for review in reviews:
    if "good" in review.lower():
        good_reviews +=1
    elif "bad" in review.lower():
        bad_reviews +=1



# ============================================================
# Step 4: Calculate percentage and rating
# ============================================================
total_reviews=good_reviews+bad_reviews
percentage=(good_reviews/total_reviews)*100
rating=""
if percentage>=70:
    rating="positive"
elif percentage <70 and percentage >=40:
    rating="mixed"
elif percentage <40:
    rating="negative"


characters=len(lines)
# ============================================================
# Step 5: Write results to file
# ============================================================
with open("review_results.txt","w") as file:
    file.write("Review Text Analysis\n")
    file.write("------------------------------\n")
    file.write(f"Total Characters: {characters}\n")
    file.write(f"Good Reviews: {good_reviews}\n")
    file.write(f"Bad Reviews: {bad_reviews}\n")
    file.write(f"percentage of good reviews: {percentage:.2f}%\n")
    file.write(f"Overall Rating: {rating}")

               


# ============================================================
# Step 6: Print results to console
# ============================================================
print("Review Text Analysis")
print("------------------------------")
print(f"Total Characters: {characters}")
print(f"Good Reviews: {good_reviews}")
print(f"Bad Reviews: {bad_reviews}")
print(f"percentage of good reviews: {percentage:.2f}%")
print(f"Overall Rating: {rating}")