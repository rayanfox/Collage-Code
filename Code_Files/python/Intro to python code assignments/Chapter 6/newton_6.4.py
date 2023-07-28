import unittest

# Your newton, limitReached, improveEstimate functions here

def limitReached(estimate, previous_estimate, tolerance):
    """Check if the difference between the current and previous estimate is within the tolerance."""
    return abs(estimate - previous_estimate) <= tolerance

def improveEstimate(estimate, x):
    """Compute a new approximation using Newton's method."""
    return (estimate + x / estimate) / 2

def newton(x, tolerance=0.000001):
    """Compute the square root of a number using Newton's method."""
    estimate = 1.0
    while True:
        previous_estimate = estimate
        estimate = improveEstimate(estimate, x)
        if limitReached(estimate, previous_estimate, tolerance):
            break
    return estimate

class UnitTests(unittest.TestCase):
    def test_unit_test_1(self):
        self.assertAlmostEqual(newton(2), 1.4142135623746899, places=12)

    def test_unit_test_2(self):
        self.assertAlmostEqual(newton(13), 3.6055513629176015, places=12)

if __name__ == "__main__":
    unittest.main()
