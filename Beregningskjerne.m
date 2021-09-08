from dataclasses import dataclass

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
        return "Romoppvarming: {0.Romoppvarming}, Ventilasjonsvarme: {0.Ventilasjonsvarme}, Varmtvann: {0.Varmtvann}, Vifter: {0.Vifter}, Pumper: {0.Pumper}, Belysning: {0.Belysning}, Teknisk_utstyr: {0.Teknisk_utstyr}, Kjoeling: {0.Kjoeling}, Totalt_netto_energibehov: {0.Totalt_netto_energibehov}, Totalt_netto_energibehov: {0.Totalt_netto_energibehov}".format(self)

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
    REF : int    
    
    def calculate(self):
        # This is where all the calculation stuff happens ie. your code
        # if the code is a lib, we can import it and call a calc function from it passing self
        # import 'your-library'
        # result = your-library.calculate(self.param1, self.param2 ...)
        # return Output(result['abc'], ...)

        # Example we may not do it like this but something like described above
        ### 2
        J237 = self.energibehov_tappevann # NS3031*- Energibehov for varmt tappevann, spesifikt - Varmtvann
        C238 = self.areal_oppv            # NS3031 - Energibehov for varmt tappevann - Oppvarmed del av BRA
        C237 =  J237*C238            # NS3031 - Energibehov for varmt tappevann - Årlig energibehov
        Varmtvann = C237             # # - Energipost (2) (Energibehov [kWh/år]) - Varmtvann

        ### 4
        J272 = self.energibehov_belysning # NS3031*- Energibehov for belysning, spesifikt - Belysning
        C273 = self.areal_oppv            # NS3031 - Energibehov for belysning - Oppvarmed del av BRA
        C272 = J272*C273             # NS3031 - Energibehov for belysning - Årlig energibehov
        Belysning = C272             # # - Energipost (4) (Energibehov [kWh/år]) - Belysning

        ### 5
        J277 = self.energibehov_utstyr # NS3031*- Energibehov for teknisk utstyr - Teknisk utstyr
        C278 = self.areal_oppv         # NS3031 - Energibehov for teknisk utstyr - Oppvarmed del av BRA
        C277 = J277*C278          # NS3031 - Energibehov for utstyr - Årlig energibehov
        Teknisk_utstyr = C277     # # - Energipost (5) (Energibehov [kWh/år]) - Teknisk_utstyr

        ### 3a
        AE242 = (self.tid_jan)*1000  # - Timer i måneden - januar
        AE243 = (self.tid_feb)*1000  # - Timer i måneden - februar
        AE244 = (self.tid_mar)*1000  # - Timer i måneden - mars
        AE245 = (self.tid_apr)*1000  # - Timer i måneden - april
        AE246 = (self.tid_mai)*1000  # - Timer i måneden - mai
        AE247 = (self.tid_jun)*1000  # - Timer i måneden - juni
        AE248 = (self.tid_jul)*1000  # - Timer i måneden - juli
        AE249 = (self.tid_aug)*1000  # - Timer i måneden - august
        AE250 = (self.tid_sep)*1000  # - Timer i måneden - september
        AE251 = (self.tid_okt)*1000  # - Timer i måneden - oktober
        AE252 = (self.tid_nov)*1000  # - Timer i måneden - november
        AE253 = (self.tid_des)*1000  # - Timer i måneden - desember
        AE254 = np.mean([AE242,AE243,AE244,AE245,AE246,AE247,AE248,AE249,AE250,AE251,AE252,AE253])
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
        Q254 = np.mean([Q242,Q243,Q244,Q245,Q246,Q247,Q248,Q249,Q250,Q251,Q252,Q253]) # - Timer i driftstid for ventilasjon (Timer for måneden) - AVERAGE
        X242 = AE242-Q242  # - Timer i driftstid for ventilasjon (Timer for måneden) - januar
        X243 = AE243-Q243  # - Timer i driftstid for ventilasjon (Timer for måneden) - februar
        X244 = AE244-Q244  # - Timer i driftstid for ventilasjon (Timer for måneden) - mars
        X245 = AE245-Q245  # - Timer i driftstid for ventilasjon (Timer for måneden) - april
        X246 = AE246-Q246  # - Timer i driftstid for ventilasjon (Timer for måneden) - mai
        X247 = AE247-Q247  # - Timer i driftstid for ventilasjon (Timer for måneden) - juni
        X248 = AE248-Q248  # - Timer i driftstid for ventilasjon (Timer for måneden) - juli
        X249 = AE249-Q249  # - Timer i driftstid for ventilasjon (Timer for måneden) - august
        X250 = AE250-Q250  # - Timer i driftstid for ventilasjon (Timer for måneden) - september
        X251 = AE251-Q251  # - Timer i driftstid for ventilasjon (Timer for måneden) - oktober
        X252 = AE252-Q252  # - Timer i driftstid for ventilasjon (Timer for måneden) - november
        X253 = AE253-Q253  # - Timer i driftstid for ventilasjon (Timer for måneden) - desember
        X254 = np.mean([X242,X243,X244,X245,X246,X247,X248,X249,X250,X251,X252,X253]) # - Timer i driftstid for ventilasjon (Timer for måneden) - AVERAGE
        J242 = self.areal_oppv                              # - Driftstid for ventilasjon - Oppvarmed del av BRA
        J244 = self.vifteeffekt_spesifikk_i_driftstid       # - Driftstid for ventilasjon - Spesifikk vifteeffekt i driftstiden
        J245 = self.vifteeffekt_spesifikk_utenfor_driftstid # - Driftstid for ventilasjon - Spesifikk vifteeffekt utenfor driftstiden
        J249 = self.luftmengde_spesifikk_i_driftstid        # - Driftstid for ventilasjon - Spesifikk luftmengde i driftstiden
        J250 = self.luftmengde_spesifikk_utenfor_driftstid  # - Driftstid for ventilasjon - Spesifikk luftmengde utenfor driftstiden
        J247 = J249*J242                               # - Driftstid for ventilasjon - Luftmengde i driftstiden
        J248 = J250*J242                               # - Driftstid for ventilasjon - Luftmengde utenfor driftstiden
        C244 = (J247*Q242*J244+J248*X242*J245)/3600 # NS3031 - Energibehov for vifter og pumper - januar
        C245 = (J247*Q243*J244+J248*X243*J245)/3600 # NS3031 - Energibehov for vifter og pumper - februar
        C246 = (J247*Q244*J244+J248*X244*J245)/3600 # NS3031 - Energibehov for vifter og pumper - mars
        C247 = (J247*Q245*J244+J248*X245*J245)/3600 # NS3031 - Energibehov for vifter og pumper - april
        C248 = (J247*Q246*J244+J248*X246*J245)/3600 # NS3031 - Energibehov for vifter og pumper - mai
        C249 = (J247*Q247*J244+J248*X247*J245)/3600 # NS3031 - Energibehov for vifter og pumper - juni
        C250 = (J247*Q248*J244+J248*X248*J245)/3600 # NS3031 - Energibehov for vifter og pumper - juli
        C251 = (J247*Q249*J244+J248*X249*J245)/3600 # NS3031 - Energibehov for vifter og pumper - august
        C252 = (J247*Q250*J244+J248*X250*J245)/3600 # NS3031 - Energibehov for vifter og pumper - september
        C253 = (J247*Q251*J244+J248*X251*J245)/3600 # NS3031 - Energibehov for vifter og pumper - oktober
        C254 = (J247*Q252*J244+J248*X252*J245)/3600 # NS3031 - Energibehov for vifter og pumper - november
        C255 = (J247*Q253*J244+J248*X253*J245)/3600 # NS3031 - Energibehov for vifter og pumper - desember
        C242 = C244+C245+C246+C247+C248+C249+C250+C251+C252+C253+C254+C255 # NS3031 - Energibehov for vifter og pumper (Vifter) - Totalt, Efan
        Vifter = C242 # # - Energipost (3a) (Energibehov [kWh/år]) - Vifter

        ### 1a
        C197 = tid_jan # - Timer per måned - januar
        C198 = tid_feb # - Timer per måned - februar
        C199 = tid_mar # - Timer per måned - mars
        C200 = tid_apr # - Timer per måned - april
        C201 = tid_mai # - Timer per måned - mai
        C202 = tid_jun # - Timer per måned - juni
        C203 = tid_jul # - Timer per måned - juli
        C204 = tid_aug # - Timer per måned - august
        C205 = tid_sep # - Timer per måned - september
        C206 = tid_okt # - Timer per måned - oktober
        C207 = tid_nov # - Timer per måned - november
        C208 = tid_des # - Timer per måned - desember
        X120 = straalingsfluks_soer_jan   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - januar
        X121 = straalingsfluks_soer_feb   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - februar
        X122 = straalingsfluks_soer_mars  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - mars
        X123 = straalingsfluks_soer_april # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - april
        X124 = straalingsfluks_soer_mai   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - mai
        X125 = straalingsfluks_soer_juni  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - juni
        X126 = straalingsfluks_soer_juli  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - juli
        X127 = straalingsfluks_soer_aug   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - august
        X128 = straalingsfluks_soer_sept  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - september
        X129 = straalingsfluks_soer_okt   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - oktober
        X130 = straalingsfluks_soer_nov   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - november
        X131 = straalingsfluks_soer_des   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - desember
        X137 = straalingsfluks_ostvest_jan   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - januar
        X138 = straalingsfluks_ostvest_feb   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - februar
        X139 = straalingsfluks_ostvest_mars  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - mars
        X140 = straalingsfluks_ostvest_april # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - april
        X141 = straalingsfluks_ostvest_mai   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - mai
        X142 = straalingsfluks_ostvest_juni  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - juni
        X143 = straalingsfluks_ostvest_juli  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - juli
        X144 = straalingsfluks_ostvest_aug   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - august
        X145 = straalingsfluks_ostvest_sept  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - september
        X146 = straalingsfluks_ostvest_okt   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - oktober
        X147 = straalingsfluks_ostvest_nov   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - november
        X148 = straalingsfluks_ostvest_des   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007) - desember
        AE120 = straalingsfluks_nord_jan   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - januar
        AE121 = straalingsfluks_nord_feb   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - februar
        AE122 = straalingsfluks_nord_mars  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - mars
        AE123 = straalingsfluks_nord_april # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - april
        AE124 = straalingsfluks_nord_mai   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - mai
        AE125 = straalingsfluks_nord_juni  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - juni
        AE126 = straalingsfluks_nord_juli  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - juli
        AE127 = straalingsfluks_nord_aug   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - august
        AE128 = straalingsfluks_nord_sept  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - september
        AE129 = straalingsfluks_nord_okt   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - oktober
        AE130 = straalingsfluks_nord_nov   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - november
        AE131 = straalingsfluks_nord_des   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007) - desember
        AE137 = straalingsfluks_tak_jan   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - januar
        AE138 = straalingsfluks_tak_feb   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - februar
        AE139 = straalingsfluks_tak_mars  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - mars
        AE140 = straalingsfluks_tak_april # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - april
        AE141 = straalingsfluks_tak_mai   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - mai
        AE142 = straalingsfluks_tak_juni  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - juni
        AE143 = straalingsfluks_tak_juli  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - juli
        AE144 = straalingsfluks_tak_aug   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - august
        AE145 = straalingsfluks_tak_sept  # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - september
        AE146 = straalingsfluks_tak_okt   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - oktober
        AE147 = straalingsfluks_tak_nov   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - november
        AE148 = straalingsfluks_tak_des   # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, tak (Tillegg M - NS3031:2007) - desember
        Q120 = (1-sol_tidsvariabel_ost_vest_jan)  *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_jan  *solfaktor_total_glass_skjerming_oest
        Q121 = (1-sol_tidsvariabel_ost_vest_feb)  *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_feb  *solfaktor_total_glass_skjerming_oest
        Q122 = (1-sol_tidsvariabel_ost_vest_mars) *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_mars *solfaktor_total_glass_skjerming_oest
        Q123 = (1-sol_tidsvariabel_ost_vest_april)*solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_april*solfaktor_total_glass_skjerming_oest
        Q124 = (1-sol_tidsvariabel_ost_vest_mai)  *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_mai  *solfaktor_total_glass_skjerming_oest
        Q125 = (1-sol_tidsvariabel_ost_vest_juni) *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_juni *solfaktor_total_glass_skjerming_oest
        Q126 = (1-sol_tidsvariabel_ost_vest_juli) *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_juli *solfaktor_total_glass_skjerming_oest
        Q127 = (1-sol_tidsvariabel_ost_vest_aug)  *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_aug  *solfaktor_total_glass_skjerming_oest
        Q128 = (1-sol_tidsvariabel_ost_vest_sept) *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_sept *solfaktor_total_glass_skjerming_oest
        Q129 = (1-sol_tidsvariabel_ost_vest_okt)  *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_okt  *solfaktor_total_glass_skjerming_oest
        Q130 = (1-sol_tidsvariabel_ost_vest_nov)  *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_nov  *solfaktor_total_glass_skjerming_oest
        Q131 = (1-sol_tidsvariabel_ost_vest_des)  *solfaktor_vindu_oest + sol_tidsvariabel_ost_vest_des  *solfaktor_total_glass_skjerming_oest
        Q133 = (1-sol_tidsvariabel_ost_vest_jan)  *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_jan  *solfaktor_total_glass_skjerming_vest
        Q134 = (1-sol_tidsvariabel_ost_vest_feb)  *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_feb  *solfaktor_total_glass_skjerming_vest
        Q135 = (1-sol_tidsvariabel_ost_vest_mars) *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_mars *solfaktor_total_glass_skjerming_vest
        Q136 = (1-sol_tidsvariabel_ost_vest_april)*solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_april*solfaktor_total_glass_skjerming_vest
        Q137 = (1-sol_tidsvariabel_ost_vest_mai)  *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_mai  *solfaktor_total_glass_skjerming_vest
        Q138 = (1-sol_tidsvariabel_ost_vest_juni) *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_juni *solfaktor_total_glass_skjerming_vest
        Q139 = (1-sol_tidsvariabel_ost_vest_juli) *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_juli *solfaktor_total_glass_skjerming_vest
        Q140 = (1-sol_tidsvariabel_ost_vest_aug)  *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_aug  *solfaktor_total_glass_skjerming_vest
        Q141 = (1-sol_tidsvariabel_ost_vest_sept) *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_sept *solfaktor_total_glass_skjerming_vest
        Q142 = (1-sol_tidsvariabel_ost_vest_okt)  *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_okt  *solfaktor_total_glass_skjerming_vest
        Q143 = (1-sol_tidsvariabel_ost_vest_nov)  *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_nov  *solfaktor_total_glass_skjerming_vest
        Q144 = (1-sol_tidsvariabel_ost_vest_des)  *solfaktor_vindu_vest + sol_tidsvariabel_ost_vest_des  *solfaktor_total_glass_skjerming_vest
        Q146 = (1-sol_tidsvariabel_soer_jan)  *solfaktor_vindu_soer + sol_tidsvariabel_soer_jan  *solfaktor_total_glass_skjerming_soer
        Q147 = (1-sol_tidsvariabel_soer_feb)  *solfaktor_vindu_soer + sol_tidsvariabel_soer_feb  *solfaktor_total_glass_skjerming_soer
        Q148 = (1-sol_tidsvariabel_soer_mars) *solfaktor_vindu_soer + sol_tidsvariabel_soer_mars *solfaktor_total_glass_skjerming_soer
        Q149 = (1-sol_tidsvariabel_soer_april)*solfaktor_vindu_soer + sol_tidsvariabel_soer_april*solfaktor_total_glass_skjerming_soer
        Q150 = (1-sol_tidsvariabel_soer_mai)  *solfaktor_vindu_soer + sol_tidsvariabel_soer_mai  *solfaktor_total_glass_skjerming_soer
        Q151 = (1-sol_tidsvariabel_soer_juni) *solfaktor_vindu_soer + sol_tidsvariabel_soer_juni *solfaktor_total_glass_skjerming_soer
        Q152 = (1-sol_tidsvariabel_soer_juli) *solfaktor_vindu_soer + sol_tidsvariabel_soer_juli *solfaktor_total_glass_skjerming_soer
        Q153 = (1-sol_tidsvariabel_soer_aug)  *solfaktor_vindu_soer + sol_tidsvariabel_soer_aug  *solfaktor_total_glass_skjerming_soer
        Q154 = (1-sol_tidsvariabel_soer_sept) *solfaktor_vindu_soer + sol_tidsvariabel_soer_sept *solfaktor_total_glass_skjerming_soer
        Q155 = (1-sol_tidsvariabel_soer_okt)  *solfaktor_vindu_soer + sol_tidsvariabel_soer_okt  *solfaktor_total_glass_skjerming_soer
        Q156 = (1-sol_tidsvariabel_soer_nov)  *solfaktor_vindu_soer + sol_tidsvariabel_soer_nov  *solfaktor_total_glass_skjerming_soer
        Q157 = (1-sol_tidsvariabel_soer_des)  *solfaktor_vindu_soer + sol_tidsvariabel_soer_des  *solfaktor_total_glass_skjerming_soer
        Q159 = (1-sol_tidsvariabel_nord_jan)  *solfaktor_vindu_nord + sol_tidsvariabel_nord_jan  *solfaktor_total_glass_skjerming_nord
        Q160 = (1-sol_tidsvariabel_nord_feb)  *solfaktor_vindu_nord + sol_tidsvariabel_nord_feb  *solfaktor_total_glass_skjerming_nord
        Q161 = (1-sol_tidsvariabel_nord_mars) *solfaktor_vindu_nord + sol_tidsvariabel_nord_mars *solfaktor_total_glass_skjerming_nord
        Q162 = (1-sol_tidsvariabel_nord_april)*solfaktor_vindu_nord + sol_tidsvariabel_nord_april*solfaktor_total_glass_skjerming_nord
        Q163 = (1-sol_tidsvariabel_nord_mai)  *solfaktor_vindu_nord + sol_tidsvariabel_nord_mai  *solfaktor_total_glass_skjerming_nord
        Q164 = (1-sol_tidsvariabel_nord_juni) *solfaktor_vindu_nord + sol_tidsvariabel_nord_juni *solfaktor_total_glass_skjerming_nord
        Q165 = (1-sol_tidsvariabel_nord_juli) *solfaktor_vindu_nord + sol_tidsvariabel_nord_juli *solfaktor_total_glass_skjerming_nord
        Q166 = (1-sol_tidsvariabel_nord_aug)  *solfaktor_vindu_nord + sol_tidsvariabel_nord_aug  *solfaktor_total_glass_skjerming_nord
        Q167 = (1-sol_tidsvariabel_nord_sept) *solfaktor_vindu_nord + sol_tidsvariabel_nord_sept *solfaktor_total_glass_skjerming_nord
        Q168 = (1-sol_tidsvariabel_nord_okt)  *solfaktor_vindu_nord + sol_tidsvariabel_nord_okt  *solfaktor_total_glass_skjerming_nord
        Q169 = (1-sol_tidsvariabel_nord_nov)  *solfaktor_vindu_nord + sol_tidsvariabel_nord_nov  *solfaktor_total_glass_skjerming_nord
        Q170 = (1-sol_tidsvariabel_nord_des)  *solfaktor_vindu_nord + sol_tidsvariabel_nord_des  *solfaktor_total_glass_skjerming_nord
        C157 = areal_vindu_oest # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, øst
        C158 = areal_vindu_vest # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, vest
        C159 = areal_vindu_soer # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, sør
        C160 = areal_vindu_nord # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, nord
        C161 = areal_vindu_tak  # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, tak
        C163 = arealfraksjon_karm_oest # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, øst
        C164 = arealfraksjon_karm_vest # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, vest
        C165 = arealfraksjon_karm_soer # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, sør
        C166 = arealfraksjon_karm_nord # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, nord
        C167 = arealfraksjon_karm_tak  # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, tak
        AE154 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - januar (Solfaktor x 0,9, dvs. forenklet)
        AE155 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - februar (Solfaktor x 0,9, dvs. forenklet)
        AE156 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - mars (Solfaktor x 0,9, dvs. forenklet)
        AE157 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - april (Solfaktor x 0,9, dvs. forenklet)
        AE158 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - mai (Solfaktor x 0,9, dvs. forenklet)
        AE159 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - juni (Solfaktor x 0,9, dvs. forenklet)
        AE160 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - juli (Solfaktor x 0,9, dvs. forenklet)
        AE161 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - august (Solfaktor x 0,9, dvs. forenklet)
        AE162 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - sept (Solfaktor x 0,9, dvs. forenklet)
        AE163 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - okt (Solfaktor x 0,9, dvs. forenklet)
        AE164 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - nov (Solfaktor x 0,9, dvs. forenklet)
        AE165 = solfaktor_vindu_tak*0,9 # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt - des (Solfaktor x 0,9, dvs. forenklet)
        AE166 = np.mean([AE154,AE155,AE156,AE157,AE158,AE159,AE160,AE161,AE162,AE163,AE164,AE165]) # Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt (tak)
        J172 = C161*AE166*(1-C167) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, tak
        J120 = C157*Q120*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - januar
        J121 = C157*Q121*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - februar
        J122 = C157*Q122*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - mars
        J123 = C157*Q123*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - april
        J124 = C157*Q124*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - mai
        J125 = C157*Q125*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - juni
        J126 = C157*Q126*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - juli
        J127 = C157*Q127*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - august
        J128 = C157*Q128*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - september
        J129 = C157*Q129*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - oktober
        J130 = C157*Q130*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - november
        J131 = C157*Q131*(1-C163) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst - desember
        J133 = C158*Q133*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - januar
        J134 = C158*Q134*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - februar
        J135 = C158*Q135*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - mars
        J136 = C158*Q136*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - april
        J137 = C158*Q137*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - mai
        J138 = C158*Q138*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - juni
        J139 = C158*Q139*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - juli
        J140 = C158*Q140*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - august
        J141 = C158*Q141*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - september
        J142 = C158*Q142*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - oktober
        J143 = C158*Q143*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - november
        J144 = C158*Q144*(1-C164) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest - desember
        J146 = C159*Q146*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - januar
        J147 = C159*Q147*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - februar
        J148 = C159*Q148*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - mars
        J149 = C159*Q149*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - april
        J150 = C159*Q150*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - mai
        J151 = C159*Q151*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - juni
        J152 = C159*Q152*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - juli
        J153 = C159*Q153*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - august
        J154 = C159*Q154*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - september
        J155 = C159*Q155*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - oktober
        J156 = C159*Q156*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - november
        J157 = C159*Q157*(1-C165) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør - desember
        J159 = C160*Q159*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - januar
        J160 = C160*Q160*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - februar
        J161 = C160*Q161*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - mars
        J162 = C160*Q162*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - april
        J163 = C160*Q163*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - mai
        J164 = C160*Q164*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - juni
        J165 = C160*Q165*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - juli
        J166 = C160*Q166*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - august
        J167 = C160*Q167*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - september
        J168 = C160*Q168*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - oktober
        J169 = C160*Q169*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - november
        J170 = C160*Q170*(1-C166) # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord - desember
        X159 = solskjermingsfaktor_horisont_oest # - Solskjermingsfaktor - Fhor,øst
        X160 = solskjermingsfaktor_horisont_vest # - Solskjermingsfaktor - Fhor,vest
        X161 = solskjermingsfaktor_horisont_soer # - Solskjermingsfaktor - Fhor,sør
        X162 = solskjermingsfaktor_horisont_nord # - Solskjermingsfaktor - Fhor,nord
        X163 = solskjermingsfaktor_horisont_tak  # - Solskjermingsfaktor - Fhor,tak
        X164 = solskjermingsfaktor_overheng_oest # - Solskjermingsfaktor - Fov,øst
        X165 = solskjermingsfaktor_overheng_vest # - Solskjermingsfaktor - Fov,vest
        X166 = solskjermingsfaktor_overheng_soer # - Solskjermingsfaktor - Fov,sør
        X167 = solskjermingsfaktor_overheng_nord # - Solskjermingsfaktor - Fov,nord
        X168 = solskjermingsfaktor_overheng_tak  # - Solskjermingsfaktor - Fov,tak
        X169 = solskjermingsfaktor_finner_oest # - Solskjermingsfaktor - Ffin,vest
        X170 = solskjermingsfaktor_finner_vest # - Solskjermingsfaktor - Ffin,vest
        X171 = solskjermingsfaktor_finner_soer # - Solskjermingsfaktor - Ffin,vest
        X172 = solskjermingsfaktor_finner_nord # - Solskjermingsfaktor - Ffin,vest
        X173 = solskjermingsfaktor_finner_tak  # - Solskjermingsfaktor - Ffin,vest
        X153 = X159*X164*X169 # - Solskjermingsfaktor - Solskjermingsfaktor, øst
        X154 = X160*X165*X170 # - Solskjermingsfaktor - Solskjermingsfaktor, vest
        X155 = X161*X166*X171 # - Solskjermingsfaktor - Solskjermingsfaktor, sør
        X156 = X162*X167*X172 # - Solskjermingsfaktor - Solskjermingsfaktor, nord
        X157 = X163*X168*X173 # - Solskjermingsfaktor - Solskjermingsfaktor, tak
        C151 = X153 # NS3031 - Varmettilskudd fra sol - Solskjermingsfaktor, øst
        C152 = X154 # NS3031 - Varmettilskudd fra sol - Solskjermingsfaktor, vest
        C153 = X155 # NS3031 - Varmettilskudd fra sol - Solskjermingsfaktor, sør
        C154 = X156 # NS3031 - Varmettilskudd fra sol - Solskjermingsfaktor, nord
        C155 = X157 # NS3031 - Varmettilskudd fra sol - Solskjermingsfaktor, tak
        C138 = C197*(X120*J120*C151 + X137*J133*C152 + X137*J146*C153 + AE120*C154*J159 + AE137*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - januar 
        C139 = C198*(X121*J121*C151 + X138*J134*C152 + X138*J147*C153 + AE121*C154*J160 + AE138*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - februar
        C140 = C199*(X122*J122*C151 + X139*J135*C152 + X139*J148*C153 + AE122*C154*J161 + AE139*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - mars
        C141 = C200*(X123*J123*C151 + X140*J136*C152 + X140*J149*C153 + AE123*C154*J162 + AE140*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - april
        C142 = C201*(X124*J124*C151 + X141*J137*C152 + X141*J150*C153 + AE124*C154*J163 + AE141*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - mai
        C143 = C202*(X125*J125*C151 + X142*J138*C152 + X142*J151*C153 + AE125*C154*J164 + AE142*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - juni
        C144 = C203*(X126*J126*C151 + X143*J139*C152 + X143*J152*C153 + AE126*C154*J165 + AE143*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - juli
        C145 = C204*(X127*J127*C151 + X144*J140*C152 + X144*J153*C153 + AE127*C154*J166 + AE144*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - august
        C146 = C205*(X128*J128*C151 + X145*J141*C152 + X145*J154*C153 + AE128*C154*J167 + AE145*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - september
        C147 = C206*(X129*J129*C151 + X146*J142*C152 + X146*J155*C153 + AE129*C154*J168 + AE146*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - oktober
        C148 = C207*(X130*J130*C151 + X147*J143*C152 + X147*J156*C153 + AE130*C154*J169 + AE147*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - novmeber
        C149 = C208*(X131*J131*C151 + X148*J144*C152 + X148*J157*C153 + AE131*C154*J170 + AE148*J172*C155) # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - desember
        J179 = varmetilskudd_lys_jan   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- januar (W/m2)
        J180 = varmetilskudd_lys_feb   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- februar (W/m2)
        J181 = varmetilskudd_lys_mar   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- mars (W/m2)
        J182 = varmetilskudd_lys_apr   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- april (W/m2)
        J183 = varmetilskudd_lys_mai   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- mai (W/m2)
        J184 = varmetilskudd_lys_jun   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- juni (W/m2)
        J185 = varmetilskudd_lys_jul   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- juli (W/m2)
        J186 = varmetilskudd_lys_aug   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- august (W/m2)
        J187 = varmetilskudd_lys_sep   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- september (W/m2)
        J188 = varmetilskudd_lys_okt   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- oktober (W/m2)
        J189 = varmetilskudd_lys_nov   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- november (W/m2)
        J190 = varmetilskudd_lys_des   # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- desember (W/m2)
        J197 = tid_drift_oppv_belysn_utstyr_jan   # - Timer i driftstid for belysning - januar (timer)
        J198 = tid_drift_oppv_belysn_utstyr_feb   # - Timer i driftstid for belysning - februar (timer)
        J199 = tid_drift_oppv_belysn_utstyr_mar   # - Timer i driftstid for belysning - mars (timer)
        J200 = tid_drift_oppv_belysn_utstyr_apr   # - Timer i driftstid for belysning - april (timer)
        J201 = tid_drift_oppv_belysn_utstyr_mai   # - Timer i driftstid for belysning - mai (timer)
        J202 = tid_drift_oppv_belysn_utstyr_jun   # - Timer i driftstid for belysning - juni (timer)
        J203 = tid_drift_oppv_belysn_utstyr_jul   # - Timer i driftstid for belysning - juli (timer)
        J204 = tid_drift_oppv_belysn_utstyr_aug   # - Timer i driftstid for belysning - august (timer)
        J205 = tid_drift_oppv_belysn_utstyr_sep   # - Timer i driftstid for belysning - september (timer)
        J206 = tid_drift_oppv_belysn_utstyr_okt   # - Timer i driftstid for belysning - oktober (timer)
        J207 = tid_drift_oppv_belysn_utstyr_nov   # - Timer i driftstid for belysning - november (timer)
        J208 = tid_drift_oppv_belysn_utstyr_des   # - Timer i driftstid for belysning - desember (timer)
        Q179 = varmetilskudd_utstyr_jan   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- januar (W/m2)
        Q180 = varmetilskudd_utstyr_feb   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- februar (W/m2)
        Q181 = varmetilskudd_utstyr_mar   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- mars (W/m2)
        Q182 = varmetilskudd_utstyr_apr   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- april (W/m2)
        Q183 = varmetilskudd_utstyr_mai   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- mai (W/m2)
        Q184 = varmetilskudd_utstyr_jun   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- juni (W/m2)
        Q185 = varmetilskudd_utstyr_jul   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- juli (W/m2)
        Q186 = varmetilskudd_utstyr_aug   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- august (W/m2)
        Q187 = varmetilskudd_utstyr_sep   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- september (timer)
        Q188 = varmetilskudd_utstyr_okt   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- oktober (W/m2)
        Q189 = varmetilskudd_utstyr_nov   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- november (W/m2)
        Q190 = varmetilskudd_utstyr_des   # - Spesifikk gjennomsnittlig varmetilskudd fra utstyr- desember (W/m2)
        Q197 = tid_drift_oppv_belysn_utstyr_jan   # - Timer i driftstid for belysning - januar (timer)
        Q198 = tid_drift_oppv_belysn_utstyr_feb   # - Timer i driftstid for belysning - februar (timer)
        Q199 = tid_drift_oppv_belysn_utstyr_mar   # - Timer i driftstid for belysning - mars (timer)
        Q200 = tid_drift_oppv_belysn_utstyr_apr   # - Timer i driftstid for belysning - april (timer)
        Q201 = tid_drift_oppv_belysn_utstyr_mai   # - Timer i driftstid for belysning - mai (timer)
        Q202 = tid_drift_oppv_belysn_utstyr_jun   # - Timer i driftstid for belysning - juni (timer)
        Q203 = tid_drift_oppv_belysn_utstyr_jul   # - Timer i driftstid for belysning - juli (timer)
        Q204 = tid_drift_oppv_belysn_utstyr_aug   # - Timer i driftstid for belysning - august (timer)
        Q205 = tid_drift_oppv_belysn_utstyr_sep   # - Timer i driftstid for belysning - september (timer)
        Q206 = tid_drift_oppv_belysn_utstyr_okt   # - Timer i driftstid for belysning - oktober (timer)
        Q207 = tid_drift_oppv_belysn_utstyr_nov   # - Timer i driftstid for belysning - november (timer)
        Q208 = tid_drift_oppv_belysn_utstyr_des   # - Timer i driftstid for belysning - desember (timer)
        X179 = varmetilskudd_person_jan   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - januar (W/m2)
        X180 = varmetilskudd_person_feb   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - februar (W/m2)
        X181 = varmetilskudd_person_mar   # - Spesifikk gjennomsnittlig varmetilskudd fra personer- mars (W/m2)
        X182 = varmetilskudd_person_apr   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - april (W/m2)
        X183 = varmetilskudd_person_mai   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - mai (W/m2)
        X184 = varmetilskudd_person_jun   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - juni (W/m2)
        X185 = varmetilskudd_person_jul   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - juli (W/m2)
        X186 = varmetilskudd_person_aug   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - august (W/m2)
        X187 = varmetilskudd_person_sep   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - september (W/m2)
        X188 = varmetilskudd_person_okt   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - oktober (W/m2)
        X189 = varmetilskudd_person_nov   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - november (W/m2)
        X190 = varmetilskudd_person_des   # - Spesifikk gjennomsnittlig varmetilskudd fra personer - desember (W/m2)
        X197 = tid_drift_person_jan   # - Timer i driftstid for personer - januar (timer) 
        X198 = tid_drift_person_feb   # - Timer i driftstid for personer - februar (timer)
        X199 = tid_drift_person_mar   # - Timer i driftstid for personer - mars (timer)
        X200 = tid_drift_person_apr   # - Timer i driftstid for personer - april (timer)
        X201 = tid_drift_person_mai   # - Timer i driftstid for personer - mai (timer)
        X202 = tid_drift_person_jun   # - Timer i driftstid for personer - juni (timer)
        X203 = tid_drift_person_jul   # - Timer i driftstid for personer - juli (timer)
        X204 = tid_drift_person_aug   # - Timer i driftstid for personer - august (timer)
        X205 = tid_drift_person_sep   # - Timer i driftstid for personer - september (timer)
        X206 = tid_drift_person_okt   # - Timer i driftstid for personer - oktober (timer)
        X207 = tid_drift_person_nov   # - Timer i driftstid for personer - november (timer)
        X208 = tid_drift_person_des   # - Timer i driftstid for personer - desember (timer)
        C192 = areal_oppv # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - Oppvarmed del av BRA
        X72 = Q254 # NS3031* - Ventilasjonsvarmetap, HV - Antall timer i måneden i driftstiden, ton
        X73 = X254 # NS3031* - Ventilasjonsvarmetap, HV - Antall timer i måneden utenfor driftstiden, tred
        X76 = luftmengde_spesifikk_i_driftstid # NS3031* - Ventilasjonsvarmetap, HV - Spesifikk luftmengde for ventilasjon ihht. byggkategori i driftstid
        X77 = luftmengde_spesifikk_utenfor_driftstid # NS3031* - Ventilasjonsvarmetap, HV - Spesifikk luftmengde for ventilasjon ihht. byggkategori utenfor driftstid
        X78 = BygningskategoriErForretningsbygg# NS3031* - Ventilasjonsvarmetap, HV - Hvorvidt bygningen tilhører kategorien forretningsbygg eller bolig
        term1 = (1.6-0.007*(areal_oppv-50)) if areal_oppv<110 else 1.2
        X74 = term1 if X78==0 else X76 # NS3031* - Ventilasjonsvarmetap, HV - Arealkorreksjon for bolig, på spesifikk luftmengde for ventilasjon i driftstid
        X75 = term1 if X78==0 else X77 # NS3031* - Ventilasjonsvarmetap, HV - Arealkorreksjon for bolig, på spesifikk luftmengde for ventilasjon utenfor driftstid
        X67 = X74*areal_oppv # NS3031* - Ventilasjonsvarmetap, HV - Gjennomsnittlig ventilasjon i driftstiden
        X68 = X75*areal_oppv # NS3031* - Ventilasjonsvarmetap, HV - Gjennomsnittlig ventilasjon utenfor driftstiden
        X70 = varmekapasitet_luft # NS3031* - Ventilasjonsvarmetap, HV - Luftens varmekapasitet per volum
        X69 = tempvirkningsgrad_varmegjenvinner# NS3031* - Ventilasjonsvarmetap, HV - Temperaturvirkningsgrad for varmegjenvinner
        X66 = (X72*X67+X73*X68)/(X72+X73) # NS3031* - Ventilasjonsvarmetap, HV - Gjennomsnittlig ventilasjonsmengde
        X64 = X70*X66*(1-X69) # NS3031* - Ventilasjonsvarmetap, HV - Totalt, HV
        X65 = X64/areal_oppv# NS3031* - Ventilasjonsvarmetap, HV - G
        AE180 = 0.37 * np.mean([vifteeffekt_spesifikk_i_driftstid,vifteeffekt_spesifikk_utenfor_driftstid]) # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Temperaturøkning over avtrekksvifte
        AE179 = 0.37 * np.mean([vifteeffekt_spesifikk_i_driftstid,vifteeffekt_spesifikk_utenfor_driftstid]) # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Temperaturøkning over tilluftsvifte
        AE181 = X66                                                                                         # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Gjennomsnittlig ventilasjon
        AE183 = tempvirkningsgrad_varmegjenvinner                                                           # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Varmegjenvinnerens temperaturvirkningsgrad
        AE185 = areal_oppv                                                                                  # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Oppvarmed del av BRA (m2)
        AE177 = 0 if AE183<=0 else varmekapasitet_luft*(AE181*((1-AE183)*AE179+AE183*AE180))/AE185          # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Varmetilskudd fra vifter
        C179 = (J197/1000*J179 + Q197/1000*Q179 + X197/1000*X179 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - januar
        C180 = (J198/1000*J180 + Q198/1000*Q180 + X198/1000*X180 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - februar
        C181 = (J199/1000*J181 + Q199/1000*Q181 + X199/1000*X181 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - mars
        C182 = (J200/1000*J182 + Q200/1000*Q182 + X200/1000*X182 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - april
        C183 = (J201/1000*J183 + Q201/1000*Q183 + X201/1000*X183 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - mail
        C184 = (J202/1000*J184 + Q202/1000*Q184 + X202/1000*X184 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - juni
        C185 = (J203/1000*J185 + Q203/1000*Q185 + X203/1000*X185 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - juli
        C186 = (J204/1000*J186 + Q204/1000*Q186 + X204/1000*X186 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - august
        C187 = (J205/1000*J187 + Q205/1000*Q187 + X205/1000*X187 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - september
        C188 = (J206/1000*J188 + Q206/1000*Q188 + X206/1000*X188 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - oktober
        C189 = (J207/1000*J189 + Q207/1000*Q189 + X207/1000*X189 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - november
        C190 = (J208/1000*J190 + Q208/1000*Q190 + X208/1000*X190 + AE177/1000*np.mean([Q254,AE254]))*C192 # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - desember        
        C120 = C138 + C179 # NS3031 - Varmettilskudd - januar
        C121 = C139 + C180 # NS3031 - Varmettilskudd - februar
        C122 = C140 + C181 # NS3031 - Varmettilskudd - mars
        C123 = C141 + C182 # NS3031 - Varmettilskudd - april
        C124 = C142 + C183 # NS3031 - Varmettilskudd - mai
        C125 = C143 + C184 # NS3031 - Varmettilskudd - juni
        C126 = C144 + C185 # NS3031 - Varmettilskudd - juli
        C127 = C145 + C186 # NS3031 - Varmettilskudd - august
        C128 = C146 + C187 # NS3031 - Varmettilskudd - september
        C129 = C147 + C188 # NS3031 - Varmettilskudd - oktober  
        C130 = C148 + C189 # NS3031 - Varmettilskudd - november 
        C131 = C149 + C190 # NS3031 - Varmettilskudd - desember
        X46 = tid_drift_oppv_belysn_utstyr_jan # - Timer i driftstid for oppvarming - Timer for måneden - januar
        X47 = tid_drift_oppv_belysn_utstyr_feb # - Timer i driftstid for oppvarming - Timer for måneden - februar
        X48 = tid_drift_oppv_belysn_utstyr_mar # - Timer i driftstid for oppvarming - Timer for måneden - mars
        X49 = tid_drift_oppv_belysn_utstyr_apr # - Timer i driftstid for oppvarming - Timer for måneden - april
        X50 = tid_drift_oppv_belysn_utstyr_mai # - Timer i driftstid for oppvarming - Timer for måneden - mai
        X51 = tid_drift_oppv_belysn_utstyr_jun # - Timer i driftstid for oppvarming - Timer for måneden - juni
        X52 = tid_drift_oppv_belysn_utstyr_jul # - Timer i driftstid for oppvarming - Timer for måneden - juli
        X53 = tid_drift_oppv_belysn_utstyr_aug # - Timer i driftstid for oppvarming - Timer for måneden - august
        X54 = tid_drift_oppv_belysn_utstyr_sep # - Timer i driftstid for oppvarming - Timer for måneden - september
        X55 = tid_drift_oppv_belysn_utstyr_okt # - Timer i driftstid for oppvarming - Timer for måneden - oktober
        X56 = tid_drift_oppv_belysn_utstyr_nov # - Timer i driftstid for oppvarming - Timer for måneden - november
        X57 = tid_drift_oppv_belysn_utstyr_des # - Timer i driftstid for oppvarming - Timer for måneden - desember
        AE46 = AE242-X46 # Timer utenfor driftstid for oppvarming - januar
        AE47 = AE243-X47 # Timer utenfor driftstid for oppvarming - februar
        AE48 = AE244-X48 # Timer utenfor driftstid for oppvarming - mars
        AE49 = AE245-X49 # Timer utenfor driftstid for oppvarming - april
        AE50 = AE246-X50 # Timer utenfor driftstid for oppvarming - mai
        AE51 = AE247-X51 # Timer utenfor driftstid for oppvarming - juni
        AE52 = AE248-X52 # Timer utenfor driftstid for oppvarming - juli
        AE53 = AE249-X53 # Timer utenfor driftstid for oppvarming - august
        AE54 = AE250-X54 # Timer utenfor driftstid for oppvarming - september
        AE55 = AE251-X55 # Timer utenfor driftstid for oppvarming - oktober
        AE56 = AE252-X56 # Timer utenfor driftstid for oppvarming - november
        AE57 = AE253-X57 # Timer utenfor driftstid for oppvarming - desember
        C84 = U_tak                   # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, tak
        C85 = U_vegg_oest             # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg øst, uten vindu og dør
        C86 = U_vegg_vest             # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg vest, uten vindu og dør
        C87 = U_vegg_soer             # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg sør, uten vindu og dør
        C88 = U_vegg_nord             # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg nord, uten vindu og dør
        C89 = U_gulv_mot_det_fri      # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, gulv, mot det fri
        C91 = U_vindu_oest            # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, øst
        C92 = U_vindu_vest            # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, vest
        C93 = U_vindu_soer            # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, sør
        C94 = U_vindu_nord            # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, nord
        C95 = U_vindu_tak             # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, tak
        C96 = U_dor                   # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, dør
        C98 = areal_tak               # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, tak
        C99 = areal_vegg_oest         # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg øst, uten vindu og dør
        C100 = areal_vegg_vest        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg vest, uten vindu og dør
        C101 = areal_vegg_soer        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg sør, uten vindu og dør
        C102 = areal_vegg_nord        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg nord, uten vindu og dør
        C103 = areal_gulv_mot_det_fri # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, gulv mot det fri
        C105 = areal_vindu_oest       # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vindu, øst
        C106 = areal_vindu_vest       # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vindu, vest
        C107 = areal_vindu_soer       # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vindu, sør
        C108 = areal_vindu_nord       # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vindu, nord
        C109 = areal_vindu_tak        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vindu, tak
        C110 = areal_dor              # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, dører
        C71 = C84*C98  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - tak
        C72 = C85*C99  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg øst, uten vindu
        C73 = C86*C100 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg vest, uten vindu
        C74 = C87*C101 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg sør, uten vindu
        C75 = C88*C102 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg nord, uten vindu
        C76 = C89*C103 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - gulv mot det fri
        C77 = C91*C105 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, øst
        C78 = C92*C106 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, vest
        C79 = C93*C107 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, sør
        C80 = C94*C108 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, nord
        C81 = C95*C109 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, tak
        C82 = C96*C110 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - dører
        C66 = C71+C72+C73+C74+C75+C76 + C77+C78+C79+C80+C81+C82 # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Summert UiAi for bygningsdeler
        C68 = areal_oppv           # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD -  Oppvarmet del av BRA
        C69 = kuldebro_normalisert # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD -  Normalisert kuldebro
        C67 = C68*C69              # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Normalisert kuldebro ganget med oppvarmet areal
        C64 = C66+C67              # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Totalt, HD
        AE81 = BygningskategoriErForretningsbygg                        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Hvorvidt bygningen tilhører kategorien forretningsbygg eller bolig (1 = Forretningsbygg, 0 = Bolig)
        AE79 = luftmengde_spesifikk_tilluft                             # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE80 = luftmengde_spesifikk_avtrekksluft                        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE77 = term1 if AE81==0 else AE79                               # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Arealkorreksjon for bolig, på spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE78 = term1 if AE81==0 else AE80                               # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Arealkorreksjon for bolig, på spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))

        AE75 = 0 if AE79==0 else AE77                                   # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Korreksjon for luftmengde = 0, på spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE76 = 0 if AE80==0 else AE78                                   # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Korreksjon for luftmengde = 0, på spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE68 = varmekapasitet_luft                                      # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftens varmekapasitet per volum
        AE69 = lekkasjetall                                             # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Terrengskjermingskoeffisient, e
        AE70 = terrengskjermingskoeff_e                                 # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Lekkasjetall, n50
        AE71 = terrengskjermingskoeff_f                                 # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftens varmekapasitet per volum
        AE72 = areal_oppv*AE75                                          # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/h)
        AE73 = areal_oppv*AE76                                          # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Avtrekksmengde i det mekaniske ventilasjonsanlegget (m3/h)
        AE74 = etasjehoyde_innvendig                                    # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Etasjehøyde, innvendig
        AE67 = C68*AE74                                                 # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Oppvarmet luftvolum (Nettovolum av en bygnig beregnet innenfor dens innvendige, omsluttende flater)§
        AE66 = (AE69*AE70)/(1+(AE71/AE70)*((AE72-AE73)/(AE67*AE69))**2) # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftskifte for infiltrasjon
        AE64 = AE68*AE66*AE67                                           # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Totalt, Hinf
        Q99 =varmekonduktivitet_grunn                                           # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmekonduktivitet til grunnen, λ
        Q100 =dybde_periodisk_nedtrengning                                      # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Periodiske nedtrengningsdybde, δ
        Q104 = tykkelse_grunnmur                                                # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Tykkelse på grunnmur/ringmur, w [meter]
        Q105 = U_gulvkonstruksjon                                               # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmegjennomgangskoeffisient til selve gulvkonstruksjonen uten hensyn til varmemotstanden i grunnen, Ufl [W/(m2 K)]
        Q106 = U_kjellerveggskonstruksjon                                       # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmegjennomgangskoeffisient til selve veggkonstruksjonen uten hensyn til varmemotstanden i grunnen, Uw [W/(m2 K)]
        Q107 = kantisol_tykkelse                                                # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Tykkelse på kantisolasjon, diso [meter]
        Q108 = varmekonduktivitet_kantisol                                      # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmekonduktivitet til kantisolasjonen, λiso ([W/(m K)]) (>0)
        Q101 = Q104+Q99/Q105                                                    # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for gulvet, dt
        Q102 = Q107*(Q99/Q108-1)                                                # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for kantisolasjon, d'
        Q103 = Q99/Q106                                                         # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for kjellerveggene, dw
        Q109 = kantisol_horisontal_dybde                                        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Horisontal dybde på kantisolasjon, D [meter]
        Q110 = kantisol_vertikal_bredde                                         # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Vertikal bredde på kantisolasjon, D [meter]
        Q112 = faseforskjell_utetemp_varmetap                                   # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Faseforskjell mellom utetemp og varmetap (2 mnd for gulv og 1 mnd for kjeller)
        Q114 = temp_amplitudevar                                                # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Amplitudevariasjonen omkring årsmiddeltemperaturen ute
        Q97 = -(Q99/np.pi)*(np.log(Q109/Q101+1)-np.log(Q109/(Q101+Q102)+1))     # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Lineær varmegjennomgangs-koeffisient, horisontal kantisolasjon
        Q98 = -(Q99/np.pi)*(np.log(2*Q110/Q101+1)-np.log(2*Q110/(Q101+Q102)+1)) # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Lineær varmegjennomgangs-koeffisient, vertikal kantisolasjon
        Q94 = areal_gulv_kjeller                                                # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ag
        Q95 = omkrets_gulv                                                      # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Omkrets på gulv (omkrets mot det fri), P
        Q96 = oppfyllingshoyde_kjellervegg                                      # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Oppfyllingshøyden mot kjellervegg, z
        Q92 = Q94/(0.5*Q95)                                                     # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Karakteristisk dimensjon for gulvet, B'
        Q93 = 2*Q99/(np.pi*Q96)*(1+((0.5*Q101)/(Q101+Q96)))*np.log(Q96/Q103+1)  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Vegg mot grunn, Ubw
        Q84 = 0.37*Q95*Q99*((1-np.exp(-(Q109/Q100)))  *np.log(Q100/(Q101+Q102))+np.exp(-(Q109/Q100))  *np.log(Q100/Q101+1))                          ## NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For gulv mot grunnen, vertikal kantisolasjon (D' = D)
        Q85 = 0.37*Q95*Q99*((1-np.exp(-(2*Q110/Q100)))*np.log(Q100/(Q101+Q102))+np.exp(-(2*Q110/Q100))*np.log(Q100/Q101+1))                           # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For gulv mot grunnen, horisontal kantisolasjon (D' = 2 x D)
        Q86 = 0.37*Q95*Q99*((1-np.exp(-(Q96/Q100)))   *np.log(Q100/Q103+1)     +np.exp(-(Q96/Q100))   *np.log(Q100/Q101+1))                           # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For vegg og gulv mot grunnen
        Q89 = Q99/(0.457*Q92+Q101+0.5*Q96)                                      # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ug (Hvis B'<dt + 0,5*z)
        Q88 = REF if Q92>Q101+0.5*Q96 else Q89                                  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ug (Hvis B'>dt + 0,5*z)
        # Nima Darabi: OBS! Q88 ser ut som er kopiert med offset
        Q81 = Q88*Q94+Q97*Q95                                                   # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Stasjonær varmetransportkoeffisient, Hg] - For gulv mot grunnen
        Q82 = Q88*Q94+Q96*Q95*Q93                                               # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Stasjonær varmetransportkoeffisient, Hg] - For vegg og gulv mot grunnen
        Q78 = aarsmiddeltemp_inne                                               # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Årsmiddeltemperatur inne, i driftstiden
        Q79 = aarsmiddeltemp_ute                                                # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Årsmiddeltemperatur ute
        Q66 = C197 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(1-1-Q112)/12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - januar
        Q67 = C198 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(2-1-Q112)/12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - februar
        Q68 = C199 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(3-1-Q112)/12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - mars
        Q69 = C200 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(4-1-Q112)/12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - april
        Q70 = C201 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(5-1-Q112)/12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - mai
        Q71 = C202 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(6-1-Q112)/12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - juni
        Q72 = C203 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(7-1-Q112)/12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - juli
        Q73 = C204 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(8-1-Q112)/12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - august
        Q74 = C205 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(9-1-Q112)/12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - september
        Q75 = C206 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(10-1-Q112)/12)) # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - oktober
        Q76 = C207 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(11-1-Q112)/12)) # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - novemeber
        Q77 = C208 * ((Q81 if Q112==2 else Q82)*(Q78-Q79) + (max([Q84,Q85]) if Q112==2 else Q86) * Q114 * np.cos(2*np.pi*(12-1-Q112)/12)) # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - desember
        Q64 = Q66 + Q67 + Q68 + Q69 + Q70 + Q71 + Q72 + Q73 + Q74 + Q75 + Q76 + Q77 
        J67 = 0                     #  NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Det regnes ikke tillegg for kuldebro mot uoppvarmet rom
        # Nima Darabi: OBS! direkt verditildeling paa J67
        J69 = kuldebro_normalisert  #  NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU -Normalisert kuldebro
        J70 = varmetapsfaktor_uoppv #  NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU -Varmetapsfaktor, b
        J74 = U_mot_uoppvarmet_sone #  NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - U-verdi mot uoppvarmet
        J75 = areal_mot_uoppvarmet  #  NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Areal, mot uoppvarmet
        J72 = J74*J75               #  NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU -
        J68 = sum([J75])            #  NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Oppvarmet areal, uoppvarmet sone
        J66 = J72                   #  NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Summert UiAi for bygningsdeler
        J64 = J70*(J66+J67)         # NS3031 - Varmetransmisjonstap til uoppvarmede soner, HU - Totalt, HU
        J50 = C64  # (Varmetapstall) - Varmetransmisjonstap, HD
        J51 = J64  # (Varmetapstall) - Varmetransmisjonstap, HU
        J52 = Q64  # (Varmetapstall) - Varmetap mot grunnen, et helt år
        J53 = X64  # (Varmetapstall) - Ventilasjonsvarmetap, HV
        J54 = AE64 # (Varmetapstall) - Infiltrasjonsvarmetap, Hinf
        Q46 = utetemp_jan # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - januar
        Q47 = utetemp_feb # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - februar
        Q48 = utetemp_mar # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - mars
        Q49 = utetemp_apr # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - april
        Q50 = utetemp_mai # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - mai
        Q51 = utetemp_jun # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - juni
        Q52 = utetemp_jul # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - juli
        Q53 = utetemp_aug # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - august
        Q54 = utetemp_sep # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - september
        Q55 = utetemp_okt # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - oktober
        Q56 = utetemp_nov # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - november
        Q57 = utetemp_des # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - desember
        Q59 = temp_settpunkt_oppvarming      # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - temp_settpunkt_oppvarming
        Q60 = temp_settpunkt_oppvarming_natt # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - temp_settpunkt_oppvarming
        term49 = (J50+J51+J53+J54)*(Q59-Q46)*X46/1000+(J50+J51+J53+J54)*(Q60-Q46)*AE46/1000+Q66
        term50 = (J50+J51+J53+J54)*(Q59-Q47)*X47/1000+(J50+J51+J53+J54)*(Q60-Q47)*AE47/1000+Q67
        term51 = (J50+J51+J53+J54)*(Q59-Q48)*X48/1000+(J50+J51+J53+J54)*(Q60-Q48)*AE48/1000+Q68
        term52 = (J50+J51+J53+J54)*(Q59-Q49)*X49/1000+(J50+J51+J53+J54)*(Q60-Q49)*AE49/1000+Q69
        term53 = (J50+J51+J53+J54)*(Q59-Q50)*X50/1000+(J50+J51+J53+J54)*(Q60-Q50)*AE50/1000+Q70
        term54 = (J50+J51+J53+J54)*(Q59-Q51)*X51/1000+(J50+J51+J53+J54)*(Q60-Q51)*AE51/1000+Q71
        term55 = (J50+J51+J53+J54)*(Q59-Q52)*X52/1000+(J50+J51+J53+J54)*(Q60-Q52)*AE52/1000+Q72
        term56 = (J50+J51+J53+J54)*(Q59-Q53)*X53/1000+(J50+J51+J53+J54)*(Q60-Q53)*AE53/1000+Q73
        term57 = (J50+J51+J53+J54)*(Q59-Q54)*X54/1000+(J50+J51+J53+J54)*(Q60-Q54)*AE54/1000+Q74
        term58 = (J50+J51+J53+J54)*(Q59-Q55)*X55/1000+(J50+J51+J53+J54)*(Q60-Q55)*AE55/1000+Q75
        term59 = (J50+J51+J53+J54)*(Q59-Q56)*X56/1000+(J50+J51+J53+J54)*(Q60-Q56)*AE56/1000+Q76
        term60 = (J50+J51+J53+J54)*(Q59-Q57)*X57/1000+(J50+J51+J53+J54)*(Q60-Q57)*AE57/1000+Q77
        C49 = 0.1 if term49<0 else term49 # NS3031* - Varmetap - januar
        C50 = 0.1 if term50<0 else term50 # NS3031* - Varmetap - februar
        C51 = 0.1 if term51<0 else term51 # NS3031* - Varmetap - mars
        C52 = 0.1 if term52<0 else term52 # NS3031* - Varmetap - april
        C53 = 0.1 if term53<0 else term53 # NS3031* - Varmetap - mai
        C54 = 0.1 if term54<0 else term54 # NS3031* - Varmetap - juni
        C55 = 0.1 if term55<0 else term55 # NS3031* - Varmetap - juli
        C56 = 0.1 if term56<0 else term56 # NS3031* - Varmetap - august
        C57 = 0.1 if term57<0 else term57 # NS3031* - Varmetap - september
        C58 = 0.1 if term58<0 else term58 # NS3031* - Varmetap - oktober
        C59 = 0.1 if term59<0 else term59 # NS3031* - Varmetap - november
        C60 = 0.1 if term60<0 else term60 # NS3031* - Varmetap - desember
        C37 = norm_varmekap                                # NS3031 - Oppvarmingsbehov - Bygningens normaliserte varmekapasitet, C" (Wh/(m3 K))
        C39 = J50+J51+J53+J54 + (Q81 if Q112==2 else Q82)  # NS3031 - Oppvarmingsbehov - Bygningens varmetransportkoeffisient [W/K]
        C36 = C37*areal_oppv/C39                           # NS3031 - Oppvarmingsbehov - Varmetreghet, aH
        C35 = 1 + C36/16                                   # NS3031 - Oppvarmingsbehov - Tidskonstant, τ
        Q22 = C120/C49 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - januar
        Q23 = C121/C50 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - februar
        Q24 = C122/C51 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - mars
        Q25 = C123/C52 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - april
        Q26 = C124/C53 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - mai
        Q27 = C125/C54 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - juni
        Q28 = C126/C55 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - juli
        Q29 = C127/C56 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - august
        Q30 = C128/C57 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - september
        Q31 = C129/C58 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - oktober
        Q32 = C130/C59 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - november
        Q33 = C131/C60 # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - desember
        J22 = 1/Q22 if Q22<0 else C35/(C35+1) if Q22==1 else (1-Q22 ** C35)/(1-Q22 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - januar
        J23 = 1/Q23 if Q23<0 else C35/(C35+1) if Q23==1 else (1-Q23 ** C35)/(1-Q23 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - februar
        J24 = 1/Q24 if Q24<0 else C35/(C35+1) if Q24==1 else (1-Q24 ** C35)/(1-Q24 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - mars
        J25 = 1/Q25 if Q25<0 else C35/(C35+1) if Q25==1 else (1-Q25 ** C35)/(1-Q25 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - april
        J26 = 1/Q26 if Q26<0 else C35/(C35+1) if Q26==1 else (1-Q26 ** C35)/(1-Q26 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - mai
        J27 = 1/Q27 if Q27<0 else C35/(C35+1) if Q27==1 else (1-Q27 ** C35)/(1-Q27 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - juni
        J28 = 1/Q28 if Q28<0 else C35/(C35+1) if Q28==1 else (1-Q28 ** C35)/(1-Q28 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - juli
        J29 = 1/Q29 if Q29<0 else C35/(C35+1) if Q29==1 else (1-Q29 ** C35)/(1-Q29 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - august
        J30 = 1/Q30 if Q30<0 else C35/(C35+1) if Q30==1 else (1-Q30 ** C35)/(1-Q30 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - september 
        J31 = 1/Q31 if Q31<0 else C35/(C35+1) if Q31==1 else (1-Q31 ** C35)/(1-Q31 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - october
        J32 = 1/Q32 if Q32<0 else C35/(C35+1) if Q32==1 else (1-Q32 ** C35)/(1-Q32 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - november
        J33 = 1/Q33 if Q33<0 else C35/(C35+1) if Q33==1 else (1-Q33 ** C35)/(1-Q33 **(C35+1)) # NS3031 - Utnyttingsfaktor for måneden - desember
        C22 = C49-J22*C120 # NS3031 - Oppvarmingsbehov - januar
        C23 = C50-J23*C121 # NS3031 - Oppvarmingsbehov - februar
        C24 = C51-J24*C122 # N	S3031 - Oppvarmingsbehov - mars
        C25 = C52-J25*C123 # NS3031 - Oppvarmingsbehov - april
        C26 = C53-J26*C124 # NS3031 - Oppvarmingsbehov - mai
        C27 = C54-J27*C125 # NS3031 - Oppvarmingsbehov - juni
        C28 = C55-J28*C126 # NS3031 - Oppvarmingsbehov - juli
        C29 = C56-J29*C127 # NS3031 - Oppvarmingsbehov - august
        C30 = C57-J30*C128 # NS3031 - Oppvarmingsbehov - september
        C31 = C58-J31*C129 # NS3031 - Oppvarmingsbehov - oktober
        C32 = C59-J32*C130 # NS3031 - Oppvarmingsbehov - november
        C33 = C60-J33*C131 # NS3031 - Oppvarmingsbehov - desember
        C20 = C22+C23+C24+C25+C26+C27+C28+C29+C30+C31+C32+C33 # NS3031 - Oppvarmingsbehov - Årlig energibehov
        Romoppvarming = C20  # # - Energipost (1a) (Energibehov [kWh/år]) - Romoppvarming 

        ### 1-b
        # 6.1.7 -> Trond Ivar Bøhn: OBS! Denne referansen finnes ikke lenger i NS 3031:2014. Det er nå slik at temperaturvirkningsgraden korrigeres for frostsikringen, ref. NS 3031:2014 tillegg H.9. Men om dette skal gjøres om på, må biblioteksverdier for varmegjenvinning vurderes på nytt
        C297 = temp_avtrekk                                                # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Temperatur før gjenvinner på avtrekkssiden, θ3
        C298 = frostsikringstemperatur                                     # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Frostsikringstemperaturen, θ4
        C296 = C297-(C297-C298)/(tempvirkningsgrad_varmegjenvinner+0.001)  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Minste utetemperatur som ikke innebærer frostsikring av varmegjenvinneren, θ1,min
        C283 = 0.33*X66*C197*max([0, C296-Q46])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - januar
        C284 = 0.33*X66*C198*max([0, C296-Q47])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - februar
        C285 = 0.33*X66*C199*max([0, C296-Q48])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - mars
        C286 = 0.33*X66*C200*max([0, C296-Q49])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - april
        C287 = 0.33*X66*C201*max([0, C296-Q50])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - mai
        C288 = 0.33*X66*C202*max([0, C296-Q51])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - juni
        C289 = 0.33*X66*C203*max([0, C296-Q52])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - juli
        C290 = 0.33*X66*C204*max([0, C296-Q53])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - august
        C291 = 0.33*X66*C205*max([0, C296-Q54])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - september
        C292 = 0.33*X66*C206*max([0, C296-Q55])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - oktober
        C293 = 0.33*X66*C207*max([0, C296-Q56])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - november
        C294 = 0.33*X66*C208*max([0, C296-Q57])                            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - desember
        C281 = C283+C284+C285+C286+C287+C288+C289+C290+C291+C292+C293+C294 # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7) - Totalt, Edefrost
        Ventilasjonsvarme = C281     # # - Energipost (1b) (Energibehov [kWh/år]) Trond Ivar Bøhn: OBS! Dette ser ikke ut til å være ventilasjonsoppvarming, men kun frostsikring. Ventilasjonsvarmetapet inngår derimot i posten romoppvarming! Spm til NVE: Brukes disse enkeltpostene for netto energibehov til noe i Enova-modulen? I så fall burde vel dette ordnes opp i?!
        print (Ventilasjonsvarme)

        ### 3-b
        Pumper = 43
        ### 6
        Kjoeling = 0
        Totalt_netto_energibehov = Romoppvarming+Ventilasjonsvarme +\
                                   Varmtvann+\
                                   Vifter+Pumper+\
                                   Belysning+\
                                   Teknisk_utstyr+\
                                   Kjoeling
        
        return Output( Romoppvarming,\
                       Ventilasjonsvarme,\
                       Varmtvann,\
                       Vifter,\
                       Pumper,\
                       Belysning,\
                       Teknisk_utstyr,\
                       Kjoeling,\
                       Totalt_netto_energibehov)


    
if __name__ == "__main__":
    """ Example usage """
    calcEngine = EnergiBeregning(

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
    U_vindu_tak =1.60,

    varmetapsfaktor_uoppv=0.95,
    areal_mot_uoppvarmet =0.0,
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

    #Per mnd. da skoler eller andre bygg kan ha variasjon i tilskudd. f.eks. i ferier=
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

    BygningskategoriErForretningsbygg = 0, # Nima Darabi: OBS! finnes ikke i input? (1 = Forretningsbygg, 0 = Bolig)
    REF = 123456789 # Nima Darabi: OBS! Hva er verdi for #REF! i Q88
        )
    print(calcEngine.calculate())

