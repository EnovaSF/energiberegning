from dataclasses import dataclass
import numpy as np


@dataclass
class Output:
    """ This class holds the calculation result, one field per value """
    Romoppvarming: float
    Ventilasjonsvarme: float
    Varmtvann: float
    Vifter: float
    Pumper: float
    Belysning: float
    Teknisk_utstyr: float
    Kjoeling: float
    Totalt_netto_energibehov: float

    def __str__(self):
        return "Romoppvarming: {0.Romoppvarming}, Ventilasjonsvarme: {0.Ventilasjonsvarme}, Varmtvann: {0.Varmtvann}, Vifter: {0.Vifter}, Pumper: {0.Pumper}, Belysning: {0.Belysning}, Teknisk_utstyr: {0.Teknisk_utstyr}, Kjoeling: {0.Kjoeling}, Totalt_netto_energibehov: {0.Totalt_netto_energibehov}, Totalt_netto_energibehov: {0.Totalt_netto_energibehov}".format(
            self)


@dataclass
class EnergiBeregning:
    """ This class wraps all the calculations"""

    areal_oppv: float
    norm_varmekap: int
    kuldebro_normalisert: float
    temp_settpunkt_oppvarming: float
    temp_settpunkt_oppvarming_natt: float
    areal_tak: float
    areal_vegg_oest: float
    areal_vegg_vest: float
    areal_vegg_soer: float
    areal_vegg_nord: float
    areal_gulv_mot_det_fri: float
    areal_vindu_oest: float
    areal_vindu_vest: float
    areal_vindu_soer: float
    areal_vindu_nord: float
    areal_vindu_tak: float
    areal_dor: float
    U_tak: float
    U_vegg_oest: float
    U_vegg_vest: float
    U_vegg_soer: float
    U_vegg_nord: float
    U_gulv_mot_det_fri: float
    U_dor: float
    U_vindu_oest: float
    U_vindu_vest: float
    U_vindu_soer: float
    U_vindu_nord: float
    U_vindu_tak: float
    varmetapsfaktor_uoppv: float
    areal_mot_uoppvarmet: float
    U_mot_uoppvarmet_sone: float
    areal_gulv_kjeller: float
    faseforskjell_utetemp_varmetap: float
    aarsmiddeltemp_inne: float
    omkrets_gulv: float
    U_gulvkonstruksjon: float
    U_kjellerveggskonstruksjon: float
    tykkelse_grunnmur: float
    oppfyllingshoyde_kjellervegg: float
    varmekonduktivitet_kantisol: float
    kantisol_tykkelse: float
    kantisol_horisontal_dybde: float
    kantisol_vertikal_bredde: float
    dybde_periodisk_nedtrengning: float
    varmekonduktivitet_grunn: float
    tempvirkningsgrad_varmegjenvinner: float
    luftmengde_spesifikk_i_driftstid: float
    luftmengde_spesifikk_utenfor_driftstid: float
    terrengskjermingskoeff_e: float
    terrengskjermingskoeff_f: float
    lekkasjetall: float
    etasjehoyde_innvendig: float
    luftmengde_spesifikk_tilluft: float
    luftmengde_spesifikk_avtrekksluft: float
    vifteeffekt_spesifikk_i_driftstid: float
    vifteeffekt_spesifikk_utenfor_driftstid: float
    frostsikringstemperatur: float
    solskjermingsfaktor_horisont_oest: float
    solskjermingsfaktor_horisont_vest: float
    solskjermingsfaktor_horisont_soer: float
    solskjermingsfaktor_horisont_nord: float
    solskjermingsfaktor_horisont_tak: float
    solskjermingsfaktor_overheng_oest: float
    solskjermingsfaktor_overheng_vest: float
    solskjermingsfaktor_overheng_soer: float
    solskjermingsfaktor_overheng_nord: float
    solskjermingsfaktor_overheng_tak: float
    solskjermingsfaktor_finner_oest: float
    solskjermingsfaktor_finner_vest: float
    solskjermingsfaktor_finner_soer: float
    solskjermingsfaktor_finner_nord: float
    solskjermingsfaktor_finner_tak: float
    arealfraksjon_karm_oest: float
    arealfraksjon_karm_vest: float
    arealfraksjon_karm_soer: float
    arealfraksjon_karm_nord: float
    arealfraksjon_karm_tak: float
    sol_tidsvariabel_soer_jan: float
    sol_tidsvariabel_soer_feb: float
    sol_tidsvariabel_soer_mars: float
    sol_tidsvariabel_soer_april: float
    sol_tidsvariabel_soer_mai: float
    sol_tidsvariabel_soer_juni: float
    sol_tidsvariabel_soer_juli: float
    sol_tidsvariabel_soer_aug: float
    sol_tidsvariabel_soer_sept: float
    sol_tidsvariabel_soer_okt: float
    sol_tidsvariabel_soer_nov: float
    sol_tidsvariabel_soer_des: float
    sol_tidsvariabel_ost_vest_jan: float
    sol_tidsvariabel_ost_vest_feb: float
    sol_tidsvariabel_ost_vest_mars: float
    sol_tidsvariabel_ost_vest_april: float
    sol_tidsvariabel_ost_vest_mai: float
    sol_tidsvariabel_ost_vest_juni: float
    sol_tidsvariabel_ost_vest_juli: float
    sol_tidsvariabel_ost_vest_aug: float
    sol_tidsvariabel_ost_vest_sept: float
    sol_tidsvariabel_ost_vest_okt: float
    sol_tidsvariabel_ost_vest_nov: float
    sol_tidsvariabel_ost_vest_des: float
    sol_tidsvariabel_nord_jan: float
    sol_tidsvariabel_nord_feb: float
    sol_tidsvariabel_nord_mars: float
    sol_tidsvariabel_nord_april: float
    sol_tidsvariabel_nord_mai: float
    sol_tidsvariabel_nord_juni: float
    sol_tidsvariabel_nord_juli: float
    sol_tidsvariabel_nord_aug: float
    sol_tidsvariabel_nord_sept: float
    sol_tidsvariabel_nord_okt: float
    sol_tidsvariabel_nord_nov: float
    sol_tidsvariabel_nord_des: float
    solfaktor_vindu_oest: float
    solfaktor_vindu_vest: float
    solfaktor_vindu_soer: float
    solfaktor_vindu_nord: float
    solfaktor_vindu_tak: float
    solfaktor_total_glass_skjerming_oest: float
    solfaktor_total_glass_skjerming_vest: float
    solfaktor_total_glass_skjerming_soer: float
    solfaktor_total_glass_skjerming_nord: float
    solfaktor_total_glass_skjerming_tak: float
    varmetilskudd_lys_jan: float
    varmetilskudd_lys_feb: float
    varmetilskudd_lys_mar: float
    varmetilskudd_lys_apr: float
    varmetilskudd_lys_mai: float
    varmetilskudd_lys_jun: float
    varmetilskudd_lys_jul: float
    varmetilskudd_lys_aug: float
    varmetilskudd_lys_sep: float
    varmetilskudd_lys_okt: float
    varmetilskudd_lys_nov: float
    varmetilskudd_lys_des: float
    varmetilskudd_utstyr_jan: float
    varmetilskudd_utstyr_feb: float
    varmetilskudd_utstyr_mar: float
    varmetilskudd_utstyr_apr: float
    varmetilskudd_utstyr_mai: float
    varmetilskudd_utstyr_jun: float
    varmetilskudd_utstyr_jul: float
    varmetilskudd_utstyr_aug: float
    varmetilskudd_utstyr_sep: float
    varmetilskudd_utstyr_okt: float
    varmetilskudd_utstyr_nov: float
    varmetilskudd_utstyr_des: float
    varmetilskudd_person_jan: float
    varmetilskudd_person_feb: float
    varmetilskudd_person_mar: float
    varmetilskudd_person_apr: float
    varmetilskudd_person_mai: float
    varmetilskudd_person_jun: float
    varmetilskudd_person_jul: float
    varmetilskudd_person_aug: float
    varmetilskudd_person_sep: float
    varmetilskudd_person_okt: float
    varmetilskudd_person_nov: float
    varmetilskudd_person_des: float
    energibehov_tappevann: float
    energibehov_belysning: float
    energibehov_utstyr: float
    areal_avkjoelt_andel: float
    temp_settpunkt_kjoeling: float
    pumpeeffekt_spesifikk_oppv: float
    tid_drift_pumpe_oppv: float
    temp_differanse_veskekrets_oppvarming: float
    pumpeeffekt_spesifikk_kjoling: float
    tid_drift_pumpe_kjoling: float
    temp_differanse_veskekrets_kjoling: float
    el_solcelle_andel_el_spesifikt_forbruk: float
    el_er_andel_energi_oppv_ventilasjon: float
    el_hp_andel_energi_oppv_ventilasjon: float
    el_Tsol_andel_energi_oppv_ventilasjon: float
    el_er_andel_energi_tappevann_varme: float
    el_hp_andel_energi_tappevann_varme: float
    el_Tsol_andel_energi_tappevann_varme: float
    systemvirkningsgrad_solcelle: float
    systemvirkningsgrad_elektrisk_oppv_ventilasjon: float
    systemvirkningsgrad_elektrisk_tappevann_varme: float
    systemvirkningsgrad_varmepumpeanlegg_oppv_ventilasjon: float
    systemvirkningsgrad_varmepumpeanlegg_tappevann_varme: float
    systemvirkningsgrad_solfanger_termisk_oppv_ventilasjon: float
    systemvirkningsgrad_solfanger_termisk_tappevann_varme: float
    effektfaktor_kjoeleanlegg: float
    olje_andel_energi_oppv_ventilasjon: float
    olje_andel_energi_tappevann_varme: float
    systemvirkningsgrad_olje_oppv_ventilasjon: float
    systemvirkningsgrad_olje_tappevann_varme: float
    gass_andel_energi_oppv_ventilasjon: float
    gass_andel_energi_tappevann_varme: float
    systemvirkningsgrad_gass_oppv_ventilasjon: float
    systemvirkningsgrad_gass_tappevann_varme: float
    fjernvarme_andel_energi_oppv_ventilasjon: float
    fjernvarme_andel_energi_tappevann_varme: float
    systemvirkningsgrad_fjernvarme_oppv_ventilasjon: float
    systemvirkningsgrad_fjernvarme_tappevann: float
    bio_andel_energi_oppv_ventilasjon: float
    bio_andel_energi_tappevann_varme: float
    systemvirkningsgrad_bio_oppv_ventilasjon: float
    systemvirkningsgrad_bio_tappevann: float
    annet_andel_energi_oppv_ventilasjon: float
    annet_andel_energi_tappevann_varme: float
    systemvirkningsgrad_annet_oppv_ventilasjon: float
    systemvirkningsgrad_annet_tappevann: float
    CO2_faktor_el: float
    CO2_faktor_olje: float
    CO2_faktor_gass: float
    CO2_faktor_fjernvarme: float
    CO2_faktor_bio: float
    CO2_faktor_annet: float
    Primaerenergi_faktor_el: float
    Primaerenergi_faktor_olje: float
    Primaerenergi_faktor_gass: float
    Primaerenergi_faktor_fjernvarme: float
    Primaerenergi_faktor_bio: float
    Primaerenergi_faktor_annet: float
    Energipris_el: float
    Energipris_olje: float
    Energipris_gass: float
    Energipris_fjernvarme: float
    Energipris_bio: float
    Energipris_annet: float
    Energipol_vektingsfaktor_el: float
    Energipol_vektingsfaktor_olje: float
    Energipol_vektingsfaktor_gass: float
    Energipol_vektingsfaktor_fjernvarme: float
    Energipol_vektingsfaktor_bio: float
    Energipol_vektingsfaktor_annet: float
    tid_drift_oppv_belysn_utstyr_jan: float
    tid_drift_oppv_belysn_utstyr_feb: float
    tid_drift_oppv_belysn_utstyr_mar: float
    tid_drift_oppv_belysn_utstyr_apr: float
    tid_drift_oppv_belysn_utstyr_mai: float
    tid_drift_oppv_belysn_utstyr_jun: float
    tid_drift_oppv_belysn_utstyr_jul: float
    tid_drift_oppv_belysn_utstyr_aug: float
    tid_drift_oppv_belysn_utstyr_sep: float
    tid_drift_oppv_belysn_utstyr_okt: float
    tid_drift_oppv_belysn_utstyr_nov: float
    tid_drift_oppv_belysn_utstyr_des: float
    tid_drift_vent_jan: float
    tid_drift_vent_feb: float
    tid_drift_vent_mar: float
    tid_drift_vent_apr: float
    tid_drift_vent_mai: float
    tid_drift_vent_jun: float
    tid_drift_vent_jul: float
    tid_drift_vent_aug: float
    tid_drift_vent_sep: float
    tid_drift_vent_okt: float
    tid_drift_vent_nov: float
    tid_drift_vent_des: float
    tid_drift_person_jan: float
    tid_drift_person_feb: float
    tid_drift_person_mar: float
    tid_drift_person_apr: float
    tid_drift_person_mai: float
    tid_drift_person_jun: float
    tid_drift_person_jul: float
    tid_drift_person_aug: float
    tid_drift_person_sep: float
    tid_drift_person_okt: float
    tid_drift_person_nov: float
    tid_drift_person_des: float
    utetemp_jan: float
    utetemp_feb: float
    utetemp_mar: float
    utetemp_apr: float
    utetemp_mai: float
    utetemp_jun: float
    utetemp_jul: float
    utetemp_aug: float
    utetemp_sep: float
    utetemp_okt: float
    utetemp_nov: float
    utetemp_des: float
    aarsmiddeltemp_ute: float
    straalingsfluks_soer_jan: float
    straalingsfluks_soer_feb: float
    straalingsfluks_soer_mars: float
    straalingsfluks_soer_april: float
    straalingsfluks_soer_mai: float
    straalingsfluks_soer_juni: float
    straalingsfluks_soer_juli: float
    straalingsfluks_soer_aug: float
    straalingsfluks_soer_sept: float
    straalingsfluks_soer_okt: float
    straalingsfluks_soer_nov: float
    straalingsfluks_soer_des: float
    straalingsfluks_ostvest_jan: float
    straalingsfluks_ostvest_feb: float
    straalingsfluks_ostvest_mars: float
    straalingsfluks_ostvest_april: float
    straalingsfluks_ostvest_mai: float
    straalingsfluks_ostvest_juni: float
    straalingsfluks_ostvest_juli: float
    straalingsfluks_ostvest_aug: float
    straalingsfluks_ostvest_sept: float
    straalingsfluks_ostvest_okt: float
    straalingsfluks_ostvest_nov: float
    straalingsfluks_ostvest_des: float
    straalingsfluks_nord_jan: float
    straalingsfluks_nord_feb: float
    straalingsfluks_nord_mars: float
    straalingsfluks_nord_april: float
    straalingsfluks_nord_mai: float
    straalingsfluks_nord_juni: float
    straalingsfluks_nord_juli: float
    straalingsfluks_nord_aug: float
    straalingsfluks_nord_sept: float
    straalingsfluks_nord_okt: float
    straalingsfluks_nord_nov: float
    straalingsfluks_nord_des: float
    straalingsfluks_tak_jan: float
    straalingsfluks_tak_feb: float
    straalingsfluks_tak_mars: float
    straalingsfluks_tak_april: float
    straalingsfluks_tak_mai: float
    straalingsfluks_tak_juni: float
    straalingsfluks_tak_juli: float
    straalingsfluks_tak_aug: float
    straalingsfluks_tak_sept: float
    straalingsfluks_tak_okt: float
    straalingsfluks_tak_nov: float
    straalingsfluks_tak_des: float
    temp_avtrekk: float
    varmekapasitet_luft: float
    temp_amplitudevar: float
    tid_jan: float
    tid_feb: float
    tid_mar: float
    tid_apr: float
    tid_mai: float
    tid_jun: float
    tid_jul: float
    tid_aug: float
    tid_sep: float
    tid_okt: float
    tid_nov: float
    tid_des: float
    varmekapasitet_vann: float
    densitet_vann: float
    varmekapasitet_kuldebaerer: float
    densitet_kuldebaerer: float
    BygningskategoriErForretningsbygg: int
    REF: int

    def calculate(self):
        # This is where all the calculation stuff happens ie. your code
        # if the code is a lib, we can import it and call a calc function from it passing self
        # import 'your-library'
        # result = your-library.calculate(self.param1, self.param2 ...)
        # return Output(result['abc'], ...)

        # Example we may not do it like this but something like described above
        ### 2
        J237 = self.energibehov_tappevann  # NS3031*- Energibehov for varmt tappevann, spesifikt - Varmtvann
        C238 = self.areal_oppv  # NS3031 - Energibehov for varmt tappevann - Oppvarmed del av BRA
        C237 = J237 * C238  # NS3031 - Energibehov for varmt tappevann - Årlig energibehov
        Varmtvann = C237  # # - Energipost (2) (Energibehov [kWh/år]) - Varmtvann
        ### 4
        J272 = self.energibehov_belysning  # NS3031*- Energibehov for belysning, spesifikt - Belysning
        C273 = self.areal_oppv  # NS3031 - Energibehov for belysning - Oppvarmed del av BRA
        C272 = J272 * C273  # NS3031 - Energibehov for belysning - Årlig energibehov
        Belysning = C272  # # - Energipost (4) (Energibehov [kWh/år]) - Belysning
        ### 5
        J277 = self.energibehov_utstyr  # NS3031*- Energibehov for teknisk utstyr - Teknisk utstyr
        C278 = self.areal_oppv  # NS3031 - Energibehov for teknisk utstyr - Oppvarmed del av BRA
        C277 = J277 * C278  # NS3031 - Energibehov for utstyr - Årlig energibehov
        Teknisk_utstyr = C277  # # - Energipost (5) (Energibehov [kWh/år]) - Teknisk_utstyr
        ### 3a
        AE242 = (self.tid_jan) * 1000  # - Timer i måneden - januar
        AE243 = (self.tid_feb) * 1000  # - Timer i måneden - februar
        AE244 = (self.tid_mar) * 1000  # - Timer i måneden - mars
        AE245 = (self.tid_apr) * 1000  # - Timer i måneden - april
        AE246 = (self.tid_mai) * 1000  # - Timer i måneden - mai
        AE247 = (self.tid_jun) * 1000  # - Timer i måneden - juni
        AE248 = (self.tid_jul) * 1000  # - Timer i måneden - juli
        AE249 = (self.tid_aug) * 1000  # - Timer i måneden - august
        AE250 = (self.tid_sep) * 1000  # - Timer i måneden - september
        AE251 = (self.tid_okt) * 1000  # - Timer i måneden - oktober
        AE252 = (self.tid_nov) * 1000  # - Timer i måneden - november
        AE253 = (self.tid_des) * 1000  # - Timer i måneden - desember
        AE254 = np.mean([AE242, AE243, AE244, AE245, AE246, AE247, AE248, AE249, AE250, AE251, AE252, AE253])
        Q242 = self.tid_drift_vent_jan  # - Timer i driftstid for ventilasjon (Timer for måneden) - januar
        Q243 = self.tid_drift_vent_feb  # - Timer i driftstid for ventilasjon (Timer for måneden) - februar
        Q244 = self.tid_drift_vent_mar  # - Timer i driftstid for ventilasjon (Timer for måneden) - mars
        Q245 = self.tid_drift_vent_apr  # - Timer i driftstid for ventilasjon (Timer for måneden) - april
        Q246 = self.tid_drift_vent_mai  # - Timer i driftstid for ventilasjon (Timer for måneden) - mai
        Q247 = self.tid_drift_vent_jun  # - Timer i driftstid for ventilasjon (Timer for måneden) - juni
        Q248 = self.tid_drift_vent_jul  # - Timer i driftstid for ventilasjon (Timer for måneden) - juli
        Q249 = self.tid_drift_vent_aug  # - Timer i driftstid for ventilasjon (Timer for måneden) - august
        Q250 = self.tid_drift_vent_sep  # - Timer i driftstid for ventilasjon (Timer for måneden) - september
        Q251 = self.tid_drift_vent_okt  # - Timer i driftstid for ventilasjon (Timer for måneden) - oktober
        Q252 = self.tid_drift_vent_nov  # - Timer i driftstid for ventilasjon (Timer for måneden) - november
        Q253 = self.tid_drift_vent_des  # - Timer i driftstid for ventilasjon (Timer for måneden) - desember
        Q254 = np.mean([Q242, Q243, Q244, Q245, Q246, Q247, Q248, Q249, Q250, Q251, Q252,
                        Q253])  # - Timer i driftstid for ventilasjon (Timer for måneden) - AVERAGE
        X242 = AE242 - Q242  # - Timer i driftstid for ventilasjon (Timer for måneden) - januar
        X243 = AE243 - Q243  # - Timer i driftstid for ventilasjon (Timer for måneden) - februar
        X244 = AE244 - Q244  # - Timer i driftstid for ventilasjon (Timer for måneden) - mars
        X245 = AE245 - Q245  # - Timer i driftstid for ventilasjon (Timer for måneden) - april
        X246 = AE246 - Q246  # - Timer i driftstid for ventilasjon (Timer for måneden) - mai
        X247 = AE247 - Q247  # - Timer i driftstid for ventilasjon (Timer for måneden) - juni
        X248 = AE248 - Q248  # - Timer i driftstid for ventilasjon (Timer for måneden) - juli
        X249 = AE249 - Q249  # - Timer i driftstid for ventilasjon (Timer for måneden) - august
        X250 = AE250 - Q250  # - Timer i driftstid for ventilasjon (Timer for måneden) - september
        X251 = AE251 - Q251  # - Timer i driftstid for ventilasjon (Timer for måneden) - oktober
        X252 = AE252 - Q252  # - Timer i driftstid for ventilasjon (Timer for måneden) - november
        X253 = AE253 - Q253  # - Timer i driftstid for ventilasjon (Timer for måneden) - desember
        X254 = np.mean([X242, X243, X244, X245, X246, X247, X248, X249, X250, X251, X252,
                        X253])  # - Timer i driftstid for ventilasjon (Timer for måneden) - AVERAGE
        J242 = self.areal_oppv  # - Driftstid for ventilasjon - Oppvarmed del av BRA
        J244 = self.vifteeffekt_spesifikk_i_driftstid  # - Driftstid for ventilasjon - Spesifikk vifteeffekt i driftstiden
        J245 = self.vifteeffekt_spesifikk_utenfor_driftstid  # - Driftstid for ventilasjon - Spesifikk vifteeffekt utenfor driftstiden
        J249 = self.luftmengde_spesifikk_i_driftstid  # - Driftstid for ventilasjon - Spesifikk luftmengde i driftstiden
        J250 = self.luftmengde_spesifikk_utenfor_driftstid  # - Driftstid for ventilasjon - Spesifikk luftmengde utenfor driftstiden
        J247 = J249 * J242  # - Driftstid for ventilasjon - Luftmengde i driftstiden
        J248 = J250 * J242  # - Driftstid for ventilasjon - Luftmengde utenfor driftstiden
        C244 = (J247 * Q242 * J244 + J248 * X242 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - januar
        C245 = (J247 * Q243 * J244 + J248 * X243 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - februar
        C246 = (J247 * Q244 * J244 + J248 * X244 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - mars
        C247 = (J247 * Q245 * J244 + J248 * X245 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - april
        C248 = (J247 * Q246 * J244 + J248 * X246 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - mai
        C249 = (J247 * Q247 * J244 + J248 * X247 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - juni
        C250 = (J247 * Q248 * J244 + J248 * X248 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - juli
        C251 = (J247 * Q249 * J244 + J248 * X249 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - august
        C252 = (J247 * Q250 * J244 + J248 * X250 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - september
        C253 = (J247 * Q251 * J244 + J248 * X251 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - oktober
        C254 = (J247 * Q252 * J244 + J248 * X252 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - november
        C255 = (J247 * Q253 * J244 + J248 * X253 * J245) / 3600  # NS3031 - Energibehov for vifter og pumper - desember
        C242 = C244 + C245 + C246 + C247 + C248 + C249 + C250 + C251 + C252 + C253 + C254 + C255  # NS3031 - Energibehov for vifter og pumper (Vifter) - Totalt, Efan
        Vifter = C242  # # - Energipost (3a) (Energibehov [kWh/år]) - Vifter
        ### 1a
        Romoppvarming = 11810
        ### 1b
        Ventilasjonsvarme = 236
        ### 3b
        Pumper = 43
        ### 6
        Kjoeling = 0
        Totalt_netto_energibehov = Romoppvarming + Ventilasjonsvarme + \
                                   Varmtvann + \
                                   Vifter + Pumper + \
                                   Belysning + \
                                   Teknisk_utstyr + \
                                   Kjoeling

        return Output(Romoppvarming,
                      Ventilasjonsvarme,
                      Varmtvann,
                      Vifter,
                      Pumper,
                      Belysning,
                      Teknisk_utstyr,
                      Kjoeling,
                      Totalt_netto_energibehov)
