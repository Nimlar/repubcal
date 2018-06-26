#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
"""
Provide an extension of datetime to manage revolutionnary date
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
SANSCULOTTIDES = ['Jour de la vertu', 'Jour du génie', 'Jour du travail', 'Jour de l’opinion',
                  'Jour des récompenses', 'Jour de la Révolution']

FETES = [
    [# Vendémiaire
        ("le Raisin", "Raisin", "🍇"), ("le Safran", "Safran (épice)"), ("la Châtaigne", "Châtaigne"), ("le Colchique", "Colchique"), ("le Cheval", "Cheval"), ("la Balsamine", "Balsaminaceae"), ("la Carotte", "Carotte"), ("l’Amarante", "Amarante (plante)"), ("le Panais", "Panais"), ("la Cuve", "Cuve"), ("la Pomme de terre", "Pomme de terre"), ("l’Immortelle", "Immortelle commune"), ("le Potiron", "Potiron"), ("le Réséda", "Réséda"), ("l’Âne", "Âne"), ("la Belle de nuit", "Mirabilis jalapa"), ("la Citrouille", "Citrouille", "🎃"), ("le Sarrasin", "Sarrasin (plante)"), ("le Tournesol", "Tournesol", "🌻"), ("le Pressoir", "Pressoir"), ("le Chanvre", "Chanvre"), ("la Pêche", "Pêche (fruit)", "🍑"), ("le Navet", "Navet"), ("l’Amaryllis", "Amaryllis (plante)"), ("le Bœuf", "Bos taurus"), ("l’Aubergine", "Aubergine", "🍆"), ("le Piment", "Piment"), ("la Tomate", "Tomate", "🍅"), ("l’Orge", "Orge commune"), ("le Tonneau", "Tonneau (récipient)")],
    [# Brumaire
        ("la Pomme", "Pomme", "🍎🍏"), ("le Céleri", "Céleri"), ("la Poire", "Poire", "🍐"), ("la Betterave", "Betterave"), ("l’Oie", "Oie"), ("l’Héliotrope", "Héliotrope"), ("la Figue", "Figue"), ("la Scorsonère", "Scorsonère"), ("l’Alisier", "Sorbus torminalis"), ("la Charrue", "Charrue"), ("le Salsifis", "Salsifis"), ("la Mâcre", "Mâcre nageante"), ("le Topinambour", "Topinambour"), ("l’Endive", "Endive"), ("le Dindon", "Dinde"), ("le Chervis", "Chervis"), ("le Cresson", "Cresson de fontaine"), ("la Dentelaire", "Plumbago"), ("la Grenade", "Grenade (fruit)"), ("la Herse", "Herse (agriculture)"), ("la Bacchante", "Baccharis halimifolia"), ("l’Azerole", "Azerole"), ("la Garance", "Garance des teinturiers"), ("l’Orange", "Orange (fruit)"), ("le Faisan", "Faisan"), ("la Pistache", "Pistache"), ("le Macjonc", "Gesse tubéreuse"), ("le Coing", "Coing"), ("le Cormier", "Cormier"), ("le Rouleau", "Rouleau agricole")],
    [# Frimaire
        ("la Raiponce", "Raiponce (plante)"), ("le Turneps", "Betterave fourragère"), ("la Chicorée", "Chicorée"), ("la Nèfle", "Nèfle"), ("le Cochon", "Cochon"), ("la Mâche", "Mâche"), ("le Chou-fleur", "Chou-fleur"), ("le Miel", "Miel"), ("la Genièvre", "Juniperus communis"), ("la Pioche", "Pioche"), ("la Cire", "Cire"), ("le Raifort", "Raifort"), ("le Cèdre", "Cèdre"), ("le Sapin", "Sapin"), ("le Chevreuil", "Chevreuil"), ("l’Ajonc", "Ajonc"), ("le Cyprès", "Cyprès"), ("le Lierre", "Hedera"), ("la Sabine", "Juniperus sabina"), ("le Hoyau", "Hoyau"), ("l’Érable sucré", "Érable à sucre", "🍁"), ("la Bruyère", "Bruyère"), ("le Roseau", "Roseau"), ("l’Oseille", "Oseille"), ("le Grillon", "Gryllidae"), ("le Pignon", "Pignon de pin"), ("le Liège", "Liège"), ("la Truffe", "Truffe (champignon)"), ("l’Olive", "Olive"), ("la Pelle", "Pelle (outil)")],
    [# Nivôse
        ("la Tourbe", "Tourbe"), ("la Houille", "Houille"), ("le Bitume", "Bitume"), ("le Soufre", "Soufre"), ("le Chien", "Chien"), ("la Lave", "Lave"), ("la Terre végétale", "Humus"), ("le Fumier", "Fumier"), ("le Salpêtre", "Nitrate de potassium"), ("le Fléau", "Fléau (agriculture)"), ("le Granit", "Granit"), ("l’Argile", "Argile"), ("l’Ardoise", "Ardoise"), ("le Grès", "Grès (géologie)"), ("le Lapin", "Oryctolagus cuniculus"), ("le Silex", "Silex"), ("la Marne", "Marne (géologie)"), ("la Pierre à chaux", "Calcaire"), ("le Marbre", "Marbre"), ("le Van", "Van (agriculture)"), ("la Pierre à plâtre", "Gypse"), ("le Sel", "Chlorure de sodium"), ("le Fer", "Fer"), ("le Cuivre", "Cuivre"), ("le Chat", "Chat"), ("l’Étain", "Étain"), ("le Plomb", "Plomb"), ("le Zinc", "Zinc"), ("le Mercure", "Mercure (chimie)"), ("le Crible", "Tamis")],
    [# Pluviôse
        ("la Lauréole", "Lauréole"), ("la Mousse", "Bryophyta"), ("le Fragon", "Ruscus aculeatus"), ("le Perce-neige", "Perce-neige"), ("le Taureau", "Taureau"), ("le Laurier tin", "Viorne tin"), ("l’Amadouvier", "Amadouvier"), ("le Mézéréon", "Bois-joli"), ("le Peuplier", "Peuplier"), ("la Cognée", "Cognée"), ("l’Ellébore", "Hellébore"), ("le Brocoli", "Brocoli"), ("le Laurier", "Laurus nobilis"), ("l’Avelinier", "Noisetier"), ("la Vache", "Vache"), ("le Buis", "Buis"), ("le Lichen", "Lichen"), ("l’If", "Taxus"), ("la Pulmonaire", "pulmonaria"), ("la Serpette", "Serpette"), ("le Thlaspi", "Thlaspi"), ("le Thimele", "Daphné garou"), ("le Chiendent", "Chiendent"), ("la Trainasse", "Renouée des oiseaux"), ("le Lièvre", "Lièvre"), ("la Guède", "Guède"), ("le Noisetier", "Noisetier"), ("le Cyclamen", "Cyclamen"), ("la Chélidoine", "Chelidonium majus"), ("le Traîneau", "Traîneau")],
    [# Ventôse
        ("le Tussilage", "Tussilage"), ("le Cornouiller", "Cornus (plante)"), ("le Violier", "Vélar"), ("le Troène", "Troène"), ("le Bouc", "Bouc (animal)"), ("l’Asaret", "Asaret"), ("l’Alaterne", "Nerprun alaterne"), ("la Violette", "Viola (genre végétal)"), ("le Marceau", "Saule marsault"), ("la Bêche", "Bêche"), ("la Narcisse", "Narcissus"), ("l’Orme", "Orme"), ("la Fumeterre", "Fumeterre"), ("le Vélar", "Erysimum"), ("la Chèvre", "Chèvre"), ("l’Épinard", "Épinard"), ("le Doronic", "Doronicum"), ("le Mouron", "Mouron (flore)"), ("le Cerfeuil", "Cerfeuil commun"), ("le Cordeau", "Cordeau"), ("la Mandragore", "Mandragore"), ("le Persil", "Persil"), ("la Cochléaire", "Cochlearia"), ("la Pâquerette", "Pâquerette"), ("le Thon", "Thon"), ("le Pissenlit", "Pissenlit"), ("la Sylvie", "Anémone sylvie"), ("la Capillaire", "Capillaire de Montpellier"), ("le Frêne", "Frêne"), ("le Plantoir", "Plantoir")],
    [# Germinal
        ("la Primevère", "Primevère"), ("le Platane", "Platane"), ("l’Asperge", "Asperge"), ("la Tulipe", "Tulipe", "🌷"), ("la Poule", "Poule (animal)"), ("la Bette", "Blette (plante)"), ("le Bouleau", "Bouleau"), ("la Jonquille", "Jonquille"), ("l’Aulne", "Aulne"), ("le Couvoir", "Couvoir"), ("la Pervenche", "Pervenche"), ("le Charme", "Charme"), ("la Morille", "Morchella"), ("le Hêtre", "Fagus sylvatica"), ("l’Abeille", "Abeille"), ("la Laitue", "Laitue"), ("le Mélèze", "Mélèze"), ("la Ciguë", "Apiaceae"), ("le Radis", "Radis"), ("la Ruche", "Ruche"), ("le Gainier", "Arbre de Judée"), ("la Romaine", "Laitue romaine"), ("le Marronnier", "Marronnier commun"), ("la Roquette", "Roquette (plante)"), ("le Pigeon", "Pigeon"), ("le Lilas (commun)", "Syringa vulgaris"), ("l’Anémone", "Anémone"), ("la Pensée", "Viola (genre végétal)"), ("la Myrtille", "Myrtille"), ("le Greffoir", "Greffoir")],
    [# Floréal
        ("la Rose", "Rose (fleur)", "🌹"), ("le Chêne", "Chêne"), ("la Fougère", "Fougère"), ("l’Aubépine", "Aubépine"), ("le Rossignol", "Rossignol"), ("l’Ancolie", "Ancolie"), ("le Muguet", "Muguet de mai"), ("le Champignon", "Champignon", "🍄"), ("l’Hyacinthe", "Hyacinthus"), ("le Râteau", "Râteau (outil)"), ("la Rhubarbe", "Rhubarbe"), ("le Sainfoin", "Sainfoin"), ("le Bâton-d'or", "Erysimum"), ("le Chamérisier", "Lonicera xylosteum"), ("le Ver à soie", "Ver à soie"), ("la Consoude", "Consoude"), ("la Pimprenelle", "Pimprenelle"), ("la Corbeille d'or", "Corbeille d'or"), ("l’Arroche", "Arroche"), ("le Sarcloir", "Sarcloir"), ("le Statice", "Armérie maritime"), ("la Fritillaire", "Fritillaire"), ("la Bourrache", "Bourrache"), ("la Valériane", "Valériane"), ("la Carpe", "Carpe (poisson)"), ("le Fusain", "Fusain d'Europe"), ("la Civette", "Ciboulette (botanique)"), ("la Buglosse", "Anchusa"), ("le Sénevé", "Moutarde blanche"), ("la Houlette", "Houlette (agriculture)")],
    [# Prairial
        ("la Luzerne", "Luzerne cultivée"), ("l’Hémérocalle", "Hémérocalle"), ("le Trèfle", "Trèfle"), ("l’Angélique", "Angelica"), ("le Canard", "Canard"), ("la Mélisse", "Mélisse"), ("le Fromental", "Fromental (plante)"), ("le Lis martagon", "Lis martagon"), ("le Serpolet", "Serpolet"), ("la Faux", "Faux (outil)"), ("la Fraise", "Fraise (fruit)", "🍓"), ("la Bétoine", "Bétoine"), ("le Pois", "Pois"), ("l’Acacia", "Robinia pseudoacacia"), ("la Caille", "Caille"), ("l’Œillet", "Œillet"), ("le Sureau", "Sureau"), ("le Pavot", "Pavot"), ("le Tilleul", "Tilleul"), ("la Fourche", "Fourche"), ("le Barbeau", "Centaurea cyanus"), ("la Camomille", "Camomille romaine"), ("le Chèvrefeuille", "Chèvrefeuille"), ("le Caille-lait", "Caille-lait"), ("la Tanche", "Tanche"), ("le Jasmin", "Jasmin"), ("la Verveine", "Verveine"), ("le Thym", "Thym"), ("la Pivoine", "Pivoine"), ("le Chariot", "Chariot")],
    [# Messidor
        ("le Seigle", "Seigle"), ("l’Avoine", "Avoine cultivée"), ("l’Oignon", "Oignon"), ("la Véronique", "Véronique (plante)"), ("le Mulet", "Mulet"), ("le Romarin", "Romarin"), ("le Concombre", "Concombre"), ("l’Échalote", "Échalote"), ("l’Absinthe", "Absinthe (plante)"), ("la Faucille", "Faucille"), ("la Coriandre", "Coriandre"), ("l’Artichaut", "Artichaut"), ("la Girofle", "Girofle"), ("la Lavande", "Lavande"), ("le Chamois", "Chamois"), ("le Tabac", "Tabac"), ("la Groseille", "Groseille"), ("la Gesse", "Lathyrus"), ("la Cerise", "Cerise", "🍒"), ("le Parc", "Parc"), ("la Menthe", "Menthe"), ("le Cumin", "Cumin"), ("le Haricot", "Haricot"), ("l’Orcanète", "Orcanette des teinturiers"), ("la Pintade", "Pintade"), ("la Sauge", "Sauge"), ("l’Ail", "ail cultivé"), ("la Vesce", "Vesce"), ("le Blé", "Blé"), ("la Chalemie", "Chalemie")],
    [# Thermidor
        ("l’Épeautre", "Épeautre"), ("le Bouillon-blanc", "Bouillon-blanc"), ("le Melon", "Melon (plante)", "🍈"), ("l’Ivraie", "Ivraie"), ("le Bélier", "Bélier"), ("la Prêle", "Sphenophyta"), ("l’Armoise", "Armoise"), ("la Carthame", "Carthame"), ("la Mûre", "Mûre (fruit de la ronce)"), ("l’Arrosoir", "Arrosoir"), ("le Panic", "Panic (plante)"), ("la Salicorne", "Salicorne"), ("l’Abricot", "Abricot"), ("le Basilic", "Basilic (plante)"), ("la Brebis", "Mouton"), ("la Guimauve", "Guimauve officinale"), ("le Lin", "Lin cultivé"), ("l’Amande", "Amande"), ("la Gentiane", "Gentiane"), ("l’Écluse", "Écluse"), ("la Carline", "Carline"), ("le Câprier", "Câprier"), ("la Lentille", "Lentille cultivée"), ("l’Aunée", "Inule"), ("la Loutre", "Loutre"), ("la Myrte", "Myrte"), ("le Colza", "Colza"), ("le Lupin", "Lupin"), ("le Coton", "Coton"), ("le Moulin", "Moulin")],
    [# Fructidor
        ("la Prune", "Prune (fruit)"), ("le Millet", "Millet (graminée)"), ("le Lycoperdon", "Vesse-de-loup"), ("l’Escourgeon", "Escourgeon"), ("le Saumon", "Saumon"), ("la Tubéreuse", "Tubéreuse"), ("le Sucrion", "Escourgeon"), ("l’Apocyn", "Asclépiade commune"), ("la Réglisse", "Réglisse"), ("l’Échelle", "Échelle (outil)"), ("la Pastèque", "Pastèque", "🍉"), ("le Fenouil", "Fenouil"), ("l’Épine vinette", "Épine vinette"), ("la Noix", "Noix"), ("la Truite", "Truite"), ("le Citron", "Citron", "🍋"), ("la Cardère", "Cardère sauvage"), ("le Nerprun", "Rhamnus"), ("la Tagette", "Tagetes"), ("la Hotte", "Panier"), ("l’Églantier", "Rosa canina"), ("la Noisette", "Noisette"), ("le Houblon", "Houblon"), ("le Sorgho", "Sorgho commun"), ("l’Écrevisse", "Écrevisse"), ("la Bigarade", "Bigarade"), ("la Verge d'or", "Verge d'or"), ("le Maïs", "Maïs", "🌽"), ("le Marron", "Marron (fruit)", "🌰"), ("le Panier", "Panier")]
]

def int_to_roman(value):
    """
    Convert from decimal to Roman
    """
    if not 0 <= value < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    for i in range(len(ints)):
        count = int(value // ints[i])
        result.append(nums[i] * count)
        value -= ints[i] * count
    return "".join(result)

def annee_de_la_revolution(date):
    """
    Find corresponding revolutionnary year of current date
    """
    # Time are in UT (time at Greenwich meridian, so 0°)
    # but we want the equinox at Paris meridian time so 2°20'13,82" (the one used in 1792)
    # using the IGN value 2°20'13,82", add 14ms...
    # see http://geodesie.ign.fr/contenu/fichiers/Meridiens_greenwich_paris.pdf (fr)
    # => +0.15581138888888888888 hour == .00649214120370370370
    lasteq = ephem.Date(ephem.previous_autumn_equinox(date) + 0.00649214120370370370)
    nexteq = ephem.Date(ephem.next_autumn_equinox(date) + 0.00649214120370370370)


#    print(lasteq, nexteq)
    neq_dt = nexteq.datetime()
    if neq_dt.year == date.year and neq_dt.month == date.month and neq_dt.day == date.day:
        #the autumn equinox is the day we ask for (but after 00:00), so the lasteq is the current day
        lasteq = nexteq

    year = ((lasteq - ephem.Date(FRENCH_REVOLUTIONARY_EPOCH)) / TROPICAL_YEAR) + 1
    return (int(year), lasteq.datetime().date())

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
    nb_day_in_year = (date - equinoxe).days
    rdate['mois'] = nb_day_in_year / 30
    rdate['jour'] = nb_day_in_year % 30
    rdate['decade'] = (rdate['jour'] // 10) + 1 + 3*rdate['mois']
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
                                #Year as Roman number.
                                push(int_to_roman(rdate['an']))
                            elif char == "W":
                                #Decade number in the year.
                                push(rdate['decade'])
                            elif char == "f":
                                #fete of the day.
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push(SANSCULOTTIDES[rdate['jour'] % 10])
                                else:
                                    push(FETES[rdate['mois']][rdate['jour']][0])
                            elif char == "F":
                                #wikipedia url of the fete of the day.
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push("")
                                else:
                                    resource = FETES[rdate['mois']][rdate['jour']][1]
                                    push("{}{}".format(WIKI_BASE_URL, resource.replace(" ", "_")))
                            elif char == "u":
                                #unicode of the day.
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push("")
                                else:
                                    try:
                                        push(FETES[rdate['mois']][rdate['jour']][2])
                                    except IndexError:
                                        push("")
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
            add some new format to display date
            %r should start any revolutionarry modifiator

            %rA Week^WDecadeday as locale’s full name.
            %rw Week^WDecadeday as a decimal number, where 0 is Primid and 9 is Decadi.

            %rd Day of the month as a zero-padded decimal number.
            %rB Month as locale’s full name
            %rI link to wikipedia image for the month.
            %rm Month as a zero-padded decimal number.
            %ry Year as decimal number.
            %rY Year as Roman number.
            %rW Decade number in the year.
            %rf grain, pasture, trees, roots, flowers, fruits, animal, tool associated with the day
            %rF link to the french wikipage associated with the day
            %ru unicode emoji associated with the day (if exist, else empty)
        """
        if not isinstance(fmt, str):
            raise TypeError("must be str, not %s" % type(fmt).__name__)
        if len(fmt) != 0:
            return self.revol_strftime(fmt)
        return str(self)


def my_display(argv):
    """
    display date as I want
    """
    ldate = RDate.today()
    prefix = "Nous sommes le"
    if len(argv) == 2:
        ldate = None
        try:
            delay = int(argv[1])
            tdate = datetime.date.today() + datetime.timedelta(delay)
            ldate = RDate(tdate.year, tdate.month, tdate.day)
            if delay == 0:
                prefix = "Aujourd’hui ({0:%A %d %B %Y}) nous sommes le".format(ldate)
            elif delay == 1:
                prefix = "Demain ({0:%A %d %B %Y}) sera le".format(ldate)
            elif delay == 2:
                prefix = "Après-demain ({0:%A %d %B %Y}) sera le".format(ldate)
            elif delay == -1:
                prefix = "Hier ({0:%A %d %B %Y}) était le".format(ldate)
            elif delay == -2:
                prefix = "Avant-hier ({0:%A %d %B %Y}) était le".format(ldate)
            else:
                prefix = "Le {0:%A %d %B %Y} correspond à".format(ldate)
        except ValueError:
            print("value error")
    if len(argv) == 4:
        ldate = RDate(int(argv[1]), int(argv[2]), int(argv[3]))
        prefix = "Le {0:%A %d %B %Y} correspond à".format(ldate)
    print("{0} {1:%rA %rd %rB %rY (%ry/%rm/%rd)}".format(prefix, ldate))
    fete_name = "{0:%rf}".format(ldate)
    if fete_name.startswith("le "):
        article = "au"
        fete_name = fete_name[3:]
    else:
        article = "à"
    print("Cette journée est dédiée {} {} {:%rF}".format(article, fete_name, ldate))
    print("{0:%rB : %rI}".format(ldate))

    print("")

if __name__ == "__main__":
    import sys
    my_display(sys.argv)
