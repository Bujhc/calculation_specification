
from itertools import combinations_with_replacement
from sortedcontainers import SortedDict


# calculation volume of the current signals of the programme

def calcBackVolume (backpack):
    total_volume = 0
    for items in backpack:
        total_volume += modules_controller[items]['AI']
    return total_volume

# calculation colume of the current cost of the modules

def calcBackCost (backpack):
    total_cost = 0
    for items in backpack:
        total_cost += modules_controller[items]['price']
    return total_cost

# calculation state of the current quaility of module. it's mean quantity of signals in the module divide on the price

def calcBackQual (backpack):
    total_qual = 0
    for items in backpack:
        total_qual += modules_controller[items]['quality']
    return total_qual

# filter dictionary of the modules controller by "AI" for example

def modefideModulesController (modeles):
    criteria = "AI"
    finish_spisok_modules = []
    for items in modeles:
        if modules_controller[items][criteria] > 0:
            finish_spisok_modules.append(items)
    return finish_spisok_modules


# name of the controoler and module with signals

controller = {'MS-FAC3611-0': {'AI':8, 'BI':6, 'AO':6, 'BO':6, 'CO':0}
        }
modules_controller = {'MS-IOM2721-0': {'AI':8, 'BI':0, 'AO':2, 'BO':0, 'CO':0, 'price':83, 'quality':8.3},
                    'MS-IOM3711-2': {'AI':4, 'BI':0, 'AO':0, 'BO':4, 'CO':4, 'price':154, 'quality':12.8},
                    'MS-IOM3721-0': {'AI':0, 'BI':16, 'AO':0, 'BO':0, 'CO':0, 'price':75, 'quality':4.6},
                    'MS-IOM3731-0': {'AI':0, 'BI':8, 'AO':0, 'BO':8, 'CO':0,'price':85, 'quality':5.3},
                    'MS-IOM4711-0': {'AI':6, 'BI':2, 'AO':2, 'BO':3, 'CO':4, 'price':127, 'quality':5.7},
                    'MS-IOM1711-0': {'AI':0, 'BI':4, 'AO':0, 'BO':0, 'CO':0, 'price':77, 'quality':19.25},
                    'MS-IOM2711-2': {'AI':2, 'BI':0, 'AO':0, 'BO':2, 'CO':2, 'price':118, 'quality':19.6}
        }
# task from operator

SIGNAL_TASK = [11, 81, 5, 7]

# clear of the list

control_list = []
modules_control_list = []
rezult = []

# save to list name for controller

for i in controller:
    signals_controller = list(dict.values(controller[i]))
    control_list.append(i)

# combination for controller JC, 8 - max count of the modules connection to controller
spisok = modefideModulesController(modules_controller)
counter = 0
rezult_by_signals = {}

max_quality = 0

for i in range(1,8): # how many modules you can use
    for i, pair in enumerate(combinations_with_replacement(spisok, i), 1):
        current_volume = calcBackVolume(pair)
        current_cost = calcBackCost(pair)
        current_quality = calcBackQual(pair)
        spisok_result =[]    
        if current_volume <= SIGNAL_TASK[0] and current_quality >= max_quality:
            counter +=1
            max_quality = current_quality
            spisok_result.append(current_cost)
            spisok_result.append(current_volume)
            spisok_result.append(pair)
            rezult_by_signals.update({counter : spisok_result })
            print("NN {} price {} current colume of signals is {}. The combination is {}". format (counter, current_cost, current_volume, pair))

dict_by_price = {}
max_label = 0

# finish dictionary we filteres by signals from Task to reduce elements.

for i in rezult_by_signals:
    if rezult_by_signals[i][1] >= max_label:
        max_label = rezult_by_signals[i][1]
        dict_by_price.update({rezult_by_signals[i][0]: rezult_by_signals[i][2]})
        print(rezult_by_signals[i][1])

# Sorted dictionary ready for use in the next modules of programme

dict_by_price = SortedDict(dict_by_price)

# prepare dictionary for delete extra elements

finish_modules = {}
print(dict_by_price)
counter_1 = 0
for key in dict_by_price:
    counter_1 += 1
    finish_modules.update({counter_1:dict_by_price[key]})
    print(dict_by_price[key])

print(finish_modules)

# delete all elements except 2 first

delete = [key for key in finish_modules if key > 2]

for key in delete: del finish_modules[key]

print(finish_modules)





