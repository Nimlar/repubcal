# This Python file uses the following encoding: utf-8
"""
Provide an extension od datetime to manage revoltuonnary date
"""

# remove some warning
# pylint: disable=line-too-long



from __future__ import print_function
import datetime
import ephem

WIKI_BASE_URL = "https://fr.wikipedia.org/wiki/"
TROPICAL_YEAR = 365.24219878
FRENCH_REVOLUTIONARY_EPOCH = datetime.date(1792, 9, 22)

REV_DAY_NAMES = ['Primidi', 'Duodi', 'Tridi', 'Quartidi', 'Quintidi', 'Sextidi', 'Septidi',
                 'Octidi', 'Nonidi', 'Décadi']
REV_MONTH_NAMES = ['Vendémiaire', 'Brumaire', 'Frimaire', 'Nivôse', 'Pluviôse', 'Ventôse',
                   'Germinal', 'Floréal', 'Prairial', 'Messidor', 'Thermidor', 'Fructidor']
BASE_MONTH_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/"
REV_MONTH_IMAGES = [
    "c/cd/Vendémiaire_commence_le_22_septembre.jpg",
    "6/62/Brumaire_commence_le_23_octobre.jpg",
    "e/e3/Frimaire_commence_le_22_novembre.jpg",
    "b/b6/Nivôse_commence_le_22_décembre.jpg",
    "0/09/Pluviôse_commence_le_21_ou_22_janvier.jpg",
    "7/7a/Ventôse_commence_le_20_ou_21_février.jpg",
    "0/0a/Germinal_commence_le_21_ou_22_mars.jpg",
    "f/fe/Floréal_commence_le_21_avril.jpg",
    "4/4b/Prairial_commence_le_21_mai.jpg",
    "a/af/Messidor_commence_le_21_ou_22_juin.jpg",
    "b/bb/Thermidor_commence_le_20_ou_21_juillet.jpg",
    "8/8c/Fructidor_commence_le_21_ou_22_août.jpg"
]
SANSCULOTTIDES = ['Jour de la vertu', 'Jour du génie', 'Jour du travail', 'Jour de l\'opinion',
                  'Jour des récompenses', 'Jour de la Révolution']

FETES = [
    [# Vendémiaire
        ("Raisin", ), ("Safran", "Safran (épice)"), ("Châtaigne", ), ("Colchique", ), ("Cheval", ), ("Balsamine", "Balsaminaceae"), ("Carotte", ), ("Amarante", "Amarante (plante)"), ("Panais", ), ("Cuve", ), ("Pomme de terre", ), ("Immortelle", "Immortelle commune"), ("Potiron", ), ("Réséda", ), ("Âne", ), ("Belle de nuit", "Mirabilis jalapa"), ("Citrouille", ), ("Sarrasin", "Sarrasin (plante)"), ("Tournesol", ), ("Pressoir", ), ("Chanvre", ), ("Pêche", "Pêche (fruit)"), ("Navet", ), ("Amaryllis", "Amaryllis (plante)"), ("Bœuf", "Bos taurus"), ("Aubergine", ), ("Piment", ), ("Tomate", ), ("Orge", "Orge commune"), ("Tonneau", "Tonneau (récipient)")],
    [# Brumaire
        ("Pomme", ), ("Céleri", ), ("Poire", ), ("Betterave", ), ("Oie", ), ("Héliotrope", ), ("Figue", ), ("Scorsonère", ), ("Alisier", "Sorbus torminalis"), ("Charrue", ), ("Salsifis", ), ("Mâcre", "Mâcre nageante"), ("Topinambour", ), ("Endive", ), ("Dindon", "Dinde"), ("Chervis", ), ("Cresson", "Cresson de fontaine"), ("Dentelaire", "Plumbago"), ("Grenade", "Grenade (fruit)"), ("Herse", "Herse (agriculture)"), ("Bacchante", "Baccharis halimifolia"), ("Azerole", ), ("Garance", "Garance des teinturiers"), ("Orange", "Orange (fruit)"), ("Faisan", ), ("Pistache", ), ("Macjonc", "Gesse tubéreuse"), ("Coing", ), ("Cormier", ), ("Rouleau", "Rouleau agricole")],
    [# Frimaire
        ("Raiponce", "Raiponce (plante)"), ("Turneps", "Betterave fourragère"), ("Chicorée", ), ("Nèfle", ), ("Cochon", ), ("Mâche", ), ("Chou-fleur", ), ("Miel", ), ("Genièvre", "Juniperus communis"), ("Pioche", ), ("Cire", ), ("Raifort", ), ("Cèdre", ), ("Sapin", ), ("Chevreuil", ), ("Ajonc", ), ("Cyprès", ), ("Lierre", "Hedera"), ("Sabine", "Juniperus sabina"), ("Hoyau", ), ("Érable sucré", "Érable à sucre"), ("Bruyère", ), ("Roseau", ), ("Oseille", ), ("Grillon", "Gryllidae"), ("Pignon", "Pignon de pin"), ("Liège", ), ("Truffe", "Truffe (champignon)"), ("Olive", ), ("Pelle", "Pelle (outil)")],
    [# Nivôse
        ("Tourbe", ), ("Houille", ), ("Bitume", ), ("Soufre", ), ("Chien", ), ("Lave", ), ("Terre végétale", "Humus"), ("Fumier", ), ("Salpêtre", "Nitrate de potassium"), ("Fléau", "Fléau (agriculture)"), ("Granit", ), ("Argile", ), ("Ardoise", ), ("Grès", "Grès (géologie)"), ("Lapin", "Oryctolagus cuniculus"), ("Silex", ), ("Marne", "Marne (géologie)"), ("Pierre à chaux", "Calcaire"), ("Marbre", ), ("Van", "Van (agriculture)"), ("Pierre à plâtre", "Gypse"), ("Sel", "Chlorure de sodium"), ("Fer", ), ("Cuivre", ), ("Chat", ), ("Étain", ), ("Plomb", ), ("Zinc", ), ("Mercure", "Mercure (chimie)"), ("Crible", "Tamis")],
    [# Pluviôse
        ("Lauréole", ), ("Mousse", "Bryophyta"), ("Fragon", "Ruscus aculeatus"), ("Perce-neige", ), ("Taureau", ), ("Laurier tin", "Viorne tin"), ("Amadouvier", ), ("Mézéréon", "Bois-joli"), ("Peuplier", ), ("Cognée", ), ("Ellébore", "Hellébore"), ("Brocoli", ), ("Laurier", "Laurus nobilis"), ("Avelinier", "Noisetier"), ("Vache", ), ("Buis", ), ("Lichen", ), ("If", "Taxus"), ("Pulmonaire", "pulmonaria"), ("Serpette", ), ("Thlaspi", ), ("Thimele", "Daphné garou"), ("Chiendent", ), ("Trainasse", "Renouée des oiseaux"), ("Lièvre", ), ("Guède", ), ("Noisetier", ), ("Cyclamen", ), ("Chélidoine", "Chelidonium majus"), ("Traîneau", )],
    [# Ventôse
        ("Tussilage", ), ("Cornouiller", "Cornus (plante)"), ("Violier", "Vélar"), ("Troène", ), ("Bouc", "Bouc (animal)"), ("Asaret", ), ("Alaterne", "Nerprun alaterne"), ("Violette", "Viola (genre végétal)"), ("Marceau", "Saule marsault"), ("Bêche", ), ("Narcisse", "Narcissus"), ("Orme", ), ("Fumeterre", ), ("Vélar", "Erysimum"), ("Chèvre", ), ("Épinard", ), ("Doronic", "Doronicum"), ("Mouron", "Mouron (flore)"), ("Cerfeuil", "Cerfeuil commun"), ("Cordeau", ), ("Mandragore", ), ("Persil", ), ("Cochléaria", "Cochlearia"), ("Pâquerette", ), ("Thon", ), ("Pissenlit", ), ("Sylvie", "Anémone sylvie"), ("Capillaire", "Capillaire de Montpellier"), ("Frêne", ), ("Plantoir", )],
    [# Germinal
        ("Primevère", ), ("Platane", ), ("Asperge", ), ("Tulipe", ), ("Poule", "Poule (animal)"), ("Bette", "Blette (plante)"), ("Bouleau", ), ("Jonquille", ), ("Aulne", ), ("Greffoir", ), ("Pervenche", ), ("Charme", ), ("Morille", "Morchella"), ("Hêtre", "Fagus sylvatica"), ("Abeille", ), ("Laitue", ), ("Mélèze", ), ("Ciguë", "Apiaceae"), ("Radis", ), ("Ruche", ), ("Gainier", "Arbre de Judée"), ("Romaine", "Laitue romaine"), ("Marronnier", "Marronnier commun"), ("Roquette", "Roquette (plante)"), ("Pigeon", ), ("Lilas (commun)", "Syringa vulgaris"), ("Anémone", ), ("Pensée", "Viola (genre végétal)"), ("Myrtile", ), ("Couvoir", )],
    [# Floréal
        ("Rose", "Rose (fleur)"), ("Chêne", ), ("Fougère", ), ("Aubépine", ), ("Rossignol", ), ("Ancolie", ), ("Muguet", "Muguet de mai"), ("Champignon", ), ("Hyacinthe", "Hyacinthus"), ("Râteau", "Râteau (outil)"), ("Rhubarbe", ), ("Sainfoin", ), ("Bâton-d'or", "Erysimum"), ("Chamérisier", "Lonicera xylosteum"), ("Ver à soie", ), ("Consoude", ), ("Pimprenelle", ), ("Corbeille d'or", ), ("Arroche", ), ("Sarcloir", ), ("Statice", "Armérie maritime"), ("Fritillaire", ), ("Bourrache", ), ("Valériane", ), ("Carpe", "Carpe (poisson)"), ("Fusain", ), ("Civette", ), ("Buglosse", "Anchusa"), ("Sénevé", "Moutarde blanche"), ("Houlette", "Houlette (agriculture)")],
    [# Prairial
        ("Luzerne", "Luzerne cultivée"), ("Hémérocalle", ), ("Trèfle", ), ("Angélique", "Angelica"), ("Canard", ), ("Mélisse", ), ("Fromental", "Fromental (plante)"), ("Lis martagon", ), ("Serpolet", ), ("Faux", "Faux (outil)"), ("Fraise", "Fraise (fruit)"), ("Bétoine", ), ("Pois", ), ("Acacia", "Robinia pseudoacacia"), ("Caille", ), ("Œillet", ), ("Sureau", ), ("Pavot", ), ("Tilleul", ), ("Fourche", ), ("Barbeau", "Centaurea cyanus"), ("Camomille", "Camomille romaine"), ("Chèvrefeuille", ), ("Caille-lait", ), ("Tanche", ), ("Jasmin", ), ("Verveine", ), ("Thym", ), ("Pivoine", ), ("Chariot", )],
    [# Messidor
        ("Seigle", ), ("Avoine", "Avoine cultivée"), ("Oignon", ), ("Véronique", "Véronique (plante)"), ("Mulet", ), ("Romarin", ), ("Concombre", ), ("Échalote", ), ("Absinthe", "Absinthe (plante)"), ("Faucille", ), ("Coriandre", ), ("Artichaut", ), ("Girofle", ), ("Lavande", ), ("Chamois", ), ("Tabac", ), ("Groseille", ), ("Gesse", "Lathyrus"), ("Cerise", ), ("Parc", ), ("Menthe", ), ("Cumin", ), ("Haricot", ), ("Orcanète", "Orcanette des teinturiers"), ("Pintade", ), ("Sauge", ), ("Ail", "ail cultivé"), ("Vesce", ), ("Blé", ), ("Chalemie", )],
    [# Thermidor
        ("Épeautre", ), ("Bouillon-blanc", ), ("Melon", "Melon (plante)"), ("Ivraie", ), ("Bélier", ), ("Prêle", "Sphenophyta"), ("Armoise", ), ("Carthame", ), ("Mûre", "Mûre (fruit de la ronce)"), ("Arrosoir", ), ("Panic", "Panic (plante)"), ("Salicorne", ), ("Abricot", ), ("Basilic", "Basilic (plante)"), ("Brebis", "Mouton"), ("Guimauve", "Guimauve officinale"), ("Lin", "Lin cultivé"), ("Amande", ), ("Gentiane", ), ("Écluse", ), ("Carline", ), ("Câprier", ), ("Lentille", "Lentille cultivée"), ("Aunée", "Inule"), ("Loutre", ), ("Myrte", ), ("Colza", ), ("Lupin", ), ("Coton", ), ("Moulin", )],
    [# Fructidor
        ("Prune", "Prune (fruit)"), ("Millet", "Millet (graminée)"), ("Lycoperdon", "Vesse-de-loup"), ("Escourgeon", ), ("Saumon", ), ("Tubéreuse", ), ("Sucrion", "Escourgeon"), ("Apocyn", "Asclépiade commune"), ("Réglisse", ), ("Échelle", "Échelle (outil)"), ("Pastèque", ), ("Fenouil", ), ("Épine vinette", ), ("Noix", ), ("Truite", ), ("Citron", ), ("Cardère", "Cardère sauvage"), ("Nerprun", "Rhamnus"), ("Tagette", "Tagetes"), ("Hotte", ), ("Églantier", "Rosa canina"), ("Noisette", ), ("Houblon", ), ("Sorgho", "Sorgho commun"), ("Écrevisse", ), ("Bigarade", ), ("Verge d'or", ), ("Maïs", ), ("Marron", "Marron (fruit)"), ("Panier", )]
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

    def revo(self):
        """
        revo uple
        """
        return d_to_french_revolutionary(self)

    def revol_strftime(self, fmt):
        """ modify fmt with specific revol format """
        rdate = d_to_french_revolutionary(self)
        newformat = []
        push = lambda val: newformat.append(str(val))
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
                            elif char == "I":
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push("")
                                else:
                                    push("{}{}".format(BASE_MONTH_IMAGE,
                                                        REV_MONTH_IMAGES[rdate['mois']]))
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
                                    push(FETES[rdate['mois']][rdate['jour']][0])
                            elif char == "F":
                                #wikipedia url of the fete of the day.
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push("")
                                else:
                                    try:
                                        resource = FETES[rdate['mois']][rdate['jour']][1]
                                    except IndexError:
                                        resource = FETES[rdate['mois']][rdate['jour']][0]
                                    push("{}{}".format(WIKI_BASE_URL, resource.replace(" ", "_")))

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
            %rI link to wikipedia image for the month.
            %rm Month as a zero-padded decimal number.
            %ry Year as decimal number.
            %rY Year as Romanian number.
            %rW Decade number in the year.
            %rf grain, pasture, trees, roots, flowers, fruits, animal, tool assciated with the day
            %rF link to the french wikipage associated with the day
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


def my_display(argv):
    """
    display date as I want
    """
    ldate = RDate.today()
    if len(argv) == 2:
        ldate = None
        try:
            delay = int(argv[1])
            tdate = datetime.date.today() + datetime.timedelta(delay)
            ldate = RDate(tdate.year, tdate.month, tdate.day)
        except ValueError:
            print("value error")
    if len(argv) == 4:
        ldate = RDate(int(argv[1]),
                    int(argv[2]),
                    int(argv[3]))
    print("{0:%rA %rd %rB %rY(%ry)}".format(ldate))
    print("{0} {0:%rf %rF}".format(ldate))
    print("{0:%rB : %rI}".format(ldate))

    print("")

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        if sys.argv[1].startswith("test"):
            tests()
            exit()
    my_display(sys.argv)
