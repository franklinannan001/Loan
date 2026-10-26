# prompt the applicant for their name, credit score, monthly income, and missed payments, and print the output
def main():
    name = input("What is your name: ").strip()
    formatted_name = format_applicant(name)
    try:
        credit_score = int(input("What is your credit score: "))
        monthly_income = float(input("What is your monthly income: "))
        missed_payments = int(input("How many missed payments do you have: "))
        decision = get_decision(credit_score, monthly_income, missed_payments)
        if decision is not None:
            message = get_message(decision)
            print(
                f"{formatted_name} has a credit score of {credit_score:.0f} with KSH {monthly_income:,.2f} income — {decision}. {message}"
            )
        else:
            return None
    except ValueError:
        pass


# return the applicant's name in title case
def format_applicant(n):
    n = n.title()
    return n


# return the decision based on the applicant's credit score, monthly income and missed payments
def get_decision(credit_score, monthly_income, missed_payments):
    if (
        credit_score < 300
        or credit_score > 850
        or monthly_income < 0
        or missed_payments < 0
    ):
        return None
    elif missed_payments > 2 or monthly_income < 15000 or credit_score < 580:
        return "Rejected"
    elif credit_score >= 750:
        return "Excellent Terms"
    elif credit_score >= 650:
        return "Standard Terms"
    else:
        return "High-Interest Terms"


# return the message after determining the decision
def get_message(decision):
    match decision:
        case "Excellent Terms":
            return "You qualify for our best rate."
        case "Standard Terms":
            return "Approved at standard rate."
        case "High-Interest Terms":
            return "Approved, but at a higher rate."
        case "Rejected":
            return "Application does not meet requirements."


if __name__ == "__main__":
    main()
