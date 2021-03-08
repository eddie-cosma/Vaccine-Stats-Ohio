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
            p, q = stats.lookup("All", date(2021, 1, 1))
        self.assertEqual(p, 177063)
        self.assertEqual(q, 60)

    def test_lookup_noncumulative(self):
        with Vax_Stats() as stats:
            p, q = stats.lookup("All", date(2021, 1, 1), False)
        self.assertEqual(p, 527)
        self.assertEqual(q, 20)

    def test_lookup_county(self):
        with Vax_Stats() as stats:
            p, q = stats.lookup("Cuyahoga", date(2021, 1, 1))
        self.assertEqual(p, 20883)
        self.assertEqual(q, 2)

    def test_lookup_noncumulative_county(self):
        with Vax_Stats() as stats:
            p, q = stats.lookup("Cuyahoga", date(2021, 1, 1), False)
        self.assertEqual(p, 33)
        self.assertEqual(q, 2)

    def test_delta_percent(self):
        with Vax_Stats() as stats:
            p, q = stats.delta("All", date(2021, 1, 1), date(2021, 2, 1))
        self.assertEqual(round(p, 0), 421)
        self.assertEqual(round(q, 0), 372975)

    def test_delta_absolute(self):
        with Vax_Stats() as stats:
            p, q = stats.delta(
                "All", date(2021, 1, 1), date(2021, 2, 1), False
            )
        self.assertEqual(p, 745839)
        self.assertEqual(q, 223785)

    def test_delta_percent_county(self):
        with Vax_Stats() as stats:
            p, q = stats.delta("Cuyahoga", date(2021, 1, 1), date(2021, 2, 1))
        self.assertEqual(round(p, 0), 356)
        self.assertEqual(round(q, 0), 1257500)

    def test_delta_absolute_county(self):
        with Vax_Stats() as stats:
            p, q = stats.delta(
                "Cuyahoga", date(2021, 1, 1), date(2021, 2, 1), False
            )
        self.assertEqual(p, 74286)
        self.assertEqual(q, 25150)

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