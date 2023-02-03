# CapitalOneOA

This python script is my solution for Capital One's Credit Card Reward Point System online assessment. 

## How to run the script:
1. intall python3
2. execute the script with `python3 CreditCardSystem.py` in terminal or run the file directly from any IDE

## Explanation:
  - There are two files in the script:
    - `CreditCardSystem.py` : This file contains the point calcualation algorithm 
    - `transactions.json` : This file contains the transaction data for a user for a month (I populated it with the given sample data for testing/demonstraction purposes)
  - In the script, transacition data is first parsed from the json file and the sum of cents spent at each merchant is stored in a dictionary 
  - The dictionary is passed to a helper function which calculates and returns the total points 
  - The algorithm:
    - In order to ensure the customer reciveves the most possible points, the rules are applied in order from 1 to 7
    - This is accomplished by applying each rule as many times as possible before moving on to the next rule. When determining how many times to apply a specifc rule, I found the multiplier (dollars spent / dollar requirement for the rule) for each merchant and took the smallest one as the multiplier for that rule in order to maximize the amount of times that rule was applied. Each time a rule is applied, the subtotal spending for each merchant is updated in the dictionary to ensure the following rules do not use the same dollar multiple times
    - The last rule (7) was implemented by divinding the remaining totals for each merchant by 100 and summing it to the point total
    - After each rule is applied, the total number of points is returned
    
## Future Improvements:
  - Given more time, I would implement a frontend for this application to display the point totals 
  - I could also display how the rules were applied for customers to view 
  - I could host a backend server that contains this algorithm so it is easier to access by the frontend (would consider redoing the entire thing with javascript for simplicity) 
