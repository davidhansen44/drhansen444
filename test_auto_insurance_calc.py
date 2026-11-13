from auto_insurance_pricing_calc import (
    calculate_age_factor,
    calculate_vehicle_factor,
    calculate_driving_history_factor,
    calculate_mileage_factor,
    calculate_claim_risk_score,
    calculate_base_premium,
    calculate_final_premium
)


def test_calculate_age_factor():
    assert calculate_age_factor(20) == 1.60
    assert calculate_age_factor(35) == 1.00
    assert calculate_age_factor(70) == 1.15


def test_calculate_vehicle_factor():
    assert calculate_vehicle_factor("economy") == 0.90
    assert calculate_vehicle_factor("sedan") == 1.00
    assert calculate_vehicle_factor("sports") == 1.50


def test_calculate_driving_history_factor():
    assert calculate_driving_history_factor(0, 0) == 1.00
    assert calculate_driving_history_factor(1, 0) == 1.20
    assert calculate_driving_history_factor(2, 1) == 1.50


def test_calculate_mileage_factor():
    assert calculate_mileage_factor(4000) == 0.85
    assert calculate_mileage_factor(10000) == 1.00
    assert calculate_mileage_factor(20000) == 1.25
    assert calculate_mileage_factor(25000) == 1.40


def test_calculate_claim_risk_score():
    assert calculate_claim_risk_score(0, 0, 5000, 40) == 5
    assert calculate_claim_risk_score(1, 1, 10000, 30) == 28
    assert calculate_claim_risk_score(2, 2, 20000, 22) == 81


def test_calculate_base_premium():
    premium = calculate_base_premium(
        40,
        "sedan",
        0,
        0,
        10000
    )

    assert premium == 1200.00


def test_calculate_final_premium():
    assert calculate_final_premium(1200, 0) == 1200
    assert calculate_final_premium(1200, 50) == 1500
    assert calculate_final_premium(1200, 100) == 1800