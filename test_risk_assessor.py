import unittest

from risk_assessor import assess_goat_health, predict_delivery_risk


class RiskAssessorTests(unittest.TestCase):
    def test_delivery_risk_levels(self):
        self.assertEqual(predict_delivery_risk(2, 2, 8), "High")
        self.assertEqual(predict_delivery_risk(2, 5, 9), "Medium")
        self.assertEqual(predict_delivery_risk(4, 10, 8), "Low")

    def test_zero_crew_is_rejected(self):
        with self.assertRaises(ValueError):
            predict_delivery_risk(0, 5, 10)

    def test_goat_risk_uses_thresholds(self):
        self.assertEqual(assess_goat_health(4.2, 35, 3), "High")
        self.assertEqual(assess_goat_health(0.5, 8, 2), "Low")


if __name__ == "__main__":
    unittest.main()
