import unittest
from reference_calculations.tek_07_smaahus import *
from reference_calculations.tek_07_boligblokk import *
from reference_calculations.tek_07_barnehage import *
from reference_calculations.tek_07_kontorbygg import *
from reference_calculations.tek_07_kontorbygg_True import *
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
from reference_calculations.divide_by_zero import *

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
    (
        "TEK07 - Kontorbygg",
        tek_07_kontorbygg.calculate(),
        tek_07_kontorbygg_expected_output,
    ),
    (
        "TEK07 - Kontorbygg True",
        tek_07_kontorbygg_True.calculate(),
        tek_07_kontorbygg_True_expected_output,
    ),
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
    (
        "Divide By Zero",
        divide_by_zero.calculate(),
        divide_by_zero_expected_output,
    ),
]


class TestCalculation(unittest.TestCase):

    # energipost
    def test_romoppvarming(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.romoppvarming, round(calc_result.romoppvarming)
                )

    def test_ventilasjonsvarme(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.ventilasjonsvarme,
                    round(calc_result.ventilasjonsvarme),
                )

    def test_varmtvann(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.varmtvann, round(calc_result.varmtvann)
                )

    def test_vifter(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(expected_result.vifter, round(calc_result.vifter))

    def test_belysning(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.belysning, round(calc_result.belysning)
                )

    def test_pumper(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(expected_result.pumper, round(calc_result.pumper))

    def test_teknisk_utstyr(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.teknisk_utstyr, round(calc_result.teknisk_utstyr)
                )

    def test_kjoeling(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(expected_result.kjoeling, round(calc_result.kjoeling))

    def test_totalt_netto_energibehov(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.totalt_netto_energibehov,
                    round(calc_result.totalt_netto_energibehov),
                )

    # energivare
    def test_elektrisitet(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.elektrisitet, round(calc_result.elektrisitet)
                )

    def test_olje(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(expected_result.olje, round(calc_result.olje))

    def test_gass(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(expected_result.gass, round(calc_result.gass))

    def test_fjernvarme(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.fjernvarme, round(calc_result.fjernvarme)
                )

    def test_biobrensel(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.biobrensel, round(calc_result.biobrensel)
                )

    def test_annen_energivare(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.annen_energivare,
                    round(calc_result.annen_energivare),
                )

    def test_totalt_levert_energi(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.totalt_levert_energi,
                    round(calc_result.totalt_levert_energi),
                )

    # energivare
    def test_primaerenergi(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.primaerenergi, round(calc_result.primaerenergi)
                )

    def test_test_co2_utslipp(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.co2_utslipp, round(calc_result.co2_utslipp)
                )

    def test_energikostnader(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.energi_kostnader,
                    round(calc_result.energi_kostnader),
                )

    def test_energi_politisk(self) -> None:
        for (category, calc_result, expected_result) in calc_results:
            with self.subTest(category):
                self.assertEqual(
                    expected_result.energi_politisk, round(calc_result.energi_politisk)
                )


if __name__ == "__main__":
    unittest.main()
