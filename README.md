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

## Swelling Analysis 

- Gels (dried) were cut into smaller pieces and initial weight was recorded<br>
- Gels were placed in dH<sub>2</sub>O (I used cell culture wells) and let sit for 24hrs  <br>
- Excess water was removed from the surface of gels  <br>
- Samples were weighed, and swelling was calculated using the formula $S = \dfrac{(W_f\ -W_0)}{W_0}\cdot100$
  
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

>Gels were then placed in a 6-well plate, with wells filled with a 4-6H<sub>2</sub>O dilution of each dye. 3 plates were used, one for each dye.


| Dilution | Congo Red Abs. @498.8nm | Methylene Blue Abs. @668.5nm | Crystal Violet Abs. @590.6nm |
| -------- | ----------------------- | ---------------------------- | ---------------------------- |
|  2+8H<sub>2</sub>O  |          0.320          |             0.156            |             0.360            | 
|  4+6H<sub>2</sub>O  |          0.627          |             0.376            |             0.738            | 
|  6+4H<sub>2</sub>O  |          0.902          |             0.530            |             1.099            | 
|  8+2H<sub>2</sub>O  |          1.145          |             0.640            |             1.367            | 

### Analyzing Rested Gel Samples
>Absorbance readings were taken after gels sat in dye solution for 24h<br>

| Sample | Congo Red Abs. @498.8nm | Methylene Blue Abs. @668.5nm | Crystal Violet Abs. @590.6nm |
| ------ | --------------------- | -------------------------- | -------------------------- |
|  No Gel  |          0.827          |             0.390            |             0.913            | 
|  PVA + CA  |          0.261          |             0.075            |             0.193            | 
|  PVA/B-CD  |          0.178          |             0.098         |             0.149            | 
|  PVA/B-CD(4:1) + CA  |          0.137          |       0.184            |             0.555            | 
|  PVA/B-CD(2:1) + CA  |          0.505          |             0.157            |             0.488            |  


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
|  $\Delta$ V  |          18.55          |             18.53           |             18.46           | 
|  Molarity   |          0.01971865          |             0.01969739        |             0.01962298           |
|  Pb<sup>2+</sup> Standardized Molarity  |          0.0197        |                   |                  |
|  RSD  |        0.26%       |                   |                  | 
<br>

| PVA + CA [Pb<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V  |          18.23          |             18.26           |             18.22           | 
|  Molarity   |          0.01937849         |             0.01941038         |             0.01936785           |
|  Mean Molarity |  0.0194  |  | | 
|  RSD  |        0.11%       |                   |                  | 
<br>

| PVA/B-CD [Pb<sup>2+</sup>] |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V  |          18.39          |             18.47           |             18.4          | 
|  Molarity   |          0.01937849         |             0.01941038         |             0.0195592           |
|  Mean Molarity |  0.0194 |  | | 
|  RSD  |        0.50%       |                   |                  | 
<br>

| PVA/B-CD(4:1) +CA [Pb<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V  |         18.35           |             18.29           |           18.31         | 
|  Molarity   |         0.01950605         |           0.01944227        |          0.01946353          |
|  Mean Molarity |  0.0195 |  | | 
|  RSD  |        0.17%       |                   |                  | 
<br>

| PVA/B-CD(2:1) + CA [Pb<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V  |          18.29          |            18.28            |             18.13          | 
|  Molarity   |       0.01944227            |          0.01943164        |               0.01927219        |
|  Mean Molarity |  0.0194|  | | 
|  RSD  |        0.49%       |                   |                  | 


---

| Zn<sup>2+</sup> Solution Standardization |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  Volume Pipetted (these were the only non-10mL values)  |          4.98          |             5.00           |             5.01           | 
|  $\Delta$ V  |          2.91          |             2.99           |             3.06           | 
|  Molarity   |         todo           |         todo           |             todo          |
|  Pb<sup>2+</sup> Standardized Molarity  |          todo       |                   |                  | 
<br>

| PVA + CA [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V  |          5.82          |           5.91             |            5.89           | 
|  Molarity   |          todo         |             todo        |             todo          |
|  Mean Molarity |  not done |  | | 
<br>

| PVA/B-CD [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V  |           5.62         |           5.71             |           5.93         | 
|  Molarity   |          todo         |             todo        |             todo          |
|  Mean Molarity |  not done |  | | 
<br>

| PVA/B-CD(2:1) [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V  |          5.84          |           6.00            |         5.98          | 
|  Molarity   |          todo         |             todo        |             todo          |
|  Mean Molarity |  not done |  | | 
<br>

| PVA/B-CD(4:1) [Zn<sup>2+</sup>]  |  |  |  |
| ------ | --------- | -------------- | -------------- |
|  $\Delta$ V  |            5.99        |           6.00           |          5.99        | 
|  Molarity   |          todo(credit nico in presentation)         |             todo        |             todo          |
|  Mean Molarity |  not done... note each flask was cleaned with H<sub>2</sub>O and acetate buffer of 6 was made (3ml per titration) |  | | 
<br>


bcd+pva



















