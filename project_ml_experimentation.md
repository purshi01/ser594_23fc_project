#### SER594: Experimentation

#### Predicting the Best Time to Buy a House based on Historic Housing Data (title)

#### Purushothama Shanthappa (author)

#### (11/20/2023)

## Explainable Records

### Record 1

**Raw Data:** 1,60,RL,65.0,8450,Pave,Grvl,Reg,Lvl,AllPub,Inside,Gtl,CollgCr,Norm,Norm,1Fam,2Story,7,5,2003,2003,Gable,CompShg,VinylSd,VinylSd,BrkFace,196.0,4,3,PConc,4.0,3.0,0.0,5.0,706,0.0,0,150,856,GasA,5,Y,1,856,854,0,1710,1,0,2,1,3,1,4,8,Typ,0,3.461038961038961,Attchd,2003.0,2.0,2,548,3.0,3.0,1,0,61,0,0,0,0,Gd,0,0,2,2008,WD,Normal,208500,6.0272,2.8263

First record from the dataset, representing a property sold in 2008, with features like Overall Quality (7), Ground Living Area (1710 sq ft), Garage Area (548 sq ft), and located in the 'CollgCr' neighborhood.

**Prediction Explanation:** The model predicted a sale price of approximately $194,031. This aligns with the market expectations considering the property's high overall quality, spacious living area, and desirable neighborhood. The slight deviation from the actual sale price of $208,500 could be attributed to market conditions or other nuanced property features not fully captured in the model.V

### Record 2

**Raw Data:** 2,20,RL,80.0,9600,Pave,Grvl,Reg,Lvl,AllPub,FR2,Gtl,Veenker,Feedr,Norm,1Fam,1Story,6,8,1976,1976,Gable,CompShg,MetalSd,MetalSd,BrkFace,0.0,3,3,CBlock,4.0,3.0,3.0,4.0,978,0.0,0,284,1262,GasA,5,Y,1,1262,0,0,1262,0,1,2,0,3,1,3,6,Typ,1,3.0,Attchd,1976.0,2.0,2,460,3.0,3.0,1,298,0,0,0,0,0,Gd,0,0,5,2007,WD,Normal,181500,6.3373,2.6616

Second record from the dataset, depicting a property sold in 2007, with an Overall Quality of 6, Ground Living Area of 1262 sq ft, and Garage Area of 460 sq ft in the 'Veenker' neighborhood.

**Prediction Explanation:** The model's prediction of approximately $153,142 is a bit lower than the actual sale price of $181,500. This may indicate the model's sensitivity to certain features like the slightly lower overall quality or the smaller living area compared to the first record, or other external factors not included in the model.

## Interesting Features

### Feature A

**Feature:** OverallQual (Overall material and finish quality of the house)

**Justification:** This feature directly influences the property's appeal and market value, as higher quality often correlates with higher prices.

### Feature B

**Feature:** GrLivArea (Above-ground living area in square feet)

**Justification:** The size of the living area is a crucial factor in property valuation, with larger homes generally commanding higher prices.

## Experiments

### Varying A

**Prediction Trend Seen:** Increasing the Overall Quality rating led to an increased predicted sale price of $219,534.82. This substantial increase underscores the model's sensitivity to property quality and its impact on valuation.

### Varying B

**Prediction Trend Seen:** Expanding the Ground Living Area resulted in an increased predicted sale price of $200,336.90. This trend is consistent with real estate market expectations where larger properties command higher prices.

### Varying A and B together

**Prediction Trend Seen:** Increasing both Overall Quality and Ground Living Area simultaneously led to a predicted sale price of $317,744.82, indicating a significant combined effect on property valuation.

### Varying A and B inversely

**Prediction Trend Seen:** Increasing Overall Quality while decreasing Ground Living Area led to a predicted sale price of $215,298.42. This shows the nuanced interaction between these features, where high quality can somewhat compensate for smaller living space.
