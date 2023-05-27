from datetime import datetime

def check_freshness(purchase_date, expiration_date, consumption_date):
    try:
        purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        consumption_date = datetime.strptime(consumption_date, "%Y-%m-%d")

        if purchase_date > expiration_date:
            print("Invalid input: Purchase date cannot be later than the expiration date.")
            return

        if consumption_date < purchase_date:
            print("Invalid input: Consumption date cannot be earlier than the purchase date.")
            return

        freshness_period = expiration_date - purchase_date
        days_since_purchase = consumption_date - purchase_date

        if days_since_purchase <= freshness_period:
            print("The food is fresh.")
        else:
            print("Warning: The food may not be fresh anymore.")
            print("Days since purchase: {}".format(days_since_purchase.days))
            print("Freshness period: {} days".format(freshness_period.days))

    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")

# Example usage
purchase_date = "2023-05-20"
expiration_date = "2023-05-30"
consumption_date = "2023-05-26"

check_freshness(purchase_date, expiration_date, consumption_date)
