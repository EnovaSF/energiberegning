import unittest
from reference_calculations.tek_07_smaahus import *
from reference_calculations.tek_07_boligblokk import *
from reference_calculations.tek_07_barnehage import *
from reference_calculations.tek_07_kontorbygg import *
from reference_calculations.ashrae_besttest_600 import *
from reference_calculations.ashrae_besttest_610 import *
from reference_calculations.ashrae_besttest_620 import *
from reference_calculations.ashrae_besttest_630 import *
from reference_calculations.ashrae_besttest_640 import *
from reference_calculations.ashrae_besttest_650 import *
from reference_calculations.ashrae_besttest_900 import *
from reference_calculations.ashrae_besttest_910 import *
from reference_calculations.ashrae_besttest_920 import *
from reference_calculations.ashrae_besttest_930 import *
from reference_calculations.ashrae_besttest_940 import *
from reference_calculations.ashrae_besttest_950 import *

calc_results = [
    ("TEK07 - Småhus", tek_07_smaahus.calculate(), tek_07_smaahus_expected_output),
    (
        "TEK07 - Boligblokk",
        tek_07_boligblokk.calculate(),
        tek_07_boligblokk_expected_output,
    ),
    (
        "TEK07 - Barnehage",
        tek_07_barnehage.calculate(),
        tek_07_barnehage_expected_output,
    ),
    # ("TEK07 - Kontorbygg", tek_07_kontorbygg.calculate(), tek_07_kontorbygg_expected_output), # TODO fix
    (
        "ASHRAE BESTTEST 600",
        ashrae_besttest_600.calculate(),
        ashrae_besttest_600_expected_output,
    ),
    (
        "ASHRAE BESTTEST 610",
        ashrae_besttest_610.calculate(),
        ashrae_besttest_610_expected_output,
    ),
    (
        "ASHRAE BESTTEST 900",
        ashrae_besttest_900.calculate(),
        ashrae_besttest_900_expected_output,
    ),
    (
        "ASHRAE BESTTEST 910",
        ashrae_besttest_910.calculate(),
        ashrae_besttest_910_expected_output,
    ),
    (
        "ASHRAE BESTTEST 620",
        ashrae_besttest_620.calculate(),
        ashrae_besttest_620_expected_output,
    ),
    (
        "ASHRAE BESTTEST 920",
        ashrae_besttest_920.calculate(),
        ashrae_besttest_920_expected_output,
    ),
    (
        "ASHRAE BESTTEST 630",
        ashrae_besttest_630.calculate(),
        ashrae_besttest_630_expected_output,
    ),
    (
        "ASHRAE BESTTEST 930",
        ashrae_besttest_930.calculate(),
        ashrae_besttest_930_expected_output,
    ),
    (
        "ASHRAE BESTTEST 640",
        ashrae_besttest_640.calculate(),
        ashrae_besttest_640_expected_output,
    ),
    (
        "ASHRAE BESTTEST 940",
        ashrae_besttest_940.calculate(),
        ashrae_besttest_940_expected_output,
    ),
    (
        "ASHRAE BESTTEST 650",
        ashrae_besttest_650.calculate(),
        ashrae_besttest_650_expected_output,
    ),
    (
        "ASHRAE BESTTEST 950",
        ashrae_besttest_950.calculate(),
        ashrae_besttest_950_expected_output,
    ),
]


class TestCalculation(unittest.TestCase):

    # energipost
    def test_romoppvarming(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Romoppvarming, round(calc_result.Romoppvarming)
                )

    def test_ventilasjonsvarme(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Ventilasjonsvarme,
                    round(calc_result.Ventilasjonsvarme),
                )

    def test_varmtvann(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Varmtvann, round(calc_result.Varmtvann)
                )

    def test_vifter(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(expected_result.Vifter, round(calc_result.Vifter))

    def test_pumper(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(expected_result.Pumper, round(calc_result.Pumper))

    def test_teknisk_utstyr(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Teknisk_utstyr, round(calc_result.Teknisk_utstyr)
                )

    def test_kjoeling(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(expected_result.Kjoeling, round(calc_result.Kjoeling))

    def test_totalt_netto_energibehov(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Totalt_netto_energibehov,
                    round(calc_result.Totalt_netto_energibehov),
                )

    # energivare
    def test_elektrisitet(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Elektrisitet, round(calc_result.Elektrisitet)
                )

    def test_olje(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(expected_result.Olje, round(calc_result.Olje))

    def test_gass(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(expected_result.Gass, round(calc_result.Gass))

    def test_fjernvarme(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Fjernvarme, round(calc_result.Fjernvarme)
                )

    def test_biobrensel(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Biobrensel, round(calc_result.Biobrensel)
                )

    def test_annen_energivare(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Annen_energivare,
                    round(calc_result.Annen_energivare),
                )

    def test_totalt_levert_energi(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Totalt_levert_energi,
                    round(calc_result.Totalt_levert_energi),
                )

    # energivare
    def test_primaerenergi(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Primaerenergi, round(calc_result.Primaerenergi)
                )

    def test_test_co2_utslipp(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.CO2_utslipp, round(calc_result.CO2_utslipp)
                )

    def test_energikostnader(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Energi_kostnader,
                    round(calc_result.Energi_kostnader),
                )

    def test_energi_politisk(self):
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.Energi_politisk, round(calc_result.Energi_politisk)
                )


if __name__ == "__main__":
    unittest.main()
