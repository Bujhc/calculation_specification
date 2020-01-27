
from itertools import combinations_with_replacement
from sortedcontainers import SortedDict


# calculation volume of the current signals of the programme
# type of signals mean AI, BI, AO, BO, CO, UI

def calcBackVolume_signals (backpack, type_of_signals):
    total_volume = 0
    for items in backpack:
        total_volume += modules_controller[items][type_of_signals]
    return total_volume

# calculation colume of the current cost of the modules

def calcBackCost (backpack):
    total_cost = 0
    for items in backpack:
        total_cost += modules_controller[items]['price']
    return total_cost

# filter dictionary of the modules controller by "AI" for example to use modules with signals without ZERO
# in the other case those modules will be calculate together with usefull modules

def modefideModulesController (modeles, type_of_signals):
    criteria = type_of_signals
    finish_spisok_modules = []
    for items in modeles:
        if modules_controller[items][criteria] > 0:
            finish_spisok_modules.append(items)
    return finish_spisok_modules

def switch_brand(brand):
    brand = {
        0: "JC",
        1: "SH",
        2: "Carel"
    }
    return brand

def switch_type(type_of_signals_module):
    type_of_signals_module = {
        0: "AI",
        1: "BI",
        2: "AO",
        3: "DO",
        4: "UI",
        5: "CO",
        6: "BO"
    }
    return type_of_signals_module

def index_max_SIGNAL_TASK(task):
    return task.index(max(task))



# name of the controoler and module with signals

controller = {'MS-FAC3611-0': {'AI':8, 'BI':6, 'AO':6, 'BO':6, 'CO':0}
        }
modules_controller = {'MS-IOM2721-0': {'AI':8, 'BI':0, 'AO':2, 'BO':0, 'CO':0, 'price':83},
                    'MS-IOM3711-2': {'AI':4, 'BI':0, 'AO':0, 'BO':4, 'CO':4, 'price':154},
                    'MS-IOM3721-0': {'AI':0, 'BI':16, 'AO':0, 'BO':0, 'CO':0, 'price':75},
                    'MS-IOM3731-0': {'AI':0, 'BI':8, 'AO':0, 'BO':8, 'CO':0,'price':85},
                    'MS-IOM4711-0': {'AI':6, 'BI':2, 'AO':2, 'BO':3, 'CO':4, 'price':127},
                    'MS-IOM1711-0': {'AI':0, 'BI':4, 'AO':0, 'BO':0, 'CO':0, 'price':77},
                    'MS-IOM2711-2': {'AI':2, 'BI':0, 'AO':0, 'BO':2, 'CO':2, 'price':118}
        }
# task from operator

SIGNAL_TASK = [40,11,5,7]

print(index_max_SIGNAL_TASK(SIGNAL_TASK))

# clear of the list

control_list = []
modules_control_list = []
rezult = []

# save to list name for controller

for i in controller:
    signals_controller = list(dict.values(controller[i]))
    control_list.append(i)

# combination for controller JC, 8 - max count of the modules connection to controller
spisok = modefideModulesController(modules_controller, 'AI')
print(spisok)
counter = 0
rezult_by_signals = {}

max_quality = 0

for i in range(1,8): # how many modules you can use
    for i, pair in enumerate(combinations_with_replacement(spisok, i), 1):
        current_volume = calcBackVolume_signals(pair, 'AI')
        current_cost = calcBackCost(pair)
        spisok_result =[]    
        if current_volume <= SIGNAL_TASK[0]:
            counter +=1
            spisok_result.append(current_cost)
            spisok_result.append(current_volume)
            spisok_result.append(pair)
            rezult_by_signals.update({counter : spisok_result })
            print("NN {} price {} current colume of signals is {}. The combination is {}". format (counter, current_cost, current_volume, pair))

dict_by_price = {}
max_label = 0
test_list_signals = []
# finish dictionary we filteres by signals from Task to reduce elements.

for i in rezult_by_signals:
    if rezult_by_signals[i][1] >= max_label:
        max_label = rezult_by_signals[i][1]
        dict_by_price.update({rezult_by_signals[i][0]: rezult_by_signals[i][2]})
        #print(rezult_by_signals[i][1])
        test_list_signals.append(rezult_by_signals[i][1])

print(test_list_signals)
print(test_list_signals.index(max(test_list_signals)))
for key in dict_by_price:
    print("Price is {} Combination is {}" .format(key, dict_by_price[key]))

