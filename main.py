# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:18:02 2024

@author: Bindler, Sebastian

"""

###### --- User Input --- #####

#Add Custom Tag for PVP
customTag1 = "!#PVP"
customTag2 = ""
customTag3 = ""

#Add Custom Tag for Trade
customTagTrade1 = "!#pvptrade"
customTagTrade2 = "!#trade"
customTagTrade3 = ""

# Max Rank
maxRankGreatLiga = 50
maxRankUltraLiga = 50
maxRankMasterLiga = 30

# IVs 0 - 4 for Great
atkMinGreat = "0"
atkMaxGreat = "2"
defMinGreat = "3"
defMaxGreat = "4"
hpMinGreat = "3"
hpMaxGreat = "4"

# IVs 0 - 4 for Ultra
atkMinUltra = "0"
atkMaxUltra = "2"
defMinUltra = "3"
defMaxUltra = "4"
hpMinUltra = "3"
hpMaxUltra = "4"

# IVs 0 - 4 for Master
atkMinMaster = "4"
atkMaxMaster = "4"
defMinMaster = "3"
defMaxMaster = "4"
hpMinMaster = "3"
hpMaxMaster = "4"

###############################
import glob
import csv
import json 

targetPatternGreatLiga = r"input/cp1500*.csv"
targetPatternUltraLiga = r"input/cp2500*.csv"
targetPatternMasterLiga = r"input/cp10000*.csv"

filenameOutputDeGreat = "output/de/searchGreat.txt"
filenameOutputDeUltra = "output/de/searchUltra.txt"
filenameOutputDeMaster = "output/de/searchMaster.txt"
filenameOutputDeGreatAndUltra = "output/de/searchGreatAndUltra.txt"

filenameOutputTradeDeGreat = "output/de/tradeGreat.txt"
filenameOutputTradeDeUltra = "output/de/tradeUltra.txt"
filenameOutputTradeDeMaster = "output/de/tradeMaster.txt"
filenameOutputDeTradeGreatAndUltra = "output/de/tradeGratAndUltra.txt"

filenameOutputEnGreat = "output/en/searchGreat.txt"
filenameOutputEnUltra = "output/en/searchUltra.txt"
filenameOutputEnMaster = "output/en/searchMaster.txt"
filenameOutputEnGreatAndUltra = "output/en/searchGreatAndUltra.txt"
filenameOutputEnTradeGreatAndUltra = "output/en/searchTradeGratAndUltra.txt"

filenameOutputTradeEnGreat = "output/en/tradeGreat.txt"
filenameOutputTradeEnUltra = "output/en/tradeUltra.txt"
filenameOutputTradeEnMaster = "output/en/tradeMaster.txt"
filenameOutputEnTradeGreatAndUltra = "output/en/tradeGratAndUltra.txt"

listGreat = []
listUltra = []
listMaster = []

deOutputGreat = "{}-{}angriffs-wert&{}-{}verteidigungs-wert&{}-{}kp&wp-1500".format(atkMinGreat, atkMaxGreat, defMinGreat, defMaxGreat, hpMinGreat, hpMaxGreat)
enOutputGreat = "{}-{}attack&{}-{}defsnse&{}-{}hp&cp-1500".format(atkMinGreat, atkMaxGreat, defMinGreat, defMaxGreat, hpMinGreat, hpMaxGreat)

deOutputUltra = "{}-{}angriffs-wert&{}-{}verteidigungs-wert&{}-{}kp&wp-2500".format(atkMinUltra, atkMaxUltra, defMinUltra, defMaxUltra, hpMinUltra, hpMaxUltra)
enOutputUltra = "{}-{}attack&{}-{}defsnse&{}-{}hp&cp-2500".format(atkMinUltra, atkMaxUltra, defMinUltra, defMaxUltra, hpMinUltra, hpMaxUltra)

deOutputMaster = "{}-{}angriffs-wert&{}-{}verteidigungs-wert&{}-{}kp".format(atkMinMaster, atkMaxMaster, defMinMaster, defMaxMaster, hpMinMaster, hpMaxMaster)
enOutputMaster = "{}-{}attack&{}-{}defsnse&{}-{}hp".format(atkMinMaster, atkMaxMaster, defMinMaster, defMaxMaster, hpMinMaster, hpMaxMaster)

deOutputTradeGreat ="Entfernung0-105&!Favorit&!Getauscht&!4*&!Schillernd&!Erlöst&!Ultrabestien&!Crypto&!Legendär&!Mysteriös&!Jahr2016&!Jahr2017&!Jahr2018&!Jahr2019&!Jahr2020&!Jahr2021&!Jahr2022&!Jahr2023&!Kumpel1&!Kumpel2&!Kumpel3&!Kumpel4&!Kumpel5&!Hintergrund"
deOutputTradeUltra ="Entfernung0-105&!Favorit&!Getauscht&!4*&!Schillernd&!Erlöst&!Ultrabestien&!Crypto&!Legendär&!Mysteriös&!Jahr2016&!Jahr2017&!Jahr2018&!Jahr2019&!Jahr2020&!Jahr2021&!Jahr2022&!Jahr2023&!Kumpel1&!Kumpel2&!Kumpel3&!Kumpel4&!Kumpel5&!Hintergrund"
deOutputTradeMaster ="Entfernung0-105&!Favorit&!Getauscht&!4*&!Schillernd&!Erlöst&!Crypto&!Mysteriös&!Jahr2016&!Jahr2017&!Jahr2018&!Jahr2019&!Jahr2020&!Jahr2021&!Jahr2022&!Jahr2023&!Kumpel1&!Kumpel2&!Kumpel3&!Kumpel4&!Kumpel5&!Hintergrund"

enOutputTradeGreat ="distance0-105&!favourite&!traded&!4*&!shiny&!purified&!ultra beasts&!shadow&!legendary&!mythical&!year2016&!year2017&!year2018&!year2019&!year2020&!year2021&!year2022&!year2023&!Buddy1&!Buddy2&!Buddy3&!Buddy4&!Buddy5&!location cards"
enOutputTradeUltra ="distance0-105&!favourite&!traded&!4*&!shiny&!purified&!ultra beasts&!shadow&!legendary&!mythical&!year2016&!year2017&!year2018&!year2019&!year2020&!year2021&!year2022&!year2023&!Buddy1&!Buddy2&!Buddy3&!Buddy4&!Buddy5&!location cards"
enOutputTradeMaster ="distance0-105&!favourite&!traded&!4*&!shiny&!purified&!shadow&!mythical&!year2016&!year2017&!year2018&!year2019&!year2020&!year2021&!year2022&!year2023&!Buddy1&!Buddy2&!Buddy3&!Buddy4&!Buddy5&!location cards"

def getPokemonList(_target, _max, _list):
    with open(_target) as csvdatei:
        csv_reader_object = csv.reader(csvdatei)
        for row in csv_reader_object:
            if row[2] != "Dex" and len(_list) < _max:
                _list.append(int(row[2]))         
    return _list

def cleanList(_list):
    _list = list(dict.fromkeys(_list))
    return sorted(_list)

def getList(_list, _json):
    Output = ""
    for i in range(len(_list)):
        
        with open(_json, 'r') as json_data:
            data = json.load(json_data)
            Output = Output + "+" + data[str(_list[i])] + ","
            json_data.close()
    return Output.rstrip(',')

if __name__ == "__main__":
    
    targetPatternGreatLiga = glob.glob(targetPatternGreatLiga)[0]
    targetPatternUltraLiga = glob.glob(targetPatternUltraLiga)[0]
    targetPatternMasterLiga = glob.glob(targetPatternMasterLiga)[0]
    
    listGreat = getPokemonList(targetPatternGreatLiga, maxRankGreatLiga, listGreat)
    listUltra = getPokemonList(targetPatternUltraLiga, maxRankUltraLiga, listUltra)
    listMaster = getPokemonList(targetPatternMasterLiga, maxRankMasterLiga, listMaster)
    
    listGreat = cleanList(listGreat)
    listUltra = cleanList(listUltra)
    listMaster = cleanList(listMaster)
    
    if customTag1 != "":
        deOutputGreat = deOutputGreat + "&" + customTag1
        enOutputGreat = enOutputGreat + "&" + customTag1
        deOutputUltra = deOutputUltra + "&" + customTag1
        enOutputUltra = enOutputUltra + "&" + customTag1
        deOutputMaster = deOutputMaster + "&" + customTag1
        enOutputMaster = enOutputMaster + "&" + customTag1
    
    if customTag2 != "":
        deOutputGreat = deOutputGreat + "&" + customTag2
        enOutputGreat = enOutputGreat + "&" + customTag2
        deOutputUltra = deOutputUltra + "&" + customTag2
        enOutputUltra = enOutputUltra + "&" + customTag2
        deOutputMaster = deOutputMaster + "&" + customTag2
        enOutputMaster = enOutputMaster + "&" + customTag2
        
    if customTag3 != "":
        deOutputGreat = deOutputGreat + "&" + customTag3
        enOutputGreat = enOutputGreat + "&" + customTag3
        deOutputUltra = deOutputUltra + "&" + customTag3
        enOutputUltra = enOutputUltra + "&" + customTag3
        deOutputMaster = deOutputMaster + "&" + customTag3
        enOutputMaster = enOutputMaster + "&" + customTag3
        
    if customTagTrade1 != "":
        deOutputTradeTradeGreat = deOutputTradeGreat + "&" + customTagTrade1
        enOutputTradeGreat = enOutputTradeGreat + "&" + customTagTrade1
        deOutputTradeUltra = deOutputTradeUltra + "&" + customTagTrade1
        enOutputTradeUltra = enOutputTradeUltra + "&" + customTagTrade1
        deOutputTradeMaster = deOutputTradeMaster + "&" + customTagTrade1
        enOutputTradeMaster = enOutputTradeMaster + "&" + customTagTrade1
    
    if customTagTrade2 != "":
        deOutputTradeGreat = deOutputTradeGreat + "&" + customTagTrade2
        enOutputTradeGreat = enOutputTradeGreat + "&" + customTagTrade2
        deOutputTradeUltra = deOutputTradeUltra + "&" + customTagTrade2
        enOutputTradeUltra = enOutputTradeUltra + "&" + customTagTrade2
        deOutputTradeMaster = deOutputTradeMaster + "&" + customTagTrade2
        enOutputTradeMaster = enOutputTradeMaster + "&" + customTagTrade2
        
    if customTagTrade3 != "":
        deOutputTradeGreat = deOutputTradeGreat + "&" + customTagTrade3
        enOutputTradeGreat = enOutputTradeGreat + "&" + customTagTrade3
        deOutputTradeUltra = deOutputTradeUltra + "&" + customTagTrade3
        enOutputTradeUltra = enOutputTradeUltra + "&" + customTagTrade3
        deOutputTradeMaster = deOutputTradeMaster + "&" + customTagTrade3
        enOutputTradeMaster = enOutputTradeMaster + "&" + customTagTrade3   

    
    with open("README.md", "w", encoding="utf-16") as readme:
        
        readme.write("# German\n\n")
        readme.write("### Superliga suche\n`" + deOutputGreat + "&" + getList(cleanList(listGreat),'lang/de.json') +"`\n\n")
        readme.write("### Hyperliga suche\n`" + deOutputUltra + "&" + getList(cleanList(listUltra),'lang/de.json') +"`\n\n")
        readme.write("### Meisterliga suche\n`" + deOutputMaster + "&" + getList(cleanList(listMaster),'lang/de.json') +"`\n\n")
        readme.write("### Super- und Hyperliga suche\n`" + deOutputUltra + "&" + getList(cleanList(listGreat + listUltra),'lang/de.json') +"`\n\n")
        readme.write("### Superliga tauschgesuche\n`" + deOutputTradeGreat + "&" + getList(cleanList(listGreat),'lang/de.json') +"`\n\n")
        readme.write("### Hyperliga tauschgesuche\n`" + deOutputTradeUltra + "&" + getList(cleanList(listUltra),'lang/de.json') +"`\n\n")
        readme.write("### Meisterliga tauschgesuche\n`" + deOutputTradeMaster + "&" + getList(cleanList(listMaster),'lang/de.json') +"`\n\n")
        readme.write("### Super- und Hyperliga tauschgesuche\n`" + deOutputTradeUltra + "&" + getList(cleanList(listGreat + listUltra),'lang/de.json') +"`\n\n")
        
        readme.write("\n")
        
        readme.write("# English\n\n")
        readme.write("### Greatliga search\n`" + enOutputGreat + "&" + getList(cleanList(listGreat),'lang/en.json') +"`\n\n")
        readme.write("### Ultraliga search\n`" + enOutputUltra + "&" + getList(cleanList(listUltra),'lang/en.json') +"`\n\n")
        readme.write("### Masterliga search\n`" + enOutputMaster + "&" + getList(cleanList(listMaster),'lang/en.json') +"`\n\n")
        readme.write("### Great- and Ultraliga search\n`" + enOutputUltra + "&" + getList(cleanList(listGreat + listUltra),'lang/en.json') +"`\n\n")
        readme.write("### Greatliga trade search\n`" + enOutputTradeGreat + "&" + getList(cleanList(listGreat),'lang/en.json') +"`\n\n")
        readme.write("### Ultraliga trade search\n`" + enOutputTradeUltra + "&" + getList(cleanList(listUltra),'lang/en.json') +"`\n\n")
        readme.write("### Masterliga trade search\n`" + enOutputTradeMaster + "&" + getList(cleanList(listMaster),'lang/en.json') +"`\n\n")
        readme.write("### Great- and Ultraliga trade search\n`" + enOutputTradeUltra + "&" + getList(cleanList(listGreat + listUltra),'lang/en.json') +"`\n\n")
        
        readme.close()
        
    with open(filenameOutputDeGreat, "w", encoding="utf-16") as o:
        o.write(deOutputGreat + "&" + getList(cleanList(listGreat),'lang/de.json'))     
        o.close()
    with open(filenameOutputDeUltra, "w", encoding="utf-16") as o:
        o.write(deOutputUltra + "&" + getList(cleanList(listUltra),'lang/de.json'))
        o.close()
    with open(filenameOutputDeMaster, "w", encoding="utf-16") as o:
        o.write(deOutputMaster + "&" + getList(cleanList(listMaster),'lang/de.json'))
        o.close()
    with open(filenameOutputDeGreatAndUltra, "w", encoding="utf-16") as o:
        o.write(deOutputUltra + "&" + getList(cleanList(listGreat + listUltra),'lang/de.json'))
        o.close()
        
    with open(filenameOutputTradeDeGreat, "w", encoding="utf-16") as o:
        o.write(deOutputTradeGreat + "&" + getList(cleanList(listGreat),'lang/de.json'))
        o.close()
    with open(filenameOutputTradeDeUltra, "w", encoding="utf-16") as o:
        o.write(deOutputTradeUltra + "&" + getList(cleanList(listUltra),'lang/de.json'))
        o.close()
    with open(filenameOutputTradeDeMaster, "w", encoding="utf-16") as o:
        o.write(deOutputTradeMaster + "&" + getList(cleanList(listMaster),'lang/de.json'))
        o.close()
    with open(filenameOutputDeTradeGreatAndUltra, "w", encoding="utf-16") as o:
        o.write(deOutputTradeGreat + "&" + getList(cleanList(listGreat + listUltra),'lang/de.json'))
        o.close()
      
    with open(filenameOutputEnGreat, "w", encoding="utf-16") as o:
        o.write(enOutputGreat + "&" + getList(cleanList(listGreat),'lang/en.json'))
        o.close()
    with open(filenameOutputEnUltra, "w", encoding="utf-16") as o:
        o.write(enOutputUltra + "&" + getList(cleanList(listUltra),'lang/en.json'))
        o.close()
    with open(filenameOutputEnMaster, "w", encoding="utf-16") as o:
        o.write(enOutputMaster + "&" + getList(cleanList(listMaster),'lang/en.json'))
        o.close()
    with open(filenameOutputEnGreatAndUltra, "w", encoding="utf-16") as o:
        o.write(enOutputUltra + "&" + getList(cleanList(listGreat + listUltra),'lang/en.json'))
        o.close()
        
    with open(filenameOutputTradeEnGreat, "w", encoding="utf-16") as o:
        o.write(deOutputTradeGreat + "&" + getList(cleanList(listGreat),'lang/en.json'))
        o.close()
    with open(filenameOutputTradeEnUltra, "w", encoding="utf-16") as o:
        o.write(deOutputTradeUltra + "&" + getList(cleanList(listUltra),'lang/en.json'))
        o.close()
    with open(filenameOutputTradeEnMaster, "w", encoding="utf-16") as o:
        o.write(deOutputTradeMaster + "&" + getList(cleanList(listMaster),'lang/en.json'))
        o.close()
    with open(filenameOutputEnTradeGreatAndUltra, "w", encoding="utf-16") as o:
        o.write(deOutputTradeGreat + "&" + getList(cleanList(listGreat + listUltra),'lang/en.json'))
        o.close()
            
        

    