#QA assyrance and L testing
#SDET (sw dev in test)
# When joining two tabels (inner)
# matching parameters and making new row with the joining of the rows from the other charts
# Output table is created of matching rows
# Outter join
"""
outter join uses them all and fill the missing values with NAs

Aspects of Attributes
-data(storage)types
-measurment scales
-Semantic type - what do the values represent

-noisy vs invalid
-labeled vs unlabeled

Measurment scales
-nominal - discrete values without an inherent ordering
    occupation 
-ordinal - discerte values with an inherent order
    Letter grades, tshirt sizes
- no gurantee on the distance between 2 values

- interval - values measured on a scale of equal sized widths
    -no inherent zero point
        (absence of a value)
-Ratio - interval values with an inherent 0 point
    temp in kelvin


Noisy Vs. Invalid
    Noisy- Valid on the scale but recorded incorrectly
        entering the wrong data, but valid data nonetheless
    Invalid- Invalid data, asked for state and enter 12


Labeled vs unlabeled
    Labeled data is an attribute that represents a "class"
        Gender, month
        supervised machine learning -  To predict a class for an unseen instance
unlabeled data- Not a class attribute
    (dataset doesn't have a class attribute)
    


"""