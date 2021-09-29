from dataclasses import dataclass
import statistics
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

    Elektrisitet: float
    Olje: float
    Gass: float
    Fjernvarme: float
    Biobrensel: float
    Annen_energivare: float
    Totalt_levert_energi: float

    def __str__(self):
        return "Romoppvarming: {0.Romoppvarming},Ventilasjonsvarme: {0.Ventilasjonsvarme}, \
		Varmtvann: {0.Varmtvann}, Vifter: {0.Vifter}, \
		Pumper: {0.Pumper}, Belysning: {0.Belysning}, \
		Teknisk_utstyr: {0.Teknisk_utstyr}, Kjoeling: {0.Kjoeling}, \
		Totalt_netto_energibehov: {0.Totalt_netto_energibehov}, \
		Elektrisitet: {0.Elektrisitet}, \
		Olje: {0.Olje}, \
		Gass: {0.Gass}, \
		Fjernvarme: {0.Fjernvarme}, \
		Biobrensel: {0.Biobrensel},\
		Annen_energivare: {0.Annen_energivare}, \
		Totalt_levert_energi: {0.Totalt_levert_energi}".format(
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

    @property
    def calculate(self):

        # Config / setup

        maaneder = ['jan','feb','mar','apr','mai','jun','jul','aug','sep', 'okt', 'nov', 'des']

        tid = {'jan': self.tid_jan,
               'feb': self.tid_feb,
               'mar': self.tid_mar,
               'apr': self.tid_apr,
               'mai': self.tid_mai,
               'jun': self.tid_jun,
               'jul': self.tid_jul,
               'aug': self.tid_aug,
               'sep': self.tid_sep,
               'okt': self.tid_okt,
               'nov': self.tid_nov,
               'des': self.tid_des
        }

        tid_drift_vent = {
            'jan': self.tid_drift_vent_jan,
            'feb': self.tid_drift_vent_feb,
            'mar': self.tid_drift_vent_mar,
            'apr': self.tid_drift_vent_apr,
            'mai': self.tid_drift_vent_mai,
            'jun': self.tid_drift_vent_jun,
            'jul': self.tid_drift_vent_jul,
            'aug': self.tid_drift_vent_aug,
            'sep': self.tid_drift_vent_sep,
            'okt': self.tid_drift_vent_okt,
            'nov': self.tid_drift_vent_nov,
            'des': self.tid_drift_vent_des
        }

        tid_drift_oppv_belysn_utstyr = {
            'jan': self.tid_drift_oppv_belysn_utstyr_jan,
            'feb': self.tid_drift_oppv_belysn_utstyr_feb,
            'mar': self.tid_drift_oppv_belysn_utstyr_mar,
            'apr': self.tid_drift_oppv_belysn_utstyr_apr,
            'mai': self.tid_drift_oppv_belysn_utstyr_mai,
            'jun': self.tid_drift_oppv_belysn_utstyr_jun,
            'jul': self.tid_drift_oppv_belysn_utstyr_jul,
            'aug': self.tid_drift_oppv_belysn_utstyr_aug,
            'sep': self.tid_drift_oppv_belysn_utstyr_sep,
            'okt': self.tid_drift_oppv_belysn_utstyr_okt,
            'nov': self.tid_drift_oppv_belysn_utstyr_nov,
            'des': self.tid_drift_oppv_belysn_utstyr_des
        }

        ### energipost 2
        # NS3031*- Energibehov for varmt tappevann, spesifikt - Varmtvann
        # NS3031 - Energibehov for varmt tappevann - Oppvarmed del av BRA
        # NS3031 - Energibehov for varmt tappevann - Årlig energibehov
        Varmtvann = self.energibehov_tappevann * self.areal_oppv  # # - Energipost (2) (Energibehov [kWh/år]) - Varmtvann

        ### energipost 4
        # NS3031*- Energibehov for belysning, spesifikt - Belysning
        # NS3031 - Energibehov for belysning - Oppvarmed del av BRA
        # NS3031 - Energibehov for belysning - Årlig energibehov
        Belysning = self.energibehov_belysning * self.areal_oppv  # # - Energipost (4) (Energibehov [kWh/år]) - Belysning

        ### energipost 5
        # NS3031*- Energibehov for teknisk utstyr - Teknisk utstyr
        # NS3031 - Energibehov for teknisk utstyr - Oppvarmed del av BRA
        # NS3031 - Energibehov for utstyr - Årlig energibehov
        Teknisk_utstyr = self.energibehov_utstyr * self.areal_oppv  # # - Energipost (5) (Energibehov [kWh/år]) - Teknisk_utstyr


        ### energipost 3-a timer per måned
        timer = {}
        for maaned in maaneder:
            timer[maaned] = tid[maaned] * 1000

        mean_timer_per_aar = np.mean(list(timer.values()))

        # - Timer i driftstid for ventilasjon (Timer for måneden)
        tid_drift_uvent = {}
        for maaned in maaneder:
            tid_drift_uvent[maaned] = timer[maaned] - tid_drift_vent[maaned]

        # - Timer i driftstid for ventilasjon (Timer for måneden) - AVERAGE
        mean_tid_drift_ventilasjon = np.mean(list(tid_drift_uvent.values()))

        # Vifter
        spesifikk_i_driftstid = self.luftmengde_spesifikk_i_driftstid * self.areal_oppv * self.vifteeffekt_spesifikk_i_driftstid
        spesifikk_utenfor_driftstid = self.luftmengde_spesifikk_utenfor_driftstid * self.areal_oppv * self.vifteeffekt_spesifikk_utenfor_driftstid

        # NS3031 - Energibehov for vifter og pumper (Vifter) - Totalt, Efan
        Vifter = 0 # - Energipost (3a) (Energibehov [kWh/år]) - Vifter
        for maaned in maaneder:
            Vifter += (spesifikk_i_driftstid * tid_drift_vent[maaned] + spesifikk_utenfor_driftstid * tid_drift_uvent[maaned]) / 3600

        ### energipost 1-a
        # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007)
        straalingsfluks_soer = {
            'jan': self.straalingsfluks_soer_jan,
            'feb': self.straalingsfluks_soer_feb,
            'mar': self.straalingsfluks_soer_mars,
            'apr': self.straalingsfluks_soer_april,
            'mai': self.straalingsfluks_soer_mai,
            'jun': self.straalingsfluks_soer_juni,
            'jul': self.straalingsfluks_soer_juli,
            'aug': self.straalingsfluks_soer_aug,
            'sep': self.straalingsfluks_soer_sept,
            'okt': self.straalingsfluks_soer_okt,
            'nov': self.straalingsfluks_soer_nov,
            'des': self.straalingsfluks_soer_des
        }

        # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007)
        straalingsfluks_ostvest = {
            'jan': self.straalingsfluks_ostvest_jan,
            'feb': self.straalingsfluks_ostvest_feb,
            'mar': self.straalingsfluks_ostvest_mars,
            'apr': self.straalingsfluks_ostvest_april,
            'mai': self.straalingsfluks_ostvest_mai,
            'jun': self.straalingsfluks_ostvest_juni,
            'jul': self.straalingsfluks_ostvest_juli,
            'aug': self.straalingsfluks_ostvest_aug,
            'sep': self.straalingsfluks_ostvest_sept,
            'okt': self.straalingsfluks_ostvest_okt,
            'nov': self.straalingsfluks_ostvest_nov,
            'des': self.straalingsfluks_ostvest_des
        }

        # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007)
        straalingsfluks_nord = {
            'jan': self.straalingsfluks_nord_jan,
            'feb': self.straalingsfluks_nord_feb,
            'mar': self.straalingsfluks_nord_mars,
            'apr': self.straalingsfluks_nord_april,
            'mai': self.straalingsfluks_nord_mai,
            'jun': self.straalingsfluks_nord_juni,
            'jul': self.straalingsfluks_nord_juli,
            'aug': self.straalingsfluks_nord_aug,
            'sep': self.straalingsfluks_nord_sept,
            'okt': self.straalingsfluks_nord_okt,
            'nov': self.straalingsfluks_nord_nov,
            'des': self.straalingsfluks_nord_des
        }

        # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007)
        straalingsfluks_tak = {
            'jan': self.straalingsfluks_tak_jan,
            'feb': self.straalingsfluks_tak_feb,
            'mar': self.straalingsfluks_tak_mars,
            'apr': self.straalingsfluks_tak_april,
            'mai': self.straalingsfluks_tak_mai,
            'jun': self.straalingsfluks_tak_juni,
            'jul': self.straalingsfluks_tak_juli,
            'aug': self.straalingsfluks_tak_aug,
            'sep': self.straalingsfluks_tak_sept,
            'okt': self.straalingsfluks_tak_okt,
            'nov': self.straalingsfluks_tak_nov,
            'des': self.straalingsfluks_tak_des
        }

        sol_tidsvariabel_ost_vest = {
            'jan': self.sol_tidsvariabel_ost_vest_jan,
            'feb': self.sol_tidsvariabel_ost_vest_feb,
            'mar': self.sol_tidsvariabel_ost_vest_mars,
            'apr': self.sol_tidsvariabel_ost_vest_april,
            'mai': self.sol_tidsvariabel_ost_vest_mai,
            'jun': self.sol_tidsvariabel_ost_vest_juni,
            'jul': self.sol_tidsvariabel_ost_vest_juli,
            'aug': self.sol_tidsvariabel_ost_vest_aug,
            'sep': self.sol_tidsvariabel_ost_vest_sept,
            'okt': self.sol_tidsvariabel_ost_vest_okt,
            'nov': self.sol_tidsvariabel_ost_vest_nov,
            'des': self.sol_tidsvariabel_ost_vest_des
        }

        sol_tidsvariabel_sor = {
            'jan': self.sol_tidsvariabel_soer_jan,
            'feb': self.sol_tidsvariabel_soer_feb,
            'mar': self.sol_tidsvariabel_soer_mars,
            'apr': self.sol_tidsvariabel_soer_april,
            'mai': self.sol_tidsvariabel_soer_mai,
            'jun': self.sol_tidsvariabel_soer_juni,
            'jul': self.sol_tidsvariabel_soer_juli,
            'aug': self.sol_tidsvariabel_soer_aug,
            'sep': self.sol_tidsvariabel_soer_sept,
            'okt': self.sol_tidsvariabel_soer_okt,
            'nov': self.sol_tidsvariabel_soer_nov,
            'des': self.sol_tidsvariabel_soer_des
        }

        sol_tidsvariabel_nord = {
            'jan': self.sol_tidsvariabel_nord_jan,
            'feb': self.sol_tidsvariabel_nord_feb,
            'mar': self.sol_tidsvariabel_nord_mars,
            'apr': self.sol_tidsvariabel_nord_april,
            'mai': self.sol_tidsvariabel_nord_mai,
            'jun': self.sol_tidsvariabel_nord_juni,
            'jul': self.sol_tidsvariabel_nord_juli,
            'aug': self.sol_tidsvariabel_nord_aug,
            'sep': self.sol_tidsvariabel_nord_sept,
            'okt': self.sol_tidsvariabel_nord_okt,
            'nov': self.sol_tidsvariabel_nord_nov,
            'des': self.sol_tidsvariabel_nord_des
        }

        # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, øst
        areal_vindu_oest = self.areal_vindu_oest
        # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, vest
        areal_vindu_vest = self.areal_vindu_vest
        # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, sør
        areal_vindu_soer = self.areal_vindu_soer
        # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, nord
        areal_vindu_nord = self.areal_vindu_nord
        # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, tak
        areal_vindu_tak = self.areal_vindu_tak
        # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, øst
        arealfraksjon_karm_oest = self.arealfraksjon_karm_oest
        # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, vest
        arealfraksjon_karm_vest = self.arealfraksjon_karm_vest
        # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, sør
        arealfraksjon_karm_soer = self.arealfraksjon_karm_soer
        # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, nord
        arealfraksjon_karm_nord = self.arealfraksjon_karm_nord
        # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, tak
        arealfraksjon_karm_tak = self.arealfraksjon_karm_tak

        # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt (Solfaktor x 0.9, dvs. forenklet)
        # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt (tak)
        # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, tak
        total_solfaktor_gjennomsnitt_vindu_tak = areal_vindu_tak * self.solfaktor_vindu_tak * 0.9 * (1 - arealfraksjon_karm_tak)

        # NS3031* - Ventilasjonsvarmetap, HV - Antall timer i måneden i driftstiden, ton
        ventilasjonsvarmetap_timer = np.mean(list(tid_drift_vent.values()))

        # NS3031* - Ventilasjonsvarmetap, HV - Hvorvidt bygningen tilhører kategorien forretningsbygg eller bolig
        term1 = (1.6 - 0.007 * (self.areal_oppv - 50)) if self.areal_oppv < 110 else 1.2
        # NS3031* - Ventilasjonsvarmetap, HV - Arealkorreksjon for bolig, på spesifikk luftmengde for ventilasjon i driftstid
        # NS3031* - Ventilasjonsvarmetap, HV - Arealkorreksjon for bolig, på spesifikk luftmengde for ventilasjon utenfor driftstid
        # NS3031* - Ventilasjonsvarmetap, HV - Gjennomsnittlig ventilasjon i driftstiden
        # NS3031* - Ventilasjonsvarmetap, HV - Gjennomsnittlig ventilasjon utenfor driftstiden
        # NS3031* - Ventilasjonsvarmetap, HV - Luftens varmekapasitet per volum
        # NS3031* - Ventilasjonsvarmetap, HV - Temperaturvirkningsgrad for varmegjenvinner
        # NS3031* - Ventilasjonsvarmetap, HV - Gjennomsnittlig ventilasjonsmengde
        # NS3031* - Ventilasjonsvarmetap, HV - Totalt, HV

        # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Temperaturøkning over avtrekksvifte
        # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Temperaturøkning over tilluftsvifte
        # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Gjennomsnittlig ventilasjon
        # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Varmegjenvinnerens temperaturvirkningsgrad
        # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Oppvarmed del av BRA (m2)
        # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Varmetilskudd fra vifter
        tid_drift_gjsnitt = (np.mean(list(tid_drift_vent.values())))

        tid_drift_oppv_belysn_utstyr = {
            'jan': self.tid_drift_oppv_belysn_utstyr_jan,
            'feb': self.tid_drift_oppv_belysn_utstyr_feb,
            'mar': self.tid_drift_oppv_belysn_utstyr_mar,
            'apr': self.tid_drift_oppv_belysn_utstyr_apr,
            'mai': self.tid_drift_oppv_belysn_utstyr_mai,
            'jun': self.tid_drift_oppv_belysn_utstyr_jun,
            'jul': self.tid_drift_oppv_belysn_utstyr_jul,
            'aug': self.tid_drift_oppv_belysn_utstyr_aug,
            'sep': self.tid_drift_oppv_belysn_utstyr_sep,
            'okt': self.tid_drift_oppv_belysn_utstyr_okt,
            'nov': self.tid_drift_oppv_belysn_utstyr_nov,
            'des': self.tid_drift_oppv_belysn_utstyr_des
        }

        tid_drift_person = {
            'jan': self.tid_drift_person_jan,
            'feb': self.tid_drift_person_feb,
            'mar': self.tid_drift_person_mar,
            'apr': self.tid_drift_person_apr,
            'mai': self.tid_drift_person_mai,
            'jun': self.tid_drift_person_jun,
            'jul': self.tid_drift_person_jul,
            'aug': self.tid_drift_person_aug,
            'sep': self.tid_drift_person_sep,
            'okt': self.tid_drift_person_okt,
            'nov': self.tid_drift_person_nov,
            'des': self.tid_drift_person_des
        }

        varmetilskudd_person = {
            'jan': self.varmetilskudd_person_jan,
            'feb': self.varmetilskudd_person_feb,
            'mar': self.varmetilskudd_person_mar,
            'apr': self.varmetilskudd_person_apr,
            'mai': self.varmetilskudd_person_mai,
            'jun': self.varmetilskudd_person_jun,
            'jul': self.varmetilskudd_person_jul,
            'aug': self.varmetilskudd_person_aug,
            'sep': self.varmetilskudd_person_sep,
            'okt': self.varmetilskudd_person_okt,
            'nov': self.varmetilskudd_person_nov,
            'des': self.varmetilskudd_person_des
        }

        varmetilskudd_lys = {
            'jan': self.varmetilskudd_lys_jan,
            'feb': self.varmetilskudd_lys_feb,
            'mar': self.varmetilskudd_lys_mar,
            'apr': self.varmetilskudd_lys_apr,
            'mai': self.varmetilskudd_lys_mai,
            'jun': self.varmetilskudd_lys_jun,
            'jul': self.varmetilskudd_lys_jul,
            'aug': self.varmetilskudd_lys_aug,
            'sep': self.varmetilskudd_lys_sep,
            'okt': self.varmetilskudd_lys_okt,
            'nov': self.varmetilskudd_lys_nov,
            'des': self.varmetilskudd_lys_des
        }

        varmetilskudd_utstyr = {
            'jan': self.varmetilskudd_utstyr_jan,
            'feb': self.varmetilskudd_utstyr_feb,
            'mar': self.varmetilskudd_utstyr_mar,
            'apr': self.varmetilskudd_utstyr_apr,
            'mai': self.varmetilskudd_utstyr_mai,
            'jun': self.varmetilskudd_utstyr_jun,
            'jul': self.varmetilskudd_utstyr_jul,
            'aug': self.varmetilskudd_utstyr_aug,
            'sep': self.varmetilskudd_utstyr_sep,
            'okt': self.varmetilskudd_utstyr_okt,
            'nov': self.varmetilskudd_utstyr_nov,
            'des': self.varmetilskudd_utstyr_des
        }

        varmetilskudd = {}
        for maaned in maaneder:
            varmetilskudd[maaned] = tid[maaned] * (straalingsfluks_soer[maaned] * areal_vindu_oest * (
                    (1 - sol_tidsvariabel_ost_vest[maaned]) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                maaned] * self.solfaktor_total_glass_skjerming_oest) * (
                                                          1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                                                  straalingsfluks_ostvest[maaned] * areal_vindu_vest * (
                                                          (1 - sol_tidsvariabel_ost_vest[maaned]) * self.solfaktor_vindu_vest +
                                                          sol_tidsvariabel_ost_vest[
                                                              maaned] * self.solfaktor_total_glass_skjerming_vest) * (
                                                          1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                                                  straalingsfluks_ostvest[maaned] * areal_vindu_soer * (
                                                          (1 - sol_tidsvariabel_sor[maaned]) * self.solfaktor_vindu_soer +
                                                          sol_tidsvariabel_sor[maaned] * self.solfaktor_total_glass_skjerming_soer) * (
                                                          1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                                                  straalingsfluks_nord[
                                                      maaned] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                                          (1 - sol_tidsvariabel_nord[maaned]) * self.solfaktor_vindu_nord +
                                                          sol_tidsvariabel_nord[maaned] * self.solfaktor_total_glass_skjerming_nord) * (
                                                          1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                                                      maaned] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                            tid_drift_oppv_belysn_utstyr[maaned] / 1000 * varmetilskudd_lys[maaned] + tid_drift_oppv_belysn_utstyr[maaned] / 1000 * varmetilskudd_utstyr[maaned] + tid_drift_person[maaned] / 1000 * varmetilskudd_person[maaned] + (
                                        0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * ((
                                                                                                                                  ventilasjonsvarmetap_timer * (
                                                                                                                              term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                                                                                                      term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                                                                                                  ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * (
                                                                                                                                  (
                                                                                                                                          1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                                                                                              [(
                                                                                                                                  self.vifteeffekt_spesifikk_i_driftstid),
                                                                                                                                  (
                                                                                                                                      self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                                                                                              [(
                                                                                                                                  self.vifteeffekt_spesifikk_i_driftstid),
                                                                                                                                  (
                                                                                                                                      self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                        [tid_drift_gjsnitt, mean_timer_per_aar])) * self.areal_oppv

        # NS3031 - Varmettilskudd - januar
        varmetilskudd_feb = tid['feb'] * (straalingsfluks_soer['feb'] * areal_vindu_oest * (
                    (1 - sol_tidsvariabel_ost_vest['feb']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                'feb'] * self.solfaktor_total_glass_skjerming_oest) * (
                                         1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                             straalingsfluks_ostvest['feb'] * areal_vindu_vest * (
                                         (1 - sol_tidsvariabel_ost_vest['feb']) * self.solfaktor_vindu_vest +
                                         sol_tidsvariabel_ost_vest[
                                             'feb'] * self.solfaktor_total_glass_skjerming_vest) * (
                                         1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                             straalingsfluks_ostvest['feb'] * areal_vindu_soer * (
                                         (1 - sol_tidsvariabel_sor['feb']) * self.solfaktor_vindu_soer +
                                         sol_tidsvariabel_sor['feb'] * self.solfaktor_total_glass_skjerming_soer) * (
                                         1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                             straalingsfluks_nord[
                                 'feb'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                         (1 - sol_tidsvariabel_nord['feb']) * self.solfaktor_vindu_nord +
                                         sol_tidsvariabel_nord['feb'] * self.solfaktor_total_glass_skjerming_nord) * (
                                         1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                                 'feb'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                           self.tid_drift_oppv_belysn_utstyr_feb / 1000 * self.varmetilskudd_lys_feb + self.tid_drift_oppv_belysn_utstyr_feb / 1000 * self.varmetilskudd_utstyr_feb + self.tid_drift_person_feb / 1000 * self.varmetilskudd_person_feb + (
                       0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * ((
                                                                                                                     ventilasjonsvarmetap_timer * (
                                                                                                                 term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                                                                                         term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                                                                                     ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * (
                                                                                                                     (
                                                                                                                                 1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                                                                                 [(
                                                                                                                      self.vifteeffekt_spesifikk_i_driftstid),
                                                                                                                  (
                                                                                                                      self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                                                                                 [(
                                                                                                                      self.vifteeffekt_spesifikk_i_driftstid),
                                                                                                                  (
                                                                                                                      self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                       [tid_drift_gjsnitt, mean_timer_per_aar])) * self.areal_oppv
        # NS3031 - Varmettilskudd - februar
        varmetilskudd_mar = tid['mar'] * (
                        straalingsfluks_soer[
                            'mar'] * areal_vindu_oest * (
                                (1 - sol_tidsvariabel_ost_vest['mar']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                            'mar'] * self.solfaktor_total_glass_skjerming_oest) * (
                                1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                        straalingsfluks_ostvest['mar'] * areal_vindu_vest * (
                                (1 - sol_tidsvariabel_ost_vest['mar']) * self.solfaktor_vindu_vest + sol_tidsvariabel_ost_vest[
                            'mar'] * self.solfaktor_total_glass_skjerming_vest) * (
                                1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                        straalingsfluks_ostvest[
                            'mar'] * areal_vindu_soer * (
                                (1 - sol_tidsvariabel_sor['mar']) * self.solfaktor_vindu_soer + sol_tidsvariabel_sor[
                            'mar'] * self.solfaktor_total_glass_skjerming_soer) * (
                                1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                        straalingsfluks_nord[
                            'mar'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                (1 - sol_tidsvariabel_nord['mar']) * self.solfaktor_vindu_nord + sol_tidsvariabel_nord[
                            'mar'] * self.solfaktor_total_glass_skjerming_nord) * (
                                1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                            'mar'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                                   self.tid_drift_oppv_belysn_utstyr_mar / 1000 * self.varmetilskudd_lys_mar + self.tid_drift_oppv_belysn_utstyr_mar / 1000 * self.varmetilskudd_utstyr_mar + self.tid_drift_person_mar / 1000 * self.varmetilskudd_person_mar + (
                                               0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                       (ventilasjonsvarmetap_timer * (
                                                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                               ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * ((
                                                                                                                                   1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                               [tid_drift_gjsnitt,
                                                mean_timer_per_aar])) * self.areal_oppv  # NS3031 - Varmettilskudd - mars
        varmetilskudd_apr = tid['apr'] * (
                        straalingsfluks_soer[
                            'apr'] * areal_vindu_oest * (
                                (1 - sol_tidsvariabel_ost_vest['apr']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                            'apr'] * self.solfaktor_total_glass_skjerming_oest) * (
                                1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                        straalingsfluks_ostvest['apr'] * areal_vindu_vest * (
                                (1 - sol_tidsvariabel_ost_vest['apr']) * self.solfaktor_vindu_vest + sol_tidsvariabel_ost_vest[
                            'apr'] * self.solfaktor_total_glass_skjerming_vest) * (
                                1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                        straalingsfluks_ostvest[
                            'apr'] * areal_vindu_soer * (
                                (1 - sol_tidsvariabel_sor['apr']) * self.solfaktor_vindu_soer + sol_tidsvariabel_sor[
                            'apr'] * self.solfaktor_total_glass_skjerming_soer) * (
                                1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                        straalingsfluks_nord[
                            'apr'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                (1 - sol_tidsvariabel_nord['apr']) * self.solfaktor_vindu_nord + sol_tidsvariabel_nord[
                            'apr'] * self.solfaktor_total_glass_skjerming_nord) * (
                                1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                            'apr'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                                   self.tid_drift_oppv_belysn_utstyr_apr / 1000 * self.varmetilskudd_lys_apr + self.tid_drift_oppv_belysn_utstyr_apr / 1000 * self.varmetilskudd_utstyr_apr + self.tid_drift_person_apr / 1000 * self.varmetilskudd_person_apr + (
                                               0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                       (ventilasjonsvarmetap_timer * (
                                                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                               ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * ((
                                                                                                                                   1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                               [tid_drift_gjsnitt,
                                                mean_timer_per_aar])) * self.areal_oppv  # NS3031 - Varmettilskudd - april
        C124 = tid['mai'] * (
                        straalingsfluks_soer[
                            'mai'] * areal_vindu_oest * (
                                (1 - sol_tidsvariabel_ost_vest['mai']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                            'mai'] * self.solfaktor_total_glass_skjerming_oest) * (
                                1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                        straalingsfluks_ostvest['mai'] * areal_vindu_vest * (
                                (1 - sol_tidsvariabel_ost_vest['mai']) * self.solfaktor_vindu_vest + sol_tidsvariabel_ost_vest[
                            'mai'] * self.solfaktor_total_glass_skjerming_vest) * (
                                1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                        straalingsfluks_ostvest[
                            'mai'] * areal_vindu_soer * (
                                (1 - sol_tidsvariabel_sor['mai']) * self.solfaktor_vindu_soer + sol_tidsvariabel_sor[
                            'mai'] * self.solfaktor_total_glass_skjerming_soer) * (
                                1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                        straalingsfluks_nord[
                            'mai'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                (1 - sol_tidsvariabel_nord['mai']) * self.solfaktor_vindu_nord + sol_tidsvariabel_nord[
                            'mai'] * self.solfaktor_total_glass_skjerming_nord) * (
                                1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                            'mai'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                                   self.tid_drift_oppv_belysn_utstyr_mai / 1000 * self.varmetilskudd_lys_mai + self.tid_drift_oppv_belysn_utstyr_mai / 1000 * self.varmetilskudd_utstyr_mai + self.tid_drift_person_mai / 1000 * self.varmetilskudd_person_mai + (
                                               0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                       (ventilasjonsvarmetap_timer * (
                                                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                               ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * ((
                                                                                                                                   1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                               [tid_drift_gjsnitt,
                                                mean_timer_per_aar])) * self.areal_oppv  # NS3031 - Varmettilskudd - mai
        C125 = tid['jun'] * (
                        straalingsfluks_soer[
                            'jun'] * areal_vindu_oest * (
                                (1 - sol_tidsvariabel_ost_vest['jun']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                            'jun'] * self.solfaktor_total_glass_skjerming_oest) * (
                                1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                        straalingsfluks_ostvest['jun'] * areal_vindu_vest * (
                                (1 - sol_tidsvariabel_ost_vest['jun']) * self.solfaktor_vindu_vest + sol_tidsvariabel_ost_vest[
                            'jun'] * self.solfaktor_total_glass_skjerming_vest) * (
                                1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                        straalingsfluks_ostvest[
                            'jun'] * areal_vindu_soer * (
                                (1 - sol_tidsvariabel_sor['jun']) * self.solfaktor_vindu_soer + sol_tidsvariabel_sor[
                            'jun'] * self.solfaktor_total_glass_skjerming_soer) * (
                                1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                        straalingsfluks_nord[
                            'jun'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                (1 - sol_tidsvariabel_nord['jun']) * self.solfaktor_vindu_nord + sol_tidsvariabel_nord[
                            'jun'] * self.solfaktor_total_glass_skjerming_nord) * (
                                1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                            'jun'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                                   self.tid_drift_oppv_belysn_utstyr_jun / 1000 * self.varmetilskudd_lys_jun + self.tid_drift_oppv_belysn_utstyr_jun / 1000 * self.varmetilskudd_utstyr_jun + self.tid_drift_person_jun / 1000 * self.varmetilskudd_person_jun + (
                                               0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                       (ventilasjonsvarmetap_timer * (
                                                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                               ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * ((
                                                                                                                                   1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                               [tid_drift_gjsnitt,
                                                mean_timer_per_aar])) * self.areal_oppv  # NS3031 - Varmettilskudd - juni
        C126 = tid['jul'] * (
                        straalingsfluks_soer[
                            'jul'] * areal_vindu_oest * (
                                (1 - sol_tidsvariabel_ost_vest['jul']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                            'jul'] * self.solfaktor_total_glass_skjerming_oest) * (
                                1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                        straalingsfluks_ostvest['jul'] * areal_vindu_vest * (
                                (1 - sol_tidsvariabel_ost_vest['jul']) * self.solfaktor_vindu_vest + sol_tidsvariabel_ost_vest[
                            'jul'] * self.solfaktor_total_glass_skjerming_vest) * (
                                1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                        straalingsfluks_ostvest[
                            'jul'] * areal_vindu_soer * (
                                (1 - sol_tidsvariabel_sor['jul']) * self.solfaktor_vindu_soer + sol_tidsvariabel_sor[
                            'jul'] * self.solfaktor_total_glass_skjerming_soer) * (
                                1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                        straalingsfluks_nord[
                            'jul'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                (1 - sol_tidsvariabel_nord['jul']) * self.solfaktor_vindu_nord + sol_tidsvariabel_nord[
                            'jul'] * self.solfaktor_total_glass_skjerming_nord) * (
                                1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                            'jul'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                                   self.tid_drift_oppv_belysn_utstyr_jul / 1000 * self.varmetilskudd_lys_jul + self.tid_drift_oppv_belysn_utstyr_jul / 1000 * self.varmetilskudd_utstyr_jul + self.tid_drift_person_jul / 1000 * self.varmetilskudd_person_jul + (
                                               0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                       (ventilasjonsvarmetap_timer * (
                                                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                               ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * ((
                                                                                                                                   1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                               [tid_drift_gjsnitt,
                                                mean_timer_per_aar])) * self.areal_oppv  # NS3031 - Varmettilskudd - juli
        C127 = tid['aug'] * (
                        straalingsfluks_soer[
                            'aug'] * areal_vindu_oest * (
                                (1 - sol_tidsvariabel_ost_vest['aug']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                            'aug'] * self.solfaktor_total_glass_skjerming_oest) * (
                                1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                        straalingsfluks_ostvest['aug'] * areal_vindu_vest * (
                                (1 - sol_tidsvariabel_ost_vest['aug']) * self.solfaktor_vindu_vest + sol_tidsvariabel_ost_vest[
                            'aug'] * self.solfaktor_total_glass_skjerming_vest) * (
                                1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                        straalingsfluks_ostvest[
                            'aug'] * areal_vindu_soer * (
                                (1 - sol_tidsvariabel_sor['aug']) * self.solfaktor_vindu_soer + sol_tidsvariabel_sor[
                            'aug'] * self.solfaktor_total_glass_skjerming_soer) * (
                                1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                        straalingsfluks_nord[
                            'aug'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                (1 - sol_tidsvariabel_nord['aug']) * self.solfaktor_vindu_nord + sol_tidsvariabel_nord[
                            'aug'] * self.solfaktor_total_glass_skjerming_nord) * (
                                1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                            'aug'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                                   self.tid_drift_oppv_belysn_utstyr_aug / 1000 * self.varmetilskudd_lys_aug + self.tid_drift_oppv_belysn_utstyr_aug / 1000 * self.varmetilskudd_utstyr_aug + self.tid_drift_person_aug / 1000 * self.varmetilskudd_person_aug + (
                                               0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                       (ventilasjonsvarmetap_timer * (
                                                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                               ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * ((
                                                                                                                                   1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                               [tid_drift_gjsnitt,
                                                mean_timer_per_aar])) * self.areal_oppv  # NS3031 - Varmettilskudd - august
        C128 = tid['sep'] * (
                        straalingsfluks_soer[
                            'sep'] * areal_vindu_oest * (
                                (1 - sol_tidsvariabel_ost_vest['sep']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                            'sep'] * self.solfaktor_total_glass_skjerming_oest) * (
                                1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                        straalingsfluks_ostvest['sep'] * areal_vindu_vest * (
                                (1 - sol_tidsvariabel_ost_vest['sep']) * self.solfaktor_vindu_vest + sol_tidsvariabel_ost_vest[
                            'sep'] * self.solfaktor_total_glass_skjerming_vest) * (
                                1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                        straalingsfluks_ostvest[
                            'sep'] * areal_vindu_soer * (
                                (1 - sol_tidsvariabel_sor['sep']) * self.solfaktor_vindu_soer + sol_tidsvariabel_sor[
                            'sep'] * self.solfaktor_total_glass_skjerming_soer) * (
                                1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                        straalingsfluks_nord[
                            'sep'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                (1 - sol_tidsvariabel_nord['sep']) * self.solfaktor_vindu_nord + sol_tidsvariabel_nord[
                            'sep'] * self.solfaktor_total_glass_skjerming_nord) * (
                                1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                            'sep'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                                   self.tid_drift_oppv_belysn_utstyr_sep / 1000 * self.varmetilskudd_lys_sep + self.tid_drift_oppv_belysn_utstyr_sep / 1000 * self.varmetilskudd_utstyr_sep + self.tid_drift_person_sep / 1000 * self.varmetilskudd_person_sep + (
                                               0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                       (ventilasjonsvarmetap_timer * (
                                                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                               ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * ((
                                                                                                                                   1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                               [tid_drift_gjsnitt,
                                                mean_timer_per_aar])) * self.areal_oppv  # NS3031 - Varmettilskudd - september
        C129 = tid['okt'] * (
                        straalingsfluks_soer[
                            'okt'] * areal_vindu_oest * (
                                (1 - sol_tidsvariabel_ost_vest['okt']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                            'okt'] * self.solfaktor_total_glass_skjerming_oest) * (
                                1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                        straalingsfluks_ostvest['okt'] * areal_vindu_vest * (
                                (1 - sol_tidsvariabel_ost_vest['okt']) * self.solfaktor_vindu_vest + sol_tidsvariabel_ost_vest[
                            'okt'] * self.solfaktor_total_glass_skjerming_vest) * (
                                1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                        straalingsfluks_ostvest[
                            'okt'] * areal_vindu_soer * (
                                (1 - sol_tidsvariabel_sor['okt']) * self.solfaktor_vindu_soer + sol_tidsvariabel_sor[
                            'okt'] * self.solfaktor_total_glass_skjerming_soer) * (
                                1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                        straalingsfluks_nord[
                            'okt'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                (1 - sol_tidsvariabel_nord['okt']) * self.solfaktor_vindu_nord + sol_tidsvariabel_nord[
                            'okt'] * self.solfaktor_total_glass_skjerming_nord) * (
                                1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                            'okt'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                                   self.tid_drift_oppv_belysn_utstyr_okt / 1000 * self.varmetilskudd_lys_okt + self.tid_drift_oppv_belysn_utstyr_okt / 1000 * self.varmetilskudd_utstyr_okt + self.tid_drift_person_okt / 1000 * self.varmetilskudd_person_okt + (
                                               0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                       (ventilasjonsvarmetap_timer * (
                                                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                               ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * ((
                                                                                                                                   1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                               [tid_drift_gjsnitt,
                                                mean_timer_per_aar])) * self.areal_oppv  # NS3031 - Varmettilskudd - oktober
        C130 = tid['nov'] * (
                        straalingsfluks_soer[
                            'nov'] * areal_vindu_oest * (
                                (1 - sol_tidsvariabel_ost_vest['nov']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                            'nov'] * self.solfaktor_total_glass_skjerming_oest) * (
                                1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                        straalingsfluks_ostvest['nov'] * areal_vindu_vest * (
                                (1 - sol_tidsvariabel_ost_vest['nov']) * self.solfaktor_vindu_vest + sol_tidsvariabel_ost_vest[
                            'nov'] * self.solfaktor_total_glass_skjerming_vest) * (
                                1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                        straalingsfluks_ostvest[
                            'nov'] * areal_vindu_soer * (
                                (1 - sol_tidsvariabel_sor['nov']) * self.solfaktor_vindu_soer + sol_tidsvariabel_sor[
                            'nov'] * self.solfaktor_total_glass_skjerming_soer) * (
                                1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                        straalingsfluks_nord[
                            'nov'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                (1 - sol_tidsvariabel_nord['nov']) * self.solfaktor_vindu_nord + sol_tidsvariabel_nord[
                            'nov'] * self.solfaktor_total_glass_skjerming_nord) * (
                                1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                            'nov'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                                   self.tid_drift_oppv_belysn_utstyr_nov / 1000 * self.varmetilskudd_lys_nov + self.tid_drift_oppv_belysn_utstyr_nov / 1000 * self.varmetilskudd_utstyr_nov + self.tid_drift_person_nov / 1000 * self.varmetilskudd_person_nov + (
                                               0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                       (ventilasjonsvarmetap_timer * (
                                                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                               ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * ((
                                                                                                                                   1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                               [tid_drift_gjsnitt,
                                                mean_timer_per_aar])) * self.areal_oppv  # NS3031 - Varmettilskudd - november
        C131 = tid['des'] * (
                        straalingsfluks_soer[
                            'des'] * areal_vindu_oest * (
                                (1 - sol_tidsvariabel_ost_vest['des']) * self.solfaktor_vindu_oest + sol_tidsvariabel_ost_vest[
                            'des'] * self.solfaktor_total_glass_skjerming_oest) * (
                                1 - arealfraksjon_karm_oest) * self.solskjermingsfaktor_horisont_oest * self.solskjermingsfaktor_overheng_oest * self.solskjermingsfaktor_finner_oest +
                        straalingsfluks_ostvest['des'] * areal_vindu_vest * (
                                (1 - sol_tidsvariabel_ost_vest['des']) * self.solfaktor_vindu_vest + sol_tidsvariabel_ost_vest[
                            'des'] * self.solfaktor_total_glass_skjerming_vest) * (
                                1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                        straalingsfluks_ostvest[
                            'des'] * areal_vindu_soer * (
                                (1 - sol_tidsvariabel_sor['des']) * self.solfaktor_vindu_soer + sol_tidsvariabel_sor[
                            'des'] * self.solfaktor_total_glass_skjerming_soer) * (
                                1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                        straalingsfluks_nord[
                            'des'] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                (1 - sol_tidsvariabel_nord['des']) * self.solfaktor_vindu_nord + sol_tidsvariabel_nord[
                            'des'] * self.solfaktor_total_glass_skjerming_nord) * (
                                1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                            'des'] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                                   self.tid_drift_oppv_belysn_utstyr_des / 1000 * self.varmetilskudd_lys_des + self.tid_drift_oppv_belysn_utstyr_des / 1000 * self.varmetilskudd_utstyr_des + self.tid_drift_person_des / 1000 * self.varmetilskudd_person_des + (
                                               0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                       (ventilasjonsvarmetap_timer * (
                                                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                               ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * ((
                                                                                                                                   1 - self.tempvirkningsgrad_varmegjenvinner) * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]) + self.tempvirkningsgrad_varmegjenvinner * 0.37 * np.mean(
                                                   [(self.vifteeffekt_spesifikk_i_driftstid),
                                                    (
                                                        self.vifteeffekt_spesifikk_utenfor_driftstid)]))) / self.areal_oppv) / 1000 * np.mean(
                                               [tid_drift_gjsnitt,
                                                mean_timer_per_aar])) * self.areal_oppv  # NS3031 - Varmettilskudd - desember

        X46 = self.tid_drift_oppv_belysn_utstyr_jan  # - Timer i driftstid for oppvarming - Timer for måneden - januar
        X47 = self.tid_drift_oppv_belysn_utstyr_feb  # - Timer i driftstid for oppvarming - Timer for måneden - februar
        X48 = self.tid_drift_oppv_belysn_utstyr_mar  # - Timer i driftstid for oppvarming - Timer for måneden - mars
        X49 = self.tid_drift_oppv_belysn_utstyr_apr  # - Timer i driftstid for oppvarming - Timer for måneden - april
        X50 = self.tid_drift_oppv_belysn_utstyr_mai  # - Timer i driftstid for oppvarming - Timer for måneden - mai
        X51 = self.tid_drift_oppv_belysn_utstyr_jun  # - Timer i driftstid for oppvarming - Timer for måneden - juni
        X52 = self.tid_drift_oppv_belysn_utstyr_jul  # - Timer i driftstid for oppvarming - Timer for måneden - juli
        X53 = self.tid_drift_oppv_belysn_utstyr_aug  # - Timer i driftstid for oppvarming - Timer for måneden - august
        X54 = self.tid_drift_oppv_belysn_utstyr_sep  # - Timer i driftstid for oppvarming - Timer for måneden - september
        X55 = self.tid_drift_oppv_belysn_utstyr_okt  # - Timer i driftstid for oppvarming - Timer for måneden - oktober
        X56 = self.tid_drift_oppv_belysn_utstyr_nov  # - Timer i driftstid for oppvarming - Timer for måneden - november
        X57 = self.tid_drift_oppv_belysn_utstyr_des  # - Timer i driftstid for oppvarming - Timer for måneden - desember

        AE46 = timer['jan'] - X46  # Timer utenfor driftstid for oppvarming - januar
        AE47 = timer['feb'] - X47  # Timer utenfor driftstid for oppvarming - februar
        AE48 = timer['mar'] - X48  # Timer utenfor driftstid for oppvarming - mars
        AE49 = timer['apr'] - X49  # Timer utenfor driftstid for oppvarming - april
        AE50 = timer['mai'] - X50  # Timer utenfor driftstid for oppvarming - mai
        AE51 = timer['jun'] - X51  # Timer utenfor driftstid for oppvarming - juni
        AE52 = timer['jul'] - X52  # Timer utenfor driftstid for oppvarming - juli
        AE53 = timer['aug'] - X53  # Timer utenfor driftstid for oppvarming - august
        AE54 = timer['sep'] - X54  # Timer utenfor driftstid for oppvarming - september
        AE55 = timer['okt'] - X55  # Timer utenfor driftstid for oppvarming - oktober
        AE56 = timer['nov'] - X56  # Timer utenfor driftstid for oppvarming - november
        AE57 = timer['des'] - X57  # Timer utenfor driftstid for oppvarming - desember

        C84 = self.U_tak  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, tak
        C85 = self.U_vegg_oest  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg øst, uten vindu og dør
        C86 = self.U_vegg_vest  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg vest, uten vindu og dør
        C87 = self.U_vegg_soer  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg sør, uten vindu og dør
        C88 = self.U_vegg_nord  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg nord, uten vindu og dør
        C89 = self.U_gulv_mot_det_fri  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, gulv, mot det fri
        C91 = self.U_vindu_oest  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, øst
        C92 = self.U_vindu_vest  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, vest
        C93 = self.U_vindu_soer  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, sør
        C94 = self.U_vindu_nord  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, nord
        C95 = self.U_vindu_tak  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, tak
        C96 = self.U_dor  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, dør
        C98 = self.areal_tak  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, tak
        C99 = self.areal_vegg_oest  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg øst, uten vindu og dør
        C100 = self.areal_vegg_vest  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg vest, uten vindu og dør
        C101 = self.areal_vegg_soer  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg sør, uten vindu og dør
        C102 = self.areal_vegg_nord  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg nord, uten vindu og dør
        C103 = self.areal_gulv_mot_det_fri  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, gulv mot det fri
        C105 = areal_vindu_oest  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vindu, øst
        C106 = areal_vindu_vest  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vindu, vest
        C107 = areal_vindu_soer  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vindu, sør
        C108 = areal_vindu_nord  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vindu, nord
        C109 = areal_vindu_tak  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vindu, tak
        C110 = self.areal_dor  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, dører

        C71 = C84 * C98  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - tak
        C72 = C85 * C99  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg øst, uten vindu
        C73 = C86 * C100  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg vest, uten vindu
        C74 = C87 * C101  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg sør, uten vindu
        C75 = C88 * C102  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg nord, uten vindu
        C76 = C89 * C103  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - gulv mot det fri
        C77 = C91 * C105  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, øst
        C78 = C92 * C106  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, vest
        C79 = C93 * C107  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, sør
        C80 = C94 * C108  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, nord
        C81 = C95 * C109  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, tak
        C82 = C96 * C110  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - dører

        C66 = C71 + C72 + C73 + C74 + C75 + C76 + C77 + C78 + C79 + C80 + C81 + C82  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Summert UiAi for bygningsdeler

        C68 = self.areal_oppv  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD -  Oppvarmet del av BRA
        C69 = self.kuldebro_normalisert  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD -  Normalisert kuldebro
        C67 = C68 * C69  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Normalisert kuldebro ganget med oppvarmet areal
        C64 = C66 + C67  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Totalt, HD

        AE81 = self.BygningskategoriErForretningsbygg  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Hvorvidt bygningen tilhører kategorien forretningsbygg eller bolig (1 = Forretningsbygg, 0 = Bolig)
        AE79 = self.luftmengde_spesifikk_tilluft  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE80 = self.luftmengde_spesifikk_avtrekksluft  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE77 = term1 if AE81 == 0 else AE79  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Arealkorreksjon for bolig, på spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE78 = term1 if AE81 == 0 else AE80  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Arealkorreksjon for bolig, på spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE75 = 0 if AE79 == 0 else AE77  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Korreksjon for luftmengde = 0, på spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE76 = 0 if AE80 == 0 else AE78  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Korreksjon for luftmengde = 0, på spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        AE68 = self.varmekapasitet_luft  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftens varmekapasitet per volum
        AE69 = self.lekkasjetall  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Terrengskjermingskoeffisient, e
        AE70 = self.terrengskjermingskoeff_e  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Lekkasjetall, n50
        AE71 = self.terrengskjermingskoeff_f  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftens varmekapasitet per volum
        AE72 = self.areal_oppv * AE75  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/h)
        AE73 = self.areal_oppv * AE76  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Avtrekksmengde i det mekaniske ventilasjonsanlegget (m3/h)
        AE74 = self.etasjehoyde_innvendig  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Etasjehøyde, innvendig
        AE67 = C68 * AE74  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Oppvarmet luftvolum (Nettovolum av en bygnig beregnet innenfor dens innvendige, omsluttende flater)§
        AE66 = (AE69 * AE70) / (1 + (AE71 / AE70) * ((AE72 - AE73) / (
                    AE67 * AE69)) ** 2)  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftskifte for infiltrasjon
        AE64 = AE68 * AE66 * AE67  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Totalt, Hinf

        Q99 = self.varmekonduktivitet_grunn  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmekonduktivitet til grunnen, λ
        Q100 = self.dybde_periodisk_nedtrengning  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Periodiske nedtrengningsdybde, δ
        Q104 = self.tykkelse_grunnmur  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Tykkelse på grunnmur/ringmur, w [meter]
        Q105 = self.U_gulvkonstruksjon  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmegjennomgangskoeffisient til selve gulvkonstruksjonen uten hensyn til varmemotstanden i grunnen, Ufl [W/(m2 K)]
        Q106 = self.U_kjellerveggskonstruksjon  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmegjennomgangskoeffisient til selve veggkonstruksjonen uten hensyn til varmemotstanden i grunnen, Uw [W/(m2 K)]
        Q107 = self.kantisol_tykkelse  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Tykkelse på kantisolasjon, diso [meter]
        Q108 = self.varmekonduktivitet_kantisol  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmekonduktivitet til kantisolasjonen, λiso ([W/(m K)]) (>0)
        Q101 = Q104 + Q99 / Q105  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for gulvet, dt
        Q102 = Q107 * (
                    Q99 / Q108 - 1)  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for kantisolasjon, d'
        Q103 = Q99 / Q106  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for kjellerveggene, dw
        Q109 = self.kantisol_horisontal_dybde  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Horisontal dybde på kantisolasjon, D [meter]
        Q110 = self.kantisol_vertikal_bredde  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Vertikal bredde på kantisolasjon, D [meter]
        Q112 = self.faseforskjell_utetemp_varmetap  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Faseforskjell mellom utetemp og varmetap (2 mnd for gulv og 1 mnd for kjeller)
        Q114 = self.temp_amplitudevar  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Amplitudevariasjonen omkring årsmiddeltemperaturen ute
        Q97 = -(Q99 / np.pi) * (np.log(Q109 / Q101 + 1) - np.log(Q109 / (
                    Q101 + Q102) + 1))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Lineær varmegjennomgangs-koeffisient, horisontal kantisolasjon
        Q98 = -(Q99 / np.pi) * (np.log(2 * Q110 / Q101 + 1) - np.log(2 * Q110 / (
                    Q101 + Q102) + 1))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Lineær varmegjennomgangs-koeffisient, vertikal kantisolasjon
        Q94 = self.areal_gulv_kjeller  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ag
        Q95 = self.omkrets_gulv  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Omkrets på gulv (omkrets mot det fri), P
        Q96 = self.oppfyllingshoyde_kjellervegg  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Oppfyllingshøyden mot kjellervegg, z
        Q92 = Q94 / (
                    0.5 * Q95)  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Karakteristisk dimensjon for gulvet, B'
        Q93 = 2 * Q99 / (np.pi * Q96) * (1 + ((0.5 * Q101) / (Q101 + Q96))) * np.log(
            Q96 / Q103 + 1)  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Vegg mot grunn, Ubw
        Q84 = 0.37 * Q95 * Q99 * (
                    (1 - np.exp(-(Q109 / Q100))) * np.log(Q100 / (Q101 + Q102)) + np.exp(-(Q109 / Q100)) * np.log(
                Q100 / Q101 + 1))  ## NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For gulv mot grunnen, vertikal kantisolasjon (D' = D)
        Q85 = 0.37 * Q95 * Q99 * ((1 - np.exp(-(2 * Q110 / Q100))) * np.log(Q100 / (Q101 + Q102)) + np.exp(
            -(2 * Q110 / Q100)) * np.log(
            Q100 / Q101 + 1))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For gulv mot grunnen, horisontal kantisolasjon (D' = 2 x D)
        Q86 = 0.37 * Q95 * Q99 * (
                    (1 - np.exp(-(Q96 / Q100))) * np.log(Q100 / Q103 + 1) + np.exp(-(Q96 / Q100)) * np.log(
                Q100 / Q101 + 1))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For vegg og gulv mot grunnen

        Q89 = 2*Q99 / (
                    np.pi*Q92+Q101*0.5*Q96)*np.log((np.pi * Q92 )/( Q101 + 0.5 * Q96)+1)   # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ug (Hvis B'<dt + 0,5*z)
        Q90 = Q99/(0.457*Q92+Q101+0.5*Q96)                                          # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ug (Hvis B'>dt + 0,5*z)
        Q88 = Q89 if Q92 > Q101 + 0.5 * Q96 else Q90
        # Nima Darabi: OBS! Q88 ser ut som er kopiert med offset
        Q81 = Q88 * Q94 + Q97 * Q95  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Stasjonær varmetransportkoeffisient, Hg] - For gulv mot grunnen
        Q82 = Q88 * Q94 + Q96 * Q95 * Q93  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Stasjonær varmetransportkoeffisient, Hg] - For vegg og gulv mot grunnen
        Q78 = self.aarsmiddeltemp_inne  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Årsmiddeltemperatur inne, i driftstiden
        Q79 = self.aarsmiddeltemp_ute  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Årsmiddeltemperatur ute

        Q66 = tid['jan'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (1 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - januar
        Q67 = tid['feb'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (2 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - februar
        Q68 = tid['mar'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (3 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - mars
        Q69 = tid['apr'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (4 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - april
        Q70 = tid['mai'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (5 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - mai
        Q71 = tid['jun'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (6 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - juni
        Q72 = tid['jul'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (7 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - juli
        Q73 = tid['aug'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (8 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - august
        Q74 = tid['sep'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (9 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - september
        Q75 = tid['okt'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (10 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - oktober
        Q76 = tid['nov'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (11 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - novemeber
        Q77 = tid['des'] * (
                (Q81 if Q112 == 2 else Q82) * (Q78 - Q79) + (max([Q84, Q85]) if Q112 == 2 else Q86) * Q114 * np.cos(
            2 * np.pi * (12 - 1 - Q112) / 12))  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - desember
        Q64 = Q66 + Q67 + Q68 + Q69 + Q70 + Q71 + Q72 + Q73 + Q74 + Q75 + Q76 + Q77

        J67 = 0  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Det regnes ikke tillegg for kuldebro mot uoppvarmet rom
        # Nima Darabi: OBS! direkt verditildeling paa J67
        J69 = self.kuldebro_normalisert  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU -Normalisert kuldebro
        J70 = self.varmetapsfaktor_uoppv  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU -Varmetapsfaktor, b
        J74 = self.U_mot_uoppvarmet_sone  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - U-verdi mot uoppvarmet
        J75 = self.areal_mot_uoppvarmet  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Areal, mot uoppvarmet
        J72 = J74 * J75  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU -
        J68 = sum([J75])  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Oppvarmet areal, uoppvarmet sone
        J66 = J72  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Summert UiAi for bygningsdeler
        J64 = J70 * (J66 + J67)  # NS3031 - Varmetransmisjonstap til uoppvarmede soner, HU - Totalt, HU
        J50 = C64  # (Varmetapstall) - Varmetransmisjonstap, HD
        J51 = J64  # (Varmetapstall) - Varmetransmisjonstap, HU
        J52 = Q64  # (Varmetapstall) - Varmetap mot grunnen, et helt år
        J53 = self.varmekapasitet_luft * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                              term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                      ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * (
                      1 - self.tempvirkningsgrad_varmegjenvinner)  # (Varmetapstall) - Ventilasjonsvarmetap, HV
        J54 = AE64  # (Varmetapstall) - Infiltrasjonsvarmetap, Hinf
        Q46 = self.utetemp_jan  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - januar
        Q47 = self.utetemp_feb  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - februar
        Q48 = self.utetemp_mar  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - mars
        Q49 = self.utetemp_apr  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - april
        Q50 = self.utetemp_mai  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - mai
        Q51 = self.utetemp_jun  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - juni
        Q52 = self.utetemp_jul  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - juli
        Q53 = self.utetemp_aug  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - august
        Q54 = self.utetemp_sep  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - september
        Q55 = self.utetemp_okt  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - oktober
        Q56 = self.utetemp_nov  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - november
        Q57 = self.utetemp_des  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - desember
        Q59 = self.temp_settpunkt_oppvarming  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - temp_settpunkt_oppvarming
        Q60 = self.temp_settpunkt_oppvarming_natt  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - temp_settpunkt_oppvarming

        term49 = (J50 + J51 + J53 + J54) * (Q59 - Q46) * X46 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q46) * AE46 / 1000 + Q66
        term50 = (J50 + J51 + J53 + J54) * (Q59 - Q47) * X47 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q47) * AE47 / 1000 + Q67
        term51 = (J50 + J51 + J53 + J54) * (Q59 - Q48) * X48 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q48) * AE48 / 1000 + Q68
        term52 = (J50 + J51 + J53 + J54) * (Q59 - Q49) * X49 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q49) * AE49 / 1000 + Q69
        term53 = (J50 + J51 + J53 + J54) * (Q59 - Q50) * X50 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q50) * AE50 / 1000 + Q70
        term54 = (J50 + J51 + J53 + J54) * (Q59 - Q51) * X51 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q51) * AE51 / 1000 + Q71
        term55 = (J50 + J51 + J53 + J54) * (Q59 - Q52) * X52 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q52) * AE52 / 1000 + Q72
        term56 = (J50 + J51 + J53 + J54) * (Q59 - Q53) * X53 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q53) * AE53 / 1000 + Q73
        term57 = (J50 + J51 + J53 + J54) * (Q59 - Q54) * X54 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q54) * AE54 / 1000 + Q74
        term58 = (J50 + J51 + J53 + J54) * (Q59 - Q55) * X55 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q55) * AE55 / 1000 + Q75
        term59 = (J50 + J51 + J53 + J54) * (Q59 - Q56) * X56 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q56) * AE56 / 1000 + Q76
        term60 = (J50 + J51 + J53 + J54) * (Q59 - Q57) * X57 / 1000 + (J50 + J51 + J53 + J54) * (
                    Q60 - Q57) * AE57 / 1000 + Q77
        C49 = 0.1 if term49 < 0 else term49  # NS3031* - Varmetap - januar
        C50 = 0.1 if term50 < 0 else term50  # NS3031* - Varmetap - februar
        C51 = 0.1 if term51 < 0 else term51  # NS3031* - Varmetap - mars
        C52 = 0.1 if term52 < 0 else term52  # NS3031* - Varmetap - april
        C53 = 0.1 if term53 < 0 else term53  # NS3031* - Varmetap - mai
        C54 = 0.1 if term54 < 0 else term54  # NS3031* - Varmetap - juni
        C55 = 0.1 if term55 < 0 else term55  # NS3031* - Varmetap - juli
        C56 = 0.1 if term56 < 0 else term56  # NS3031* - Varmetap - august
        C57 = 0.1 if term57 < 0 else term57  # NS3031* - Varmetap - september
        C58 = 0.1 if term58 < 0 else term58  # NS3031* - Varmetap - oktober
        C59 = 0.1 if term59 < 0 else term59  # NS3031* - Varmetap - november
        C60 = 0.1 if term60 < 0 else term60  # NS3031* - Varmetap - desember
        C37 = self.norm_varmekap  # NS3031 - Oppvarmingsbehov - Bygningens normaliserte varmekapasitet, C" (Wh/(m3 K))
        C39 = J50 + J51 + J53 + J54 + (
            Q81 if Q112 == 2 else Q82)  # NS3031 - Oppvarmingsbehov - Bygningens varmetransportkoeffisient [W/K]
        C36 = C37 * self.areal_oppv / C39  # NS3031 - Oppvarmingsbehov - Varmetreghet, aH
        C35 = 1 + C36 / 16  # NS3031 - Oppvarmingsbehov - Tidskonstant, τ

        Q22 = varmetilskudd[
                  'jan'] / C49  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - januar
        Q23 = varmetilskudd_feb / C50  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - februar
        Q24 = varmetilskudd_mar / C51  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - mars
        Q25 = varmetilskudd_apr / C52  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - april
        Q26 = C124 / C53  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - mai
        Q27 = C125 / C54  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - juni
        Q28 = C126 / C55  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - juli
        Q29 = C127 / C56  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - august
        Q30 = C128 / C57  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - september
        Q31 = C129 / C58  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - oktober
        Q32 = C130 / C59  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - november
        Q33 = C131 / C60  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - desember

        J22 = 1 / Q22 if Q22 < 0 else C35 / (C35 + 1) if Q22 == 1 else (1 - Q22 ** C35) / (
                    1 - Q22 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - januar
        J23 = 1 / Q23 if Q23 < 0 else C35 / (C35 + 1) if Q23 == 1 else (1 - Q23 ** C35) / (
                    1 - Q23 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - februar
        J24 = 1 / Q24 if Q24 < 0 else C35 / (C35 + 1) if Q24 == 1 else (1 - Q24 ** C35) / (
                    1 - Q24 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - mars
        J25 = 1 / Q25 if Q25 < 0 else C35 / (C35 + 1) if Q25 == 1 else (1 - Q25 ** C35) / (
                    1 - Q25 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - april
        J26 = 1 / Q26 if Q26 < 0 else C35 / (C35 + 1) if Q26 == 1 else (1 - Q26 ** C35) / (
                    1 - Q26 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - mai
        J27 = 1 / Q27 if Q27 < 0 else C35 / (C35 + 1) if Q27 == 1 else (1 - Q27 ** C35) / (
                    1 - Q27 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - juni
        J28 = 1 / Q28 if Q28 < 0 else C35 / (C35 + 1) if Q28 == 1 else (1 - Q28 ** C35) / (
                    1 - Q28 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - juli
        J29 = 1 / Q29 if Q29 < 0 else C35 / (C35 + 1) if Q29 == 1 else (1 - Q29 ** C35) / (
                    1 - Q29 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - august
        J30 = 1 / Q30 if Q30 < 0 else C35 / (C35 + 1) if Q30 == 1 else (1 - Q30 ** C35) / (
                    1 - Q30 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - september
        J31 = 1 / Q31 if Q31 < 0 else C35 / (C35 + 1) if Q31 == 1 else (1 - Q31 ** C35) / (
                    1 - Q31 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - october
        J32 = 1 / Q32 if Q32 < 0 else C35 / (C35 + 1) if Q32 == 1 else (1 - Q32 ** C35) / (
                    1 - Q32 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - november
        J33 = 1 / Q33 if Q33 < 0 else C35 / (C35 + 1) if Q33 == 1 else (1 - Q33 ** C35) / (
                    1 - Q33 ** (C35 + 1))  # NS3031 - Utnyttingsfaktor for måneden - desember
        C22 = C49 - J22 * varmetilskudd['jan']  # NS3031 - Oppvarmingsbehov - januar
        C23 = C50 - J23 * varmetilskudd_feb  # NS3031 - Oppvarmingsbehov - februar
        C24 = C51 - J24 * varmetilskudd_mar  # NS3031 - Oppvarmingsbehov - mars
        C25 = C52 - J25 * varmetilskudd_apr  # NS3031 - Oppvarmingsbehov - april
        C26 = C53 - J26 * C124  # NS3031 - Oppvarmingsbehov - mai
        C27 = C54 - J27 * C125  # NS3031 - Oppvarmingsbehov - juni
        C28 = C55 - J28 * C126  # NS3031 - Oppvarmingsbehov - juli
        C29 = C56 - J29 * C127  # NS3031 - Oppvarmingsbehov - august
        C30 = C57 - J30 * C128  # NS3031 - Oppvarmingsbehov - september
        C31 = C58 - J31 * C129  # NS3031 - Oppvarmingsbehov - oktober
        C32 = C59 - J32 * C130  # NS3031 - Oppvarmingsbehov - november
        C33 = C60 - J33 * C131  # NS3031 - Oppvarmingsbehov - desember
        C20 = C22 + C23 + C24 + C25 + C26 + C27 + C28 + C29 + C30 + C31 + C32 + C33  # NS3031 - Oppvarmingsbehov - Årlig energibehov
        Romoppvarming = C20  # # - Energipost (1a) (Energibehov [kWh/år]) - Romoppvarming

        ### energipost 1-b
        # 6.1.7 -> Trond Ivar Bøhn: OBS! Denne referansen finnes ikke lenger i NS 3031:2014. Det er nå slik at temperaturvirkningsgraden korrigeres for frostsikringen, ref. NS 3031:2014 tillegg H.9. Men om dette skal gjøres om på, må biblioteksverdier for varmegjenvinning vurderes på nytt
        C297 = self.temp_avtrekk  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Temperatur før gjenvinner på avtrekkssiden, θ3
        C298 = self.frostsikringstemperatur  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Frostsikringstemperaturen, θ4
        C296 = C297 - (C297 - C298) / (
                self.tempvirkningsgrad_varmegjenvinner + 0.001)  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Minste utetemperatur som ikke innebærer frostsikring av varmegjenvinneren, θ1,min
        C283 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['jan'] * max([0,
                                                                                                    C296 - Q46])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - januar
        C284 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['feb'] * max([0,
                                                                                                    C296 - Q47])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - februar
        C285 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['mar'] * max([0,
                                                                                                    C296 - Q48])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - mars
        C286 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['apr'] * max([0,
                                                                                                    C296 - Q49])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - april
        C287 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['mai'] * max([0,
                                                                                                    C296 - Q50])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - mai
        C288 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['jun'] * max([0,
                                                                                                    C296 - Q51])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - juni
        C289 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['jul'] * max([0,
                                                                                                    C296 - Q52])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - juli
        C290 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['aug'] * max([0,
                                                                                                    C296 - Q53])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - august
        C291 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['sep'] * max([0,
                                                                                                    C296 - Q54])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - september
        C292 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['okt'] * max([0,
                                                                                                    C296 - Q55])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - oktober
        C293 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['nov'] * max([0,
                                                                                                    C296 - Q56])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - november
        C294 = 0.33 * (ventilasjonsvarmetap_timer * (
            term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                           term1 if self.BygningskategoriErForretningsbygg == 0 else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                       ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * tid['des'] * max([0,
                                                                                                    C296 - Q57])  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - desember
        C281 = C283 + C284 + C285 + C286 + C287 + C288 + C289 + C290 + C291 + C292 + C293 + C294  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7) - Totalt, Edefrost

        Ventilasjonsvarme = C281  # # - Energipost (1b) (Energibehov [kWh/år]) Trond Ivar Bøhn: OBS! Dette ser ikke ut til å være ventilasjonsoppvarming, men kun frostsikring. Ventilasjonsvarmetapet inngår derimot i posten romoppvarming! Spm til NVE: Brukes disse enkeltpostene for netto energibehov til noe i Enova-modulen? I så fall burde vel dette ordnes opp i?!

        ### energipost 3-b
        Q228 = self.temp_settpunkt_kjoeling  # NS3031 - Setpunkttemperatur for kjøling

        Q215 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'jan'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - januar
        Q216 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'feb'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - februar
        Q217 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'mar'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - mars
        Q218 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'apr'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - april
        Q219 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'mai'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - mai
        Q220 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'jun'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - juni
        Q221 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'jul'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - juli
        Q222 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'aug'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - august
        Q223 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'sep'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - september
        Q224 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'okt'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - oktober
        Q225 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'nov'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - november
        Q226 = (J50 + J51 + J53 + J54) * (
                Q228 - Q46) * tid[
                   'des'] + Q66  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - desember
        Q213 = Q215 + Q216 + Q217 + Q218 + Q219 + Q220 + Q221 + Q222 + Q223 + Q224 + Q225 + Q226  # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - Total

        J215 = varmetilskudd['jan']  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - januar
        J216 = varmetilskudd_feb  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - februar
        J217 = varmetilskudd_mar  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - mars
        J218 = varmetilskudd_apr  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - april
        J219 = C124  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - mai
        J220 = C125  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - juni
        J221 = C126  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - juli
        J222 = C127  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - august
        J223 = C128  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - september
        J224 = C129  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - oktober
        J225 = C130  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - november
        J226 = C131  # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - desember

        AE215 = J215 / Q215  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - januar
        AE216 = J216 / Q216  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - februar
        AE217 = J217 / Q217  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - mars
        AE218 = J218 / Q218  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - april
        AE219 = J219 / Q219  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - mai
        AE220 = J220 / Q220  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - juni
        AE221 = J221 / Q221  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - juli
        AE222 = J222 / Q222  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - august
        AE223 = J223 / Q223  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - september
        AE224 = J224 / Q224  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - oktober
        AE225 = J225 / Q225  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - november
        AE226 = J226 / Q226  # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - desember

        X215 = 1 / AE215 if AE215 < 0 else (C35 / (C35 + 1) if AE215 == 1 else (1 - AE215 ** C35) / (
                    1 - AE215 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - januar
        X216 = 1 / AE216 if AE216 < 0 else (C35 / (C35 + 1) if AE216 == 1 else (1 - AE216 ** C35) / (
                    1 - AE216 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - februar
        X217 = 1 / AE217 if AE217 < 0 else (C35 / (C35 + 1) if AE217 == 1 else (1 - AE217 ** C35) / (
                    1 - AE217 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - mars
        X218 = 1 / AE218 if AE218 < 0 else (C35 / (C35 + 1) if AE218 == 1 else (1 - AE218 ** C35) / (
                    1 - AE218 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - april
        X219 = 1 / AE219 if AE219 < 0 else (C35 / (C35 + 1) if AE219 == 1 else (1 - AE219 ** C35) / (
                    1 - AE219 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - mai
        X220 = 1 / AE220 if AE220 < 0 else (C35 / (C35 + 1) if AE220 == 1 else (1 - AE220 ** C35) / (
                    1 - AE220 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - juni
        X221 = 1 / AE221 if AE221 < 0 else (C35 / (C35 + 1) if AE221 == 1 else (1 - AE221 ** C35) / (
                    1 - AE221 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - juli
        X222 = 1 / AE222 if AE222 < 0 else (C35 / (C35 + 1) if AE222 == 1 else (1 - AE222 ** C35) / (
                    1 - AE222 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - august
        X223 = 1 / AE223 if AE223 < 0 else (C35 / (C35 + 1) if AE223 == 1 else (1 - AE223 ** C35) / (
                    1 - AE223 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - september
        X224 = 1 / AE224 if AE224 < 0 else (C35 / (C35 + 1) if AE224 == 1 else (1 - AE224 ** C35) / (
                    1 - AE224 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - oktober
        X225 = 1 / AE225 if AE225 < 0 else (C35 / (C35 + 1) if AE225 == 1 else (1 - AE225 ** C35) / (
                    1 - AE225 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - november
        X226 = 1 / AE226 if AE226 < 0 else (C35 / (C35 + 1) if AE226 == 1 else (1 - AE226 ** C35) / (
                    1 - AE226 ** (C35 + 1)))  # NS3031 - Utnyttingsfaktor - desember

        C231 = self.areal_avkjoelt_andel

        C215 = (0 if J215 - X215 * Q215 < 0 else J215 - X215 * Q215) * C231
        C216 = (0 if J216 - X216 * Q216 < 0 else J216 - X216 * Q216) * C231
        C217 = (0 if J217 - X217 * Q217 < 0 else J217 - X217 * Q217) * C231
        C218 = (0 if J218 - X218 * Q218 < 0 else J218 - X218 * Q218) * C231
        C219 = (0 if J219 - X219 * Q219 < 0 else J219 - X219 * Q219) * C231
        C220 = (0 if J220 - X220 * Q220 < 0 else J220 - X220 * Q220) * C231
        C221 = (0 if J221 - X220 * Q220 < 0 else J220 - X220 * Q220) * C231
        C222 = (0 if J222 - X221 * Q221 < 0 else J221 - X221 * Q221) * C231
        C223 = (0 if J223 - X222 * Q222 < 0 else J222 - X222 * Q222) * C231
        C224 = (0 if J224 - X223 * Q223 < 0 else J223 - X223 * Q223) * C231
        C225 = (0 if J225 - X224 * Q224 < 0 else J224 - X224 * Q224) * C231
        C226 = (0 if J226 - X225 * Q225 < 0 else J225 - X225 * Q225) * C231
        C213 = C215 + C216 + C217 + C218 + C219 + C220 + C221 + C222 + C223 + C224 + C225 + C226

        J265 = self.temp_differanse_veskekrets_oppvarming  # NS3031* - Energibehov, pumper (Oppvarming) - Temperatur differanse tur-retur væskekrets
        J266 = self.varmekapasitet_vann  # NS3031* - Energibehov, pumper (Oppvarming) - Spesifikk varmekapasitet for vann
        J267 = self.densitet_vann  # NS3031* - Energibehov, pumper (Oppvarming) - Densitet for vann
        J264 = C20 / 8760 * 1000  # NS3031* - Energibehov, pumper (Oppvarming) - Varmebehov
        J262 = self.tid_drift_pumpe_oppv  # NS3031* - Energibehov, pumper (Oppvarming) - Driftstid i året
        J261 = self.pumpeeffekt_spesifikk_oppv  # NS3031* - Energibehov, pumper (Oppvarming) - Spesifikk pumpeeffekt
        J260 = J264 / (
                    J265 * J266 * J267) * 1000  # NS3031* - Energibehov, pumper (Oppvarming) - Sirkulert vannmengde gjennom pumpen
        J258 = J260 * J261 * J262  # NS3031* - Energibehov, pumper (Oppvarming) - Totalt, Ep

        Q265 = self.temp_differanse_veskekrets_kjoling  # NS3031* - Energibehov, pumper (Kjøling) - Temperatur differanse tur-retur væskekrets, kjøling
        Q266 = self.varmekapasitet_kuldebaerer  # NS3031* - Energibehov, pumper (Kjøling) - Spesifikk varmekapasitet for kuldebærer
        Q267 = self.densitet_kuldebaerer  # NS3031* - Energibehov, pumper (Kjøling) - Densitet for kuldebærer
        Q264 = C213 / 8760 * 1000  # NS3031* - Energibehov, pumper (Kjøling) - Kjølebehov

        Q262 = self.tid_drift_pumpe_kjoling  # NS3031* - Energibehov, pumper (Kjøling) - Driftstid i året
        Q261 = self.pumpeeffekt_spesifikk_kjoling  # NS3031* - Energibehov, pumper (Kjøling) - Spesifikk pumpeeffekt
        Q260 = Q264 / (
                    Q265 * Q266 * Q267) * 1000  # NS3031* - Energibehov, pumper (Kjøling) - Sirkulert vannmengde gjennom pumpen
        Q258 = Q260 * Q261 * Q262  # NS3031* - Energibehov, pumper (Kjøling) - Totalt, Ep

        C258 = J258 + Q258  # NS3031 - Energibehov for vifter og pumper (Pumper) - Totalt, Ep

        Pumper = C258  # # - Energipost (3b) (Energibehov [kWh/år]) - Pumper

        ### energipost 6
        C215 = (
                   0 if J215 - X215 * Q215 < 0 else J215 - X215 * Q215) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - januar
        C216 = (
                   0 if J216 - X216 * Q216 < 0 else J216 - X216 * Q216) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - februar
        C217 = (
                   0 if J217 - X217 * Q217 < 0 else J217 - X217 * Q215) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - mars
        C218 = (
                   0 if J218 - X218 * Q218 < 0 else J218 - X218 * Q216) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - april
        C219 = (
                   0 if J219 - X219 * Q219 < 0 else J219 - X219 * Q215) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - mai
        C220 = (
                   0 if J220 - X220 * Q220 < 0 else J220 - X220 * Q220) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - juni
        C221 = (
                   0 if J221 - X221 * Q221 < 0 else J221 - X221 * Q221) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - juli
        C222 = (
                   0 if J222 - X222 * Q222 < 0 else J222 - X222 * Q222) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - august
        C223 = (
                   0 if J223 - X223 * Q223 < 0 else J223 - X223 * Q223) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - september
        C224 = (
                   0 if J224 - X224 * Q224 < 0 else J224 - X224 * Q224) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - oktober
        C225 = (
                   0 if J225 - X225 * Q225 < 0 else J225 - X225 * Q225) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - november
        C226 = (
                   0 if J226 - X226 * Q226 < 0 else J226 - X226 * Q226) * C231  # NS3031 - Energibehov for kjøling (6.1.2) [kWh] - desember
        C213 = C215 + C216 + C217 + C218 + C219 + C220 + C221 + C222 + C223 + C224 + C225 + C226
        Kjoeling = C213  # # - Energipost (6) (Energibehov [kWh/år]) - Kjoeling

        Totalt_netto_energibehov = Romoppvarming + Ventilasjonsvarme + \
                                   Varmtvann + \
                                   Vifter + Pumper + \
                                   Belysning + \
                                   Teknisk_utstyr + \
                                   Kjoeling

        # energivare 1
        J306 = self.el_solcelle_andel_el_spesifikt_forbruk  # NS3031 - Andel av energibehov - Andel til el-spesifikt forbruk som dekkes av solcelleanlegg
        J307 = np.nan  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme (Trond Ivar: Egentlig burde man vel også delt opp romoppvarming og ventilasjonsvarme, for å benytte (om ønskelig) forskjellig andel av netto energibehov.)
        J308 = self.el_er_andel_energi_oppv_ventilasjon  # NS3031 - Andel av energibehov - fra elektrisk varmesystem
        J309 = self.el_hp_andel_energi_oppv_ventilasjon  # NS3031 - Andel av energibehov - fra varmepumpe
        J310 = self.el_Tsol_andel_energi_oppv_ventilasjon  # NS3031 - Andel av energibehov - fra solfangeranlegg
        J311 = np.nan  # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann
        J312 = self.el_er_andel_energi_tappevann_varme  # NS3031 - Andel av energibehov - fra elektrisk varmesystem
        J313 = self.el_hp_andel_energi_tappevann_varme  # NS3031 - Andel av energibehov - fra varmepumpe
        J314 = self.el_Tsol_andel_energi_tappevann_varme  # NS3031 - Andel av energibehov - fra solfangeranlegg

        Q305 = np.nan  # NS3031 - Systemvirkningsgrader - Årsgjennomsnittlig
        Q306 = self.systemvirkningsgrad_solcelle  # NS3031 - Systemvirkningsgrader - Solcellesystemer (elektrisitetsproduksjon)
        Q307 = np.nan  # NS3031 - Systemvirkningsgrader - Systemvirkningsgrader for romoppvarming og ventilasjonsvarme
        Q308 = self.systemvirkningsgrad_elektrisk_oppv_ventilasjon  # NS3031 - Systemvirkningsgrader - for elektrisk varmesystem
        Q309 = self.systemvirkningsgrad_varmepumpeanlegg_oppv_ventilasjon  # NS3031 - Systemvirkningsgrader - for varmepumpeanlegg
        Q310 = self.systemvirkningsgrad_solfanger_termisk_oppv_ventilasjon  # NS3031 - Systemvirkningsgrader - for termisk solfangeranlegg
        Q311 = np.nan  # NS3031 - Systemvirkningsgrader - Systemvirkningsgrader for oppvarming av tappevann
        Q312 = self.systemvirkningsgrad_elektrisk_tappevann_varme  # NS3031 - Systemvirkningsgrader - for elektrisk varmesystem
        Q313 = self.systemvirkningsgrad_varmepumpeanlegg_tappevann_varme  # NS3031 - Systemvirkningsgrader - for varmepumpeanlegg
        Q314 = self.systemvirkningsgrad_solfanger_termisk_tappevann_varme  # NS3031 - Systemvirkningsgrader - for termisk solfangeranlegg
        Q316 = self.effektfaktor_kjoeleanlegg  # NS3031 - Systemvirkningsgrader - Årsgjennomsnittlig effektfaktor for kjøleanlegg (komfortkjøling)

        C308 = Vifter + C258 + self.energibehov_belysning * self.areal_oppv + self.energibehov_utstyr * self.areal_oppv  # NS3031 - Systemvirkningsgrader - Netto el-spesifikt forbruk
        C309 = ((
                        C20 + C281) * J308 / Q308 + self.energibehov_tappevann * self.areal_oppv * J312 / Q312)  # NS3031 - Systemvirkningsgrader - Levert elektrisitet til elektriske varmesystemer
        C310 = ((
                        C20 + C281) * J309 / Q309 + self.energibehov_tappevann * self.areal_oppv * J313 / Q313)  # NS3031 - Systemvirkningsgrader - Levert elektrisitet til varmepumpesystemer
        C311 = ((
                        C20 + C281) * J310 / Q310 + self.energibehov_tappevann * self.areal_oppv * J314 / Q314)  # NS3031 - Systemvirkningsgrader - Levert elektrisitet til termiske solenergisystemer
        C312 = C213 / Q316  # NS3031 - Systemvirkningsgrader - Levert elektrisitet til kjølesystemer
        C307 = C308 * (
                    1 - J306) + C308 * J306 / Q306  # NS3031 - Systemvirkningsgrader - Levert elektrisitet til el-spesifikt forbruk
        C306 = C307 + C309 + C310 + C311 + C312  # NS3031 - Systemvirkningsgrader - Levert elektrisitet

        Elektrisitet = C306  # # - Energivare (1) (Levert energi [kWh/år]) - Elektrisitet

        # energivare 2
        Q321 = self.systemvirkningsgrad_olje_oppv_ventilasjon  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Oljebasert varmesystem for romoppvarming og ventilasjonsvarme
        Q322 = self.systemvirkningsgrad_olje_tappevann_varme  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Oljebasert varmesystem for tappevann
        J321 = self.olje_andel_energi_oppv_ventilasjon  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme oljebasert system
        J322 = self.olje_andel_energi_tappevann_varme  # NS3031 - Andel av energibehov - AAndel av netto energibehov for oppvarming av tappevann oljebasert system
        C321 = ((
                        C20 + C281) * J321 / Q321 + self.energibehov_tappevann * self.areal_oppv * J322 / Q322)  # NS3031 - Beregning av behov for levert olje - Levert energi i form av olje
        Olje = C321  # # - Energivare (2) (Levert energi [kWh/år]) - Olje

        # energivare 3
        Q327 = self.systemvirkningsgrad_gass_oppv_ventilasjon  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Gassbasert varmesystem for romoppvarming og ventilasjonsvarme
        Q328 = self.systemvirkningsgrad_gass_tappevann_varme  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Gassbasert varmesystem for tappevann
        J327 = self.gass_andel_energi_oppv_ventilasjon  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme gassbasert system
        J328 = self.gass_andel_energi_tappevann_varme  # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann gassbasert system
        C327 = ((
                        C20 + C281) * J327 / Q327 + self.energibehov_tappevann * self.areal_oppv * J328 / Q328)  # NS3031 - Beregning av behov for levert gass - Levert energi i form av gass
        Gass = C327  # # - Energivare (3) (Levert energi [kWh/år]) - Gass

        # energivare 4
        Q333 = self.systemvirkningsgrad_fjernvarme_oppv_ventilasjon  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Fjernvarmebasert varmesystem for romoppvarming og ventilasjonsvarme
        Q334 = self.systemvirkningsgrad_fjernvarme_tappevann  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Fjernvarmebasert varmesystem for tappevann
        J333 = self.fjernvarme_andel_energi_oppv_ventilasjon  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme fjernvarmebasert system
        J334 = self.fjernvarme_andel_energi_tappevann_varme  # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann fjernvarmebasert system
        C333 = ((
                        C20 + C281) * J333 / Q333 + self.energibehov_tappevann * self.areal_oppv * J334 / Q334)  # NS3031 - Beregning av behov for levert fjernvarme - Levert energi i form av fjernvarme
        Fjernvarme = C333  # # - Energivare (4) (Levert energi [kWh/år]) - Fjernvarme

        # energivare 5
        Q339 = self.systemvirkningsgrad_bio_oppv_ventilasjon  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Biobrenselbasert varmesystem for romoppvarming og ventilasjonsvarme
        Q340 = self.systemvirkningsgrad_bio_tappevann  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Biobrenselbasert varmesystem for tappevann
        J339 = self.bio_andel_energi_oppv_ventilasjon  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme biobrenselbasert system
        J340 = self.bio_andel_energi_tappevann_varme  # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann biobrenselbasert system
        C339 = ((
                        C20 + C281) * J339 / Q339 + self.energibehov_tappevann * self.areal_oppv * J340 / Q340)  # NS3031 - Beregning av behov for levert biobrensel - Levert energi i form av biobrensel
        Biobrensel = C339  # # - Energivare (5) (Levert energi [kWh/år]) - Biobrensel

        # energivare 6
        Q345 = self.systemvirkningsgrad_annet_oppv_ventilasjon  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - varmesystem basert på andre energivarer for romoppvarming og ventilasjonsvarme
        Q346 = self.systemvirkningsgrad_annet_tappevann  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - varmesystem basert på andre energivarer for tappevann
        J345 = self.annet_andel_energi_oppv_ventilasjon  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme basert på andre energivarer system
        J346 = self.annet_andel_energi_tappevann_varme  # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann basert på andre energivarer system
        C345 = ((
                        C20 + C281) * J345 / Q345 + self.energibehov_tappevann * self.areal_oppv * J346 / Q346)  # NS3031 - Beregning av behov for levert andre energivarer - Levert energi i form av andre energivarer
        Annen_energivare = C345  # # - Energivare (6) (Levert energi [kWh/år]) - Andre energivarer

        Totalt_netto_energibehov = Romoppvarming + Ventilasjonsvarme + \
                                   Varmtvann + \
                                   Vifter + Pumper + \
                                   Belysning + \
                                   Teknisk_utstyr + \
                                   Kjoeling

        Totalt_levert_energi = Elektrisitet + \
                               Olje + \
                               Gass + \
                               Fjernvarme + \
                               Biobrensel + \
                               Annen_energivare

        return Output(Romoppvarming,
                      Ventilasjonsvarme,
                      Varmtvann,
                      Vifter,
                      Pumper,
                      Belysning,
                      Teknisk_utstyr,
                      Kjoeling,
                      Totalt_netto_energibehov,

                      Elektrisitet,
                      Olje,
                      Gass,
                      Fjernvarme,
                      Biobrensel,
                      Annen_energivare,
                      Totalt_levert_energi)
