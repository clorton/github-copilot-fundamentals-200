import unittest

def calculate_amortization(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_payments = years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)
    return round(monthly_payment, 2)

class TestAmortizationCalculation(unittest.TestCase):
    def test_case_1(self):
        self.assertAlmostEqual(calculate_amortization(100000, 5, 30), 536.82, places=2)

    def test_case_2(self):
        self.assertAlmostEqual(calculate_amortization(200000, 3.75, 15), 1459.44, places=2)

    def test_case_3(self):
        self.assertAlmostEqual(calculate_amortization(300000, 4.5, 20), 1896.20, places=2)

    def test_case_4(self):
        self.assertAlmostEqual(calculate_amortization(400000, 6, 30), 2398.21, places=2)

    def test_case_5(self):
        self.assertAlmostEqual(calculate_amortization(500000, 3.5, 25), 2503.48, places=2)

if __name__ == '__main__':
    unittest.main()
