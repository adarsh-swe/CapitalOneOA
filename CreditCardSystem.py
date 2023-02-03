import json 
import datetime

def calculatePoints(spending):
    points = 0
    # Rule 1 
    if ((spending["sportcheck"] >= 7500) and (spending["tim_hortons"] >= 2500) and (spending["subway"] >= 2500)):
        multiplier = min(spending["sportcheck"]//7500, spending["tim_hortons"]//2500, spending["subway"]//2500)
        spending["sportcheck"] -= multiplier*7500
        spending["tim_hortons"] -= multiplier*2500
        spending["subway"] -= multiplier*2500
        points += multiplier*500
    # Rule 2 
    if ((spending["sportcheck"] >= 7500) and (spending["tim_hortons"] >= 2500)):
        multiplier = min(spending["sportcheck"]//7500, spending["tim_hortons"]//2500)
        spending["sportcheck"] -= multiplier*7500
        spending["tim_hortons"] -= multiplier*2500
        points += multiplier*300
    # Rule 3 
    if ((spending["sportcheck"] >= 7500)):
        multiplier = spending["sportcheck"]//7500
        spending["sportcheck"] -= multiplier*7500
        points += multiplier*200
    # Rule 4 
    if ((spending["sportcheck"] >= 2500) and (spending["tim_hortons"] >= 1000) and (spending["subway"] >= 1000)):
        multiplier = min(spending["sportcheck"]//2500, spending["tim_hortons"]//1000, spending["subway"]//1000)
        spending["sportcheck"] -= multiplier*2500
        spending["tim_hortons"] -= multiplier*1000
        spending["subway"] -= multiplier*1000
        points += multiplier*150
    # Rule 5
    if ((spending["sportcheck"] >= 2500) and (spending["tim_hortons"] >= 1000)):
        multiplier = min(spending["sportcheck"]//2500, spending["tim_hortons"]//1000)
        spending["sportcheck"] -= multiplier*2500
        spending["tim_hortons"] -= multiplier*1000
        points += multiplier*75
    # Rule 6 
    if ((spending["sportcheck"] >= 2000)):
        multiplier = spending["sportcheck"]//2000
        spending["sportcheck"] -= multiplier*2000
        points += multiplier*75
    # Rule 7 
    points += spending["sportcheck"]//100
    points += spending["tim_hortons"]//100
    points += spending["subway"]//100
    return points

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
    print("Customer is awarded " + str(points) + " points")

main()
