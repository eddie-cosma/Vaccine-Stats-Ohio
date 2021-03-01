import unittest
from vaccine_stats import Vax_Stats
from datetime import date


class TestStats(unittest.TestCase):

    stats = Vax_Stats()

    def test_lookup(self):
        p, q = self.stats.lookup("All", date(2021, 1, 1))
        self.assertEqual(p, 176928)
        self.assertEqual(q, 47)

    def test_lookup_noncumulative(self):
        p, q = self.stats.lookup("All", date(2021, 1, 1), False)
        self.assertEqual(p, 485)
        self.assertEqual(q, 20)

    def test_lookup_county(self):
        p, q = self.stats.lookup("Cuyahoga", date(2021, 1, 1))
        self.assertEqual(p, 20869)
        self.assertEqual(q, 2)

    def test_lookup_noncumulative_county(self):
        p, q = self.stats.lookup("Cuyahoga", date(2021, 1, 1), False)
        self.assertEqual(p, 33)
        self.assertEqual(q, 2)

    def test_delta_percent(self):
        p, q = self.stats.delta("All", date(2021, 1, 1), date(2021, 2, 1))
        self.assertEqual(round(p, 0), 421)
        self.assertEqual(round(q, 0), 475153)

    def test_delta_absolute(self):
        p, q = self.stats.delta(
            "All", date(2021, 1, 1), date(2021, 2, 1), False
        )
        self.assertEqual(p, 744725)
        self.assertEqual(q, 223322)

    def test_delta_percent_county(self):
        p, q = self.stats.delta("Cuyahoga", date(2021, 1, 1), date(2021, 2, 1))
        self.assertEqual(round(p, 0), 355)
        self.assertEqual(round(q, 0), 1254800)

    def test_delta_absolute_county(self):
        p, q = self.stats.delta(
            "Cuyahoga", date(2021, 1, 1), date(2021, 2, 1), False
        )
        self.assertEqual(p, 74175)
        self.assertEqual(q, 25096)

    def test_percent_vaccinated_full(self):
        p = self.stats.percent_vaccinated("All", date(2021, 2, 1))
        self.assertEqual(round(p, 1), 1.9)

    def test_percent_vaccinated_started(self):
        p = self.stats.percent_vaccinated("All", date(2021, 2, 1), False)
        self.assertEqual(round(p, 1), 7.9)

    def test_percent_vaccinated_full_county(self):
        p = self.stats.percent_vaccinated("Cuyahoga", date(2021, 2, 1))
        self.assertEqual(round(p, 1), 2.0)

    def test_percent_vaccinated_started_county(self):
        p = self.stats.percent_vaccinated("Cuyahoga", date(2021, 2, 1), False)
        self.assertEqual(round(p, 1), 7.7)