from revolcal import RDate
import datetime



if __name__ == "__main__" :
    import sys
    ldate = RDate.today()
    if len(sys.argv) == 2:
        ldate = None
        if sys.argv[1].startswith("test"):
            tests()
            exit()
        try:
            delay = int(sys.argv[1])
            tdate = datetime.date.today() + datetime.timedelta(delay)
            ldate=RDate(tdate.year, tdate.month, tdate.day)
        except ValueError :
            print("value error")
    if len(sys.argv) == 4:
            ldate=RDate(int(sys.argv[1]),
                    int(sys.argv[2]),
                    int(sys.argv[3]))

    print("{0} {0:%rA %rd %rB [Decade %rW] an %rY(%ry) %rf}".format(ldate))

