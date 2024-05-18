# About
This repository contains graphs created using Matplotlib for my 2023-2024 Science Research Project on the Synthesis, Characterization, and Viability of Beta-Cyclodextrin Crosslinked PVA Hydrogels. This project was conducted at Charles Wright Academy in Tacoma, WA, and includes data collection from various experiments and hydrogel FTIR spectra obtained through a partnership with the University of Puget Sound.

# Procedure
This section details the notes and procedures I followed in the synthesis and testing of Beta-Cyclodextrin Crosslinked PVA Hydrogels. I hope that other students may find this documentation useful for their research. The method described here worked for me, though it may not be perfect. The data provided could also be valuable to other researchers.

**Acronyms:**
- **PVA:** Polyvinyl Alcohol
- **CA:** Citric Acid
- **B-CD:** Beta Cyclodextrin

---

<details>
<summary>Synthesis of Gels</summary>
<br>

These detailed steps helped me stay organized and efficient in the lab.

### PVA + CA Hydrogel (Control)
- 15.00g PVA to 90mL dH2O
- Stir at 70-80°C for 3 hours, then at 40-50°C overnight (~18 hours)
- Place solution under vacuum to remove air bubbles
- Add 10mL of 0.10M CA
- Transfer solution into molds (Petri dishes recommended; silicone molds could be better)
- Place in a 100°C oven for 12 hours

### PVA/B-CD (4:1) + CA Hydrogel
- 15.00g PVA to 90mL dH2O
- Add 3.75g B-CD to achieve a PVA/B-CD weight ratio of 4:1
- Stir at 70-80°C for 3 hours, then at 40-50°C overnight (~18 hours)
- Place solution under vacuum to remove air bubbles
- Add 10mL of 0.10M CA
- Transfer solution into molds
- Place in a 100°C oven for 12 hours

### PVA/B-CD (2:1) + CA Hydrogel
- 15.00g PVA to 90mL dH2O
- Add 7g B-CD to achieve a PVA/B-CD weight ratio of 2:1
- Stir at 70-80°C for 3 hours, then at 40-50°C overnight (~18 hours)
- Place solution under vacuum to remove air bubbles
- Add 10mL of 0.10M CA
- Transfer solution into molds
- Place in a 100°C oven for 12 hours

### PVA/B-CD (4:1) Hydrogel
- 15.00g PVA to 100mL dH2O
- Add 3.75g B-CD to achieve a PVA/B-CD weight ratio of 4:1
- Stir at 70-80°C for 3 hours, then at 40-50°C overnight (~18 hours)
- Place solution under vacuum to remove air bubbles
- Transfer solution into molds
- Place in a 100°C oven for 12 hours

</details>

<details>
<summary>Swelling Analysis</summary>
<br>

- Cut each gel into smaller pieces and record the weight of dried gels.
- Place gels in dH2O (I used cell culture wells) and let sit for 24 hours.
- Dry off excess water from the surface.
- Weigh, then calculate swelling using the formula: 

  \( S = \dfrac{(W_f - W_0)}{W_0} \cdot 100 \)

</details>

<details>
<summary>Organic Dye Absorbance UV-Vis Assay</summary>
<br>

### Methylene Blue
- ~0.02g Methylene Blue (MW 318.85) added to a 100mL Volumetric Flask with dH2O
  - Actual Weight Used: 0.0202g
  - Serial Dilution: 2mL in 100mL
  - Tested @ 668.5 nm

### Congo Red
- ~0.5g Congo Red (MW 696.665) added to a 100mL Volumetric Flask with dH2O
  - Actual Weight Used: 0.2339g
  - Serial Dilution: 5mL in 100mL
  - Tested @ 498.8 nm

### Crystal Violet
- ~0.001g Crystal Violet (MW 401.979) added to a 100mL Volumetric Flask with H2O
  - Actual Weight Used: 0.0045g
  - Serial Dilution: 20mL in 100mL
  - Tested @ 590.4 nm

### Preparing Standard Curves
Prepare 4 solutions of known molarity for each dye and compare to Beer’s law curve.

| Dilution | Congo Red Abs. @498.8nm | Methylene Blue Abs. @668.5nm | Crystal Violet Abs. @590.6nm |
| -------- | ----------------------- | ---------------------------- | ---------------------------- |
|  2+8H2O  |          0.320          |             0.156            |             0.360            | 
|  4+6H2O  |          0.627          |             0.376            |             0.738            | 
|  6+4H2O  |          0.902          |             0.530            |             1.099            | 
|  8+2H2O  |          1.145          |             0.640            |             1.367            | 

Gels were placed in a 6-well plate, with wells filled with a 4-6H2O dilution of each dye. Three plates were used, one for each dye.

### Analyzing Rested Gel Samples
Absorbance readings were taken after gels sat in dye solution for 24 hours.

| Sample | Congo Red Abs. @498.8nm | Methylene Blue Abs. @668.5nm | Crystal Violet Abs. @590.6nm |
| ------ | ----------------------- | ---------------------------- | ---------------------------- |
|  No Gel  |          0.827          |             0.390            |             0.913            | 
|  PVA + CA  |          0.261          |             0.075            |             0.193            | 
|  PVA/B-CD  |          0.178          |             0.098            |             0.149            | 
|  PVA/B-CD (4:1) + CA  |          0.137          |             0.184            |             0.555            | 
|  PVA/B-CD (2:1) + CA  |          0.505          |             0.157            |             0.488            |  

Weight after 24 hours. Gels were all initially weighed and cut to be 0.23g.

| Sample | Congo Red | Methylene Blue | Crystal Violet |
| ------ | --------- | -------------- | -------------- |
|  PVA + CA  |          0.29          |             0.28            |             0.29            | 
|  PVA/B-CD  |          0.34          |             0.31            |             0.33            | 
|  PVA/B-CD (4:1) + CA  |          0.31          |             0.30            |             0.29            | 
|  PVA/B-CD (2:1) + CA  |          0.33          |             0.31            |             0.31            | 

### Results
- **Gels vs No Gel:** All gels significantly reduce the absorbance of the dyes compared to no gel, indicating effective dye absorption by the gels.
- **PVA + CA:** Shows good absorption for all dyes, particularly effective for Methylene Blue.
- **PVA/B-CD:** Strong absorption for Congo Red and Crystal Violet but less effective for Methylene Blue compared to PVA + CA.
- **PVA/B-CD (4:1) + CA and PVA/B-CD (2:1) + CA:** The ratio of B-CD influences the absorbance:
  - For Congo Red: PVA/B-CD (4:1) + CA is most effective.
  - For Methylene Blue: Lower ratios (or no ratio) of B-CD (PVA + CA) are more effective.
  - For Crystal Violet: PVA/B-CD without CA is most effective.
- **Weight Increase:** Among Cyclodextrin Hydrogels, weight increase is consistently above that of PVA + CA.

</details>

<details>
<summary>Metal Ion Absorbance Assay (Complexometric Titration)</summary>
<br>

The same 0.01063M EDTA solution was used for all trials.

| Pb<sup>2+</sup> Solution Standardization using 0.01063M EDTA  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  Volume Pipetted  |          10.00          |             10.00           |             10.00           | 
|  ΔV  |          18.53           |             18.46           | 
|  Molarity   |          0.01971865          |             0.01969739        |             0.01962298           |
|  Pb<sup>2+</sup> Standardized Molarity  |          0.0197        |                   |                  |
|  RSD  |        0.26%       |                   |                  | 

| PVA + CA [Pb<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  ΔV  |          18.23          |             18.26           |             18.22           | 
|  Molarity   |          0.01937849         |             0.01941038         |             0.01936785           |
|  Mean Molarity |  0.0194  |  | | 
|  RSD  |        0.11%       |                   |                  | 

| PVA/B-CD [Pb<sup>2+</sup>] |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  ΔV  |          18.39          |             18.47           |             18.4          | 
|  Molarity   |          0.01937849         |             0.01941038         |             0.0195592           |
|  Mean Molarity |  0.0194 |  | | 
|  RSD  |        0.50%       |                   |                  | 

| PVA/B-CD (4:1) + CA [Pb<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  ΔV  |         18.35           |             18.29           |           18.31         | 
|  Molarity   |         0.01950605         |           0.01944227        |          0.01946353          |
|  Mean Molarity |  0.0195 |  | | 
|  RSD  |        0.17%       |                   |                  | 

| PVA/B-CD (2:1) + CA [Pb<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  ΔV  |          18.29          |            18.28            |             18.13          | 
|  Molarity   |       0.01944227            |          0.01943164        |               0.01927219        |
|  Mean Molarity |  0.0194|  | | 
|  RSD  |        0.49%       |                   |                  | 

---

| Zn<sup>2+</sup> Solution Standardization using 0.01063M EDTA  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  Volume Pipetted (these were the only non-10mL values)  |          4.98          |             5.00           |             5.01           | 
|  ΔV  |          2.91          |             2.99           |             3.06           | 
|  Molarity   |         TODO           |         TODO           |             TODO          |
|  Zn<sup>2+</sup> Standardized Molarity  |          TODO       |                   |                  | 

| PVA + CA [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  ΔV  |          5.82          |           5.91             |            5.89           | 
|  Molarity   |          TODO         |             TODO        |             TODO          |
|  Mean Molarity |  Not Done |  | | 

| PVA/B-CD [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  ΔV  |           5.62         |           5.71             |           5.93         | 
|  Molarity   |          TODO         |             TODO        |             TODO          |
|  Mean Molarity |  Not Done |  | | 

| PVA/B-CD (2:1) [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  ΔV  |          5.84          |           6.00            |         5.98          | 
|  Molarity   |          TODO         |             TODO        |             TODO          |
|  Mean Molarity |  Not Done |  | | 

| PVA/B-CD (4:1) [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  ΔV  |            5.99        |           6.00           |          5.99        | 
|  Molarity   |          TODO (credit Nico in presentation)         |             TODO        |             TODO          |
|  Mean Molarity |  Not Done... Note each flask was cleaned with H2O and acetate buffer of 6 was made (3ml per titration) |  | | 

</details>
