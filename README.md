# About
This is primarily a repository of graphs made using Matplotlib for my 2023-2024 Science Research Project on the Synthesis, Characterization, and Viability of Beta-Cyclodextrin crosslinked PVA Hydrogels. This project was associated with Charles Wright Academy in Tacoma, WA. There is also data collection from other experiments/trials and a collection of hydrogel FTIR spectra that were obtained through a partnership with the University of Puget Sound.

# Procedure
This is a copy of the notes/procedure I created and used in the synthesis and testing of Beta-Cyclodextrin Crosslinked PVA Hydrogels. I am publishing this documentation to the world in the hope that other students may base their procedures on my method. The method I used certainly wasn't perfect, but it worked for me. The data in this repo may come in handy to some researchers, too!  
<br>
A couple of acronyms that are used throughout the procedure:
```
PVA: Polyvinyl Alcohol  
CA: Citric Acid  
B-CD: Beta Cyclodextrin
```

## Synthesis of Gels  
>These may seem redundant, but going to this level of detail helped me be organized and operate more efficiently when working in the lab.

<details>
<summary>PVA + CA Hydrogel (Control)</summary>
  
```
- 15.00g PVA to 90mL dH2O
- Stir at 70-80°C for 3h then at 40-50°C overnight (~18h)
- Place solution under vacuum to remove air bubbles
- Add 10mL of 0.10M CA
- Transfer solution into molds (I used Petri dishes. If I were to do this project again, I would use a silicone/more flexible mold.)
- Place in a 100°C oven for 12h
```

</details>

  
<details>
<summary>PVA/B-CD(4:1) + CA Hydrogel</summary>
  
  ```
  - 15.00g PVA to 90mL dH2O  
  - Add 3.75g B-CD to reach a PVA/B-CD weight ratio of 4:1  
  - Stir at 70-80C for 3h then at 40-50C overnight (~18h)  
  - Placed solution under vacuum to remove air bubbles  
  - Add 10mL of 0.10M CA  
  - Transfer solution into molds  
  - Place in a 100C oven for 12h
  ```
</details>


<details>
<summary>PVA/B-CD(2:1) + CA Hydrogel</summary>
  
  ```
  - 15.00g PVA to 90mL dH2O  
  - Add 7g B-CD to reach a PVA/B-CD weight ratio of 4:1  
  - Stir at 70-80C for 3h then at 40-50C overnight (~18h)  
  - Placed solution under vacuum to remove air bubbles  
  - Add 10mL of 0.10M CA  
  - Transfer solution into molds  
  - Place in a 100C oven for 12h  
  ```
</details>

<details>
<summary>PVA/B-CD(4:1) Hydrogel</summary>
  
  ```
  - Add 15.00g PVA to 100mL dH2O  
  - Add 3.75g B-CD to reach a PVA/B-CD weight ratio of 4:1  
  - Stir at 70-80C for 3h then at 40-50C overnight (~18h)  
  - Placed solution under vacuum to remove air bubbles  
  - Transfer solution into molds  
  - Place in a 100C oven for 12h  
  ```
</details>

## ATR-FTIR 
-  Thank you to Prof. Dan Burgard at the University of Puget Sound for allowing me to use the university's FTIR equipment!
-  FTIR spectra were obtained using a PerkinElmer UATR Two Diamond on a PerkinElmer Spectrum One
-  Unlike Mansur et al., we had to use an ATR attachment due to poor readings in transmittance mode (this may have been due to the thickness of gels, but we did have somewhat thin gels (<1mm)
-  FTIR readings were obtained from swelled hydrogels. Using swelled gels produced cleaner spectra and were more pliable to the force used to press gels into the ATR.

## Swelling Analysis 
- Gels (dried) were cut into smaller pieces and initial weight was recorded<br>
- Gels were placed in dH<sub>2</sub>O (I used cell culture wells) and let sit for 24hrs  <br>
- Excess water was removed from the surface of gels  <br>
- Samples were weighed, and swelling was calculated using the formula $S = \dfrac{(W_f\ -W_0)}{W_0}\cdot100$

<details><summary>Swelling Analysis Graph</summary>
  
![image](https://github.com/sabshr/SciResearchGraphs/assets/168509660/43ead6c6-8811-4d88-ad55-b9ebb00c2b8f)
</details>

  
## Organic Dye Absorbance UV-Vis Assay 
  
### Methylene Blue

~0.02g Methylene Blue (MW 318.85) needs to be added to a 100mL Volumetric Flask with dH<sub>2</sub>O<br>
```
- Actual Weight Used: 0.0202g
- Serial Dilution: 2mL in 100mL (This was a pain to do. Needed in order to get readable results from my spectrophotometer)<br>
- Tested @ 668.5 nm
```
### Congo Red
~0.5g Congo Red (MW 696.665) needs to be added to a 100mL Volumetric Flask with dH<sub>2</sub>O<br>
```
- Actual Weight Used: 0.2339g
- Serial Dilution: 5mL in 100mL
- Tested @ 498.8 nm
```
### Crystal Violet
~0.001g Crystal Violet (MW 401.979) needs to be added to a 100mL Volumetric Flask with H<sub>2</sub>O<br>
```
- Actual Weight Used: 0.0045g
- Serial Dilution: 20mL in 100mL
- Tested @ 590.4 nm
```
### Preparing Standard Curves + Setup
>Prepare 4 solutions of known molarity solutions for each dye - Compare to Beer’s law curve (determine the error between actual molarity and estimated molarity on Beer’s law curve)<br>

>Gels were then placed in a 6-well plate, with wells filled with a 4-6H<sub>2</sub>O dilution of each dye. 3 plates were used, one for each dye. There are hyperlinks to a data visualization on desmos with each sample on this graph. 

| Dilution | [Congo Red Abs. @498.8nm](https://www.desmos.com/calculator/jpirurhp8b) | [Methylene Blue Abs. @668.5nm](https://www.desmos.com/calculator/mpqpil1rlb) | [Crystal Violet Abs. @590.6nm](https://www.desmos.com/calculator/ois8airu3k)|
| -------- | ----------------------- | ---------------------------- | ---------------------------- |
|  2+8H<sub>2</sub>O  |          0.320          |             0.156            |             0.360            | 
|  4+6H<sub>2</sub>O  |          0.627          |             0.376            |             0.738            | 
|  6+4H<sub>2</sub>O  |          0.902          |             0.530            |             1.099            | 
|  8+2H<sub>2</sub>O  |          1.145          |             0.640            |             1.367            | 

<details><summary>Congo Red Calibration Curve in LaTEX</summary>
  
![image](https://github.com/sabshr/SciResearchGraphs/assets/168509660/808dd582-4677-43cc-8539-be121b0cc43f)
</details>

<details><summary>Methylene Blue Calibration Curve in LaTEX</summary>

![image](https://github.com/sabshr/SciResearchGraphs/assets/168509660/7ea4bb0c-e15e-4a57-a0ca-6ff386f6ac0a)
</details>

<details><summary>Crystal Violet Calibration Curve in LaTEX</summary>
  
![image](https://github.com/sabshr/SciResearchGraphs/assets/168509660/937558ba-fe29-4096-9214-7f3df9b16e83)
</details>

### Analyzing Rested Gel Samples
>Absorbance readings were taken after gels sat in dye solution for 24h.<br>

| Sample | Congo Red Abs. @498.8nm | Methylene Blue Abs. @668.5nm | Crystal Violet Abs. @590.6nm |
| ------ | --------------------- | -------------------------- | -------------------------- |
|  No Gel (Control)  |          0.827          |             0.390            |             0.913            | 
|  PVA + CA  |          0.261          |             0.075            |             0.193            | 
|  PVA/B-CD  |          0.178          |             0.098         |             0.149            | 
|  PVA/B-CD(4:1) + CA  |          0.137          |       0.184            |             0.555            | 
|  PVA/B-CD(2:1) + CA  |          0.505          |             0.157            |             0.488            |  
<br>

> Using our Standardized Curves, we can now determine the molarity of each sample:

| Sample | Congo Red Conc. (Mm) | Methylene Blue Conc. (µM) | Crystal Violet Conc. (µM) |
| ------ | --------------------- | -------------------------- | -------------------------- |
|  No Gel (Control)  |          0.094          |             0.006           |             0.011            | 
|  PVA + CA  |          0.025          |             0.006            |             0.001            | 
|  PVA/B-CD  |          0.015          |             0.001         |             0.0003            | 
|  PVA/B-CD(4:1) + CA  |          0.010          |       0.003            |             0.006            | 
|  PVA/B-CD(2:1) + CA  |          0.054          |             0.002            |             0.005            |  

### Weight after 24hrs
>Gels were all initially weighed and cut to be 0.23g<br>

| Sample | Congo Red | Methylene Blue | Crystal Violet |
| ------ | --------- | -------------- | -------------- |
|  PVA + CA  |          0.29          |             0.28           |             0.29            | 
|  PVA/B-CD  |          0.34          |             0.31         |             0.33           | 
|  PVA/B-CD(4:1) + CA  |          0.31         |       0.30            |             0.29           | 
|  PVA/B-CD(2:1) + CA  |          0.33          |             0.31            |             0.31            | 

### Results
- Gels vs No Gel: All gels significantly reduce the absorbance of the dyes compared to no gel, indicating effective dye absorption by the gels.
- PVA + CA: Generally shows good absorption for all dyes, particularly effective for Methylene Blue.
- PVA/B-CD: Shows strong absorption for Congo Red and Crystal Violet but less effective for Methylene Blue compared to PVA + CA.
- For Congo Red: PVA/B-CD(4:1) + CA is most effective.
- For Methylene Blue: Lower ratios (or no ratio) of B-CD (PVA + CA) are more effective.
- For Crystal Violet: PVA/B-CD without CA is most effective.
- The weight increase among Cyclodextrin Hydrogels is pretty consistently above that of PVA + CA



## Metal Ion Absorbance Assay (Complexometric Titration)
>The same 0.01063M EDTA solution was used for all trials
  
| Pb<sup><sup>2+</sup></sup> Solution Standardization |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  Volume Pipetted  |          10.00          |             10.00           |             10.00           | 
|  $\Delta$ V (mL) |          18.55          |             18.53           |             18.46           | 
|  Molarity   |          0.01971865          |             0.01969739        |             0.01962298           |
|  Pb<sup>2+</sup> Standardized Molarity  |          0.0197        |                   |                  |
|  RSD  |        0.26%       |                   |                  | 
|  Lead in 10mL (mg)  |        40.84 ± 0.094      |                   |                  | 
<br>

| PVA + CA [Pb<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V (mL) |          18.23          |             18.26           |             18.22           | 
|  Molarity   |          0.01937849         |             0.01941038         |             0.01936785           |
|  Mean Molarity |  0.0194  |  | | 
|  RSD  |        0.11%       |                   |                  | 
|  Lead in 10mL (mg)  |        40.19 ± 0.043     |                   |                  | 
<br>

| PVA/B-CD [Pb<sup>2+</sup>] |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V (mL)  |          18.39          |             18.47           |             18.4          | 
|  Molarity   |          0.01937849         |             0.01941038         |             0.0195592           |
|  Mean Molarity |  0.0194 |  | | 
|  RSD  |        0.50%       |                   |                  |
|  Lead in 10mL (mg)  |        40.18 ± 0.20     |                   |                  | 
<br>

| PVA/B-CD(4:1) + CA [Pb<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V (mL) |         18.35           |             18.29           |           18.31         | 
|  Molarity   |         0.01950605         |           0.01944227        |          0.01946353          |
|  Mean Molarity |  0.0195 |  | | 
|  RSD  |        0.17%       |                   |                  | 
|  Lead in 10mL (mg)  |        40.40 ± 0.07     |                   |                  | 
<br>

| PVA/B-CD(2:1) + CA [Pb<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V (mL) |          18.29          |            18.28            |             18.13          | 
|  Molarity   |       0.01944227            |          0.01943164        |               0.01927219        |
|  Mean Molarity |  0.0194|  | | 
|  RSD  |        0.49%       |                   |                  | 
|  Lead in 10mL (mg)  |        40.20 ± 0.20     |                   |                  | 
<br>

>Collating data points into a table (this is what is later converted to a graph), we get:

| Pb<sup>2+</sup> in 10mL aliquots (mg) |  |
| ------ | --------- |
|  Control (no gel) |         40.84 ± 0.094          |
|  PVA + CA   |      40.19 ± 0.043           | 
|  PVA/B-CD |   40.18 ± 0.20               | 
|  PVA/B-CD(4:1) + CA  |        40.40 ± 0.07        |
| PVA/B-CD(2:1) + CA  |        40.20 ± 0.20     |    

<details><summary>View Pb<sup>2+</sup> Absorbance Graph</summary>
  
![image](https://github.com/sabshr/SciResearchGraphs/assets/168509660/1162b707-701b-4688-9550-61aa5aa684d3)
</details>


---

| Zn<sup>2+</sup> Solution Standardization |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  Volume Pipetted (these were the only non-10mL values)  |          4.98          |             5.00           |             5.01           | 
|  $\Delta$ V (mL)  |          2.91          |             2.99           |             3.06           | 
|  Molarity   |         0.0062115060241          |         0.00635674           |             0.0064925748503          |
|  Zn<sup>2+</sup> Standardized Molarity  |          0.0064       |                   |                  | 
|  RSD  |        2.21%       |                   |                  | 
|  Zinc in 10mL (mg)  |      4.18 ± 0.09      |                   |                  | 
<br>

| PVA + CA [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V (mL) |          5.82          |           5.91             |            5.89           | 
|  Molarity   |          0.00618666        |             0.00628233       |             0.00626107          |
|  Mean Molarity |  0.0062 |  | | 
|  RSD  |        0.81%       |                   |                  | 
|  Zinc in 10mL (mg)  |    4.05 ± 0.03        |                   |                  | 
<br>

| PVA/B-CD [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V (mL) |           5.62         |           5.71             |           5.93         | 
|  Molarity   |          0.00597406         |             0.00606973        |             0.00630359          |
|  Mean Molarity |  0.0061  | | 
|  RSD  |        2.77%       |                   |                  | 
|  Zinc in 10mL (mg)  |     3.99 ± 0.11       |                   |                  | 
<br>

| PVA/B-CD(2:1) [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V (mL) |          5.84          |           6.00            |         5.98          | 
|  Molarity   |          0.00620792         |             0.006378        |             0.00635674          |
|  Mean Molarity |  0.0063 |  | | 
|  RSD  |        1.47% |                   |                  | 
|  Zinc in 10mL (mg)  |     4.12 ± 0.06       |                   |                  | 
<br>

| PVA/B-CD(4:1) [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V (mL) |            5.99        |           6.00           |          5.99        | 
|  Molarity   |          0.00636737         |             0.006378        |             0.00636737          |
|  Mean Molarity |  0.0064 |  | | 
|  RSD  |        0.10%       |                   |                  | 
|  Zinc in 10mL (mg)  |      4.179 ± 0.004      |                   |                  | 
<br>

>Collating data points into a table (this is what is later converted to a graph), we get:

| Zn<sup>2+</sup> in 10mL aliquots (mg) |  |
| ------ | --------- |
|  Control (no gel) |         4.18 ± 0.09          |
|  PVA + CA   |      4.05 ± 0.03           | 
|  PVA/B-CD |   3.99 ± 0.11               | 
|  PVA/B-CD(4:1) + CA  |        4.12 ± 0.06        |
| PVA/B-CD(2:1) + CA  |       4.179 ± 0.004     |   

<details><summary>View Zn<sup>2+</sup> Absorbance Graph</summary>
  
![image](https://github.com/sabshr/SciResearchGraphs/assets/168509660/dda80ee0-3659-48e9-9067-afa97bb72e06)
</details>

# Bibliography 
(1) Kawano, S.; Kida, T.; Miyawaki, K.; Fukuda, Y.; Kato, E.; Nakano, T.; Akashi, M. Adsorption Capability of Urethane-Crosslinked Heptakis(2,6-Di-O-Methyl)-β-Cyclodextrin Polymers toward Polychlorobiphenyls in Nonpolar Organic Media. Polym J 2015, 47 (6), 443–448. https://doi.org/10.1038/pj.2015.13.<br><br>
(2) Alpha-cyclodextrin, Beta-cyclodextrin, and Gamma-cyclodextrin; Exemption from the Requirement of a Tolerance. Federal Register. https://www.federalregister.gov/documents/2005/07/06/05-13263/alpha-cyclodextrin-beta-cyclodextrin-and-gamma-cyclodextrin-exemption-from-the-requirement-of-a (accessed 2024-05-03).<br><br>
(3) Li, T.; Guo, R.; Zong, Q.; Ling, G. Application of Molecular Docking in Elaborating Molecular Mechanisms and Interactions of Supramolecular Cyclodextrin. Carbohydrate Polymers 2022, 276, 118644. https://doi.org/10.1016/j.carbpol.2021.118644.<br><br>
(4) Pinho, E. Chapter 4 - Cyclodextrins-Based Hydrogel. In Plant and Algal Hydrogels for Drug Delivery and Regenerative Medicine; Giri, T. K., Ghosh, B., Eds.; Woodhead Publishing Series in Biomaterials; Woodhead Publishing, 2021; pp 113–141. https://doi.org/10.1016/B978-0-12-821649-1.00004-0.<br><br>
(5) Mäkelä, M.; Korpela, T.; Laakso, S. Colorimetric Determination of β-Cyclodextrin: Two Assay Modifications Based on Molecular Complexation of Phenolphatalein. Journal of Biochemical and Biophysical Methods 1987, 14 (2), 85–92. https://doi.org/10.1016/0165-022X(87)90043-1.<br><br>
(6) Hernández, R.; Rusa, M.; Rusa, C. C.; López, D.; Mijangos, C.; Tonelli, A. E. Controlling PVA Hydrogels with γ-Cyclodextrin. Macromolecules 2004, 37 (25), 9620–9625. https://doi.org/10.1021/ma048375i.<br><br>
(7) Kawano, S.; Kida, T.; Miyawaki, K.; Noguchi, Y.; Kato, E.; Nakano, T.; Akashi, M. Cyclodextrin Polymers as Highly Effective Adsorbents for Removal and Recovery of Polychlorobiphenyl (PCB) Contaminants in Insulating Oil. Environ. Sci. Technol. 2014, 48 (14), 8094–8100. https://doi.org/10.1021/es501243v.<br><br>
(8) Wacławek, S.; Krawczyk, K.; Silvestri, D.; Padil, V. V. T.; Řezanka, M.; Černík, M.; Jaroniec, M. Cyclodextrin-Based Strategies for Removal of Persistent Organic Pollutants. Advances in Colloid and Interface Science 2022, 310, 102807. https://doi.org/10.1016/j.cis.2022.102807.<br><br>
(9) Liu, J.; Tian, B.; Liu, Y.; Wan, J.-B. Cyclodextrin-Containing Hydrogels: A Review of Preparation Method, Drug Delivery, and Degradation Behavior. International Journal of Molecular Sciences 2021, 22 (24), 13516. https://doi.org/10.3390/ijms222413516.<br><br>
(10) Cid-Samamed, A.; Rakmai, J.; Mejuto, J. C.; Simal-Gandara, J.; Astray, G. Cyclodextrins Inclusion Complex: Preparation Methods, Analytical Techniques and Food Industry Applications. Food Chemistry 2022, 384, 132467. https://doi.org/10.1016/j.foodchem.2022.132467.<br><br>
(11) Figure 1: The structure of the most abundant PBDEs in technical... ResearchGate. https://www.researchgate.net/figure/The-structure-of-the-most-abundant-PBDEs-in-technical-mixtures-and-the-environment_fig1_344114219 (accessed 2024-02-22).<br><br>
(12) Mansur, H. S.; Sadahira, C. M.; Souza, A. N.; Mansur, A. A. P. FTIR Spectroscopy Characterization of Poly (Vinyl Alcohol) Hydrogel with Different Hydrolysis Degree and Chemically Crosslinked with Glutaraldehyde. Materials Science and Engineering: C 2008, 28 (4), 539–548. https://doi.org/10.1016/j.msec.2007.10.088.<br><br>
(13) Kim, G. J.; Yoon, K. J.; Kim, K. O. Glucose-Responsive Poly(Vinyl Alcohol)/β-Cyclodextrin Hydrogel with Glucose Oxidase Immobilization. J Mater Sci 2019, 54 (19), 12806–12817. https://doi.org/10.1007/s10853-019-03805-0.<br><br>
(14) Darban, Z.; Shahabuddin, S.; Gaur, R.; Ahmad, I.; Sridewi, N. Hydrogel-Based Adsorbent Material for the Effective Removal of Heavy Metals from Wastewater: A Comprehensive Review. Gels 2022, 8 (5), 263. https://doi.org/10.3390/gels8050263.<br><br>
(15) Ahmed, E. M. Hydrogel: Preparation, Characterization, and Applications: A Review. J Adv Res 2015, 6 (2), 105–121. https://doi.org/10.1016/j.jare.2013.07.006.<br><br>
(16) Thangprasert, A.; Tansakul, C.; Thuaksubun, N.; Meesane, J. Mimicked Hybrid Hydrogel Based on Gelatin/PVA for Tissue Engineering in Subchondral Bone Interface for Osteoarthritis Surgery. Materials & Design 2019, 183, 108113. https://doi.org/10.1016/j.matdes.2019.108113.<br><br>
(17) Konieczynska, M. D.; Grinstaff, M. W. On-Demand Dissolution of Chemically Cross-Linked Hydrogels. Acc Chem Res 2017, 50 (2), 151–160. https://doi.org/10.1021/acs.accounts.6b00547.<br><br>
(18) Kodavanti, P. R. S.; Loganathan, B. Organohalogen Pollutants and Human Health. In International Encyclopedia of Public Health; 2016. https://doi.org/10.1016/B978-0-12-803678-5.00318-0.<br><br>
(19) Stauffer, S. R.; Peppast, N. A. Poly(Vinyl Alcohol) Hydrogels Prepared by Freezing-Thawing Cyclic Processing. Polymer 1992, 33 (18), 3932–3936. https://doi.org/10.1016/0032-3861(92)90385-A.<br><br>
(20) Xu, L.; Bai, X.; Yang, J.; Li, J.; Xing, J.; Yuan, H.; Xie, J.; Li, J. Preparation and Characterisation of a Gellan Gum-Based Hydrogel Enabling Osteogenesis and Inhibiting Enterococcus Faecalis. International Journal of Biological Macromolecules 2020, 165, 2964–2973. https://doi.org/10.1016/j.ijbiomac.2020.10.083.<br>
(21) Kim, T.-J.; Kim, B.-C.; Lee, H.-S. Production of Cyclodextrin Using Raw Corn Starch without a Pretreatment. Enzyme and Microbial Technology 1997, 20 (7), 506–509. https://doi.org/10.1016/S0141-0229(96)00186-X.<br><br>
(22) Wang, L.-Y.; Wang, M.-J. Removal of Heavy Metal Ions by Poly(Vinyl Alcohol) and Carboxymethyl Cellulose Composite Hydrogels Prepared by a Freeze–Thaw Method. ACS Sustainable Chem. Eng. 2016, 4 (5), 2830–2837. https://doi.org/10.1021/acssuschemeng.6b00336.<br><br>
(23) Saokham, P.; Muankaew, C.; Jansook, P.; Loftsson, T. Solubility of Cyclodextrins and Drug/Cyclodextrin Complexes. Molecules : A Journal of Synthetic Chemistry and Natural Product Chemistry 2018, 23 (5). https://doi.org/10.3390/molecules23051161.<br><br>
(24) Saha, S.; Roy, A.; Roy, K.; Roy, M. N. Study to Explore the Mechanism to Form Inclusion Complexes of β-Cyclodextrin with Vitamin Molecules. Sci Rep 2016, 6 (1), 35764. https://doi.org/10.1038/srep35764.<br><br>




















