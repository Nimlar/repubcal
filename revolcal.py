# This Python file uses the following encoding: utf-8
"""
Provide an extension od datetime to manage revoltuonnary date
"""

from __future__ import print_function
import datetime
import ephem


TROPICAL_YEAR = 365.24219878
FRENCH_REVOLUTIONARY_EPOCH = datetime.date(1792, 9, 22)

REV_DAY_NAMES = ['Primidi', 'Duodi', 'Tridi', 'Quartidi', 'Quintidi', 'Sextidi', 'Septidi',
                 'Octidi', 'Nonidi', 'Décadi']
REV_MONTH_NAMES = ['Vendémiaire', 'Brumaire', 'Frimaire', 'Nivôse', 'Pluviôse', 'Ventôse',
                   'Germinal', 'Floréal', 'Prairial', 'Messidor', 'Thermidor', 'Fructidor']
SANSCULOTTIDES = ['Jour de la vertu', 'Jour du génie', 'Jour du travail', 'Jour de l\'opinion',
                  'Jour des récompenses', 'Jour de la Révolution']

FETES=[["Raisin", "Safran", "Châtaigne", "Colchique", "Cheval", "Balsamine", "Carotte", "Amaranthe", "Panais", "Cuve", "Pomme de terre", "Immortelle", "Potiron", "Réséda", "Ane", "Belle de nuit", "Citrouille", "Sarrasin", "Tournesol", "Pressoir", "Chanvre", "Pêche", "Navet", "Amarillis", "Bœuf", "Aubergine", "Piment", "Tomate", "Orge", "Tonneau"],
       ["Pomme", "Céleri", "Poire", "Betterave", "Oie", "Héliotrope", "Figue", "Scorsonère", "Alisier", "Charrue", "Salsifis", "Macre", "Topinambour", "Endive", "Dindon", "Chervis", "Cresson", "Dentelaire", "Grenade", "Herse", "Bacchante", "Azerole", "Garance", "Orange", "Faisan", "Pistache", "Macjonc", "Coing", "Cormier", "Rouleau"]                   ,
       ["Raiponce", "Turneps", "Chicorée", "Nèfle", "Cochon", "Mâche", "Chou-fleur", "Miel", "Genièvre", "Pioche", "Cire", "Raifort", "Cèdre", "Sapin", "Chevreuil", "Ajonc", "Cyprès", "Lierre", "Sabine", "Hoyau", "Erable sucré", "Bruyère", "Roseau", "Oseille", "Grillon", "Pignon", "Liège", "Truffe", "Olive", "Pelle"]            ,
       ["Tourbe", "Houille", "Bitume", "Soufre", "Chien", "Lave", "Terre végétale", "Fumier", "Salpêtre", "Fléau", "Granit", "Argile", "Ardoise", "Grès", "Lapin", "Silex", "Marne", "Pierre à chaux", "Marbre", "Van", "Pierre à Plâtre", "Sel", "Fer", "Cuivre", "Chat", "Etain", "Plomb", "Zinc", "Mercure", "Crible"]                     ,
       ["Lauréole", "Mousse", "Fragon", "Perce Neige", "Taureau", "Laurier thym", "Amadouvier", "Mézéréon", "Peuplier", "Coignée", "Ellébore", "Brocoli", "Laurier", "Avelinier", "Vache", "Buis", "Lichen", "If", "Pulmonaire", "Serpette", "Thlaspi", "Thimèle", "Chiendent", "Trainasse", "Lièvre", "Guède", "Noisetier", "Cyclamen", "Chélidoine", "Traineau"],
       ["Tussilage", "Cornouiller", "Violier", "Troëne", "Bouc", "Asaret", "Alaterne", "Violette", "Marceau", "Bêche", "Narcisse", "Orme", "Fumeterre", "Vélar", "Chèvre", "Epinard", "Doronic", "Mouron", "Cerfeuil", "Cordeau", "Mandragore", "Persil", "Cochiéaria", "Pâquerette", "Thon", "Pissenlit", "Sylve", "Capillaire", "Frêne", "Plantoir"],
       ["Primevère", "Platane", "Asperge", "Tulipe", "Poule", "Bette", "Bouleau", "Jonquille", "Aulne", "Couvoir", "Pervenche", "Charme", "Morille", "Hêtre", "Abeille", "Laitue", "Mélèze", "Cigüe", "Radis", "Ruche", "Gainier", "Romaine", "Marronnier", "Roquette", "Pigeon", "Lilas", "Anémone", "Pensée", "Myrtille", "Greffoir"]           ,
       ["Rose", "Chêne", "Fougère", "Aubépine", "Rossignol", "Ancolie", "Muguet", "Champignon", "Hyacinthe", "Rateau", "Rhubarbe", "Sainfoin", "Bâton d'or", "Chamerops", "Ver à soie", "Consoude", "Pimprenelle", "Corbeille d'or", "Arroche", "Sarcloir", "Statice", "Fritillaire", "Bourache", "Valériane", "Carpe", "Fusain", "Civette", "Buglosse", "Sénevé", "Houlette"],
       ["Luzerne", "Hémérocalle", "Trèfle", "Angélique", "Canard", "Mélisse", "Fromental", "Martagon", "Serpolet", "Faux", "Fraise", "Bétoine", "Pois", "Acacia", "Caille", "Œillet", "Sureau", "Pavot", "Tilleul", "Fouche", "Barbeau", "Camomille", "Chèvrefeuille", "Caille-lait", "Tanche", "Jasmin", "Verveine", "Thym", "Pivoine", "Chariot"],
       ["Seigle", "Avoine", "Oignon", "Véronique", "Mulet", "Romarin", "Concombre", "Echalotte", "Absinthe", "Faucille", "Coriandre", "Artichaut", "Girofle", "Lavande", "Chamois", "Tabac", "Groseille", "Gesse", "Cerise", "Parc", "Menthe", "Cumin", "Haricot", "Orcanète", "Pintade", "Sauge", "Ail", "Vesce", "Blé", "Chalémie"]                         ,
       ["Epeautre", "Bouillon blanc", "Melon", "Ivraie", "Bélier", "Prêle", "Armoise", "Carthame", "Mûre", "Arrosoir", "Panis", "Salicorne", "Abricot", "Basilic", "Brebis", "Guimauve", "Lin", "Amande", "Gentiane", "Ecluse", "Carline", "Câprier", "Lentille", "Aunée", "Loutre", "Myrte", "Colza", "Lupin", "Coton", "Moulin"]                        ,
       ["Prune", "Millet", "Lycoperdon", "Escourgeon", "Saumon", "Tubéreuse", "Sucrion", "Apocyn", "Réglisse", "Echelle", "Pastèque", "Fenouil", "Epine vinette", "Noix", "Truite", "Citron", "Cardère", "Nerprun", "Tagette", "Hotte", "Eglantier", "Noisette", "Houblon", "Sorgho", "Ecrevisse", "Bigarade", "Verge d'or", "Maïs", "Marron", "Panier"]
]

def int_to_roman(value):
    """
    Convert from decimal to Roman
    """
    if not 0 <= value < 4000:
        raise ValueError, "Argument must be between 1 and 3999"
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = ""
    for i in range(len(ints)):
        count = int(value / ints[i])
        result += nums[i] * count
        value -= ints[i] * count
    return result

def equinoxe_automn(year):
    """
        get the automn equinox
    """
    return ephem.next_autumn_equinox(datetime.date(year, 1, 1))-1
    #why -1 ???

def annee_de_la_revolution(date):
    """
    Find corresponding revolutionnary year of current date
    """
    guess = date.year - 2
    edate = ephem.Date(date)
    #print("edate {}".format(edate))
    #print("guess0 {}".format(guess))
    lasteq = equinoxe_automn(guess)
    #print("lasteq0 {}".format(lasteq))
    while lasteq > edate:
        guess -= 1
        #print("guess1 {}".fromat(guess))
        lasteq = equinoxe_automn(guess)
        #print("lasteq1 {}".fromat(lasteq))
    nexteq = lasteq - 1
    while not int(lasteq) <= edate < int(nexteq):
        lasteq = nexteq
        guess += 1
        #print("guess2 {}".format(guess))
        nexteq = equinoxe_automn(guess)
        #print("lasteq2 {}".foramt(lasteq))
        #print("nexteq2 {}".format(nexteq))
    #print(lasteq)
    #print(ephem.Date(FRENCH_REVOLUTIONARY_EPOCH))
    #print(((int(lasteq) - ephem.Date(FRENCH_REVOLUTIONARY_EPOCH)) / TROPICAL_YEAR))
    year = round((lasteq - ephem.Date(FRENCH_REVOLUTIONARY_EPOCH)) / TROPICAL_YEAR) + 1
    return (int(year), lasteq)

def d_to_french_revolutionary(date):
    """
    return a dictionnary contain revolutionnary information

    'an' : Year number
    'mois': nb month, if > len(month) this are the extra Revolutionnaries months (ie extra days)
            starting 0
    'jour': nb days in month, starting 0
    'decade': nb of the decade in the year ( ~week number)
    """
    rdate = {}
    rdate['an'], equinoxe = annee_de_la_revolution(date)
    rdate['mois'] = (int(ephem.Date(date) - equinoxe) / 30)
    rdate['jour'] = int(ephem.Date(date) - equinoxe) % 30
    rdate['decade'] = (rdate['jour'] / 10) + 1 +3*rdate['mois']
    return rdate



class RDate(datetime.date):
    """
    Revolutionnary datetime.date
    """
    def __new__(cls, year, month, day):
        return datetime.date.__new__(cls, year, month, day)

    def revo_str(self):
        """
        to remove
        """
        return print_to_revo(self)

    def revo(self):
        """
        revo uple
        """
        return d_to_french_revolutionary(self)

    def revol_strftime(self, fmt):
        """ modify fmt with specific revol format """
        rdate = d_to_french_revolutionary(self)
        newformat = []
        push = lambda val : newformat.append(str(val))
        i, n = 0, len(fmt)
        while i < n:
            char = fmt[i]
            i += 1
            if char == "%":
                if i < n:
                    char = fmt[i]
                    i += 1
                    if char == "r":
                        if i < n:
                            char = fmt[i]
                            i += 1
                            if char == "A":
                                # Decadeday as locale’s full name.
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push(SANSCULOTTIDES[rdate['jour'] % 10])
                                else:
                                    push(REV_DAY_NAMES[rdate['jour'] % 10])
                            elif char == "w":
                                # Decadeday as a decimal number, where 0 is Primid and 9 is Decadi.
                                push(rdate['jour'] % 10)
                            elif char == "d":
                                #Day of the month as a zero-padded decimal number.
                                push("%02d" % (rdate['jour'] + 1))
                            elif char == "B":
                                #Month as locale’s full name
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push("")
                                else:
                                    push(REV_MONTH_NAMES[rdate['mois']])
                            elif char == "m":
                                #Month as a zero-padded decimal number
                                push("%02d" % (rdate['mois'] + 1))
                            elif char == "y":
                                #Year as decimal number.
                                push(rdate['an'])
                            elif char == "Y":
                                #Year as Romanian number.
                                push(int_to_roman(rdate['an']))
                            elif char == "W":
                                #Decade number in the year.
                                push(rdate['decade'])
                            elif char == "f":
                                #fete oif the day.
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push(SANSCULOTTIDES[rdate['jour'] % 10])
                                else:
                                    push(FETES[rdate['mois']][rdate['jour']])
                            else:
                                push("%r")
                                push(char)
                        else:
                            push("%r")


                    else:
                        push("%")
                        push(char)
                else:
                    push("%")
            else:
                push(char)


        newformat = "".join(newformat)
        if self.year < 1900:
            return newformat
        else:
            return self.strftime(newformat)

    def __format__(self, fmt):
        """
            add some new format to dispaly date
            %r should start any revolutionarry modifiator

            %rA Week^WDecadeday as locale’s full name.
            %rw Week^Decadeday as a decimal number, where 0 is Primid and 9 is Decadi.

            %rd Day of the month as a zero-padded decimal number.
            %rB Month as locale’s full name
            %rm Month as a zero-padded decimal number.
            %ry Year as decimal number.
            %rY Year as Romanian number.
            %rW Decade number in the year.
        """
        if not isinstance(fmt, str):
            raise TypeError("must be str, not %s" % type(fmt).__name__)
        if len(fmt) != 0:
            return self.revol_strftime(fmt)
        return str(self)




def tests():
    """
    test function
    """
    def test(year, month, day, expected):
        """ test function """
        date = RDate(year, month, day)
        print("{}-{:02}-{:02} {}".format(year, month, day, expected))
        print("{0} {0:%rA %rd %rB [Decade %rW] an %rY(%ry)}".format(date))
        print("{}-{:02}-{:02} {}\n".format(year, month, day, expected))

    test(1792, 9, 22, "Primidi 01 Vendémiaire [Decade 1] an I(1)")
    test(1792, 9, 23, "Duodi 02 Vendémiaire [Decade 1] an I(1)")
    test(1793, 5, 4, "Quintidi 15 Floreal [Decade 23] an I(1)")
    test(1793, 9, 14, "Octidi 28 Fructidor [Decade 36] an I(1)")
    test(1793, 9, 20, "Jour de l'opinion [Decade 37] an I(1)")
    test(1795, 1, 18, "Nonidi 29 Nivose [Decade 3] an III(3)")
    test(1798, 9, 21, "Jour des récompenses 05 [Decade 37] an VI(6)")
    test(1798, 9, 22, "Primidi 01 Vendémiaire [Decade 1] an VII(7) error here as sextil year may have change")
    test(1798, 9, 23, "Duodi 02 Vendémiaire [Decade 1] an VII(7)")
    test(1798, 10, 20, "Nonidi 29 Vendémiaire [Decade 3] and VII(7)")
    test(1799, 9, 17, "Jour de la vertu 01 [Decade 37] an VII(7)")
    test(1799, 9, 22, "Jour de la révolution 06 [Decade 37] an VII(7)")
    test(1803, 9, 22, "Jour des recompenses 05 [Decade 37] an XI(11)")
    test(2013, 1, 21, "Duodi 02 Pluviose [Decade 13] an CCXXI(221)")
    test(2013, 10, 21, "Décadi 30 Vendémiaire [Decade 3] an CCXXII(222)")


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
    print("{0} {0:%rA %rd %rB [Decade %rW] an %rY(%ry)}".format(ldate))
    print("")
