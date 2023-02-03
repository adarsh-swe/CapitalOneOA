import json 
import datetime

def calculatePoints(spending):
    # Rule 1 
    

    # Rule 2 

    # Rule 3 

    # Rule 4 

    # Rule 5

    # Rule 6 

    # Rule 7 

    return 0

def main():
    # Read transaction data 
    file = open("./transactions.json");
    transactions = json.load(file)
    file.close()

    if (not transactions) : 
        print("No points awarded")
        return

    merchant_spending =  {
        "sportcheck" : 0,
        "tim_hortons" : 0,
        "subway" : 0
    }

    start_date = datetime.date.fromisoformat(transactions["T01"]["date"])

    # if the transaction is within the past month, sum each merchant's spending
    for t in transactions:
        date = datetime.date.fromisoformat(transactions[t]["date"]) 
        merchant = transactions[t]["merchant_code"]
        if date.month == start_date.month:
            merchant_spending[merchant] += transactions[t]["amount_cents"]
    
    points = calculatePoints(merchant_spending)

main()
