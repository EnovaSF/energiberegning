import EnergiBeregning as calc

"""
Øst- og vestvendte vinduer, lett bygg
Denver-klima
"""
ashrae_besttest_620 = calc.EnergiBeregning(
    areal_oppv=48,
    norm_varmekap=38,
    kuldebro_normalisert=0,
    temp_settpunkt_oppvarming=20,
    temp_settpunkt_oppvarming_natt=20,
    areal_tak=48,
    areal_vegg_oest=10.2,
    areal_vegg_vest=10.2,
    areal_vegg_soer=21.6,
    areal_vegg_nord=21.6,
    areal_gulv_mot_det_fri=0,
    areal_vindu_oest=6,
    areal_vindu_vest=6,
    areal_vindu_soer=0,
    areal_vindu_nord=0,
    areal_vindu_tak=0,
    areal_dor=0,
    U_tak=0.318,
    U_vegg_oest=0.514,
    U_vegg_vest=0.514,
    U_vegg_soer=0.514,
    U_vegg_nord=0.514,
    U_gulv_mot_det_fri=0.039,
    U_dor=3.000,
    U_vindu_oest=3.00,
    U_vindu_vest=3.00,
    U_vindu_soer=3.00,
    U_vindu_nord=3.00,
    U_vindu_tak=3.00,
    varmetapsfaktor_uoppv=0.5,
    areal_mot_uoppvarmet=0,
    U_mot_uoppvarmet_sone=0.514,
    areal_gulv_kjeller=48,
    faseforskjell_utetemp_varmetap=2,
    aarsmiddeltemp_inne=20,
    omkrets_gulv=28,
    U_gulvkonstruksjon=0.042,
    U_kjellerveggskonstruksjon=1,
    tykkelse_grunnmur=1,
    oppfyllingshoyde_kjellervegg=0.01,
    varmekonduktivitet_kantisol=0.3,
    kantisol_tykkelse=0,
    kantisol_horisontal_dybde=0,
    kantisol_vertikal_bredde=0,
    dybde_periodisk_nedtrengning=2.1,
    varmekonduktivitet_grunn=1.3,
    tempvirkningsgrad_varmegjenvinner=0,
    luftmengde_spesifikk_i_driftstid=0,
    luftmengde_spesifikk_utenfor_driftstid=0,
    terrengskjermingskoeff_e=0.07,
    terrengskjermingskoeff_f=15,
    lekkasjetall=5.857,
    etasjehoyde_innvendig=3,
    luftmengde_spesifikk_tilluft=0,
    luftmengde_spesifikk_avtrekksluft=0,
    vifteeffekt_spesifikk_i_driftstid=0,
    vifteeffekt_spesifikk_utenfor_driftstid=0,
    frostsikringstemperatur=-50,
    solskjermingsfaktor_horisont_oest=0.9,
    solskjermingsfaktor_horisont_vest=0.9,
    solskjermingsfaktor_horisont_soer=0.9,
    solskjermingsfaktor_horisont_nord=0.9,
    solskjermingsfaktor_horisont_tak=0.9,
    solskjermingsfaktor_overheng_oest=1,
    solskjermingsfaktor_overheng_vest=1,
    solskjermingsfaktor_overheng_soer=1,
    solskjermingsfaktor_overheng_nord=1,
    solskjermingsfaktor_overheng_tak=1,
    solskjermingsfaktor_finner_oest=1,
    solskjermingsfaktor_finner_vest=1,
    solskjermingsfaktor_finner_soer=1,
    solskjermingsfaktor_finner_nord=1,
    solskjermingsfaktor_finner_tak=1,
    arealfraksjon_karm_oest=0.1,
    arealfraksjon_karm_vest=0.1,
    arealfraksjon_karm_soer=0.1,
    arealfraksjon_karm_nord=0.1,
    arealfraksjon_karm_tak=0.1,
    sol_tidsvariabel_soer_jan=0,
    sol_tidsvariabel_soer_feb=0,
    sol_tidsvariabel_soer_mars=0,
    sol_tidsvariabel_soer_april=0,
    sol_tidsvariabel_soer_mai=0,
    sol_tidsvariabel_soer_juni=0,
    sol_tidsvariabel_soer_juli=0,
    sol_tidsvariabel_soer_aug=0,
    sol_tidsvariabel_soer_sept=0,
    sol_tidsvariabel_soer_okt=0,
    sol_tidsvariabel_soer_nov=0,
    sol_tidsvariabel_soer_des=0,
    sol_tidsvariabel_ost_vest_jan=0,
    sol_tidsvariabel_ost_vest_feb=0,
    sol_tidsvariabel_ost_vest_mars=0,
    sol_tidsvariabel_ost_vest_april=0,
    sol_tidsvariabel_ost_vest_mai=0,
    sol_tidsvariabel_ost_vest_juni=0,
    sol_tidsvariabel_ost_vest_juli=0,
    sol_tidsvariabel_ost_vest_aug=0,
    sol_tidsvariabel_ost_vest_sept=0,
    sol_tidsvariabel_ost_vest_okt=0,
    sol_tidsvariabel_ost_vest_nov=0,
    sol_tidsvariabel_ost_vest_des=0,
    sol_tidsvariabel_nord_jan=0,
    sol_tidsvariabel_nord_feb=0,
    sol_tidsvariabel_nord_mars=0,
    sol_tidsvariabel_nord_april=0,
    sol_tidsvariabel_nord_mai=0,
    sol_tidsvariabel_nord_juni=0,
    sol_tidsvariabel_nord_juli=0,
    sol_tidsvariabel_nord_aug=0,
    sol_tidsvariabel_nord_sept=0,
    sol_tidsvariabel_nord_okt=0,
    sol_tidsvariabel_nord_nov=0,
    sol_tidsvariabel_nord_des=0,
    solfaktor_vindu_oest=0.79,
    solfaktor_vindu_vest=0.79,
    solfaktor_vindu_soer=0.79,
    solfaktor_vindu_nord=0.79,
    solfaktor_vindu_tak=0.79,
    solfaktor_total_glass_skjerming_oest=0.00,
    solfaktor_total_glass_skjerming_vest=0.00,
    solfaktor_total_glass_skjerming_soer=0.00,
    solfaktor_total_glass_skjerming_nord=0.00,
    solfaktor_total_glass_skjerming_tak=0.00,
    varmetilskudd_lys_jan=1.39,
    varmetilskudd_lys_feb=1.39,
    varmetilskudd_lys_mar=1.39,
    varmetilskudd_lys_apr=1.39,
    varmetilskudd_lys_mai=1.39,
    varmetilskudd_lys_jun=1.39,
    varmetilskudd_lys_jul=1.39,
    varmetilskudd_lys_aug=1.39,
    varmetilskudd_lys_sep=1.39,
    varmetilskudd_lys_okt=1.39,
    varmetilskudd_lys_nov=1.39,
    varmetilskudd_lys_des=1.39,
    varmetilskudd_utstyr_jan=1.39,
    varmetilskudd_utstyr_feb=1.39,
    varmetilskudd_utstyr_mar=1.39,
    varmetilskudd_utstyr_apr=1.39,
    varmetilskudd_utstyr_mai=1.39,
    varmetilskudd_utstyr_jun=1.39,
    varmetilskudd_utstyr_jul=1.39,
    varmetilskudd_utstyr_aug=1.39,
    varmetilskudd_utstyr_sep=1.39,
    varmetilskudd_utstyr_okt=1.39,
    varmetilskudd_utstyr_nov=1.39,
    varmetilskudd_utstyr_des=1.39,
    varmetilskudd_person_jan=1.39,
    varmetilskudd_person_feb=1.39,
    varmetilskudd_person_mar=1.39,
    varmetilskudd_person_apr=1.39,
    varmetilskudd_person_mai=1.39,
    varmetilskudd_person_jun=1.39,
    varmetilskudd_person_jul=1.39,
    varmetilskudd_person_aug=1.39,
    varmetilskudd_person_sep=1.39,
    varmetilskudd_person_okt=1.39,
    varmetilskudd_person_nov=1.39,
    varmetilskudd_person_des=1.39,
    energibehov_tappevann=0,
    energibehov_belysning=0,
    energibehov_utstyr=0,
    areal_avkjoelt_andel=0,
    temp_settpunkt_kjoeling=27,
    pumpeeffekt_spesifikk_oppv=0.5,
    tid_drift_pumpe_oppv=0,
    temp_differanse_veskekrets_oppvarming=20,
    pumpeeffekt_spesifikk_kjoling=0.6,
    tid_drift_pumpe_kjoling=0,
    temp_differanse_veskekrets_kjoling=4,
    el_solcelle_andel_el_spesifikt_forbruk=0,
    el_er_andel_energi_oppv_ventilasjon=1,
    el_hp_andel_energi_oppv_ventilasjon=0,
    el_Tsol_andel_energi_oppv_ventilasjon=0,
    el_er_andel_energi_tappevann_varme=1,
    el_hp_andel_energi_tappevann_varme=0,
    el_Tsol_andel_energi_tappevann_varme=0,
    systemvirkningsgrad_solcelle=100,
    systemvirkningsgrad_elektrisk_oppv_ventilasjon=0.98,
    systemvirkningsgrad_elektrisk_tappevann_varme=0.98,
    systemvirkningsgrad_varmepumpeanlegg_oppv_ventilasjon=2.26,
    systemvirkningsgrad_varmepumpeanlegg_tappevann_varme=2.26,
    systemvirkningsgrad_solfanger_termisk_oppv_ventilasjon=8.12,
    systemvirkningsgrad_solfanger_termisk_tappevann_varme=8.12,
    effektfaktor_kjoeleanlegg=2.4,
    olje_andel_energi_oppv_ventilasjon=0,
    olje_andel_energi_tappevann_varme=0,
    systemvirkningsgrad_olje_oppv_ventilasjon=0.77,
    systemvirkningsgrad_olje_tappevann_varme=0.77,
    gass_andel_energi_oppv_ventilasjon=0,
    gass_andel_energi_tappevann_varme=0,
    systemvirkningsgrad_gass_oppv_ventilasjon=0.81,
    systemvirkningsgrad_gass_tappevann_varme=0.81,
    fjernvarme_andel_energi_oppv_ventilasjon=0,
    fjernvarme_andel_energi_tappevann_varme=0,
    systemvirkningsgrad_fjernvarme_oppv_ventilasjon=0.88,
    systemvirkningsgrad_fjernvarme_tappevann=0.88,
    bio_andel_energi_oppv_ventilasjon=0,
    bio_andel_energi_tappevann_varme=0,
    systemvirkningsgrad_bio_oppv_ventilasjon=0.73,
    systemvirkningsgrad_bio_tappevann=0.73,
    annet_andel_energi_oppv_ventilasjon=0,
    annet_andel_energi_tappevann_varme=0,
    systemvirkningsgrad_annet_oppv_ventilasjon=0.5,
    systemvirkningsgrad_annet_tappevann=0.5,
    CO2_faktor_el=0.057,
    CO2_faktor_olje=0.273,
    CO2_faktor_gass=0.202,
    CO2_faktor_fjernvarme=0.176,
    CO2_faktor_bio=0,
    CO2_faktor_annet=0,
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
    tid_drift_oppv_belysn_utstyr_jan=744,
    tid_drift_oppv_belysn_utstyr_feb=672,
    tid_drift_oppv_belysn_utstyr_mar=744,
    tid_drift_oppv_belysn_utstyr_apr=720,
    tid_drift_oppv_belysn_utstyr_mai=744,
    tid_drift_oppv_belysn_utstyr_jun=720,
    tid_drift_oppv_belysn_utstyr_jul=744,
    tid_drift_oppv_belysn_utstyr_aug=744,
    tid_drift_oppv_belysn_utstyr_sep=720,
    tid_drift_oppv_belysn_utstyr_okt=744,
    tid_drift_oppv_belysn_utstyr_nov=720,
    tid_drift_oppv_belysn_utstyr_des=744,
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
    utetemp_jan=-1.3,
    utetemp_feb=0.9,
    utetemp_mar=4.0,
    utetemp_apr=8.8,
    utetemp_mai=14.1,
    utetemp_jun=19.1,
    utetemp_jul=23.2,
    utetemp_aug=21.9,
    utetemp_sep=16.7,
    utetemp_okt=11.0,
    utetemp_nov=3.6,
    utetemp_des=-0.5,
    aarsmiddeltemp_ute=10.2,
    straalingsfluks_soer_jan=101.0,
    straalingsfluks_soer_feb=120.5,
    straalingsfluks_soer_mars=139.1,
    straalingsfluks_soer_april=154.3,
    straalingsfluks_soer_mai=146.2,
    straalingsfluks_soer_juni=142.1,
    straalingsfluks_soer_juli=145.4,
    straalingsfluks_soer_aug=150.3,
    straalingsfluks_soer_sept=151.9,
    straalingsfluks_soer_okt=128.0,
    straalingsfluks_soer_nov=104.0,
    straalingsfluks_soer_des=86.1,
    straalingsfluks_ostvest_jan=60.0,
    straalingsfluks_ostvest_feb=75.4,
    straalingsfluks_ostvest_mars=92.2,
    straalingsfluks_ostvest_april=104.1,
    straalingsfluks_ostvest_mai=112.7,
    straalingsfluks_ostvest_juni=124.6,
    straalingsfluks_ostvest_juli=123.6,
    straalingsfluks_ostvest_aug=111.7,
    straalingsfluks_ostvest_sept=98.7,
    straalingsfluks_ostvest_okt=85.7,
    straalingsfluks_ostvest_nov=62.9,
    straalingsfluks_ostvest_des=53.6,
    straalingsfluks_nord_jan=20.7,
    straalingsfluks_nord_feb=27.2,
    straalingsfluks_nord_mars=41.5,
    straalingsfluks_nord_april=53.9,
    straalingsfluks_nord_mai=67.8,
    straalingsfluks_nord_juni=86.0,
    straalingsfluks_nord_juli=84.1,
    straalingsfluks_nord_aug=56.7,
    straalingsfluks_nord_sept=44.4,
    straalingsfluks_nord_okt=32.1,
    straalingsfluks_nord_nov=20.7,
    straalingsfluks_nord_des=19.0,
    straalingsfluks_tak_jan=168.3,
    straalingsfluks_tak_feb=199.3,
    straalingsfluks_tak_mars=203.8,
    straalingsfluks_tak_april=228.7,
    straalingsfluks_tak_mai=253.3,
    straalingsfluks_tak_juni=274.8,
    straalingsfluks_tak_juli=274.1,
    straalingsfluks_tak_aug=249.3,
    straalingsfluks_tak_sept=234.1,
    straalingsfluks_tak_okt=208.5,
    straalingsfluks_tak_nov=183.6,
    straalingsfluks_tak_des=159.3,
    temp_avtrekk=21.0,
    varmekapasitet_luft=0.33,
    temp_amplitudevar=11.2,
    tid_jan=0.744,
    tid_feb=0.672,
    tid_mar=0.744,
    tid_apr=0.72,
    tid_mai=0.744,
    tid_jun=0.72,
    tid_jul=0.744,
    tid_aug=0.744,
    tid_sep=0.72,
    tid_okt=0.744,
    tid_nov=0.72,
    tid_des=0.744,
    varmekapasitet_vann=4180,
    densitet_vann=988,
    varmekapasitet_kuldebaerer=4210,
    densitet_kuldebaerer=999.8,
    ForretningsBygg=False,
)

ashrae_besttest_620_expected_output = calc.Output(
    romoppvarming=6900,  # TODO AssertionError: 6899 != 6900
    ventilasjonsvarme=0,
    varmtvann=0,
    vifter=0,
    belysning=0,
    pumper=0,
    teknisk_utstyr=0,
    kjoeling=0,
    totalt_netto_energibehov=6900,  # TODO AssertionError: 6899 != 6900
    elektrisitet=7041,  # TODO AssertionError: 7040 != 7041
    olje=0,
    gass=0,
    fjernvarme=0,
    biobrensel=0,
    annen_energivare=0,
    totalt_levert_energi=7041,  # TODO AssertionError: 7040 != 7041
    primaerenergi=10562,  # TODO AssertionError: 10560 != 10562
    co2_utslipp=401,
    energi_kostnader=5633,  # AssertionError: 5632 != 5633
    energi_politisk=8450,  # TODO AssertionError: 8448 != 8450
)
