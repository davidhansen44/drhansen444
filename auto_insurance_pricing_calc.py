import math
import csv
from datetime import datetime


BASE_PREMIUM = 1200.00

VEHICLE_FACTORS_FILE = "vehicle_factors.csv"


def calculate_age_factor(age):
    

    if age < 18:
        return 2.00
    elif age <= 24:
        return 1.60
    elif age <= 29:
        return 1.30
    elif age <= 64:
        return 1.00
    elif age <= 74:
        return 1.15
    else:
        return 1.30


def calculate_vehicle_factor(vehicle_type):
   

    vehicle_type = vehicle_type.lower()

    factors = {
        "economy": 0.90,
        "sedan": 1.00,
        "suv": 1.10,
        "truck": 1.15,
        "sports": 1.50,
        "luxury": 1.60
    }

    return factors.get(vehicle_type, 1.20)


def calculate_driving_history_factor(accidents, tickets):

    factor = 1.00

    factor += accidents * 0.20
    factor += tickets * 0.10

    return factor


def calculate_mileage_factor(miles):

    if miles < 5000:
        return 0.85
    elif miles <= 10000:
        return 1.00
    elif miles <= 15000:
        return 1.10
    elif miles <= 20000:
        return 1.25
    else:
        return 1.40


def calculate_claim_risk_score(accidents, tickets, miles, age):

    score = 0

    
    if age < 25:
        score += 25
    elif age < 30:
        score += 15
    elif age < 65:
        score += 5
    else:
        score += 10

    
    score += accidents * 15

   
    score += tickets * 8

    
    if miles > 20000:
        score += 20
    elif miles > 15000:
        score += 15
    elif miles > 10000:
        score += 10
    elif miles > 5000:
        score += 5


    score = min(score, 100)

    return score


def calculate_base_premium(age, vehicle_type, accidents, tickets, miles):

    age_factor = calculate_age_factor(age)
    vehicle_factor = calculate_vehicle_factor(vehicle_type)
    driving_history_factor = calculate_driving_history_factor(
        accidents, tickets
    )
    mileage_factor = calculate_mileage_factor(miles)

    premium = (
        BASE_PREMIUM
        * age_factor
        * vehicle_factor
        * driving_history_factor
        * mileage_factor
    )

    return premium


def calculate_final_premium(base_premium, claim_risk_score):

    risk_factor = 1 + (claim_risk_score / 200)

    final_premium = base_premium * risk_factor

    return final_premium


def get_driver_information():

    print(" " + "=" * 50)
    print("AUTO INSURANCE PRICING MODEL")
    print("=" * 50)

    name = input(" Driver's name: ")

    birth_date = input(" Date of birth (MM/DD/YYYY): ")

    
    birth_date = datetime.strptime(birth_date, "%m/%d/%Y")

    today = datetime.today()


    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    
    print()
    print("economy")
    print("sedan")
    print("suv")
    print("truck")
    print("sports")
    print("luxury")
    vehicle_type = input("Vehicle type: ")

    
    print()
    accidents = int(input("Number of accidents in the last 3 years: "))
    print()
    tickets = int(input("Number of tickets in the last 3 years: "))
    print()
    miles = int(input("Estimated annual mileage: "))

    return name, age, vehicle_type, accidents, tickets, miles


def main():

    name, age, vehicle_type, accidents, tickets, miles = get_driver_information()

    age_factor = calculate_age_factor(age)
    vehicle_factor = calculate_vehicle_factor(vehicle_type)
    driving_history_factor = calculate_driving_history_factor(
        accidents, tickets
    )
    mileage_factor = calculate_mileage_factor(miles)

    claim_risk_score = calculate_claim_risk_score(
        accidents,
        tickets,
        miles,
        age
    )

    base_premium = calculate_base_premium(
        age,
        vehicle_type,
        accidents,
        tickets,
        miles
    )

    final_premium = calculate_final_premium(
        base_premium,
        claim_risk_score
    )

    print(" " + "=" * 50)
    print("INSURANCE PRICING RESULTS")
    print("=" * 50)

    print(f"Driver: {name}")
    print(f"Age: {age}")
    print(f"Vehicle: {vehicle_type}")
    print(f"Annual Mileage: {miles:,}")

    print("Risk Factors")
    print("-" * 50)
    print(f"Age Factor:              {age_factor:.2f}")
    print(f"Vehicle Factor:          {vehicle_factor:.2f}")
    print(f"Driving History Factor:  {driving_history_factor:.2f}")
    print(f"Mileage Factor:          {mileage_factor:.2f}")

    print("Risk Score")
    print("-" * 50)
    print(f"Estimated Claim Risk:    {claim_risk_score}/100")

    print("Premium")
    print("-" * 50)
    print(f"Base Premium:            ${base_premium:,.2f}")
    print(f"Estimated Annual Premium:${final_premium:,.2f}")
    print(f"Estimated Monthly Cost:  ${final_premium / 12:,.2f}")

    print(" " + "=" * 50)
    print("This is an educational estimate, not an actual quote.")
    print("=" * 50)

if __name__ == "__main__":
    main()