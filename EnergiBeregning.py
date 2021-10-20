from dataclasses import dataclass
from dataclasses_json import dataclass_json
import math
import statistics

@dataclass_json
@dataclass
class Output:
    """This class holds the calculation result, one field per value"""

    romoppvarming: float
    ventilasjonsvarme: float
    varmtvann: float
    vifter: float
    pumper: float
    belysning: float
    teknisk_utstyr: float
    kjoeling: float
    totalt_netto_energibehov: float
    elektrisitet: float
    olje: float
    gass: float
    fjernvarme: float
    biobrensel: float
    annen_energivare: float
    totalt_levert_energi: float
    primaerenergi: float
    co2_utslipp: float
    energi_kostnader: float
    energi_politisk: float

    def __str__(self) -> str:
        return "romoppvarming: {0.romoppvarming},Ventilasjonsvarme: {0.ventilasjonsvarme}, \
		Varmtvann: {0.varmtvann}, Vifter: {0.vifter}, \
		Pumper: {0.pumper}, Belysning: {0.belysning}, \
		Teknisk_utstyr: {0.teknisk_utstyr}, Kjoeling: {0.kjoeling}, \
		Totalt_netto_energibehov: {0.totalt_netto_energibehov}, \
		Elektrisitet: {0.elektrisitet}, \
		Olje: {0.olje}, \
		Gass: {0.gass}, \
		Fjernvarme: {0.fjernvarme}, \
		Biobrensel: {0.biobrensel},\
		Annen_energivare: {0.annen_energivare}, \
		Totalt_levert_energi: {0.totalt_levert_energi},\
        Primaerenergi: {0.primaerenergi},\
        CO2_utslipp: {0.co2_utslipp},\
        Energi_kostnader: {0.energi_kostnader}".format(
            self
        )

@dataclass_json
@dataclass
class EnergiBeregning:
    """This class wraps all the calculations"""

    areal_oppv: float  # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i - Oppvarmed del av BRA
    norm_varmekap: int  # NS3031 - Oppvarmingsbehov - Bygningens normaliserte varmekapasitet, C" (Wh/(m3 K))
    kuldebro_normalisert: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD -  Normalisert kuldebro
    temp_settpunkt_oppvarming: float
    temp_settpunkt_oppvarming_natt: float
    areal_tak: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, tak
    areal_vegg_oest: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg øst, uten vindu og dør
    areal_vegg_vest: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg vest, uten vindu og dør
    areal_vegg_soer: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg sør, uten vindu og dør
    areal_vegg_nord: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, vegg nord, uten vindu og dør
    areal_gulv_mot_det_fri: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Areal, gulv mot det fri
    areal_vindu_oest: float  # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, øst
    areal_vindu_vest: float  # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, vest
    areal_vindu_soer: float  # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, sør
    areal_vindu_nord: float  # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, nord
    areal_vindu_tak: float  # NS3031 - Varmettilskudd fra sol - Totalt vindusareal inkludert karm og ramme, tak
    areal_dor: float
    U_tak: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, tak
    U_vegg_oest: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg øst, uten vindu og dør
    U_vegg_vest: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg vest, uten vindu og dør
    U_vegg_soer: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg sør, uten vindu og dør
    U_vegg_nord: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vegg nord, uten vindu og dør
    U_gulv_mot_det_fri: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, gulv, mot det fri
    U_dor: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, dør
    U_vindu_oest: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, øst
    U_vindu_vest: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, vest
    U_vindu_soer: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, sør
    U_vindu_nord: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, nord
    U_vindu_tak: float  # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - U-verdi, vindu, tak
    varmetapsfaktor_uoppv: float  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU -Varmetapsfaktor, b
    areal_mot_uoppvarmet: float  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Areal, mot uoppvarmet
    U_mot_uoppvarmet_sone: float  # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - U-verdi mot uoppvarmet
    areal_gulv_kjeller: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ag
    faseforskjell_utetemp_varmetap: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Faseforskjell mellom utetemp og varmetap (2 mnd for gulv og 1 mnd for kjeller)
    aarsmiddeltemp_inne: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Årsmiddeltemperatur inne, i driftstiden
    omkrets_gulv: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Omkrets på gulv (omkrets mot det fri), P
    U_gulvkonstruksjon: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmegjennomgangskoeffisient til selve gulvkonstruksjonen uten hensyn til varmemotstanden i grunnen, Ufl [W/(m2 K)]
    U_kjellerveggskonstruksjon: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmegjennomgangskoeffisient til selve veggkonstruksjonen uten hensyn til varmemotstanden i grunnen, Uw [W/(m2 K)]
    tykkelse_grunnmur: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Tykkelse på grunnmur/ringmur, w [meter]
    oppfyllingshoyde_kjellervegg: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Oppfyllingshøyden mot kjellervegg, z
    varmekonduktivitet_kantisol: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmekonduktivitet til kantisolasjonen, λiso ([W/(m K)]) (>0)
    kantisol_tykkelse: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Tykkelse på kantisolasjon, diso [meter]
    kantisol_horisontal_dybde: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Horisontal dybde på kantisolasjon, D [meter]
    kantisol_vertikal_bredde: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Vertikal bredde på kantisolasjon, D [meter]
    dybde_periodisk_nedtrengning: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Periodiske nedtrengningsdybde, δ
    varmekonduktivitet_grunn: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Varmekonduktivitet til grunnen, λ
    tempvirkningsgrad_varmegjenvinner: float  # NS3031* - Ventilasjonsvarmetap, HV - Temperaturvirkningsgrad for varmegjenvinner
    luftmengde_spesifikk_i_driftstid: float  # NS3031* - Ventilasjonsvarmetap, HV - Spesifikk luftmengde for ventilasjon ihht. byggkategori i driftstid
    luftmengde_spesifikk_utenfor_driftstid: float  # NS3031* - Ventilasjonsvarmetap, HV - Spesifikk luftmengde for ventilasjon ihht. byggkategori utenfor driftstid
    terrengskjermingskoeff_e: float  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Lekkasjetall, n50
    terrengskjermingskoeff_f: float  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftens varmekapasitet per volum
    lekkasjetall: float  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Terrengskjermingskoeffisient, e
    etasjehoyde_innvendig: float  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Etasjehøyde, innvendig
    luftmengde_spesifikk_tilluft: float  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
    luftmengde_spesifikk_avtrekksluft: float  # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
    vifteeffekt_spesifikk_i_driftstid: float
    vifteeffekt_spesifikk_utenfor_driftstid: float
    frostsikringstemperatur: float  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Frostsikringstemperaturen, θ4
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
    arealfraksjon_karm_oest: float  # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, øst
    arealfraksjon_karm_vest: float  # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, vest
    arealfraksjon_karm_soer: float  # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, sør
    arealfraksjon_karm_nord: float  # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, nord
    arealfraksjon_karm_tak: float  # NS3031 - Varmettilskudd fra sol - Karm/ramme arealfraksjon, tak
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
    solfaktor_vindu_tak: float  # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt (Solfaktor x 0.9, dvs. forenklet)
    solfaktor_total_glass_skjerming_oest: float
    solfaktor_total_glass_skjerming_vest: float
    solfaktor_total_glass_skjerming_soer: float
    solfaktor_total_glass_skjerming_nord: float
    solfaktor_total_glass_skjerming_tak: float
    varmetilskudd_lys_jan: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- jan (W/m2)
    varmetilskudd_lys_feb: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- feb (W/m2)
    varmetilskudd_lys_mar: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- mar (W/m2)
    varmetilskudd_lys_apr: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- apr (W/m2)
    varmetilskudd_lys_mai: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- mai (W/m2)
    varmetilskudd_lys_jun: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- jun (W/m2)
    varmetilskudd_lys_jul: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- jul (W/m2)
    varmetilskudd_lys_aug: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- aug (W/m2)
    varmetilskudd_lys_sep: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- sep (W/m2)
    varmetilskudd_lys_okt: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- okt (W/m2)
    varmetilskudd_lys_nov: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- nov (W/m2)
    varmetilskudd_lys_des: float  # - Spesifikk gjennomsnittlig varmetilskudd fra belysning- dev (W/m2)
    varmetilskudd_utstyr_jan: float  # - Timer i driftstid for belysning - jan (timer)
    varmetilskudd_utstyr_feb: float  # - Timer i driftstid for belysning - feb (timer)
    varmetilskudd_utstyr_mar: float  # - Timer i driftstid for belysning - mar (timer)
    varmetilskudd_utstyr_apr: float  # - Timer i driftstid for belysning - apr (timer)
    varmetilskudd_utstyr_mai: float  # - Timer i driftstid for belysning - mai (timer)
    varmetilskudd_utstyr_jun: float  # - Timer i driftstid for belysning - jun (timer)
    varmetilskudd_utstyr_jul: float  # - Timer i driftstid for belysning - jul (timer)
    varmetilskudd_utstyr_aug: float  # - Timer i driftstid for belysning - aug (timer)
    varmetilskudd_utstyr_sep: float  # - Timer i driftstid for belysning - sep (timer)
    varmetilskudd_utstyr_okt: float  # - Timer i driftstid for belysning - okt (timer)
    varmetilskudd_utstyr_nov: float  # - Timer i driftstid for belysning - nov (timer)
    varmetilskudd_utstyr_des: float  # - Timer i driftstid for belysning - des (timer)
    varmetilskudd_person_jan: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - jan (timer)
    varmetilskudd_person_feb: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - feb (timer)
    varmetilskudd_person_mar: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - mar (timer)
    varmetilskudd_person_apr: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - apr (timer)
    varmetilskudd_person_mai: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - mai (timer)
    varmetilskudd_person_jun: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - jun (timer)
    varmetilskudd_person_jul: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - jul (timer)
    varmetilskudd_person_aug: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - aug (timer)
    varmetilskudd_person_sep: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - sep (timer)
    varmetilskudd_person_okt: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - okt (timer)
    varmetilskudd_person_nov: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - nov (timer)
    varmetilskudd_person_des: float  # - Spesifikk gjennomsnittlig varmetilskudd fra personer - des (timer)
    energibehov_tappevann: float
    energibehov_belysning: float
    energibehov_utstyr: float
    areal_avkjoelt_andel: float
    temp_settpunkt_kjoeling: float  # NS3031 - Setpunkttemperatur for kjøling
    pumpeeffekt_spesifikk_oppv: float  # NS3031* - Energibehov, pumper (Oppvarming) - Spesifikk pumpeeffekt
    tid_drift_pumpe_oppv: float  # NS3031* - Energibehov, pumper (Oppvarming) - Driftstid i året
    temp_differanse_veskekrets_oppvarming: float  # NS3031* - Energibehov, pumper (Oppvarming) - Temperatur differanse tur-retur væskekrets
    pumpeeffekt_spesifikk_kjoling: float  # NS3031* - Energibehov, pumper (Kjøling) - Spesifikk pumpeeffekt
    tid_drift_pumpe_kjoling: float  # NS3031* - Energibehov, pumper (Kjøling) - Driftstid i året
    temp_differanse_veskekrets_kjoling: float  # NS3031* - Energibehov, pumper (Kjøling) - Temperatur differanse tur-retur væskekrets, kjøling
    el_solcelle_andel_el_spesifikt_forbruk: float  # NS3031 - Andel av energibehov - Andel til el-spesifikt forbruk som dekkes av solcelleanlegg
    el_er_andel_energi_oppv_ventilasjon: float  # NS3031 - Andel av energibehov - fra elektrisk varmesystem
    el_hp_andel_energi_oppv_ventilasjon: float  # NS3031 - Andel av energibehov - fra varmepumpe
    el_Tsol_andel_energi_oppv_ventilasjon: float  # NS3031 - Andel av energibehov - fra solfangeranlegg
    el_er_andel_energi_tappevann_varme: float  # NS3031 - Andel av energibehov - fra elektrisk varmesystem
    el_hp_andel_energi_tappevann_varme: float  # NS3031 - Andel av energibehov - fra varmepumpe
    el_Tsol_andel_energi_tappevann_varme: float  # NS3031 - Andel av energibehov - fra solfangeranlegg
    systemvirkningsgrad_solcelle: float  # NS3031 - Systemvirkningsgrader - Solcellesystemer (elektrisitetsproduksjon)
    systemvirkningsgrad_elektrisk_oppv_ventilasjon: float  # NS3031 - Systemvirkningsgrader - for elektrisk varmesystem
    systemvirkningsgrad_elektrisk_tappevann_varme: float  # NS3031 - Systemvirkningsgrader - for elektrisk varmesystem
    systemvirkningsgrad_varmepumpeanlegg_oppv_ventilasjon: float  # NS3031 - Systemvirkningsgrader - for varmepumpeanlegg
    systemvirkningsgrad_varmepumpeanlegg_tappevann_varme: float  # NS3031 - Systemvirkningsgrader - for varmepumpeanlegg
    systemvirkningsgrad_solfanger_termisk_oppv_ventilasjon: float  # NS3031 - Systemvirkningsgrader - for termisk solfangeranlegg
    systemvirkningsgrad_solfanger_termisk_tappevann_varme: float  # NS3031 - Systemvirkningsgrader - for termisk solfangeranlegg
    effektfaktor_kjoeleanlegg: float  # NS3031 - Systemvirkningsgrader - Årsgjennomsnittlig effektfaktor for kjøleanlegg (komfortkjøling)
    olje_andel_energi_oppv_ventilasjon: float  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme oljebasert system
    olje_andel_energi_tappevann_varme: float  # NS3031 - Andel av energibehov - AAndel av netto energibehov for oppvarming av tappevann oljebasert system
    systemvirkningsgrad_olje_oppv_ventilasjon: float  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Oljebasert varmesystem for romoppvarming og ventilasjonsvarme
    systemvirkningsgrad_olje_tappevann_varme: float  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Oljebasert varmesystem for tappevann
    gass_andel_energi_oppv_ventilasjon: float  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme gassbasert system
    gass_andel_energi_tappevann_varme: float  # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann gassbasert system
    systemvirkningsgrad_gass_oppv_ventilasjon: float  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Gassbasert varmesystem for romoppvarming og ventilasjonsvarme
    systemvirkningsgrad_gass_tappevann_varme: float  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Gassbasert varmesystem for tappevann
    fjernvarme_andel_energi_oppv_ventilasjon: float  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme fjernvarmebasert system
    fjernvarme_andel_energi_tappevann_varme: float  # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann fjernvarmebasert system
    systemvirkningsgrad_fjernvarme_oppv_ventilasjon: float  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Fjernvarmebasert varmesystem for romoppvarming og ventilasjonsvarme
    systemvirkningsgrad_fjernvarme_tappevann: float  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Fjernvarmebasert varmesystem for tappevann
    bio_andel_energi_oppv_ventilasjon: float  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme biobrenselbasert system
    bio_andel_energi_tappevann_varme: float  # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann biobrenselbasert system
    systemvirkningsgrad_bio_oppv_ventilasjon: float  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Biobrenselbasert varmesystem for romoppvarming og ventilasjonsvarme
    systemvirkningsgrad_bio_tappevann: float  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - Biobrenselbasert varmesystem for tappevann
    annet_andel_energi_oppv_ventilasjon: float  # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme basert på andre energivarer system
    annet_andel_energi_tappevann_varme: float  # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann basert på andre energivarer system
    systemvirkningsgrad_annet_oppv_ventilasjon: float  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - varmesystem basert på andre energivarer for romoppvarming og ventilasjonsvarme
    systemvirkningsgrad_annet_tappevann: float  # NS3031 - Systemvirkningsgrader (Årsgjennomsnittlig) - varmesystem basert på andre energivarer for tappevann
    CO2_faktor_el: float  # NS3031 (8.2) - CO2-utslipp; levert energi for energivaren - Levert elektrisitet
    CO2_faktor_olje: float  # NS3031 (8.2) - CO2-utslipp; levert energi for energivaren - Levert energi i form av olje
    CO2_faktor_gass: float  # NS3031 (8.2) - CO2-utslipp; levert energi for energivaren - Levert energi i form av gass
    CO2_faktor_fjernvarme: float  # NS3031 (8.2) - CO2-utslipp; levert energi for energivaren - Levert energi i form av fjernvarme
    CO2_faktor_bio: float  # NS3031 (8.2) - CO2-utslipp; levert energi for energivaren - Levert energi i form av biobrensel
    CO2_faktor_annet: float  # NS3031 (8.2) - CO2-utslipp; levert energi for energivaren - Levert energi i form av andre energivarer
    Primaerenergi_faktor_el: float  # NS3031 (8.1) - Primærenergi; faktor for energivaren - Elektrisitet
    Primaerenergi_faktor_olje: float  # NS3031 (8.1) - Primærenergi; faktor for energivaren - Olje
    Primaerenergi_faktor_gass: float  # NS3031 (8.1) - Primærenergi; faktor for energivaren - Gass
    Primaerenergi_faktor_fjernvarme: float  # NS3031 (8.1) - Primærenergi; faktor for energivaren - Fjernvarme
    Primaerenergi_faktor_bio: float  # NS3031 (8.1) - Primærenergi; faktor for energivaren - Biobrensel
    Primaerenergi_faktor_annet: float  # NS3031 (8.1) - Primærenergi; faktor for energivaren - Andre energivarer
    Energipris_el: float  # NS3031 (8.3) - Energikostnad; levert energi for energivaren - Levert elektrisitet
    Energipris_olje: float  # NS3031 (8.3) - Energikostnad; levert energi for energivaren - Levert energi i form av olje
    Energipris_gass: float  # NS3031 (8.3) - Energikostnad; levert energi for energivaren - Levert energi i form av gass
    Energipris_fjernvarme: float  # NS3031 (8.3) - Energikostnad; levert energi for energivaren - Levert energi i form av fjernvarme
    Energipris_bio: float  # NS3031 (8.3) - Energikostnad; levert energi for energivaren - Levert energi i form av biobrensel
    Energipris_annet: float  # NS3031 (8.3) - Energikostnad; levert energi for energivaren - Levert energi i form av andre energivarer
    Energipol_vektingsfaktor_el: float  # NS3031 (8.4) - Energikostnad; Levert energi for energivaren - Levert elektrisitet
    Energipol_vektingsfaktor_olje: float  # NS3031 (8.4) - Energikostnad; Levert energi for energivaren - Levert energi i form av olje
    Energipol_vektingsfaktor_gass: float  # NS3031 (8.4) - Energikostnad; Levert energi for energivaren - Levert energi i form av gass
    Energipol_vektingsfaktor_fjernvarme: float  # NS3031 (8.4) - Energikostnad; Levert energi for energivaren - Levert energi i form av fjernvarme
    Energipol_vektingsfaktor_bio: float  # NS3031 (8.4) - Energikostnad; Levert energi for energivaren - Levert energi i form av biobrensel
    Energipol_vektingsfaktor_annet: float  # NS3031 (8.4) - Energikostnad; Levert energi for energivaren - Levert energi i form av andre energivarer
    tid_drift_oppv_belysn_utstyr_jan: float  # - Timer i driftstid for belysning - jan (timer)
    tid_drift_oppv_belysn_utstyr_feb: float  # - Timer i driftstid for belysning - feb (timer)
    tid_drift_oppv_belysn_utstyr_mar: float  # - Timer i driftstid for belysning - mar (timer)
    tid_drift_oppv_belysn_utstyr_apr: float  # - Timer i driftstid for belysning - apr (timer)
    tid_drift_oppv_belysn_utstyr_mai: float  # - Timer i driftstid for belysning - mai (timer)
    tid_drift_oppv_belysn_utstyr_jun: float  # - Timer i driftstid for belysning - jun (timer)
    tid_drift_oppv_belysn_utstyr_jul: float  # - Timer i driftstid for belysning - jul (timer)
    tid_drift_oppv_belysn_utstyr_aug: float  # - Timer i driftstid for belysning - aug (timer)
    tid_drift_oppv_belysn_utstyr_sep: float  # - Timer i driftstid for belysning - sep (timer)
    tid_drift_oppv_belysn_utstyr_okt: float  # - Timer i driftstid for belysning - okt (timer)
    tid_drift_oppv_belysn_utstyr_nov: float  # - Timer i driftstid for belysning - nov (timer)
    tid_drift_oppv_belysn_utstyr_des: float  # - Timer i driftstid for belysning - des (timer)
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
    tid_drift_person_jan: float  # - Timer i driftstid for personer - jan (timer)
    tid_drift_person_feb: float  # - Timer i driftstid for personer - feb (timer)
    tid_drift_person_mar: float  # - Timer i driftstid for personer - mar (timer)
    tid_drift_person_apr: float  # - Timer i driftstid for personer - apr (timer)
    tid_drift_person_mai: float  # - Timer i driftstid for personer - mai (timer)
    tid_drift_person_jun: float  # - Timer i driftstid for personer - jun (timer)
    tid_drift_person_jul: float  # - Timer i driftstid for personer - jul (timer)
    tid_drift_person_aug: float  # - Timer i driftstid for personer - aug (timer)
    tid_drift_person_sep: float  # - Timer i driftstid for personer - sep (timer)
    tid_drift_person_okt: float  # - Timer i driftstid for personer - okt (timer)
    tid_drift_person_nov: float  # - Timer i driftstid for personer - nov (timer)
    tid_drift_person_des: float  # - Timer i driftstid for personer - des (timer)
    utetemp_jan: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - jan
    utetemp_feb: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - feb
    utetemp_mar: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - mar
    utetemp_apr: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - apr
    utetemp_mai: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - mai
    utetemp_jun: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - jun
    utetemp_jul: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - jul
    utetemp_aug: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - aug
    utetemp_sep: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - sep
    utetemp_okt: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - okt
    utetemp_nov: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - nov
    utetemp_des: float  # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - des
    aarsmiddeltemp_ute: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Årsmiddeltemperatur ute
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
    temp_avtrekk: float  # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Temperatur før gjenvinner på avtrekkssiden, θ3
    varmekapasitet_luft: float  # NS3031* - Ventilasjonsvarmetap, HV - Luftens varmekapasitet per volum
    temp_amplitudevar: float  # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Amplitudevariasjonen omkring årsmiddeltemperaturen ute
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
    varmekapasitet_vann: float  # NS3031* - Energibehov, pumper (Oppvarming) - Spesifikk varmekapasitet for vann
    densitet_vann: float  # NS3031* - Energibehov, pumper (Oppvarming) - Densitet for vann
    varmekapasitet_kuldebaerer: float  # NS3031* - Energibehov, pumper (Kjøling) - Spesifikk varmekapasitet for kuldebærer
    densitet_kuldebaerer: float  # NS3031* - Energibehov, pumper (Kjøling) - Densitet for kuldebærer
    ForretningsBygg: bool  # NS3031* - Ventilasjonsvarmetap, HV - Hvorvidt bygningen tilhører kategorien forretningsbygg eller bolig

    def calculate(self) -> Output:

        maaneder = [
            "jan",
            "feb",
            "mar",
            "apr",
            "mai",
            "jun",
            "jul",
            "aug",
            "sep",
            "okt",
            "nov",
            "des",
        ]

        tid = {
            "jan": self.tid_jan,
            "feb": self.tid_feb,
            "mar": self.tid_mar,
            "apr": self.tid_apr,
            "mai": self.tid_mai,
            "jun": self.tid_jun,
            "jul": self.tid_jul,
            "aug": self.tid_aug,
            "sep": self.tid_sep,
            "okt": self.tid_okt,
            "nov": self.tid_nov,
            "des": self.tid_des,
        }

        maaned_nummer = {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "mai": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "okt": 10,
            "nov": 11,
            "des": 12,
        }

        tid_drift_vent = {
            "jan": self.tid_drift_vent_jan,
            "feb": self.tid_drift_vent_feb,
            "mar": self.tid_drift_vent_mar,
            "apr": self.tid_drift_vent_apr,
            "mai": self.tid_drift_vent_mai,
            "jun": self.tid_drift_vent_jun,
            "jul": self.tid_drift_vent_jul,
            "aug": self.tid_drift_vent_aug,
            "sep": self.tid_drift_vent_sep,
            "okt": self.tid_drift_vent_okt,
            "nov": self.tid_drift_vent_nov,
            "des": self.tid_drift_vent_des,
        }

        tid_drift_oppv_belysn_utstyr = {
            "jan": self.tid_drift_oppv_belysn_utstyr_jan,
            "feb": self.tid_drift_oppv_belysn_utstyr_feb,
            "mar": self.tid_drift_oppv_belysn_utstyr_mar,
            "apr": self.tid_drift_oppv_belysn_utstyr_apr,
            "mai": self.tid_drift_oppv_belysn_utstyr_mai,
            "jun": self.tid_drift_oppv_belysn_utstyr_jun,
            "jul": self.tid_drift_oppv_belysn_utstyr_jul,
            "aug": self.tid_drift_oppv_belysn_utstyr_aug,
            "sep": self.tid_drift_oppv_belysn_utstyr_sep,
            "okt": self.tid_drift_oppv_belysn_utstyr_okt,
            "nov": self.tid_drift_oppv_belysn_utstyr_nov,
            "des": self.tid_drift_oppv_belysn_utstyr_des,
        }

        tid_drift_person = {
            "jan": self.tid_drift_person_jan,
            "feb": self.tid_drift_person_feb,
            "mar": self.tid_drift_person_mar,
            "apr": self.tid_drift_person_apr,
            "mai": self.tid_drift_person_mai,
            "jun": self.tid_drift_person_jun,
            "jul": self.tid_drift_person_jul,
            "aug": self.tid_drift_person_aug,
            "sep": self.tid_drift_person_sep,
            "okt": self.tid_drift_person_okt,
            "nov": self.tid_drift_person_nov,
            "des": self.tid_drift_person_des,
        }

        varmetilskudd_person = {
            "jan": self.varmetilskudd_person_jan,
            "feb": self.varmetilskudd_person_feb,
            "mar": self.varmetilskudd_person_mar,
            "apr": self.varmetilskudd_person_apr,
            "mai": self.varmetilskudd_person_mai,
            "jun": self.varmetilskudd_person_jun,
            "jul": self.varmetilskudd_person_jul,
            "aug": self.varmetilskudd_person_aug,
            "sep": self.varmetilskudd_person_sep,
            "okt": self.varmetilskudd_person_okt,
            "nov": self.varmetilskudd_person_nov,
            "des": self.varmetilskudd_person_des,
        }

        varmetilskudd_lys = {
            "jan": self.varmetilskudd_lys_jan,
            "feb": self.varmetilskudd_lys_feb,
            "mar": self.varmetilskudd_lys_mar,
            "apr": self.varmetilskudd_lys_apr,
            "mai": self.varmetilskudd_lys_mai,
            "jun": self.varmetilskudd_lys_jun,
            "jul": self.varmetilskudd_lys_jul,
            "aug": self.varmetilskudd_lys_aug,
            "sep": self.varmetilskudd_lys_sep,
            "okt": self.varmetilskudd_lys_okt,
            "nov": self.varmetilskudd_lys_nov,
            "des": self.varmetilskudd_lys_des,
        }

        varmetilskudd_utstyr = {
            "jan": self.varmetilskudd_utstyr_jan,
            "feb": self.varmetilskudd_utstyr_feb,
            "mar": self.varmetilskudd_utstyr_mar,
            "apr": self.varmetilskudd_utstyr_apr,
            "mai": self.varmetilskudd_utstyr_mai,
            "jun": self.varmetilskudd_utstyr_jun,
            "jul": self.varmetilskudd_utstyr_jul,
            "aug": self.varmetilskudd_utstyr_aug,
            "sep": self.varmetilskudd_utstyr_sep,
            "okt": self.varmetilskudd_utstyr_okt,
            "nov": self.varmetilskudd_utstyr_nov,
            "des": self.varmetilskudd_utstyr_des,
        }

        # - Temperatur (Gjennomsnittlig utetemperatur for måneden) - januar
        utetemp = {
            "jan": self.utetemp_jan,
            "feb": self.utetemp_feb,
            "mar": self.utetemp_mar,
            "apr": self.utetemp_apr,
            "mai": self.utetemp_mai,
            "jun": self.utetemp_jun,
            "jul": self.utetemp_jul,
            "aug": self.utetemp_aug,
            "sep": self.utetemp_sep,
            "okt": self.utetemp_okt,
            "nov": self.utetemp_nov,
            "des": self.utetemp_des,
        }

        ### energipost 2
        # NS3031*- Energibehov for varmt tappevann, spesifikt - Varmtvann
        # NS3031 - Energibehov for varmt tappevann - Oppvarmed del av BRA
        # NS3031 - Energibehov for varmt tappevann - Årlig energibehov
        # # - Energipost (2) (Energibehov [kWh/år]) - Varmtvann
        Varmtvann = self.energibehov_tappevann * self.areal_oppv

        ### energipost 4
        # NS3031*- Energibehov for belysning, spesifikt - Belysning
        # NS3031 - Energibehov for belysning - Oppvarmed del av BRA
        # NS3031 - Energibehov for belysning - Årlig energibehov
        # # - Energipost (4) (Energibehov [kWh/år]) - Belysning
        Belysning = self.energibehov_belysning * self.areal_oppv

        ### energipost 5
        # NS3031*- Energibehov for teknisk utstyr - Teknisk utstyr
        # NS3031 - Energibehov for teknisk utstyr - Oppvarmed del av BRA
        # NS3031 - Energibehov for utstyr - Årlig energibehov
        # # - Energipost (5) (Energibehov [kWh/år]) - Teknisk_utstyr
        Teknisk_utstyr = self.energibehov_utstyr * self.areal_oppv

        ### energipost 3-a
        # - Timer i måneden
        timer = {}
        timer_i_drift = {}
        for maaned in maaneder:
            timer[maaned] = tid[maaned] * 1000
            timer_i_drift[maaned] = timer[maaned] - tid_drift_vent[maaned]

        mean_timer_per_maaned = statistics.mean(timer.values())

        # - Timer i driftstid for ventilasjon (Timer for måneden)
        mean_timer_i_driftstid_ventilasjon = statistics.mean(timer_i_drift.values())

        # - Driftstid for ventilasjon - Oppvarmed del av BRA
        # - Driftstid for ventilasjon - Luftmengde i driftstiden
        luftmengde_i_driftstiden = (
            self.luftmengde_spesifikk_i_driftstid * self.areal_oppv
        )

        # NS3031 - Energibehov for vifter og pumper - per maaned
        energibehov_vifter_og_pumper = {}
        for maaned in maaneder:
            energibehov_vifter_og_pumper[maaned] = (
                luftmengde_i_driftstiden
                * tid_drift_vent[maaned]
                * self.vifteeffekt_spesifikk_i_driftstid
                + self.luftmengde_spesifikk_utenfor_driftstid
                * self.areal_oppv
                * timer_i_drift[maaned]
                * self.vifteeffekt_spesifikk_utenfor_driftstid
            ) / 3600

        # NS3031 - Energibehov for vifter og pumper (Vifter) - Totalt, Efan
        # # - Energipost (3a) (Energibehov [kWh/år]) - Vifter
        Vifter = sum(energibehov_vifter_og_pumper.values())

        ### energipost 1-a
        # - Timer per måned - januar
        # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, sør (Tillegg M - NS3031:2007)
        straalingsfluks_soer = {
            "jan": self.straalingsfluks_soer_jan,
            "feb": self.straalingsfluks_soer_feb,
            "mar": self.straalingsfluks_soer_mars,
            "apr": self.straalingsfluks_soer_april,
            "mai": self.straalingsfluks_soer_mai,
            "jun": self.straalingsfluks_soer_juni,
            "jul": self.straalingsfluks_soer_juli,
            "aug": self.straalingsfluks_soer_aug,
            "sep": self.straalingsfluks_soer_sept,
            "okt": self.straalingsfluks_soer_okt,
            "nov": self.straalingsfluks_soer_nov,
            "des": self.straalingsfluks_soer_des,
        }

        # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, øst/vest (Tillegg M - NS3031:2007)
        straalingsfluks_ostvest = {
            "jan": self.straalingsfluks_ostvest_jan,
            "feb": self.straalingsfluks_ostvest_feb,
            "mar": self.straalingsfluks_ostvest_mars,
            "apr": self.straalingsfluks_ostvest_april,
            "mai": self.straalingsfluks_ostvest_mai,
            "jun": self.straalingsfluks_ostvest_juni,
            "jul": self.straalingsfluks_ostvest_juli,
            "aug": self.straalingsfluks_ostvest_aug,
            "sep": self.straalingsfluks_ostvest_sept,
            "okt": self.straalingsfluks_ostvest_okt,
            "nov": self.straalingsfluks_ostvest_nov,
            "des": self.straalingsfluks_ostvest_des,
        }

        # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, nord (Tillegg M - NS3031:2007)
        straalingsfluks_nord = {
            "jan": self.straalingsfluks_nord_jan,
            "feb": self.straalingsfluks_nord_feb,
            "mar": self.straalingsfluks_nord_mars,
            "apr": self.straalingsfluks_nord_april,
            "mai": self.straalingsfluks_nord_mai,
            "jun": self.straalingsfluks_nord_juni,
            "jul": self.straalingsfluks_nord_juli,
            "aug": self.straalingsfluks_nord_aug,
            "sep": self.straalingsfluks_nord_sept,
            "okt": self.straalingsfluks_nord_okt,
            "nov": self.straalingsfluks_nord_nov,
            "des": self.straalingsfluks_nord_des,
        }

        # - Gjennomsnittlig strålingsfluks mot tak (Tillegg M - NS3031:2007)
        straalingsfluks_tak = {
            "jan": self.straalingsfluks_tak_jan,
            "feb": self.straalingsfluks_tak_feb,
            "mar": self.straalingsfluks_tak_mars,
            "apr": self.straalingsfluks_tak_april,
            "mai": self.straalingsfluks_tak_mai,
            "jun": self.straalingsfluks_tak_juni,
            "jul": self.straalingsfluks_tak_juli,
            "aug": self.straalingsfluks_tak_aug,
            "sep": self.straalingsfluks_tak_sept,
            "okt": self.straalingsfluks_tak_okt,
            "nov": self.straalingsfluks_tak_nov,
            "des": self.straalingsfluks_tak_des,
        }

        sol_tidsvariabel_ost_vest = {
            "jan": self.sol_tidsvariabel_ost_vest_jan,
            "feb": self.sol_tidsvariabel_ost_vest_feb,
            "mar": self.sol_tidsvariabel_ost_vest_mars,
            "apr": self.sol_tidsvariabel_ost_vest_april,
            "mai": self.sol_tidsvariabel_ost_vest_mai,
            "jun": self.sol_tidsvariabel_ost_vest_juni,
            "jul": self.sol_tidsvariabel_ost_vest_juli,
            "aug": self.sol_tidsvariabel_ost_vest_aug,
            "sep": self.sol_tidsvariabel_ost_vest_sept,
            "okt": self.sol_tidsvariabel_ost_vest_okt,
            "nov": self.sol_tidsvariabel_ost_vest_nov,
            "des": self.sol_tidsvariabel_ost_vest_des,
        }

        sol_tidsvariabel_sor = {
            "jan": self.sol_tidsvariabel_soer_jan,
            "feb": self.sol_tidsvariabel_soer_feb,
            "mar": self.sol_tidsvariabel_soer_mars,
            "apr": self.sol_tidsvariabel_soer_april,
            "mai": self.sol_tidsvariabel_soer_mai,
            "jun": self.sol_tidsvariabel_soer_juni,
            "jul": self.sol_tidsvariabel_soer_juli,
            "aug": self.sol_tidsvariabel_soer_aug,
            "sep": self.sol_tidsvariabel_soer_sept,
            "okt": self.sol_tidsvariabel_soer_okt,
            "nov": self.sol_tidsvariabel_soer_nov,
            "des": self.sol_tidsvariabel_soer_des,
        }

        # - Gjennomsnittlig strålingsfluks mot utsiden av vinduene, nord (Tillegg M - NS3031:2007)
        sol_tidsvariabel_nord = {
            "jan": self.sol_tidsvariabel_nord_jan,
            "feb": self.sol_tidsvariabel_nord_feb,
            "mar": self.sol_tidsvariabel_nord_mars,
            "apr": self.sol_tidsvariabel_nord_april,
            "mai": self.sol_tidsvariabel_nord_mai,
            "jun": self.sol_tidsvariabel_nord_juni,
            "jul": self.sol_tidsvariabel_nord_juli,
            "aug": self.sol_tidsvariabel_nord_aug,
            "sep": self.sol_tidsvariabel_nord_sept,
            "okt": self.sol_tidsvariabel_nord_okt,
            "nov": self.sol_tidsvariabel_nord_nov,
            "des": self.sol_tidsvariabel_nord_des,
        }

        # - Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt (Solfaktor x 0,9, dvs. forenklet)
        total_solfaktor = round(
            self.solfaktor_vindu_tak * 0,
            9,
        )
        # Total solfaktor for kombinasjon av glass og kunstig solskjerming, månedlig gj.snitt (tak)
        # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, tak
        total_solfaktor_gjennomsnitt = (
            self.areal_vindu_tak * total_solfaktor * (1 - self.arealfraksjon_karm_tak)
        )

        total_solfaktor_gjennomsnitt_ost = {}
        total_solfaktor_gjennomsnitt_ost_vest = {}
        total_solfaktor_gjennomsnitt_sor = {}
        total_solfaktor_gjennomsnitt_nord = {}
        for maaned in maaneder:
            # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, øst
            total_solfaktor_gjennomsnitt_ost[maaned] = (
                self.areal_vindu_oest
                * (
                    (1 - sol_tidsvariabel_ost_vest[maaned]) * self.solfaktor_vindu_oest
                    + sol_tidsvariabel_ost_vest[maaned]
                    * self.solfaktor_total_glass_skjerming_oest
                )
                * (1 - self.arealfraksjon_karm_oest)
            )

            # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, vest
            total_solfaktor_gjennomsnitt_ost_vest[maaned] = (
                self.areal_vindu_vest
                * (
                    (1 - sol_tidsvariabel_ost_vest[maaned]) * self.solfaktor_vindu_vest
                    + sol_tidsvariabel_ost_vest[maaned]
                    * self.solfaktor_total_glass_skjerming_vest
                )
                * (1 - self.arealfraksjon_karm_vest)
            )

            # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, sør
            total_solfaktor_gjennomsnitt_sor[maaned] = (
                self.areal_vindu_soer
                * (
                    (1 - sol_tidsvariabel_sor[maaned]) * self.solfaktor_vindu_soer
                    + sol_tidsvariabel_sor[maaned]
                    * self.solfaktor_total_glass_skjerming_soer
                )
                * (1 - self.arealfraksjon_karm_soer)
            )

            # - Total solfaktor, gjennomsnitt - Effektivt vindusareal for soltilskudd, nord
            total_solfaktor_gjennomsnitt_nord[maaned] = (
                self.areal_vindu_nord
                * (
                    (1 - sol_tidsvariabel_nord[maaned]) * self.solfaktor_vindu_nord
                    + sol_tidsvariabel_nord[maaned]
                    * self.solfaktor_total_glass_skjerming_nord
                )
                * (1 - self.arealfraksjon_karm_nord)
            )

        # NS3031 - Varmettilskudd fra sol Totalt, (Qsol, i) [kWh] - januar
        varmetilskudd_fra_sol_totalt = {}
        for maaned in maaneder:
            varmetilskudd_fra_sol_totalt[maaned] = tid[maaned] * (
                straalingsfluks_soer[maaned]
                * total_solfaktor_gjennomsnitt_ost[maaned]
                * (self.solskjermingsfaktor_horisont_oest)
                * self.solskjermingsfaktor_overheng_oest
                * self.solskjermingsfaktor_finner_oest
                + straalingsfluks_ostvest[maaned]
                * total_solfaktor_gjennomsnitt_ost_vest[maaned]
                * (self.solskjermingsfaktor_horisont_vest)
                * (self.solskjermingsfaktor_overheng_vest)
                * self.solskjermingsfaktor_finner_vest
                + straalingsfluks_ostvest[maaned]
                * total_solfaktor_gjennomsnitt_sor[maaned]
                * (self.solskjermingsfaktor_horisont_soer)
                * self.solskjermingsfaktor_overheng_soer
                * self.solskjermingsfaktor_finner_soer
                + straalingsfluks_nord[maaned]
                * (self.solskjermingsfaktor_horisont_nord)
                * (self.solskjermingsfaktor_overheng_nord)
                * self.solskjermingsfaktor_finner_nord
                * total_solfaktor_gjennomsnitt_nord[maaned]
                + straalingsfluks_tak[maaned]
                * (total_solfaktor_gjennomsnitt)
                * self.solskjermingsfaktor_horisont_tak
                * self.solskjermingsfaktor_overheng_tak
                * self.solskjermingsfaktor_finner_tak
            )

        # NS3031* - Ventilasjonsvarmetap, HV - Antall timer i måneden i driftstiden, ton
        ventilasjonsvarmetap_timer_i_drift = statistics.mean(tid_drift_vent.values())
        arealkorreksjonfaktor_for_bolig = (
            (1.6 - 0.007 * (self.areal_oppv - 50)) if self.areal_oppv < 110 else 1.2
        )

        # NS3031* - Ventilasjonsvarmetap, HV - Arealkorreksjon for bolig, på spesifikk luftmengde for ventilasjon i driftstid
        arealkorreksjon_bolig_ventilasjon_i_driftstid = (
            self.luftmengde_spesifikk_i_driftstid
            if self.ForretningsBygg
            else arealkorreksjonfaktor_for_bolig
        )

        # NS3031* - Ventilasjonsvarmetap, HV - Arealkorreksjon for bolig, på spesifikk luftmengde for ventilasjon utenfor driftstid
        arealkorreksjon_bolig_ventilasjon_utenfor_driftstid = (
            self.luftmengde_spesifikk_utenfor_driftstid
            if self.ForretningsBygg
            else arealkorreksjonfaktor_for_bolig
        )

        # NS3031* - Ventilasjonsvarmetap, HV - Gjennomsnittlig ventilasjonsmengde
        ventilasjonsvarmetap_gjennomsnittlig_ventilasjonsmengde = (
            ventilasjonsvarmetap_timer_i_drift
            * (arealkorreksjon_bolig_ventilasjon_i_driftstid * self.areal_oppv)
            + mean_timer_i_driftstid_ventilasjon
            * (arealkorreksjon_bolig_ventilasjon_utenfor_driftstid * self.areal_oppv)
        ) / (ventilasjonsvarmetap_timer_i_drift + mean_timer_i_driftstid_ventilasjon)

        # NS3031* - Ventilasjonsvarmetap, HV - Totalt, HV
        ventilasjonsvarmetap_totalt = (
            (self.varmekapasitet_luft)
            * ventilasjonsvarmetap_gjennomsnittlig_ventilasjonsmengde
            * (1 - (self.tempvirkningsgrad_varmegjenvinner))
        )

        # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Temperaturøkning over avtrekksvifte
        mean_varmetilskudd_fra_vifter = 0.37 * statistics.mean(
            [
                (self.vifteeffekt_spesifikk_i_driftstid),
                (self.vifteeffekt_spesifikk_utenfor_driftstid),
            ]
        )

        # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Oppvarmed del av BRA (m2)
        # - Spesifikk gjennomsnittlig varmetilskudd fra vifter - Varmetilskudd fra vifter
        spesifikk_gjsnitt_varmetilskudd_fra_vifter = (
            0
            if (self.tempvirkningsgrad_varmegjenvinner) <= 0
            else self.varmekapasitet_luft
            * (
                ventilasjonsvarmetap_gjennomsnittlig_ventilasjonsmengde
                * (
                    (1 - (self.tempvirkningsgrad_varmegjenvinner))
                    * mean_varmetilskudd_fra_vifter
                    + (self.tempvirkningsgrad_varmegjenvinner)
                    * mean_varmetilskudd_fra_vifter
                )
            )
            / (self.areal_oppv)
        )

        # NS3031 - Internt varmettilskudd (6.1.1.2.1) - Totalt, Qint, i
        internt_varmetilskudd = {}
        for maaned in maaneder:
            internt_varmetilskudd[maaned] = (
                tid_drift_oppv_belysn_utstyr[maaned] / 1000 * varmetilskudd_lys[maaned]
                + tid_drift_oppv_belysn_utstyr[maaned]
                / 1000
                * varmetilskudd_utstyr[maaned]
                + tid_drift_person[maaned] / 1000 * varmetilskudd_person[maaned]
                + spesifikk_gjsnitt_varmetilskudd_fra_vifter
                / 1000
                * statistics.mean(
                    [(ventilasjonsvarmetap_timer_i_drift), mean_timer_per_maaned]
                )
            ) * self.areal_oppv

        # NS3031 - Varmettilskudd
        varmetilskudd = {}
        for maaned in maaneder:
            varmetilskudd[maaned] = (
                varmetilskudd_fra_sol_totalt[maaned] + internt_varmetilskudd[maaned]
            )

        # Timer utenfor driftstid for oppvarming
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

        # NS3031 - Varmetransmisjonstap gjennom konstruksjoner mot det fri, HD - Totalt, HD
        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Arealkorreksjon for bolig, på spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        arealkorreksjon_tilluft_mekanisk_ventilasjon = (
            self.luftmengde_spesifikk_tilluft
            if self.ForretningsBygg
            else arealkorreksjonfaktor_for_bolig
        )

        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Arealkorreksjon for bolig, på spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        arealkoreksjon_avtrekksluftmengde_mekanisk_ventilasjon = (
            (self.luftmengde_spesifikk_avtrekksluft)
            if self.ForretningsBygg
            else arealkorreksjonfaktor_for_bolig
        )

        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Korreksjon for luftmengde = 0, på spesifikk tilluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        arealkorreksjon_luftmengde0_tilluft_mekanisk_ventilasjon = (
            self.luftmengde_spesifikk_tilluft
            if (self.luftmengde_spesifikk_tilluft) == 0
            else arealkorreksjon_tilluft_mekanisk_ventilasjon
        )

        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Korreksjon for luftmengde = 0, på spesifikk avtrekksluftsmengde i det mekaniske ventilasjonsanlegget (m3/(h m2))
        arealkorreksjon_luftmengde0_avtrekksluftmengde_mekanisk_ventilasjon = (
            self.luftmengde_spesifikk_avtrekksluft
            if (self.luftmengde_spesifikk_avtrekksluft) == 0
            else arealkoreksjon_avtrekksluftmengde_mekanisk_ventilasjon
        )

        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Oppvarmet luftvolum (Nettovolum av en bygnig beregnet innenfor dens innvendige, omsluttende flater)§
        oppvarmet_luftvolum = (self.areal_oppv) * (self.etasjehoyde_innvendig)

        # NS3031 - Infiltrasjonsvarmetap, Hinf (6.1.1.1.5) - Luftskifte for infiltrasjon
        luftskifte_for_infiltrasjon = (
            (self.lekkasjetall) * (self.terrengskjermingskoeff_e)
        ) / (
            1
            + ((self.terrengskjermingskoeff_f) / (self.terrengskjermingskoeff_e))
            * (
                (
                    (
                        self.areal_oppv
                        * arealkorreksjon_luftmengde0_tilluft_mekanisk_ventilasjon
                    )
                    - (
                        self.areal_oppv
                        * arealkorreksjon_luftmengde0_avtrekksluftmengde_mekanisk_ventilasjon
                    )
                )
                / (oppvarmet_luftvolum * (self.lekkasjetall))
            )
            ** 2
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for gulvet, dt
        varmetap_mot_grunn_tykkelse_gulv_dt = (self.tykkelse_grunnmur) + (
            self.varmekonduktivitet_grunn
        ) / (self.U_gulvkonstruksjon)

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for kantisolasjon, d'
        varmetap_mot_grunn_tykkelse_kantisolasjon_d = (self.kantisol_tykkelse) * (
            (self.varmekonduktivitet_grunn) / (self.varmekonduktivitet_kantisol) - 1
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Ekvivalent tykkelse for kjellerveggene, dw
        varmetap_mot_grunn_tykkelse_kjellervegg_dw = (self.varmekonduktivitet_grunn) / (
            self.U_kjellerveggskonstruksjon
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Lineær varmegjennomgangs-koeffisient, horisontal kantisolasjon
        linear_varmegjennomgangs_koeff_horisontal_kantisolasjon = -(
            (self.varmekonduktivitet_grunn) / math.pi
        ) * (
            math.log(
                (self.kantisol_horisontal_dybde) / varmetap_mot_grunn_tykkelse_gulv_dt
                + 1
            )
            - math.log(
                (self.kantisol_horisontal_dybde)
                / (
                    varmetap_mot_grunn_tykkelse_gulv_dt
                    + varmetap_mot_grunn_tykkelse_kantisolasjon_d
                )
                + 1
            )
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Lineær varmegjennomgangs-koeffisient, vertikal kantisolasjon
        linear_varmegjennomgangs_koeff_vertikal_kantisolasjon = -(
            (self.varmekonduktivitet_grunn) / math.pi
        ) * (
            math.log(
                2
                * (self.kantisol_vertikal_bredde)
                / varmetap_mot_grunn_tykkelse_gulv_dt
                + 1
            )
            - math.log(
                2
                * (self.kantisol_vertikal_bredde)
                / (
                    varmetap_mot_grunn_tykkelse_gulv_dt
                    + varmetap_mot_grunn_tykkelse_kantisolasjon_d
                )
                + 1
            )
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Karakteristisk dimensjon for gulvet, B'
        karakteristisk_dimensjon_gulv_b = (self.areal_gulv_kjeller) / (
            0.5 * (self.omkrets_gulv)
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Vegg mot grunn, Ubw
        varmetap_vegg_mot_grunn_ubw = (
            2
            * (self.varmekonduktivitet_grunn)
            / (math.pi * (self.oppfyllingshoyde_kjellervegg))
            * (
                1
                + (
                    (0.5 * varmetap_mot_grunn_tykkelse_gulv_dt)
                    / (
                        varmetap_mot_grunn_tykkelse_gulv_dt
                        + (self.oppfyllingshoyde_kjellervegg)
                    )
                )
            )
            * math.log(
                (self.oppfyllingshoyde_kjellervegg)
                / varmetap_mot_grunn_tykkelse_kjellervegg_dw
                + 1
            )
        )

        ## NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For gulv mot grunnen, vertikal kantisolasjon (D' = D)
        varmetap_gulv_mot_grunn_vertikal_dynamisk_varmetransportkoeff_hpe = (
            0.37
            * (self.omkrets_gulv)
            * (self.varmekonduktivitet_grunn)
            * (
                (
                    1
                    - math.exp(
                        -(
                            (self.kantisol_horisontal_dybde)
                            / (self.dybde_periodisk_nedtrengning)
                        )
                    )
                )
                * math.log(
                    (self.dybde_periodisk_nedtrengning)
                    / (
                        varmetap_mot_grunn_tykkelse_gulv_dt
                        + varmetap_mot_grunn_tykkelse_kantisolasjon_d
                    )
                )
                + math.exp(
                    -(
                        (self.kantisol_horisontal_dybde)
                        / (self.dybde_periodisk_nedtrengning)
                    )
                )
                * math.log(
                    (self.dybde_periodisk_nedtrengning)
                    / varmetap_mot_grunn_tykkelse_gulv_dt
                    + 1
                )
            )
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For gulv mot grunnen, horisontal kantisolasjon (D' = 2 x D)
        varmetap_gulv_mot_grunn_horisontal_dynamisk_varmetransportkoeff_hpe = (
            0.37
            * (self.omkrets_gulv)
            * (self.varmekonduktivitet_grunn)
            * (
                (
                    1
                    - math.exp(
                        -(
                            2
                            * (self.kantisol_vertikal_bredde)
                            / (self.dybde_periodisk_nedtrengning)
                        )
                    )
                )
                * math.log(
                    (self.dybde_periodisk_nedtrengning)
                    / (
                        varmetap_mot_grunn_tykkelse_gulv_dt
                        + varmetap_mot_grunn_tykkelse_kantisolasjon_d
                    )
                )
                + math.exp(
                    -(
                        2
                        * (self.kantisol_vertikal_bredde)
                        / (self.dybde_periodisk_nedtrengning)
                    )
                )
                * math.log(
                    (self.dybde_periodisk_nedtrengning)
                    / varmetap_mot_grunn_tykkelse_gulv_dt
                    + 1
                )
            )
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Dynamisk Varmetransportkoeffisient, Hpe] - For vegg og gulv mot grunnen
        varmetap_vegg_og_gulv_mot_grunn_dynamisk_varmetransportkoeff_hpe = (
            0.37
            * (self.omkrets_gulv)
            * (self.varmekonduktivitet_grunn)
            * (
                (
                    1
                    - math.exp(
                        -(
                            (self.oppfyllingshoyde_kjellervegg)
                            / (self.dybde_periodisk_nedtrengning)
                        )
                    )
                )
                * math.log(
                    (self.dybde_periodisk_nedtrengning)
                    / varmetap_mot_grunn_tykkelse_kjellervegg_dw
                    + 1
                )
                + math.exp(
                    -(
                        (self.oppfyllingshoyde_kjellervegg)
                        / (self.dybde_periodisk_nedtrengning)
                    )
                )
                * math.log(
                    (self.dybde_periodisk_nedtrengning)
                    / varmetap_mot_grunn_tykkelse_gulv_dt
                    + 1
                )
            )
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ug (Hvis B'<dt + 0,5*z)
        varmetap_gulv_mot_grunn_qg_ug_b_lt_dt = (
            2
            * (self.varmekonduktivitet_grunn)
            / (
                math.pi * karakteristisk_dimensjon_gulv_b
                + varmetap_mot_grunn_tykkelse_gulv_dt
                * 0.5
                * (self.oppfyllingshoyde_kjellervegg)
            )
            * math.log(
                (math.pi * karakteristisk_dimensjon_gulv_b)
                / (
                    varmetap_mot_grunn_tykkelse_gulv_dt
                    + 0.5 * (self.oppfyllingshoyde_kjellervegg)
                )
                + 1
            )
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) - Gulv mot grunn, Ug (Hvis B'>dt + 0,5*z)
        varmetap_gulv_mot_grunn_qg_ug_b_bt_dt = (self.varmekonduktivitet_grunn) / (
            0.457 * karakteristisk_dimensjon_gulv_b
            + varmetap_mot_grunn_tykkelse_gulv_dt
            + 0.5 * (self.oppfyllingshoyde_kjellervegg)
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Stasjonær varmetransportkoeffisient, Hg] - For gulv mot grunnen
        varmetap_gulv_mot_grunn_stasjonar_varmetrans_koeff_hg = (
            varmetap_gulv_mot_grunn_qg_ug_b_lt_dt
            if karakteristisk_dimensjon_gulv_b
            > varmetap_mot_grunn_tykkelse_gulv_dt
            + 0.5 * (self.oppfyllingshoyde_kjellervegg)
            else varmetap_gulv_mot_grunn_qg_ug_b_bt_dt
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3) [Stasjonær varmetransportkoeffisient, Hg] - For vegg og gulv mot grunnen
        varmetap_vegg_mot_grunn_stasjonar_varmetrans_koeff_hg = (
            varmetap_gulv_mot_grunn_stasjonar_varmetrans_koeff_hg
            * (self.areal_gulv_kjeller)
            + (self.oppfyllingshoyde_kjellervegg)
            * (self.omkrets_gulv)
            * varmetap_vegg_mot_grunn_ubw
        )

        # NS3031 - Varmetap mot grunnen, Qg (6.1.1.1.3)
        varmetap_mot_grunn = {}
        for maaned in maaneder:
            varmetap_mot_grunn[maaned] = tid[maaned] * (
                (
                    varmetap_gulv_mot_grunn_stasjonar_varmetrans_koeff_hg
                    * (self.areal_gulv_kjeller)
                    + linear_varmegjennomgangs_koeff_horisontal_kantisolasjon
                    * (self.omkrets_gulv)
                    if (self.faseforskjell_utetemp_varmetap) == 2
                    else varmetap_vegg_mot_grunn_stasjonar_varmetrans_koeff_hg
                )
                * ((self.aarsmiddeltemp_inne) - (self.aarsmiddeltemp_ute))
                + (
                    max(
                        [
                            varmetap_gulv_mot_grunn_vertikal_dynamisk_varmetransportkoeff_hpe,
                            varmetap_gulv_mot_grunn_horisontal_dynamisk_varmetransportkoeff_hpe,
                        ]
                    )
                    if (self.faseforskjell_utetemp_varmetap) == 2
                    else varmetap_vegg_og_gulv_mot_grunn_dynamisk_varmetransportkoeff_hpe
                )
                * (self.temp_amplitudevar)
                * math.cos(
                    2
                    * math.pi
                    * (
                        maaned_nummer[maaned]
                        - 1
                        - (self.faseforskjell_utetemp_varmetap)
                    )
                    / 12
                )
            )

        # (Varmetapstall) - Varmetap mot grunnen, et helt år
        varmetapstall_mot_grunnen_aar = sum(varmetap_mot_grunn.values())

        #  NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU - Det regnes ikke tillegg for kuldebro mot uoppvarmet rom
        varmetransmisjonstap_uppvarmede_soner = 0

        # NS3031* - Varmetransmisjonstap til uoppvarmede soner, HU -
        varmetransmisjonstap_uoppvarmede_soner_hu = (self.U_mot_uoppvarmet_sone) * (
            self.areal_mot_uoppvarmet
        )

        # NS3031 - Varmetransmisjonstap til uoppvarmede soner, HU - Totalt, HU
        varmetransmisjonstap_uoppvarmede_soner_hu_total = (
            self.varmetapsfaktor_uoppv
        ) * (
            varmetransmisjonstap_uoppvarmede_soner_hu
            + varmetransmisjonstap_uppvarmede_soner
        )

        # (Varmetapstall) - Varmetransmisjonstap, HD
        varmetapstall_hd = (
            (self.U_tak) * (self.areal_tak)
            + (self.U_vegg_oest) * (self.areal_vegg_oest)
            + (self.U_vegg_vest) * (self.areal_vegg_vest)
            + (self.U_vegg_soer) * (self.areal_vegg_soer)
            + (self.U_vegg_nord) * (self.areal_vegg_nord)
            + (self.U_gulv_mot_det_fri) * (self.areal_gulv_mot_det_fri)
            + (self.U_vindu_oest) * (self.areal_vindu_oest)
            + (self.U_vindu_vest) * (self.areal_vindu_vest)
            + (self.U_vindu_soer) * (self.areal_vindu_soer)
            + (self.U_vindu_nord) * (self.areal_vindu_nord)
            # TODO check: This will always be 0 as no windows will be placed on the roof according to the Wizard
            + (self.U_vindu_tak) * (self.areal_vindu_tak)
            + (self.U_dor) * (self.areal_dor)
        ) + (self.areal_oppv) * (self.kuldebro_normalisert)

        # (Varmetapstall) - Infiltrasjonsvarmetap, Hinf
        varmetapstall_infiltrasjonsvarmetap_hinf = (
            (self.varmekapasitet_luft)
            * luftskifte_for_infiltrasjon
            * oppvarmet_luftvolum
        )

        # NS3031* - Varmetap
        varmetap = {}
        for maaned in maaneder:
            _varmetap = (
                (
                    varmetapstall_hd
                    + varmetransmisjonstap_uoppvarmede_soner_hu_total
                    + ventilasjonsvarmetap_totalt
                    + varmetapstall_infiltrasjonsvarmetap_hinf
                )
                * (self.temp_settpunkt_oppvarming - utetemp[maaned])
                * tid_drift_oppv_belysn_utstyr[maaned]
                / 1000
                + (
                    varmetapstall_hd
                    + varmetransmisjonstap_uoppvarmede_soner_hu_total
                    + ventilasjonsvarmetap_totalt
                    + varmetapstall_infiltrasjonsvarmetap_hinf
                )
                * (self.temp_settpunkt_oppvarming_natt - utetemp[maaned])
                * (timer[maaned] - tid_drift_oppv_belysn_utstyr[maaned])
                / 1000
                + varmetap_mot_grunn[maaned]
            )
            # Varmetap default 0.1 if negative
            varmetap[maaned] = _varmetap if _varmetap >= 0 else 0.1

        # NS3031 - Oppvarmingsbehov - Bygningens varmetransportkoeffisient [W/K]
        varmetransportkoeff_wk = (
            varmetapstall_hd
            + varmetransmisjonstap_uoppvarmede_soner_hu_total
            + ventilasjonsvarmetap_totalt
            + varmetapstall_infiltrasjonsvarmetap_hinf
            + (
                varmetap_gulv_mot_grunn_stasjonar_varmetrans_koeff_hg
                * (self.areal_gulv_kjeller)
                + linear_varmegjennomgangs_koeff_horisontal_kantisolasjon
                * (self.omkrets_gulv)
                if (self.faseforskjell_utetemp_varmetap) == 2
                else varmetap_vegg_mot_grunn_stasjonar_varmetrans_koeff_hg
            )
        )

        # NS3031 - Oppvarmingsbehov - Varmetreghet, aH
        varmetreghet_ah = (
            (self.norm_varmekap) * self.areal_oppv / varmetransportkoeff_wk
        )

        # NS3031 - Oppvarmingsbehov - Tidskonstant, τ
        oppvarmingsbehov_tidskonstant = 1 + varmetreghet_ah / 16

        oppvarmingsbehov = {}
        for maaned in maaneder:
            # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yH,i - januar
            _varmetilskudd_vs_varmetap = varmetilskudd[maaned] / varmetap[maaned]

            # NS3031 - Utnyttingsfaktor for måneden
            _utnyttingsfaktor = (
                1 / _varmetilskudd_vs_varmetap
                if _varmetilskudd_vs_varmetap < 0
                else oppvarmingsbehov_tidskonstant / (oppvarmingsbehov_tidskonstant + 1)
                if _varmetilskudd_vs_varmetap == 1
                else (1 - _varmetilskudd_vs_varmetap ** oppvarmingsbehov_tidskonstant)
                / (
                    1
                    - _varmetilskudd_vs_varmetap ** (oppvarmingsbehov_tidskonstant + 1)
                )
            )

            # NS3031 - Oppvarmingsbehov
            oppvarmingsbehov[maaned] = (
                varmetap[maaned] - _utnyttingsfaktor * varmetilskudd[maaned]
            )

        # # - Energipost (1a) (Energibehov [kWh/år]) - Romoppvarming
        Romoppvarming = sum(oppvarmingsbehov.values())

        ### energipost 1-b
        # 6.1.7 -> Trond Ivar Bøhn: OBS! Denne referansen finnes ikke lenger i NS 3031:2014. Det er nå slik at temperaturvirkningsgraden korrigeres for frostsikringen, ref. NS 3031:2014 tillegg H.9. Men om dette skal gjøres om på, må biblioteksverdier for varmegjenvinning vurderes på nytt

        # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [°C] - Minste utetemperatur som ikke innebærer frostsikring av varmegjenvinneren, θ1,min
        energibehov_frostsikring_C = (self.temp_avtrekk) - (
            (self.temp_avtrekk) - (self.frostsikringstemperatur)
        ) / (self.tempvirkningsgrad_varmegjenvinner + 0.001)

        energibehov_frostsikring = {}
        for maaned in maaneder:
            # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7 - Totalt, E_defrost) [kWh] - januar
            energibehov_frostsikring[maaned] = (
                0.33
                * ventilasjonsvarmetap_gjennomsnittlig_ventilasjonsmengde
                * tid[maaned]
                * max([0, energibehov_frostsikring_C - utetemp[maaned]])
            )

        # NS3031 - Energibehov for frostsikring av varmegjenvinner (6.1.7) - Totalt, Edefrost
        # # - Energipost (1b) (Energibehov [kWh/år]) Trond Ivar Bøhn: OBS! Dette ser ikke ut til å være ventilasjonsoppvarming, men kun frostsikring. Ventilasjonsvarmetapet inngår derimot i posten romoppvarming! Spm til NVE: Brukes disse enkeltpostene for netto energibehov til noe i Enova-modulen? I så fall burde vel dette ordnes opp i?!
        Ventilasjonsvarme = sum(energibehov_frostsikring.values())

        ### energipost 3-b

        # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls]
        kjolebehov = {}
        for maaned in maaneder:
            kjolebehov[maaned] = (
                varmetapstall_hd
                + varmetransmisjonstap_uoppvarmede_soner_hu_total
                + ventilasjonsvarmetap_totalt
                + varmetapstall_infiltrasjonsvarmetap_hinf
            ) * (self.temp_settpunkt_kjoeling - utetemp[maaned]) * tid[
                maaned
            ] + varmetap_mot_grunn[
                maaned
            ]
        # NS3031 - "Kjølebehov" (beregnet fra varmetap med setpunkttemp. for kjøling) (6.1.1.1) [Varmetap, QC,ls] - Total
        kjolebehov_totalt = sum(kjolebehov.values())

        # NS3031 - Utnyttingsfaktor
        utnyttingsfaktor = {}
        energibehov_kjoling = {}
        for maaned in maaneder:
            # NS3031 - Utnyttingsfaktor, delregning - Forhold mellom varmetilskudd og varmetap, yC,i - januar
            _varmetilskudd = varmetilskudd[maaned] / kjolebehov[maaned]
            utnyttingsfaktor[maaned] = (
                1 / (_varmetilskudd)
                if (_varmetilskudd) < 0
                else (
                    oppvarmingsbehov_tidskonstant / (oppvarmingsbehov_tidskonstant + 1)
                    if (_varmetilskudd) == 1
                    else (1 - (_varmetilskudd) ** oppvarmingsbehov_tidskonstant)
                    / (1 - (_varmetilskudd) ** (oppvarmingsbehov_tidskonstant + 1))
                )
            )

            # NS3031 - Energibehov for kjøling (6.1.2) [kWh]
            energibehov_kjoling[maaned] = (
                0
                if varmetilskudd[maaned] - utnyttingsfaktor[maaned] * kjolebehov[maaned]
                < 0
                else varmetilskudd[maaned]
                - utnyttingsfaktor[maaned] * kjolebehov[maaned]
            ) * self.areal_avkjoelt_andel

        energibehov_kjoling_total = sum(energibehov_kjoling.values())

        # NS3031* - Energibehov, pumper (Oppvarming) - Varmebehov
        pumper_oppvarming_varmebehov = (Romoppvarming) / 8760 * 1000

        # NS3031* - Energibehov, pumper (Oppvarming) - Sirkulert vannmengde gjennom pumpen
        pumper_oppvarming_sirkulert_vannmengde = (
            pumper_oppvarming_varmebehov
            / (
                (self.temp_differanse_veskekrets_oppvarming)
                * (self.varmekapasitet_vann)
                * (self.densitet_vann)
            )
            * 1000
        )

        # NS3031* - Energibehov, pumper (Oppvarming) - Totalt, Ep
        energibehov_pumper_totalt = (
            pumper_oppvarming_sirkulert_vannmengde
            * (self.pumpeeffekt_spesifikk_oppv)
            * (self.tid_drift_pumpe_oppv)
        )

        # NS3031* - Energibehov, pumper (Kjøling) - Kjølebehov
        pumper_kjolebehov = energibehov_kjoling_total / 8760 * 1000

        # NS3031* - Energibehov, pumper (Kjøling) - Sirkulert vannmengde gjennom pumpen
        pumper_kjoling_sirkulert_vannmengde = (
            pumper_kjolebehov
            / (
                (self.temp_differanse_veskekrets_kjoling)
                * (self.varmekapasitet_kuldebaerer)
                * (self.densitet_kuldebaerer)
            )
            * 1000
        )

        # NS3031* - Energibehov, pumper (Kjøling) - Totalt, Ep
        pumper_kjoling_totalt = (
            pumper_kjoling_sirkulert_vannmengde
            * (self.pumpeeffekt_spesifikk_kjoling)
            * (self.tid_drift_pumpe_kjoling)
        )

        # NS3031 - Energibehov for vifter og pumper (Pumper) - Totalt, Ep
        # # - Energipost (3b) (Energibehov [kWh/år]) - Pumper
        Pumper = energibehov_pumper_totalt + pumper_kjoling_totalt

        ### energipost 6
        # # - Energipost (6) (Energibehov [kWh/år]) - Kjoeling
        Kjoeling = energibehov_kjoling_total

        Totalt_netto_energibehov = (
            Romoppvarming
            + Ventilasjonsvarme
            + Varmtvann
            + Vifter
            + Pumper
            + Belysning
            + Teknisk_utstyr
            + Kjoeling
        )

        # energivare 1

        # NS3031 - Andel av energibehov - Andel av netto energibehov for romoppvarming og ventilasjonsvarme (Trond Ivar: Egentlig burde man vel også delt opp romoppvarming og ventilasjonsvarme, for å benytte (om ønskelig) forskjellig andel av netto energibehov.)
        # TODO: Denne er ikke i bruk, kan fjernes
        # J307 = math.nan

        # NS3031 - Andel av energibehov - Andel av netto energibehov for oppvarming av tappevann
        # TODO: Denne er ikke i bruk, kan fjernes
        # J311 = math.nan

        # NS3031 - Systemvirkningsgrader - Årsgjennomsnittlig
        # TODO: Denner er ikke i bruk, kan fjernes
        # Q305 = math.nan

        # NS3031 - Systemvirkningsgrader - Systemvirkningsgrader for romoppvarming og ventilasjonsvarme
        # TODO: Denner er ikke i bruk, kan fjernes
        # Q307 = np.nan

        # NS3031 - Systemvirkningsgrader - Systemvirkningsgrader for oppvarming av tappevann
        # TODO: Denner er ikke i bruk, kan fjernes
        # Q311 = np.nan

        # NS3031 - Systemvirkningsgrader - Netto el-spesifikt forbruk
        netto_el_spesifikt_forbruk = (
            Vifter
            + (Pumper)
            + (self.energibehov_belysning) * (self.areal_oppv)
            + (self.energibehov_utstyr) * (self.areal_oppv)
        )

        # NS3031 - Systemvirkningsgrader - Levert elektrisitet til elektriske varmesystemer
        levert_el_til_varmesystemer = (Romoppvarming + Ventilasjonsvarme) * (
            self.el_er_andel_energi_oppv_ventilasjon
        ) / (self.systemvirkningsgrad_elektrisk_oppv_ventilasjon) + (
            (self.energibehov_tappevann) * (self.areal_oppv)
        ) * (
            self.el_er_andel_energi_tappevann_varme
        ) / (
            self.systemvirkningsgrad_elektrisk_tappevann_varme
        )

        # NS3031 - Systemvirkningsgrader - Levert elektrisitet til varmepumpesystemer
        levert_el_varmepumpesystemer = (Romoppvarming + Ventilasjonsvarme) * (
            self.el_hp_andel_energi_oppv_ventilasjon
        ) / (self.systemvirkningsgrad_varmepumpeanlegg_oppv_ventilasjon) + (
            (self.energibehov_tappevann) * (self.areal_oppv)
        ) * (
            self.el_hp_andel_energi_tappevann_varme
        ) / (
            self.systemvirkningsgrad_varmepumpeanlegg_tappevann_varme
        )

        # NS3031 - Systemvirkningsgrader - Levert elektrisitet til termiske solenergisystemer
        levert_elektrisitet_termisk_solenergi = (Romoppvarming + Ventilasjonsvarme) * (
            self.el_Tsol_andel_energi_oppv_ventilasjon
        ) / (self.systemvirkningsgrad_solfanger_termisk_oppv_ventilasjon) + (
            (self.energibehov_tappevann) * (self.areal_oppv)
        ) * (
            self.el_Tsol_andel_energi_tappevann_varme
        ) / (
            self.systemvirkningsgrad_solfanger_termisk_tappevann_varme
        )

        # NS3031 - Systemvirkningsgrader - Levert elektrisitet til kjølesystemer
        levert_el_kjolseystemer = energibehov_kjoling_total / (
            self.effektfaktor_kjoeleanlegg
        )

        # NS3031 - Systemvirkningsgrader - Levert elektrisitet til el-spesifikt forbruk
        levert_el_spesifikt_forbruk = netto_el_spesifikt_forbruk * (
            1 - (self.el_solcelle_andel_el_spesifikt_forbruk)
        ) + netto_el_spesifikt_forbruk * (
            self.el_solcelle_andel_el_spesifikt_forbruk
        ) / (
            self.systemvirkningsgrad_solcelle
        )

        # NS3031 - Systemvirkningsgrader - Levert elektrisitet
        Elektrisitet = (
            levert_el_spesifikt_forbruk
            + levert_el_til_varmesystemer
            + levert_el_varmepumpesystemer
            + levert_elektrisitet_termisk_solenergi
            + levert_el_kjolseystemer
        )

        # energivare 2
        # NS3031 - Beregning av behov for levert olje - Levert energi i form av olje
        # # - Energivare (2) (Levert energi [kWh/år]) - Olje
        Olje = (Romoppvarming + Ventilasjonsvarme) * (
            self.olje_andel_energi_oppv_ventilasjon
        ) / (self.systemvirkningsgrad_olje_oppv_ventilasjon) + (
            (self.energibehov_tappevann) * (self.areal_oppv)
        ) * (
            self.olje_andel_energi_tappevann_varme
        ) / (
            self.systemvirkningsgrad_olje_tappevann_varme
        )

        # energivare 3
        # NS3031 - Beregning av behov for levert gass - Levert energi i form av gass
        # # - Energivare (3) (Levert energi [kWh/år]) - Gass
        Gass = (Romoppvarming + Ventilasjonsvarme) * (
            self.gass_andel_energi_oppv_ventilasjon
        ) / (self.systemvirkningsgrad_gass_oppv_ventilasjon) + (
            (self.energibehov_tappevann) * (self.areal_oppv)
        ) * (
            self.gass_andel_energi_tappevann_varme
        ) / (
            self.systemvirkningsgrad_gass_tappevann_varme
        )

        # energivare 4
        # NS3031 - Beregning av behov for levert fjernvarme - Levert energi i form av fjernvarme
        # # - Energivare (4) (Levert energi [kWh/år]) - Fjernvarme
        fjernvarme = (Romoppvarming + Ventilasjonsvarme) * (
            self.fjernvarme_andel_energi_oppv_ventilasjon
        ) / (self.systemvirkningsgrad_fjernvarme_oppv_ventilasjon) + (
            (self.energibehov_tappevann) * (self.areal_oppv)
        ) * (
            self.fjernvarme_andel_energi_tappevann_varme
        ) / (
            self.systemvirkningsgrad_fjernvarme_tappevann
        )

        # energivare 5
        # NS3031 - Beregning av behov for levert biobrensel - Levert energi i form av biobrensel
        # # - Energivare (5) (Levert energi [kWh/år]) - Biobrensel
        Biobrensel = (Romoppvarming + Ventilasjonsvarme) * (
            self.bio_andel_energi_oppv_ventilasjon
        ) / (self.systemvirkningsgrad_bio_oppv_ventilasjon) + (
            (self.energibehov_tappevann) * (self.areal_oppv)
        ) * (
            self.bio_andel_energi_tappevann_varme
        ) / (
            self.systemvirkningsgrad_bio_tappevann
        )

        # energivare 6
        # NS3031 - Beregning av behov for levert andre energivarer - Levert energi i form av andre energivarer
        # # - Energivare (6) (Levert energi [kWh/år]) - Andre energivarer
        Annen_energivare = (Romoppvarming + Ventilasjonsvarme) * (
            self.annet_andel_energi_oppv_ventilasjon
        ) / (self.systemvirkningsgrad_annet_oppv_ventilasjon) + (
            (self.energibehov_tappevann) * (self.areal_oppv)
        ) * (
            self.annet_andel_energi_tappevann_varme
        ) / (
            self.systemvirkningsgrad_annet_tappevann
        )

        # Primaerenergi
        # NS3031 (8.1) - Primærenergibehov - Elektrisitet (kWh)
        primaerenergibehov_el = Elektrisitet * (self.Primaerenergi_faktor_el)

        # NS3031 (8.1) - Primærenergibehov - Olje (kWh)
        primaerenergibehov_olje = Olje * (self.Primaerenergi_faktor_olje)

        # NS3031 (8.1) - Primærenergibehov - Gass (kWh)
        primaerenergibehov_gass = Gass * (self.Primaerenergi_faktor_gass)

        # NS3031 (8.1) - Primærenergibehov - Fjernvarme (kWh)
        primaerenergibehov_fjernvarme = fjernvarme * (
            self.Primaerenergi_faktor_fjernvarme
        )

        # NS3031 (8.1) - Primærenergibehov - Biobrensel (kWh)
        primaerenergibehov_biobrensel = Biobrensel * (self.Primaerenergi_faktor_bio)

        # NS3031 (8.1) - Primærenergibehov - Andre energivarer (kWh)
        primaerenergibehov_andre_energivarer = Annen_energivare * (
            self.Primaerenergi_faktor_annet
        )

        # Co2-utslipp
        # NS3031 (8.2) - CO2-utslipp - Utslipp fra elektrisitet
        co2_utslipp_el = Elektrisitet * (self.CO2_faktor_el)

        # NS3031 (8.2) - CO2-utslipp - Utslipp fra olje
        co2_utslipp_olje = Olje * (self.CO2_faktor_olje)

        # NS3031 (8.2) - CO2-utslipp - Utslipp fra gass
        co2_utslipp_gass = Gass * (self.CO2_faktor_gass)

        # NS3031 (8.2) - CO2-utslipp - Utslipp fra fjernvarme
        co2_utslipp_fjernvarme = fjernvarme * (self.CO2_faktor_fjernvarme)

        # NS3031 (8.2) - CO2-utslipp - Utslipp fra biobrensel
        co2_utslipp_biobrensel = Biobrensel * (self.CO2_faktor_bio)

        # NS3031 (8.2) - CO2-utslipp - Utslipp fra andre energivarer
        co2_utslipp_annen_energivare = Annen_energivare * (self.CO2_faktor_annet)

        # Energi-kostnader
        # NS3031 (8.3) - Energikostnader - Utslipp fra elektrisitet
        energikostnader_utslipp_el = Elektrisitet * (self.Energipris_el)

        # NS3031 (8.3) - Energikostnader - Utslipp fra olje
        energikostnader_utslipp_olje = Olje * (self.Energipris_olje)

        # NS3031 (8.3) - Energikostnader - Utslipp fra gass
        energikostnader_utslipp_gass = Gass * (self.Energipris_gass)

        # NS3031 (8.3) - Energikostnader - Utslipp fra fjernvarme
        energikostnader_utslipp_fjernvarme = fjernvarme * (self.Energipris_fjernvarme)

        # NS3031 (8.3) - Energikostnader - Utslipp fra biobrensel
        energikostnader_utslipp_biobrensel = Biobrensel * (self.Energipris_bio)

        # NS3031 (8.3) - Energikostnader - Utslipp fra andre energivarer
        energikostnader_utslipp_andre_energivarer = Annen_energivare * (
            self.Energipris_annet
        )

        # Energi-politisk
        # NS3031 (8.4) - Energipolitisk vektet levert energi - Utslipp fra elektrisitet
        energipolitisk_utslipp_el = Elektrisitet * (self.Energipol_vektingsfaktor_el)

        # NS3031 (8.4) - Energipolitisk vektet levert energi - Utslipp fra olje
        energipolitisk_utslipp_olje = Olje * (self.Energipol_vektingsfaktor_olje)

        # NS3031 (8.4) - Energipolitisk vektet levert energi - Utslipp fra gass
        energipolitisk_utslipp_gass = Gass * (self.Energipol_vektingsfaktor_gass)

        # NS3031 (8.4) - Energipolitisk vektet levert energi - Utslipp fra fjernvarme
        energipolitisk_utslipp_fjernvarme = fjernvarme * (
            self.Energipol_vektingsfaktor_fjernvarme
        )

        # NS3031 (8.4) - Energipolitisk vektet levert energi- Utslipp fra biobrensel
        energipolitisk_utslipp_biobrensel = Biobrensel * (
            self.Energipol_vektingsfaktor_bio
        )

        # NS3031 (8.4) - Energipolitisk vektet levert energi - Utslipp fra andre energivarer
        energipolitisk_utslipp_andre_energivarer = Annen_energivare * (
            self.Energipol_vektingsfaktor_annet
        )

        # Energivare - Primærenergi behov [kWh/år]
        Primaerenergi = (
            primaerenergibehov_el
            + primaerenergibehov_olje
            + primaerenergibehov_gass
            + primaerenergibehov_fjernvarme
            + primaerenergibehov_biobrensel
            + primaerenergibehov_andre_energivarer
        )

        # Energivare - CO2-utslipp [kg/år]
        CO2_utslipp = (
            co2_utslipp_el
            + co2_utslipp_olje
            + co2_utslipp_gass
            + co2_utslipp_fjernvarme
            + co2_utslipp_biobrensel
            + co2_utslipp_annen_energivare
        )

        # Energivare - Energi-kostnader [kr/år]
        Energi_kostnader = (
            energikostnader_utslipp_el
            + energikostnader_utslipp_olje
            + energikostnader_utslipp_gass
            + energikostnader_utslipp_fjernvarme
            + energikostnader_utslipp_biobrensel
            + energikostnader_utslipp_andre_energivarer
        )

        # Energivare - Energi-politisk vektet levert energi [kWh/år]
        Energi_politisk = (
            energipolitisk_utslipp_el
            + energipolitisk_utslipp_olje
            + energipolitisk_utslipp_gass
            + energipolitisk_utslipp_fjernvarme
            + energipolitisk_utslipp_biobrensel
            + energipolitisk_utslipp_andre_energivarer
        )

        Totalt_netto_energibehov = (
            Romoppvarming
            + Ventilasjonsvarme
            + Varmtvann
            + Vifter
            + Pumper
            + Belysning
            + Teknisk_utstyr
            + Kjoeling
        )

        Totalt_levert_energi = (
            Elektrisitet + Olje + Gass + fjernvarme + Biobrensel + Annen_energivare
        )

        return Output(
            Romoppvarming,
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
            fjernvarme,
            Biobrensel,
            Annen_energivare,
            Totalt_levert_energi,
            Primaerenergi,
            CO2_utslipp,
            Energi_kostnader,
            Energi_politisk,
        )
