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
    Forretningsbygg: bool

    @property
    def calculate(self):

        # Config / setup

        maaneder = ['jan', 'feb', 'mar', 'apr', 'mai', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'des']

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

        maaned_nummer = {'jan': 1,
                         'feb': 2,
                         'mar': 3,
                         'apr': 4,
                         'mai': 5,
                         'jun': 6,
                         'jul': 7,
                         'aug': 8,
                         'sep': 9,
                         'okt': 10,
                         'nov': 11,
                         'des': 12
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
        Vifter = 0  # - Energipost (3a) (Energibehov [kWh/år]) - Vifter
        for maaned in maaneder:
            Vifter += (spesifikk_i_driftstid * tid_drift_vent[maaned] + spesifikk_utenfor_driftstid * tid_drift_uvent[
                maaned]) / 3600

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
        total_solfaktor_gjennomsnitt_vindu_tak = areal_vindu_tak * self.solfaktor_vindu_tak * 0.9 * (
                1 - arealfraksjon_karm_tak)

        # NS3031* - Ventilasjonsvarmetap, HV - Antall timer i måneden i driftstiden, ton
        ventilasjonsvarmetap_timer = np.mean(list(tid_drift_vent.values()))

        # NS3031* - Ventilasjonsvarmetap, HV - Hvorvidt bygningen tilhører kategorien forretningsbygg eller bolig
        ventilasjonsvarmetapfaktor_bolig_vs_forretningsbygg = (
                1.6 - 0.007 * (self.areal_oppv - 50)) if self.areal_oppv < 110 else 1.2
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
                                                           (1 - sol_tidsvariabel_ost_vest[
                                                               maaned]) * self.solfaktor_vindu_vest +
                                                           sol_tidsvariabel_ost_vest[
                                                               maaned] * self.solfaktor_total_glass_skjerming_vest) * (
                                                           1 - arealfraksjon_karm_vest) * self.solskjermingsfaktor_horisont_vest * self.solskjermingsfaktor_overheng_vest * self.solskjermingsfaktor_finner_vest +
                                                   straalingsfluks_ostvest[maaned] * areal_vindu_soer * (
                                                           (1 - sol_tidsvariabel_sor[
                                                               maaned]) * self.solfaktor_vindu_soer +
                                                           sol_tidsvariabel_sor[
                                                               maaned] * self.solfaktor_total_glass_skjerming_soer) * (
                                                           1 - arealfraksjon_karm_soer) * self.solskjermingsfaktor_horisont_soer * self.solskjermingsfaktor_overheng_soer * self.solskjermingsfaktor_finner_soer +
                                                   straalingsfluks_nord[
                                                       maaned] * self.solskjermingsfaktor_horisont_nord * self.solskjermingsfaktor_overheng_nord * self.solskjermingsfaktor_finner_nord * areal_vindu_nord * (
                                                           (1 - sol_tidsvariabel_nord[
                                                               maaned]) * self.solfaktor_vindu_nord +
                                                           sol_tidsvariabel_nord[
                                                               maaned] * self.solfaktor_total_glass_skjerming_nord) * (
                                                           1 - arealfraksjon_karm_nord) + straalingsfluks_tak[
                                                       maaned] * total_solfaktor_gjennomsnitt_vindu_tak * self.solskjermingsfaktor_horisont_tak * self.solskjermingsfaktor_overheng_tak * self.solskjermingsfaktor_finner_tak) + (
                                            tid_drift_oppv_belysn_utstyr[maaned] / 1000 * varmetilskudd_lys[maaned] +
                                            tid_drift_oppv_belysn_utstyr[maaned] / 1000 * varmetilskudd_utstyr[maaned] +
                                            tid_drift_person[maaned] / 1000 * varmetilskudd_person[maaned] + (
                                                0 if self.tempvirkningsgrad_varmegjenvinner <= 0 else self.varmekapasitet_luft * (
                                                        (
                                                                ventilasjonsvarmetap_timer * (
                                                            ventilasjonsvarmetapfaktor_bolig_vs_forretningsbygg if self.Forretningsbygg else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                                    ventilasjonsvarmetapfaktor_bolig_vs_forretningsbygg if self.Forretningsbygg else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
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

        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - tak
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg øst, uten vindu
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg vest, uten vindu
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg sør, uten vindu
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vegg nord, uten vindu
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - gulv mot det fri
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, øst
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, vest
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, sør
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, nord
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - vindu, tak
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - dører
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Summert UiAi for bygningsdeler
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD -  Oppvarmet del av BRA
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD -  Normalisert kuldebro
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Normalisert kuldebro ganget med oppvarmet areal
        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Totalt, HD
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Hvorvidt bygningen tilhører kategorien forretningsbygg eller bolig (1 = Forretningsbygg, 0 = Bolig)
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        arealkorrekson = ventilasjonsvarmetapfaktor_bolig_vs_forretningsbygg if self.Forretningsbygg else self.luftmengde_spesifikk_tilluft  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Arealkorreksjon for bolig, på spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Arealkorreksjon for bolig, på spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        luftmengdekorreksjon_tilluft = self.luftmengde_spesifikk_tilluft == 0 if self.luftmengde_spesifikk_tilluft == 0 else arealkorrekson  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Korreksjon for luftmengde = 0, på spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        luftmengdekorreksjon_avtrekk = 0 if self.luftmengde_spesifikk_avtrekksluft == 0 else arealkorrekson  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Korreksjon for luftmengde = 0, på spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftens varmekapasitet per volum
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Terrengskjermingskoeffisient, e
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Lekkasjetall, n50
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftens varmekapasitet per volum
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/h)
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Avtrekksmengde i det mekaniske ventilasjonsanlegget (m3/h)
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Etasjehøyde, innvendig
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Oppvarmet luftvolum (Nettovolum av en bygnig beregnet innenfor dens innvendige, omsluttende flater)§
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftskifte for infiltrasjon
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Totalt, Hinf
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmekonduktivitet til grunnen, λ
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Periodiske nedtrengningsdybde, δ
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Tykkelse på grunnmur/ringmur, w [meter]
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmegjennomgangskoeffisient til selve gulvkonstruksjonen uten hensyn til varmemotstanden i grunnen, Ufl [W/(m2 K)]
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmegjennomgangskoeffisient til selve veggkonstruksjonen uten hensyn til varmemotstanden i grunnen, Uw [W/(m2 K)]
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Tykkelse på kantisolasjon, diso [meter]
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmekonduktivitet til kantisolasjonen, λiso ([W/(m K)]) (>0)
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for gulvet, dt
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for kantisolasjon, d'
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for kjellerveggene, dw
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Horisontal dybde på kantisolasjon, D [meter]
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Vertikal bredde på kantisolasjon, D [meter]
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Faseforskjell mellom utetemp og varmetap (2 mnd for gulv og 1 mnd for kjeller)
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Amplitudevariasjonen omkring årsmiddeltemperaturen ute
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Lineær varmegjennomgangs-koeffisient, horisontal kantisolasjon
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ag
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Omkrets på gulv (omkrets mot det fri), P
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Oppfyllingshøyden mot kjellervegg, z
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Karakteristisk dimensjon for gulvet, B'

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Vegg mot grunn, Ubw
        varmetap_mot_grunnen_ubv = 2 * self.varmekonduktivitet_grunn / (np.pi * self.oppfyllingshoyde_kjellervegg) * (
                1 + (
                (0.5 * (self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon)) / (
                self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon + self.oppfyllingshoyde_kjellervegg))) * np.log(
            self.oppfyllingshoyde_kjellervegg / (self.varmekonduktivitet_grunn / self.U_kjellerveggskonstruksjon) + 1)

        ## NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For gulv mot grunnen, vertikal kantisolasjon (D' = D)
        varmetransportkoeffisient_qg = 0.37 * self.omkrets_gulv * self.varmekonduktivitet_grunn * (
                (1 - np.exp(-(self.kantisol_horisontal_dybde / self.dybde_periodisk_nedtrengning))) * np.log(
            self.dybde_periodisk_nedtrengning / (
                    self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon + self.kantisol_tykkelse * (
                    self.varmekonduktivitet_grunn / self.varmekonduktivitet_kantisol - 1))) + np.exp(
            -(self.kantisol_horisontal_dybde / self.dybde_periodisk_nedtrengning)) * np.log(
            self.dybde_periodisk_nedtrengning / (
                    self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon) + 1))

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For gulv mot grunnen, horisontal kantisolasjon (D' = 2 x D)
        varmetapskoeffisient_hpe = 0.37 * self.omkrets_gulv * self.varmekonduktivitet_grunn * (
                (1 - np.exp(-(2 * self.kantisol_vertikal_bredde / self.dybde_periodisk_nedtrengning))) * np.log(
            self.dybde_periodisk_nedtrengning / (
                    self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon + self.kantisol_tykkelse * (
                    self.varmekonduktivitet_grunn / self.varmekonduktivitet_kantisol - 1))) + np.exp(
            -(2 * self.kantisol_vertikal_bredde / self.dybde_periodisk_nedtrengning)) * np.log(
            self.dybde_periodisk_nedtrengning / (
                    self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon) + 1))

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For vegg og gulv mot grunnen
        varmetapskoeffisient_hpe_vegg_og_gulv = 0.37 * self.omkrets_gulv * self.varmekonduktivitet_grunn * (
                (1 - np.exp(-(self.oppfyllingshoyde_kjellervegg / self.dybde_periodisk_nedtrengning))) * np.log(
            self.dybde_periodisk_nedtrengning / (
                    self.varmekonduktivitet_grunn / self.U_kjellerveggskonstruksjon) + 1) + np.exp(
            -(self.oppfyllingshoyde_kjellervegg / self.dybde_periodisk_nedtrengning)) * np.log(
            self.dybde_periodisk_nedtrengning / (
                    self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon) + 1))

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ug (Hvis B'<dt + 0,5*z)
        varmetapskoeffisient_ug = 2 * self.varmekonduktivitet_grunn / (
                np.pi * self.areal_gulv_kjeller / (0.5 * self.omkrets_gulv) + (
                self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon) * 0.5 * self.oppfyllingshoyde_kjellervegg) * np.log(
            (np.pi * self.areal_gulv_kjeller / (0.5 * self.omkrets_gulv)) / (
                    self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon + 0.5 * self.oppfyllingshoyde_kjellervegg) + 1)

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ug (Hvis B'>dt + 0,5*z)
        varmetap_mot_grunnen_qg_gulv_mot_grunn = self.varmekonduktivitet_grunn / (0.457 * self.areal_gulv_kjeller / (
                0.5 * self.omkrets_gulv) + self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon + 0.5 * self.oppfyllingshoyde_kjellervegg)

        # Nima Darabi: OBS! Q88 ser ut som er kopiert med offset
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Stasjonær varmetransportkoeffisient, Hg] - For gulv mot grunnen
        stasjonaer_varmetapskoeffisient_qg = (varmetapskoeffisient_ug if self.areal_gulv_kjeller / (
                0.5 * self.omkrets_gulv) > self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon + 0.5 * self.oppfyllingshoyde_kjellervegg else varmetap_mot_grunnen_qg_gulv_mot_grunn) * self.areal_gulv_kjeller + -(
                self.varmekonduktivitet_grunn / np.pi) * (
                                                     np.log(self.kantisol_horisontal_dybde / (
                                                             self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon) + 1) - np.log(
                                                 self.kantisol_horisontal_dybde / (
                                                         self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon + self.kantisol_tykkelse * (
                                                         self.varmekonduktivitet_grunn / self.varmekonduktivitet_kantisol - 1)) + 1)) * self.omkrets_gulv

        stasjonaer_varmetapskoeffisient_hg = (varmetapskoeffisient_ug if self.areal_gulv_kjeller / (
                0.5 * self.omkrets_gulv) > self.tykkelse_grunnmur + self.varmekonduktivitet_grunn / self.U_gulvkonstruksjon + 0.5 * self.oppfyllingshoyde_kjellervegg else varmetap_mot_grunnen_qg_gulv_mot_grunn) * self.areal_gulv_kjeller + self.oppfyllingshoyde_kjellervegg * self.omkrets_gulv * varmetap_mot_grunnen_ubv  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Stasjonær varmetransportkoeffisient, Hg] - For vegg og gulv mot grunnen

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Årsmiddeltemperatur inne, i driftstiden
        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Årsmiddeltemperatur ute

        varmetap_mot_grunnen_qg = {}
        for maaned in maaneder:
            # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - per måned
            varmetap_mot_grunnen_qg[maaned] = tid[maaned] * (
                    (
                        stasjonaer_varmetapskoeffisient_qg if self.faseforskjell_utetemp_varmetap == 2 else stasjonaer_varmetapskoeffisient_hg) * (
                            self.aarsmiddeltemp_inne - self.aarsmiddeltemp_ute)
                    + (max([(varmetransportkoeffisient_qg), (
                varmetapskoeffisient_hpe)]) if self.faseforskjell_utetemp_varmetap == 2 else varmetapskoeffisient_hpe_vegg_og_gulv)
                    * self.temp_amplitudevar * np.cos(
                2 * np.pi * (maaned_nummer[maaned] - 1 - self.faseforskjell_utetemp_varmetap) / 12))

        # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Det regnes ikke tillegg for kuldebro mot uoppvarmet rom

        # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU -Varmetapsfaktor, b
        # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - U-verdi mot uoppvarmet
        # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Areal, mot uoppvarmet
        # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU -
        # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Summert UiAi for bygningsdeler
        # NS3031 - Varmetransmisjonstap til uoppvarmede soner, HU - Totalt, HU
        # (Varmetapstall) - Varmetransmisjonstap, HD
        # (Varmetapstall) - Varmetransmisjonstap, HU

        varmetapstall_hv = self.varmekapasitet_luft * (ventilasjonsvarmetap_timer * (
            ventilasjonsvarmetapfaktor_bolig_vs_forretningsbygg if self.Forretningsbygg else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                           ventilasjonsvarmetapfaktor_bolig_vs_forretningsbygg if self.Forretningsbygg else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                   ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * (
                                   1 - self.tempvirkningsgrad_varmegjenvinner)  # (Varmetapstall) - Ventilasjonsvarmetap, HV

        varmetapstall_hinf = self.varmekapasitet_luft * (self.lekkasjetall * self.terrengskjermingskoeff_e) / (
                1 + (self.terrengskjermingskoeff_f / self.terrengskjermingskoeff_e) * ((
                                                                                               self.areal_oppv * luftmengdekorreksjon_tilluft - self.areal_oppv * luftmengdekorreksjon_avtrekk) / (
                                                                                               self.areal_oppv * self.etasjehoyde_innvendig * self.lekkasjetall)) ** 2) * self.areal_oppv * self.etasjehoyde_innvendig  # (Varmetapstall) - Infiltrasjonsvarmetap, Hinf

        utetemp = {
            'jan': self.utetemp_jan,
            'feb': self.utetemp_feb,
            'mar': self.utetemp_mar,
            'apr': self.utetemp_apr,
            'mai': self.utetemp_mai,
            'jun': self.utetemp_jun,
            'jul': self.utetemp_jul,
            'aug': self.utetemp_aug,
            'sep': self.utetemp_sep,
            'okt': self.utetemp_okt,
            'nov': self.utetemp_nov,
            'des': self.utetemp_des
        }

        varmetap = {}
        for maaned in maaneder:
            maaned_ = (self.U_tak * self.areal_tak + self.U_vegg_oest * self.areal_vegg_oest + self.U_vegg_vest * self.areal_vegg_vest + self.U_vegg_soer * self.areal_vegg_soer + self.U_vegg_nord * self.areal_vegg_nord + self.U_gulv_mot_det_fri * self.areal_gulv_mot_det_fri + self.U_vindu_oest * areal_vindu_oest + self.U_vindu_vest * areal_vindu_vest + self.U_vindu_soer * areal_vindu_soer + self.U_vindu_nord * areal_vindu_nord + self.U_vindu_tak * areal_vindu_tak + self.U_dor * self.areal_dor + self.areal_oppv * self.kuldebro_normalisert + self.varmetapsfaktor_uoppv * (
                                      self.U_mot_uoppvarmet_sone * self.areal_mot_uoppvarmet) + varmetapstall_hv + varmetapstall_hinf) * (
                                  self.temp_settpunkt_oppvarming - utetemp[maaned]) * tid_drift_oppv_belysn_utstyr[
                          maaned] / 1000 + (
                                  self.U_tak * self.areal_tak + self.U_vegg_oest * self.areal_vegg_oest + self.U_vegg_vest * self.areal_vegg_vest + self.U_vegg_soer * self.areal_vegg_soer + self.U_vegg_nord * self.areal_vegg_nord + self.U_gulv_mot_det_fri * self.areal_gulv_mot_det_fri + self.U_vindu_oest * areal_vindu_oest + self.U_vindu_vest * areal_vindu_vest + self.U_vindu_soer * areal_vindu_soer + self.U_vindu_nord * areal_vindu_nord + self.U_vindu_tak * areal_vindu_tak + self.U_dor * self.areal_dor + self.areal_oppv * self.kuldebro_normalisert + self.varmetapsfaktor_uoppv * (
                                      self.U_mot_uoppvarmet_sone * self.areal_mot_uoppvarmet) + varmetapstall_hv + varmetapstall_hinf) * (
                                  self.temp_settpunkt_oppvarming_natt - utetemp[maaned]) * (
                                  timer[maaned] - tid_drift_oppv_belysn_utstyr[maaned]) / 1000 + \
                      varmetap_mot_grunnen_qg[maaned]
            varmetap[maaned] = 0.1 if maaned_ < 0 else maaned_

        # NS3031 - Oppvarmingsbehov - Bygningens varmetransportkoeffisient [W/K]
        oppvarmingsbehov_tidskonstant = self.U_tak * self.areal_tak + self.U_vegg_oest * self.areal_vegg_oest + self.U_vegg_vest * self.areal_vegg_vest + self.U_vegg_soer * self.areal_vegg_soer + self.U_vegg_nord * self.areal_vegg_nord + self.U_gulv_mot_det_fri * self.areal_gulv_mot_det_fri + self.U_vindu_oest * areal_vindu_oest + self.U_vindu_vest * areal_vindu_vest + self.U_vindu_soer * areal_vindu_soer + self.U_vindu_nord * areal_vindu_nord + self.U_vindu_tak * areal_vindu_tak + self.U_dor * self.areal_dor + self.areal_oppv * self.kuldebro_normalisert + self.varmetapsfaktor_uoppv * (
                self.U_mot_uoppvarmet_sone * self.areal_mot_uoppvarmet + 0) + varmetapstall_hv + varmetapstall_hinf + (
                                            stasjonaer_varmetapskoeffisient_qg if self.faseforskjell_utetemp_varmetap == 2 else stasjonaer_varmetapskoeffisient_hg)

        # NS3031 - Oppvarmingsbehov - Varmetreghet, aH
        oppvarmingsbehov_tidskonstant = 1 + self.norm_varmekap * self.areal_oppv / oppvarmingsbehov_tidskonstant / 16  # NS3031 - Oppvarmingsbehov - Tidskonstant, τ

        utnyttingsfaktor_tmp = {}
        for maaned in maaneder:
            utnyttingsfaktor_tmp[maaned] = varmetilskudd[maaned] / varmetap[maaned]

        utnyttingsfaktor = {}
        for maaned in maaneder:
            utnyttingfaktor_tmp = varmetilskudd[maaned] / varmetap[maaned]
            utnyttingsfaktor[
                maaned] = 1 / utnyttingfaktor_tmp if utnyttingfaktor_tmp < 0 else oppvarmingsbehov_tidskonstant / (
                    oppvarmingsbehov_tidskonstant + 1) if utnyttingfaktor_tmp == 1 else (
                                                                                                1 - utnyttingfaktor_tmp ** oppvarmingsbehov_tidskonstant) / (
                                                                                                1 - utnyttingfaktor_tmp ** (
                                                                                                oppvarmingsbehov_tidskonstant + 1))

        # NS3031 - Oppvarmingsbehov
        oppvarmingsbehov = {}
        for maaned in maaneder:
            oppvarmingsbehov[maaned] = varmetap[maaned] - utnyttingsfaktor[maaned] * varmetilskudd[maaned]

        # # - Energipost (1a) (Energibehov [kWh/år]) - Romoppvarming
        Romoppvarming = sum(oppvarmingsbehov.values())

        ### energipost 1-b
        # 6.1.7 -> Trond Ivar Bøhn: OBS! Denne referansen finnes ikke lenger i NS 3031:2014. Det er nå slik at temperaturvirkningsgraden korrigeres for frostsikringen, ref. NS 3031:2014 tillegg H.9. Men om dette skal gjøres om på, må biblioteksverdier for varmegjenvinning vurderes på nytt
        # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Temperatur før gjenvinner på avtrekkssiden, θ3
        # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Frostsikringstemperaturen, θ4
        # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Minste utetemperatur som ikke innebærer frostsikring av varmegjenvinneren, θ1,min
        # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh]

        energibehov_frostsikring_av_varmegjenvinner = {}
        for maaned in maaneder:
            energibehov_frostsikring_av_varmegjenvinner[maaned] = 0.33 * (ventilasjonsvarmetap_timer * (
                ventilasjonsvarmetapfaktor_bolig_vs_forretningsbygg if self.Forretningsbygg else self.luftmengde_spesifikk_i_driftstid) * self.areal_oppv + mean_tid_drift_ventilasjon * (
                                                                              ventilasjonsvarmetapfaktor_bolig_vs_forretningsbygg if self.Forretningsbygg else self.luftmengde_spesifikk_utenfor_driftstid) * self.areal_oppv) / (
                                                                          ventilasjonsvarmetap_timer + mean_tid_drift_ventilasjon) * \
                                                                  tid[maaned] * max([0,
                                                                                     self.temp_avtrekk - (
                                                                                             self.temp_avtrekk - self.frostsikringstemperatur) / (
                                                                                             self.tempvirkningsgrad_varmegjenvinner + 0.001) -
                                                                                     utetemp[
                                                                                         maaned]])

        # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7) - Totalt, Edefrost
        # # - Energipost (1b) (Energibehov [kWh/år]) Trond Ivar Bøhn: OBS! Dette ser ikke ut til å være ventilasjonsoppvarming, men kun frostsikring. Ventilasjonsvarmetapet inngår derimot i posten romoppvarming! Spm til NVE: Brukes disse enkeltpostene for netto energibehov til noe i Enova-modulen? I så fall burde vel dette ordnes opp i?!
        Ventilasjonsvarme = sum(energibehov_frostsikring_av_varmegjenvinner.values())

        ### energipost 3-b
        # NS3031 - Setpunkttemperatur for kjøling
        # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls]
        setpunkttemp_for_kjoeling = {}
        for maaned in maaneder:
            setpunkttemp_for_kjoeling[maaned] = (
                                                        self.U_tak * self.areal_tak + self.U_vegg_oest * self.areal_vegg_oest + self.U_vegg_vest * self.areal_vegg_vest + self.U_vegg_soer * self.areal_vegg_soer + self.U_vegg_nord * self.areal_vegg_nord + self.U_gulv_mot_det_fri * self.areal_gulv_mot_det_fri + self.U_vindu_oest * areal_vindu_oest + self.U_vindu_vest * areal_vindu_vest + self.U_vindu_soer * areal_vindu_soer + self.U_vindu_nord * areal_vindu_nord + self.U_vindu_tak * areal_vindu_tak + self.U_dor * self.areal_dor + self.areal_oppv * self.kuldebro_normalisert + self.varmetapsfaktor_uoppv * (
                                                        self.U_mot_uoppvarmet_sone * self.areal_mot_uoppvarmet + 0) + varmetapstall_hv + varmetapstall_hinf) * (
                                                        self.temp_settpunkt_kjoeling - utetemp[maaned]) * tid[maaned] + \
                                                varmetap_mot_grunnen_qg['jan']  # TODO: Er dette riktig? varmetap i jan for alle?

        # NS3031 - Varmettilskudd (6.1.1.2) [kWh] - januar
        # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i
        utnytingsfaktor_tilskudd_v_varmetap = {}
        for maaned in maaneder:
            utnytingsfaktor_tilskudd_v_varmetap[maaned] = 1 / (
                    varmetilskudd[maaned] / setpunkttemp_for_kjoeling[maaned]) if varmetilskudd[maaned] / \
                                                                                  setpunkttemp_for_kjoeling[
                                                                                      maaned] < 0 else (
                oppvarmingsbehov_tidskonstant / (oppvarmingsbehov_tidskonstant + 1) if varmetilskudd[maaned] /
                                                                                       setpunkttemp_for_kjoeling[
                                                                                           maaned] == 1 else (1 - (
                        varmetilskudd[maaned] / setpunkttemp_for_kjoeling[
                    maaned]) ** oppvarmingsbehov_tidskonstant) / (1 - (varmetilskudd[
                                                                           maaned] /
                                                                       setpunkttemp_for_kjoeling[
                                                                           maaned]) ** (
                                                                          oppvarmingsbehov_tidskonstant + 1)))  # NS3031 - Utnyttingsfaktor - januar
        varmetilskudd_mnd = {}
        for maaned in maaneder:
            varmetilskudd_mnd[maaned] = (0 if varmetilskudd[maaned]
                                              - utnytingsfaktor_tilskudd_v_varmetap[maaned] * setpunkttemp_for_kjoeling[
                                                  maaned] < 0 else varmetilskudd[maaned]
                                                                   - utnytingsfaktor_tilskudd_v_varmetap[maaned] *
                                                                   setpunkttemp_for_kjoeling[
                                                                       maaned]) * self.areal_avkjoelt_andel

        varmetilskudd_mnd_total = sum(varmetilskudd_mnd.values())

        # NS3031* - Energibehov, pumper (Oppvarming) - Temperatur differanse tur-retur væskekrets
        # NS3031* - Energibehov, pumper (Oppvarming) - Spesifikk varmekapasitet for vann
        # NS3031* - Energibehov, pumper (Oppvarming) - Densitet for vann
        # NS3031* - Energibehov, pumper (Oppvarming) - Varmebehov
        # NS3031* - Energibehov, pumper (Oppvarming) - Driftstid i året
        # NS3031* - Energibehov, pumper (Oppvarming) - Spesifikk pumpeeffekt
        # NS3031* - Energibehov, pumper (Oppvarming) - Sirkulert vannmengde gjennom pumpen
        energibehov_pumper_oppvarming_total_ep = Romoppvarming / 8760 * 1000 / (
                self.temp_differanse_veskekrets_oppvarming * self.varmekapasitet_vann * self.densitet_vann) \
                                                 * 1000 * self.pumpeeffekt_spesifikk_oppv * self.tid_drift_pumpe_oppv  # NS3031* - Energibehov, pumper (Oppvarming) - Totalt, Ep

        # NS3031* - Energibehov, pumper (Kjøling) - Temperatur differanse tur-retur væskekrets, kjøling
        # NS3031* - Energibehov, pumper (Kjøling) - Spesifikk varmekapasitet for kuldebærer
        # NS3031* - Energibehov, pumper (Kjøling) - Densitet for kuldebærer
        energibehov_pumper_kjøling = varmetilskudd_mnd_total / 8760 * 1000  # NS3031* - Energibehov, pumper (Kjøling) - Kjølebehov

        # NS3031* - Energibehov, pumper (Kjøling) - Driftstid i året
        # NS3031* - Energibehov, pumper (Kjøling) - Spesifikk pumpeeffekt
        # NS3031* - Energibehov, pumper (Kjøling) - Sirkulert vannmengde gjennom pumpen
        sirkulert_vannmengde_gjennom_pumpe = energibehov_pumper_kjøling / (
                self.temp_differanse_veskekrets_kjoling * self.varmekapasitet_kuldebaerer * self.densitet_kuldebaerer) * 1000
        # NS3031* - Energibehov, pumper (Kjøling) - Totalt, Ep
        energibehov_pumper_kjoling_total = sirkulert_vannmengde_gjennom_pumpe * self.pumpeeffekt_spesifikk_kjoling * self.tid_drift_pumpe_kjoling

        # NS3031 - Energibehov for vifter og pumper (Pumper) - Totalt, Ep
        # # - Energipost (3b) (Energibehov [kWh/år]) - Pumper
        Pumper = energibehov_pumper_oppvarming_total_ep + energibehov_pumper_kjoling_total

        ### energipost 6
        # NS3031 - Energibehov for kjøling (6.1.2) [kWh]
        # # - Energipost (6) (Energibehov [kWh/år]) - Kjoeling
        Kjoeling = varmetilskudd_mnd_total

        Totalt_netto_energibehov = Romoppvarming + Ventilasjonsvarme + \
                                   Varmtvann + \
                                   Vifter + Pumper + \
                                   Belysning + \
                                   Teknisk_utstyr + \
                                   Kjoeling

        # energivare 1
        # NS3031 - Systemvirkningsgrader - Solcellesystemer (elektrisitetsproduksjon)
        # NS3031 - Systemvirkningsgrader - for elektrisk varmesystem
        # NS3031 - Systemvirkningsgrader - for varmepumpeanlegg
        # NS3031 - Systemvirkningsgrader - for termisk solfangeranlegg
        # NS3031 - Systemvirkningsgrader - for elektrisk varmesystem
        # NS3031 - Systemvirkningsgrader - for varmepumpeanlegg
        # NS3031 - Systemvirkningsgrader - for termisk solfangeranlegg
        # NS3031 - Systemvirkningsgrader - Årsgjennomsnittlig effektfaktor for kjøleanlegg (komfortkjøling)
        # NS3031 - Systemvirkningsgrader - Netto el-spesifikt forbruk

        # NS3031 - Systemvirkningsgrader - Levert elektrisitet til elektriske varmesystemer
        systemvirkningsgrad_levert_el = ((
                                                 Romoppvarming + Ventilasjonsvarme) * self.el_er_andel_energi_oppv_ventilasjon / self.systemvirkningsgrad_elektrisk_oppv_ventilasjon
                                         + self.energibehov_tappevann * self.areal_oppv * self.el_er_andel_energi_tappevann_varme / self.systemvirkningsgrad_elektrisk_tappevann_varme)
        # NS3031 - Systemvirkningsgrader - Levert elektrisitet til varmepumpesystemer
        systemvirkningsgrad_levert_el_varmepumpe = ((
                                                            Romoppvarming + Ventilasjonsvarme) * self.el_hp_andel_energi_oppv_ventilasjon / self.systemvirkningsgrad_varmepumpeanlegg_oppv_ventilasjon
                                                    + self.energibehov_tappevann * self.areal_oppv * self.el_hp_andel_energi_tappevann_varme / self.systemvirkningsgrad_varmepumpeanlegg_tappevann_varme)
        # NS3031 - Systemvirkningsgrader - Levert elektrisitet til kjølesystemer
        systemvirkningsgrad_levert_el_kjoling = ((
                                                         Romoppvarming + Ventilasjonsvarme) * self.el_Tsol_andel_energi_oppv_ventilasjon / self.systemvirkningsgrad_solfanger_termisk_oppv_ventilasjon
                                                 + self.energibehov_tappevann * self.areal_oppv * self.el_Tsol_andel_energi_tappevann_varme / self.systemvirkningsgrad_solfanger_termisk_tappevann_varme)  # NS3031 - Systemvirkningsgrader - Levert elektrisitet til termiske solenergisystemer
        # NS3031 - Systemvirkningsgrader - Levert elektrisitet til el-spesifikt forbruk
        systemvirkningsgrad_levert_el_forbruk = (
                                                        Vifter + Pumper + self.energibehov_belysning * self.areal_oppv + self.energibehov_utstyr * self.areal_oppv) * (
                                                        1 - self.el_solcelle_andel_el_spesifikt_forbruk) + (
                                                        Vifter + Pumper + self.energibehov_belysning * self.areal_oppv
                                                        + self.energibehov_utstyr * self.areal_oppv) * self.el_solcelle_andel_el_spesifikt_forbruk / self.systemvirkningsgrad_solcelle

        # NS3031 - Systemvirkningsgrader - Levert elektrisitet
        # # - Energivare (1) (Levert energi [kWh/år]) - Elektrisitet
        Elektrisitet = systemvirkningsgrad_levert_el_forbruk + systemvirkningsgrad_levert_el + systemvirkningsgrad_levert_el_varmepumpe \
                       + systemvirkningsgrad_levert_el_kjoling + varmetilskudd_mnd_total / self.effektfaktor_kjoeleanlegg

        # energivare 2
        # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Oljebasert varmesystem for romoppvarming og ventilasjonsvarme
        # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Oljebasert varmesystem for tappevann
        # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme oljebasert system
        # NS3031 - Andel av energibehov - AAndel av netto energibehov for oppvarming av tappevann oljebasert system
        # NS3031 - Beregning av behov for levert olje - Levert energi i form av olje
        Olje = ((
                        Romoppvarming + Ventilasjonsvarme) * self.olje_andel_energi_oppv_ventilasjon / self.systemvirkningsgrad_olje_oppv_ventilasjon
                + self.energibehov_tappevann * self.areal_oppv * self.olje_andel_energi_tappevann_varme / self.systemvirkningsgrad_olje_tappevann_varme)  # # - Energivare (2) (Levert energi [kWh/år]) - Olje

        # energivare 3
        # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Gassbasert varmesystem for romoppvarming og ventilasjonsvarme
        # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Gassbasert varmesystem for tappevann
        # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme gassbasert system
        # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann gassbasert system
        # NS3031 - Beregning av behov for levert gass - Levert energi i form av gass
        Gass = ((
                        Romoppvarming + Ventilasjonsvarme) * self.gass_andel_energi_oppv_ventilasjon / self.systemvirkningsgrad_gass_oppv_ventilasjon
                + self.energibehov_tappevann * self.areal_oppv * self.gass_andel_energi_tappevann_varme / self.systemvirkningsgrad_gass_tappevann_varme)  # # - Energivare (3) (Levert energi [kWh/år]) - Gass

        # energivare 4
        # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Fjernvarmebasert varmesystem for romoppvarming og ventilasjonsvarme
        # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Fjernvarmebasert varmesystem for tappevann
        # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme fjernvarmebasert system
        # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann fjernvarmebasert system
        # NS3031 - Beregning av behov for levert fjernvarme - Levert energi i form av fjernvarme
        Fjernvarme = ((
                              Romoppvarming + Ventilasjonsvarme) * self.fjernvarme_andel_energi_oppv_ventilasjon / self.systemvirkningsgrad_fjernvarme_oppv_ventilasjon
                      + self.energibehov_tappevann * self.areal_oppv * self.fjernvarme_andel_energi_tappevann_varme / self.systemvirkningsgrad_fjernvarme_tappevann)  # # - Energivare (4) (Levert energi [kWh/år]) - Fjernvarme

        # energivare 5
        # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Biobrenselbasert varmesystem for romoppvarming og ventilasjonsvarme
        # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Biobrenselbasert varmesystem for tappevann
        # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme biobrenselbasert system
        # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann biobrenselbasert system
        # NS3031 - Beregning av behov for levert biobrensel - Levert energi i form av biobrensel
        Biobrensel = ((
                              Romoppvarming + Ventilasjonsvarme) * self.bio_andel_energi_oppv_ventilasjon / self.systemvirkningsgrad_bio_oppv_ventilasjon
                      + self.energibehov_tappevann * self.areal_oppv * self.bio_andel_energi_tappevann_varme / self.systemvirkningsgrad_bio_tappevann)  # # - Energivare (5) (Levert energi [kWh/år]) - Biobrensel

        # energivare 6
        # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - varmesystem basert på andre energivarer for romoppvarming og ventilasjonsvarme
        # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - varmesystem basert på andre energivarer for tappevann
        # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme basert på andre energivarer system
        # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann basert på andre energivarer system
        # NS3031 - Beregning av behov for levert andre energivarer - Levert energi i form av andre energivarer
        Annen_energivare = ((
                                    Romoppvarming + Ventilasjonsvarme) * self.annet_andel_energi_oppv_ventilasjon / self.systemvirkningsgrad_annet_oppv_ventilasjon
                            + self.energibehov_tappevann * self.areal_oppv * self.annet_andel_energi_tappevann_varme / self.systemvirkningsgrad_annet_tappevann)  # # - Energivare (6) (Levert energi [kWh/år]) - Andre energivarer

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
