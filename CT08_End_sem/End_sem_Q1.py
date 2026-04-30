
"""
============================================================
Q1. Customer VIP Classification
============================================================
You are working with a dictionary of customer spending.
The program must classify customers into VIP and non-VIP groups.

Program Requirements:
- Use the dictionary:
  customer_spending = {
      "Alice": 950, "Bob": 1200, "Charlie": 500, 
      "Diana": 1800, "Ethan": 2200, "Fiona": 700, 
      "John": 685, "Hor Kee": 1389, "Siew Ling": 235, 
      "Matt": 452, "Kristen": 985, "Johnson": 785, 
      "Charles": 2352, "Tommy": 741, "Laura": 689 }

- Create two dictionaries:
  vip → spending > 1000
  non_vip → spending ≤ 1000

- Loop through the dictionary and classify customers

Print the result in this format for each customer:
    Hi Bob, you are now a VIP! Congratulations!
    Hi Charlie, spend $500 more to become a VIP member!

Note:
- These are example lines only
- Your program should print a message for every customer

============================================================
"""

# ============================================================
# Step 1: Create dictionaries
# ============================================================
customer_spending = {"Alice": 950, "Bob": 1200, "Charlie": 500, "Diana": 1800, "Ethan": 2200, "Fiona": 700, "John": 685, "Hor Kee": 1389, "Siew Ling": 235, "Matt": 452, "Kristen": 985, "Johnson": 785, "Charles": 2352, "Tommy": 741, "Laura": 689}
vip={}
non_vip={}


# ============================================================
# Step 2: Loop through customer_spending
# ============================================================
for name in customer_spending:



    # ============================================================
    # Step 3: Group customers into vip / non_vip
    # ============================================================

    if customer_spending[name]>1000:
        vip[name] = customer_spending[name]
    elif customer_spending[name] <= 1000:
        non_vip[name]=customer_spending[name]

# ============================================================
# Step 4: Print customer messages
# ============================================================
for name in vip:
    print(f"Hi {name}! you are now a VIP! Congratulations!")
for name in non_vip:
    print(f"Hi {name}, spend ${1000-non_vip[name]} more to become a VIP member!")