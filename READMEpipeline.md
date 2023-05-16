

0 Data joining:
We get the data we potentially want to use joined in one table.
And the added table with only the movies with Bechdel data.

1. parseGender.py
2. joinGenderAndLinks.py
3. joinMetadata.py
4. joinBechdel.py

Result:
genderAndLinksAndMetadata.csv
allDataPlusBechdel.csv

1 Important data extraction:
We want to take out the columns we have decided to not use for the current analysis.
We don'tdo that in the previous step because we might use them in further analy

2 Data cleaning and preparation:
We want to identify values that mean there is no datum about this thing,
and we want to remove these lines, so there isn't a problem afterwards.
And we want to prepare the data so that is it in a usable format (enumerationg categories and such)

3 Data processing:
The actual statistical analysis of the data.
