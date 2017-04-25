# This Python file uses the following encoding: utf-8
"""
tests for revolcal module
"""

from __future__ import print_function
from revolcal import RDate
import datetime


def tests_somedate(display=False):
    """
    test function
    """
    def test(year, month, day, expected):
        """ test function to check gregorian to republican convert"""
        date = RDate(year, month, day)
        result = "{0:%rA %rd %rB [Decade %rW] an %rY(%ry)}".format(date)
        if result != expected:
            print("Error on {}-{:02}-{:02}".format(year, month, day))
            print("   expected {}".format(expected))
            print("   we got   {}".format(result))
            print("\n")
        else:
            if display:
                print("Correct: {}-{:02}-{:02}".format(year, month, day))
                print("   {}".format(expected))
                print("   {}".format(result))
                print("\n")


    test(1792, 9, 22, "Primidi 01 Vendémiaire [Decade 1] an I(1)")
    test(1792, 9, 23, "Duodi 02 Vendémiaire [Decade 1] an I(1)")
    test(1793, 5, 4, "Quintidi 15 Floréal [Decade 23] an I(1)")
    test(1793, 9, 14, "Octidi 28 Fructidor [Decade 36] an I(1)")
    test(1793, 9, 20, "Jour de l’opinion 04  [Decade 37] an I(1)")
    test(1793, 9, 22, "Primidi 01 Vendémiaire [Decade 1] an II(2)")
    test(1794, 9, 22, "Primidi 01 Vendémiaire [Decade 1] an III(3)")
    test(1795, 1, 18, "Nonidi 29 Nivôse [Decade 12] an III(3)")
    test(1795, 9, 23, "Primidi 01 Vendémiaire [Decade 1] an IV(4)")
    test(1796, 9, 22, "Primidi 01 Vendémiaire [Decade 1] an V(5)")
    test(1797, 9, 22, "Primidi 01 Vendémiaire [Decade 1] an VI(6)")
    test(1798, 9, 21, "Jour des récompenses 05  [Decade 37] an VI(6)")
    test(1798, 9, 22, "Primidi 01 Vendémiaire [Decade 1] an VII(7)")
    test(1798, 9, 23, "Duodi 02 Vendémiaire [Decade 1] an VII(7)")
    test(1798, 10, 20, "Nonidi 29 Vendémiaire [Decade 3] an VII(7)")
    test(1799, 9, 17, "Jour de la vertu 01  [Decade 37] an VII(7)")
    test(1799, 9, 22, "Jour de la Révolution 06  [Decade 37] an VII(7)")
    test(1799, 9, 23, "Primidi 01 Vendémiaire [Decade 1] an VIII(8)")
    test(1800, 9, 23, "Primidi 01 Vendémiaire [Decade 1] an IX(9)")
    test(1801, 9, 23, "Primidi 01 Vendémiaire [Decade 1] an X(10)")
    test(1802, 9, 23, "Primidi 01 Vendémiaire [Decade 1] an XI(11)")
    test(1803, 9, 22, "Jour des récompenses 05  [Decade 37] an XI(11)")
    test(1803, 9, 24, "Primidi 01 Vendémiaire [Decade 1] an XII(12)")
    test(1804, 9, 23, "Primidi 01 Vendémiaire [Decade 1] an XIII(13)")
    test(1805, 9, 23, "Primidi 01 Vendémiaire [Decade 1] an XIV(14)")

    test(2013, 1, 21, "Duodi 02 Pluviôse [Decade 13] an CCXXI(221)")
    test(2013, 10, 21, "Décadi 30 Vendémiaire [Decade 3] an CCXXII(222)")
    test(2015, 9, 21, "Jour de l’opinion 04  [Decade 37] an CCXXIII(223)")

    test(2015, 9, 22, "Jour des récompenses 05  [Decade 37] an CCXXIII(223)")
    test(2015, 9, 23, "Primidi 01 Vendémiaire [Decade 1] an CCXXIV(224)")
    test(2016, 9, 21, "Jour des récompenses 05  [Decade 37] an CCXXIV(224)")
    test(2016, 9, 22, "Primidi 01 Vendémiaire [Decade 1] an CCXXV(225)")
    test(2016, 9, 23, "Duodi 02 Vendémiaire [Decade 1] an CCXXV(225)")
    test(2017, 9, 21, "Jour des récompenses 05  [Decade 37] an CCXXV(225)")
    test(2017, 9, 22, "Primidi 01 Vendémiaire [Decade 1] an CCXXVI(226)")
    test(2017, 9, 23, "Duodi 02 Vendémiaire [Decade 1] an CCXXVI(226)")

def tests_some_wikipediadate(display):
    """ test wome wikipedia date """
    tests_val = [
        ((1792, 9, 22), "01, 1"),
        ((1793, 9, 22), "01, 2"),
        ((1794, 9, 22), "01, 3"),
        ((1795, 9, 23), "01, 4"),
        ((1796, 9, 22), "01, 5"),
        ((1797, 9, 22), "01, 6"),
        ((1798, 9, 22), "01, 7"),
        ((1799, 9, 23), "01, 8"),
        ((1800, 9, 23), "01, 9"),
        ((1801, 9, 23), "01, 10"),
        ((1802, 9, 23), "01, 11"),
        ((1803, 9, 24), "01, 12"),
        ((1804, 9, 23), "01, 13"),
        ((1805, 9, 23), "01, 14"),

        ((2011, 9, 21), "05, 219"),
        ((2011, 9, 22), "01, 220"),
        ((2011, 9, 23), "02, 220"),
        ((2012, 9, 21), "06, 220"),
        ((2012, 9, 22), "01, 221"),
        ((2012, 9, 23), "02, 221"),
        ((2013, 9, 21), "05, 221"),
        ((2013, 9, 22), "01, 222"),
        ((2013, 9, 23), "02, 222"),
        ((2014, 9, 21), "05, 222"),
        ((2014, 9, 22), "01, 223"),
        ((2014, 9, 23), "02, 223"),
        ((2015, 9, 21), "05, 223"),
        ((2015, 9, 22), "01, 224"),
        ((2015, 9, 23), "02, 224"),
        ((2016, 9, 21), "06, 224"),
        ((2016, 9, 22), "01, 225"),
        ((2016, 9, 23), "02, 225"),
        ((2017, 9, 21), "05, 225"),
        ((2017, 9, 22), "01, 226"),
        ((2017, 9, 23), "02, 226")
    ]
    for test in tests_val:
        date = RDate(*(test[0]))
        calculated = "{0:%rd, %ry}".format(date)
        if calculated != test[1]:
            print("{} {}".format(date, calculated))
            print(" wikipedia {}".format(test[1]))
        else:
            if display:
                print("{} OK".format(test[0]))

def test_allentry():
    """ that that not table overflow occurs """
    cdate = datetime.date(2011, 9, 21)
    end_date = datetime.date(2017, 9, 21)
    fmt = "{:"+RDate.__format__.__doc__+"}"
    while cdate <= end_date:
        date = RDate(cdate.year, cdate.month, cdate.day)
        try:
            string = fmt.format(date)
        except:
            print("Error in displaying {}".format(date))
        cdate += datetime.timedelta(1)





if __name__ == "__main__":
    import sys
    display_all = False
    if len(sys.argv) != 1:
        display_all = True

    tests_somedate(display_all)
    tests_some_wikipediadate(display_all)
    test_allentry()

