# revolcal
Python module to convert to French Republican Calendar

## Usage from command line:

* To get the today information

`python revolcal.py`

* To get day information with an offset from today

`python revolcal.py -1` to print yesterday info, `python revolcal.py 2` to print after tomorrow info.

* To get any day information:

`python revolcal.py 2016 5 31`, will display republican calendar information of of Tuesday 31 May 2016

* To run the internal test
`python revolcal.py test`
Note the 1798-09-22 date that is not correct.

## Usage as module.
The `revolcal` module define a new class RDate (a sub class of datetime.date)

Only interesting part in this new class is the new `%r?` descriptors of the `format()` method.


            %rA Week^WDecadeday as locale’s full name.
            %rw Week^WDecadeday as a decimal number, where 0 is Primid and 9 is Decadi.

            %rd Day of the month as a zero-padded decimal number.
            %rB Month as locale’s full name
            %rI link to wikipedia image for the month.
            %rm Month as a zero-padded decimal number.
            %ry Year as decimal number.
            %rY Year as Romanan number.
            %rW Decade number in the year.
            %rf grain, pasture, trees, roots, flowers, fruits, animal, tool associated with the day
            %rF link to the french wikipage associated with the day

All possible date action, are inherited from the python `datetime.date` class

```python

import revolcal

date = revolcal.RDate.today()
print("Bonjour Citoyen, aujourd'hui nous somme le {:%rA %rd %rB %rY}".format(date))
```
