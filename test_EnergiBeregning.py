import unittest
import EnergiBeregning as calc

calc_engine = calc.EnergiBeregning(
    areal_oppv=200.0,
    norm_varmekap=64,
    kuldebro_normalisert=0.03,
    temp_settpunkt_oppvarming=21.0,
    temp_settpunkt_oppvarming_natt=19.0,

    areal_tak=100.0,
    areal_vegg_oest=42.5,
    areal_vegg_vest=42.5,
    areal_vegg_soer=42.5,
    areal_vegg_nord=42.5,
    areal_gulv_mot_det_fri=0.0,
    areal_vindu_oest=9.5,
    areal_vindu_vest=9.5,
    areal_vindu_soer=9.5,
    areal_vindu_nord=9.5,
    areal_vindu_tak=0.0,
    areal_dor=2.0,

    U_tak=0.18,
    U_vegg_oest=0.22,
    U_vegg_vest=0.22,
    U_vegg_soer=0.22,
    U_vegg_nord=0.22,
    U_gulv_mot_det_fri=0.18,
    U_dor=1.60,

    U_vindu_oest=1.60,
    U_vindu_vest=1.60,
    U_vindu_soer=1.60,
    U_vindu_nord=1.60,
    U_vindu_tak=1.60,

    varmetapsfaktor_uoppv=0.95,
    areal_mot_uoppvarmet=0.0,
    U_mot_uoppvarmet_sone=0.18,

    areal_gulv_kjeller=100.0,
    faseforskjell_utetemp_varmetap=2.0,
    aarsmiddeltemp_inne=21.0,
    omkrets_gulv=40.00,
    U_gulvkonstruksjon=0.15,
    U_kjellerveggskonstruksjon=0.18,
    tykkelse_grunnmur=0.30,
    oppfyllingshoyde_kjellervegg=0.01,
    varmekonduktivitet_kantisol=0.30,
    kantisol_tykkelse=0.20,
    kantisol_horisontal_dybde=0.20,
    kantisol_vertikal_bredde=0.20,
    dybde_periodisk_nedtrengning=3.20,
    varmekonduktivitet_grunn=2.00,

    tempvirkningsgrad_varmegjenvinner=0.70,
    luftmengde_spesifikk_i_driftstid=1.20,
    luftmengde_spesifikk_utenfor_driftstid=1.20,

    terrengskjermingskoeff_e=0.07,
    terrengskjermingskoeff_f=15,
    lekkasjetall=2.5,
    etasjehoyde_innvendig=2.6,
    luftmengde_spesifikk_tilluft=1.2,
    luftmengde_spesifikk_avtrekksluft=1.2,

    vifteeffekt_spesifikk_i_driftstid=2.5,
    vifteeffekt_spesifikk_utenfor_driftstid=2.5,

    frostsikringstemperatur=5.0,

    solskjermingsfaktor_horisont_oest=0.90,
    solskjermingsfaktor_horisont_vest=0.90,
    solskjermingsfaktor_horisont_soer=0.90,
    solskjermingsfaktor_horisont_nord=0.90,
    solskjermingsfaktor_horisont_tak=0.90,

    solskjermingsfaktor_overheng_oest=0.90,
    solskjermingsfaktor_overheng_vest=0.90,
    solskjermingsfaktor_overheng_soer=0.90,
    solskjermingsfaktor_overheng_nord=0.90,
    solskjermingsfaktor_overheng_tak=0.90,

    solskjermingsfaktor_finner_oest=0.90,
    solskjermingsfaktor_finner_vest=0.90,
    solskjermingsfaktor_finner_soer=0.90,
    solskjermingsfaktor_finner_nord=0.90,
    solskjermingsfaktor_finner_tak=0.90,

    arealfraksjon_karm_oest=0.10,
    arealfraksjon_karm_vest=0.10,
    arealfraksjon_karm_soer=0.10,
    arealfraksjon_karm_nord=0.10,
    arealfraksjon_karm_tak=0.10,

    sol_tidsvariabel_soer_jan=0.06,
    sol_tidsvariabel_soer_feb=0.15,
    sol_tidsvariabel_soer_mars=0.23,
    sol_tidsvariabel_soer_april=0.19,
    sol_tidsvariabel_soer_mai=0.19,
    sol_tidsvariabel_soer_juni=0.23,
    sol_tidsvariabel_soer_juli=0.21,
    sol_tidsvariabel_soer_aug=0.22,
    sol_tidsvariabel_soer_sept=0.15,
    sol_tidsvariabel_soer_okt=0.15,
    sol_tidsvariabel_soer_nov=0.10,
    sol_tidsvariabel_soer_des=0.07,

    sol_tidsvariabel_ost_vest_jan=0.02,
    sol_tidsvariabel_ost_vest_feb=0.08,
    sol_tidsvariabel_ost_vest_mars=0.16,
    sol_tidsvariabel_ost_vest_april=0.15,
    sol_tidsvariabel_ost_vest_mai=0.16,
    sol_tidsvariabel_ost_vest_juni=0.23,
    sol_tidsvariabel_ost_vest_juli=0.19,
    sol_tidsvariabel_ost_vest_aug=0.14,
    sol_tidsvariabel_ost_vest_sept=0.07,
    sol_tidsvariabel_ost_vest_okt=0.09,
    sol_tidsvariabel_ost_vest_nov=0.05,
    sol_tidsvariabel_ost_vest_des=0.03,

    sol_tidsvariabel_nord_jan=0.00,
    sol_tidsvariabel_nord_feb=0.03,
    sol_tidsvariabel_nord_mars=0.10,
    sol_tidsvariabel_nord_april=0.00,
    sol_tidsvariabel_nord_mai=0.01,
    sol_tidsvariabel_nord_juni=0.05,
    sol_tidsvariabel_nord_juli=0.03,
    sol_tidsvariabel_nord_aug=0.00,
    sol_tidsvariabel_nord_sept=0.00,
    sol_tidsvariabel_nord_okt=0.02,
    sol_tidsvariabel_nord_nov=0.00,
    sol_tidsvariabel_nord_des=0.00,

    solfaktor_vindu_oest=0.51,
    solfaktor_vindu_vest=0.51,
    solfaktor_vindu_soer=0.51,
    solfaktor_vindu_nord=0.51,
    solfaktor_vindu_tak=0.51,

    solfaktor_total_glass_skjerming_oest=0.25,
    solfaktor_total_glass_skjerming_vest=0.25,
    solfaktor_total_glass_skjerming_soer=0.20,
    solfaktor_total_glass_skjerming_nord=0.27,
    solfaktor_total_glass_skjerming_tak=0.20,

    # Per mnd. da skoler eller andre bygg kan ha variasjon i tilskudd. f.eks. i ferier=
    varmetilskudd_lys_jan=2.90,
    varmetilskudd_lys_feb=2.90,
    varmetilskudd_lys_mar=2.90,
    varmetilskudd_lys_apr=2.90,
    varmetilskudd_lys_mai=2.90,
    varmetilskudd_lys_jun=2.90,
    varmetilskudd_lys_jul=2.90,
    varmetilskudd_lys_aug=2.90,
    varmetilskudd_lys_sep=2.90,
    varmetilskudd_lys_okt=2.90,
    varmetilskudd_lys_nov=2.90,
    varmetilskudd_lys_des=2.90,

    varmetilskudd_utstyr_jan=2.40,
    varmetilskudd_utstyr_feb=2.40,
    varmetilskudd_utstyr_mar=2.40,
    varmetilskudd_utstyr_apr=2.40,
    varmetilskudd_utstyr_mai=2.40,
    varmetilskudd_utstyr_jun=2.40,
    varmetilskudd_utstyr_jul=2.40,
    varmetilskudd_utstyr_aug=2.40,
    varmetilskudd_utstyr_sep=2.40,
    varmetilskudd_utstyr_okt=2.40,
    varmetilskudd_utstyr_nov=2.40,
    varmetilskudd_utstyr_des=2.40,

    varmetilskudd_person_jan=1.50,
    varmetilskudd_person_feb=1.50,
    varmetilskudd_person_mar=1.50,
    varmetilskudd_person_apr=1.50,
    varmetilskudd_person_mai=1.50,
    varmetilskudd_person_jun=1.50,
    varmetilskudd_person_jul=1.50,
    varmetilskudd_person_aug=1.50,
    varmetilskudd_person_sep=1.50,
    varmetilskudd_person_okt=1.50,
    varmetilskudd_person_nov=1.50,
    varmetilskudd_person_des=1.50,

    energibehov_tappevann=30.0,

    energibehov_belysning=17.0,

    energibehov_utstyr=23.0,

    areal_avkjoelt_andel=0.00,
    temp_settpunkt_kjoeling=22,

    pumpeeffekt_spesifikk_oppv=0.5,
    tid_drift_pumpe_oppv=5300,
    temp_differanse_veskekrets_oppvarming=20.0,
    pumpeeffekt_spesifikk_kjoling=0.6,
    tid_drift_pumpe_kjoling=0,
    temp_differanse_veskekrets_kjoling=4.0,

    el_solcelle_andel_el_spesifikt_forbruk=0.00,
    el_er_andel_energi_oppv_ventilasjon=0.40,
    el_hp_andel_energi_oppv_ventilasjon=0.00,
    el_Tsol_andel_energi_oppv_ventilasjon=0.00,
    el_er_andel_energi_tappevann_varme=0.20,
    el_hp_andel_energi_tappevann_varme=0.00,
    el_Tsol_andel_energi_tappevann_varme=0.00,
    systemvirkningsgrad_solcelle=100,
    systemvirkningsgrad_elektrisk_oppv_ventilasjon=0.92,
    systemvirkningsgrad_elektrisk_tappevann_varme=0.98,
    systemvirkningsgrad_varmepumpeanlegg_oppv_ventilasjon=2.31,
    systemvirkningsgrad_varmepumpeanlegg_tappevann_varme=2.1,
    systemvirkningsgrad_solfanger_termisk_oppv_ventilasjon=51.84,
    systemvirkningsgrad_solfanger_termisk_tappevann_varme=20,
    effektfaktor_kjoeleanlegg=2.40,

    olje_andel_energi_oppv_ventilasjon=0.30,
    olje_andel_energi_tappevann_varme=0.50,
    systemvirkningsgrad_olje_oppv_ventilasjon=0.54,
    systemvirkningsgrad_olje_tappevann_varme=0.66,

    gass_andel_energi_oppv_ventilasjon=0.10,
    gass_andel_energi_tappevann_varme=0.10,
    systemvirkningsgrad_gass_oppv_ventilasjon=0.72,
    systemvirkningsgrad_gass_tappevann_varme=0.84,

    fjernvarme_andel_energi_oppv_ventilasjon=0.20,
    fjernvarme_andel_energi_tappevann_varme=0.20,
    systemvirkningsgrad_fjernvarme_oppv_ventilasjon=0.81,
    systemvirkningsgrad_fjernvarme_tappevann=0.98,

    bio_andel_energi_oppv_ventilasjon=0.00,
    bio_andel_energi_tappevann_varme=0.00,
    systemvirkningsgrad_bio_oppv_ventilasjon=0.74,
    systemvirkningsgrad_bio_tappevann=0.77,

    annet_andel_energi_oppv_ventilasjon=0.00,
    annet_andel_energi_tappevann_varme=0.00,
    systemvirkningsgrad_annet_oppv_ventilasjon=0.5,
    systemvirkningsgrad_annet_tappevann=0.5,

    CO2_faktor_el=0.357,
    CO2_faktor_olje=0.273,
    CO2_faktor_gass=0.202,
    CO2_faktor_fjernvarme=0.176,
    CO2_faktor_bio=0.025,
    CO2_faktor_annet=0.000,

    Primaerenergi_faktor_el=1.50,
    Primaerenergi_faktor_olje=1.35,
    Primaerenergi_faktor_gass=1.36,
    Primaerenergi_faktor_fjernvarme=1.25,
    Primaerenergi_faktor_bio=1.05,
    Primaerenergi_faktor_annet=1.00,

    Energipris_el=0.80,
    Energipris_olje=0.90,
    Energipris_gass=0.75,
    Energipris_fjernvarme=0.55,
    Energipris_bio=0.35,
    Energipris_annet=0.90,

    Energipol_vektingsfaktor_el=1.20,
    Energipol_vektingsfaktor_olje=1.50,
    Energipol_vektingsfaktor_gass=1.30,
    Energipol_vektingsfaktor_fjernvarme=1.05,
    Energipol_vektingsfaktor_bio=0.80,
    Energipol_vektingsfaktor_annet=0.90,

    tid_drift_oppv_belysn_utstyr_jan=496,
    tid_drift_oppv_belysn_utstyr_feb=448,
    tid_drift_oppv_belysn_utstyr_mar=496,
    tid_drift_oppv_belysn_utstyr_apr=480,
    tid_drift_oppv_belysn_utstyr_mai=496,
    tid_drift_oppv_belysn_utstyr_jun=480,
    tid_drift_oppv_belysn_utstyr_jul=496,
    tid_drift_oppv_belysn_utstyr_aug=496,
    tid_drift_oppv_belysn_utstyr_sep=480,
    tid_drift_oppv_belysn_utstyr_okt=496,
    tid_drift_oppv_belysn_utstyr_nov=480,
    tid_drift_oppv_belysn_utstyr_des=496,

    tid_drift_vent_jan=744,
    tid_drift_vent_feb=672,
    tid_drift_vent_mar=744,
    tid_drift_vent_apr=720,
    tid_drift_vent_mai=744,
    tid_drift_vent_jun=720,
    tid_drift_vent_jul=744,
    tid_drift_vent_aug=744,
    tid_drift_vent_sep=720,
    tid_drift_vent_okt=744,
    tid_drift_vent_nov=720,
    tid_drift_vent_des=744,

    tid_drift_person_jan=744,
    tid_drift_person_feb=672,
    tid_drift_person_mar=744,
    tid_drift_person_apr=720,
    tid_drift_person_mai=744,
    tid_drift_person_jun=720,
    tid_drift_person_jul=744,
    tid_drift_person_aug=744,
    tid_drift_person_sep=720,
    tid_drift_person_okt=744,
    tid_drift_person_nov=720,
    tid_drift_person_des=744,

    utetemp_jan=-3.7,
    utetemp_feb=-4.8,
    utetemp_mar=-0.5,
    utetemp_apr=4.8,
    utetemp_mai=11.7,
    utetemp_jun=16.5,
    utetemp_jul=17.5,
    utetemp_aug=16.9,
    utetemp_sep=11.5,
    utetemp_okt=6.4,
    utetemp_nov=0.5,
    utetemp_des=-2.5,
    aarsmiddeltemp_ute=7.5,

    straalingsfluks_soer_jan=28.0,
    straalingsfluks_soer_feb=61.0,
    straalingsfluks_soer_mars=106.0,
    straalingsfluks_soer_april=135.0,
    straalingsfluks_soer_mai=134.0,
    straalingsfluks_soer_juni=150.0,
    straalingsfluks_soer_juli=140.0,
    straalingsfluks_soer_aug=142.0,
    straalingsfluks_soer_sept=113.0,
    straalingsfluks_soer_okt=70.0,
    straalingsfluks_soer_nov=44.0,
    straalingsfluks_soer_des=28.0,

    straalingsfluks_ostvest_jan=11.0,
    straalingsfluks_ostvest_feb=32.0,
    straalingsfluks_ostvest_mars=55.0,
    straalingsfluks_ostvest_april=112.0,
    straalingsfluks_ostvest_mai=124.0,
    straalingsfluks_ostvest_juni=166.0,
    straalingsfluks_ostvest_juli=142.0,
    straalingsfluks_ostvest_aug=109.0,
    straalingsfluks_ostvest_sept=66.0,
    straalingsfluks_ostvest_okt=37.0,
    straalingsfluks_ostvest_nov=18.0,
    straalingsfluks_ostvest_des=9.0,

    straalingsfluks_nord_jan=6.0,
    straalingsfluks_nord_feb=17.0,
    straalingsfluks_nord_mars=25.0,
    straalingsfluks_nord_april=50.0,
    straalingsfluks_nord_mai=75.0,
    straalingsfluks_nord_juni=98.0,
    straalingsfluks_nord_juli=83.0,
    straalingsfluks_nord_aug=54.0,
    straalingsfluks_nord_sept=36.0,
    straalingsfluks_nord_okt=16.0,
    straalingsfluks_nord_nov=7.0,
    straalingsfluks_nord_des=3.0,

    straalingsfluks_tak_jan=13.0,
    straalingsfluks_tak_feb=43.0,
    straalingsfluks_tak_mars=90.0,
    straalingsfluks_tak_april=153.0,
    straalingsfluks_tak_mai=198.0,
    straalingsfluks_tak_juni=249.0,
    straalingsfluks_tak_juli=219.0,
    straalingsfluks_tak_aug=175.0,
    straalingsfluks_tak_sept=107.0,
    straalingsfluks_tak_okt=45.0,
    straalingsfluks_tak_nov=19.0,
    straalingsfluks_tak_des=8.0,

    temp_avtrekk=22.0,

    varmekapasitet_luft=0.33,
    temp_amplitudevar=11.2,

    tid_jan=0.744,
    tid_feb=0.672,
    tid_mar=0.744,
    tid_apr=0.720,
    tid_mai=0.744,
    tid_jun=0.720,
    tid_jul=0.744,
    tid_aug=0.744,
    tid_sep=0.720,
    tid_okt=0.744,
    tid_nov=0.720,
    tid_des=0.744,

    varmekapasitet_vann=4180,
    densitet_vann=988,
    varmekapasitet_kuldebaerer=4210,
    densitet_kuldebaerer=999.8,

    BygningskategoriErForretningsbygg=0,
    # Nima Darabi: OBS! finnes ikke i input? (1 = Forretningsbygg, 0 = Bolig)
    REF=123456789  # Nima Darabi: OBS! Hva er verdi for #REF! i Q88
)

calc_result = calc_engine.calculate()


class TestCalculation(unittest.TestCase):

    def test_romoppvarming(self):
        self.assertEqual(11810, round(calc_result.Romoppvarming))  # add assertion here

    def test_ventilasjonsvarme(self):
        self.assertEqual(236, round(calc_result.Ventilasjonsvarme))  # add assertion here

    def test_varmtvann(self):
        self.assertEqual(6000, calc_result.Varmtvann)  # add assertion here

    def test_vifter(self):
        self.assertEqual(1460, calc_result.Vifter)  # add assertion here

    def test_pumper(self):
        self.assertEqual(43, round(calc_result.Pumper))  # add assertion here

    def test_teknisk_utstyr(self):
        self.assertEqual(4600, round(calc_result.Teknisk_utstyr))  # add assertion here

    def test_kjoeling(self):
        self.assertEqual(0, calc_result.Kjoeling)  # add assertion here

    def test_totalt_netto_energibehov(self):
        self.assertEqual(27549, round(calc_result.Totalt_netto_energibehov))  # add assertion here


if __name__ == '__main__':
    unittest.main()
