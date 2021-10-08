import unittest
from vaccine_stats import Vax_Stats
from datetime import date
import pathlib

SELF_PATH = pathlib.Path(__file__).parent.absolute()
DATA_PATH = SELF_PATH.joinpath("test_stats.csv").as_uri()
Vax_Stats.ODH_URL = DATA_PATH


class TestStats(unittest.TestCase):
    def test_lookup(self):
        with Vax_Stats() as stats:
            p, q, r = stats.lookup("All", date(2021, 1, 1))
        self.assertEqual(p, 177063)
        self.assertEqual(q, 60)
        self.assertEqual(r, 10400)

    def test_lookup_noncumulative(self):
        with Vax_Stats() as stats:
            p, q, r = stats.lookup("All", date(2021, 1, 1), False)
        self.assertEqual(p, 527)
        self.assertEqual(q, 20)
        self.assertEqual(r, 433)

    def test_lookup_county(self):
        with Vax_Stats() as stats:
            p, q, r = stats.lookup("Cuyahoga", date(2021, 1, 1))
        self.assertEqual(p, 20883)
        self.assertEqual(q, 2)
        self.assertEqual(r, 55)

    def test_lookup_noncumulative_county(self):
        with Vax_Stats() as stats:
            p, q, r = stats.lookup("Cuyahoga", date(2021, 1, 1), False)
        self.assertEqual(p, 33)
        self.assertEqual(q, 2)
        self.assertEqual(r, 30)

    def test_delta_percent(self):
        with Vax_Stats() as stats:
            p, q, r = stats.delta("All", date(2021, 1, 1), date(2021, 2, 1))
        self.assertEqual(round(p, 0), 421)
        self.assertEqual(round(q, 0), 372975)
        self.assertEqual(round(r, 0), 354)

    def test_delta_absolute(self):
        with Vax_Stats() as stats:
            p, q, r = stats.delta(
                "All", date(2021, 1, 1), date(2021, 2, 1), False
            )
        self.assertEqual(p, 745839)
        self.assertEqual(q, 223785)
        self.assertEqual(r, 36828)

    def test_delta_percent_county(self):
        with Vax_Stats() as stats:
            p, q, r = stats.delta("Cuyahoga", date(2021, 1, 1), date(2021, 2, 1))
        self.assertEqual(round(p, 0), 356)
        self.assertEqual(round(q, 0), 1257500)
        self.assertEqual(round(r, 0), 67)

    def test_delta_absolute_county(self):
        with Vax_Stats() as stats:
            p, q, r = stats.delta(
                "Cuyahoga", date(2021, 1, 1), date(2021, 2, 1), False
            )
        self.assertEqual(p, 74286)
        self.assertEqual(q, 25150)
        self.assertEqual(r, 37)

    def test_percent_vaccinated_full(self):
        with Vax_Stats() as stats:
            p = stats.percent_vaccinated("All", date(2021, 2, 1))
        self.assertEqual(round(p, 1), 1.9)

    def test_percent_vaccinated_started(self):
        with Vax_Stats() as stats:
            p = stats.percent_vaccinated("All", date(2021, 2, 1), False)
        self.assertEqual(round(p, 1), 7.9)

    def test_percent_vaccinated_full_county(self):
        with Vax_Stats() as stats:
            p = stats.percent_vaccinated("Cuyahoga", date(2021, 2, 1))
        self.assertEqual(round(p, 1), 2.0)

    def test_percent_vaccinated_started_county(self):
        with Vax_Stats() as stats:
            p = stats.percent_vaccinated("Cuyahoga", date(2021, 2, 1), False)
        self.assertEqual(round(p, 1), 7.7)

    def test_percent_boosted(self):
        with Vax_Stats() as stats:
            p = stats.percent_boosted("All", date(2021, 2, 1))
        self.assertEqual(round(p, 1), 21.1)

    def test_percent_boosted_county(self):
        with Vax_Stats() as stats:
            p = stats.percent_boosted("Cuyahoga", date(2021, 1, 5))
        self.assertEqual(round(p, 1), 32.2)