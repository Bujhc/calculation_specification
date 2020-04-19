import operator

from itertools import combinations_with_replacement

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
        if modules_controller[items][criteria] != 0:
            finish_spisok_modules.append(items)
    return finish_spisok_modules

def switch_brand(brand):
    brand = {
        0: "JC",
        1: "SH",
        2: "Carel"
    }
    return brand[brand]

def switch_type(type_of_signals_module):
    switch_type_of_signals = {
        0: "AI",
        1: "BI",
        2: "AO",
        3: "BO",
        4: "UI",
        5: "CO"
    }
    return switch_type_of_signals[type_of_signals_module]

def index_max_SIGNAL_TASK(task):
    return task.index(max(task))

def modules_calculate(spisok, type_of_signal, SIGNAL_TASK):
    counter = 0
    rezult_by_signals = {}
    max_quality = 0

    for i in range(1,9): # how many modules you have to use
        for i, pair in enumerate(combinations_with_replacement(spisok, i), 1):
            current_volume = calcBackVolume_signals(pair, type_of_signal)
            current_cost = calcBackCost(pair)
            spisok_result =[]    
            if current_volume <= SIGNAL_TASK[index_max_SIGNAL_TASK(SIGNAL_TASK)]:
                counter +=1
                spisok_result.append(current_cost)
                spisok_result.append(current_volume)
                spisok_result.append(pair)
                rezult_by_signals.update({counter : spisok_result })
                #print("NN {} price {} current colume of signals is {}. The combination is {}". format (counter, current_cost, current_volume, pair))
    return rezult_by_signals

def filterModulesSpisok (rezult_by_signals):
    dict_by_price = {}
    max_label = 0
    list_signals = []

    # finish dictionary we filteres by signals from Task to reduce elements.
    print(rezult_by_signals)
    counter_1 = 0
    for i in rezult_by_signals:
        if rezult_by_signals[i][1] >= max_label:
            counter_1 +=1
            max_label = rezult_by_signals[i][1]
            dict_by_price.update({counter_1: rezult_by_signals[i][2]})
            
            list_signals.append(rezult_by_signals[i][1])
    
    if len(list_signals) > 1:
        
        index_in_sort_dictionary = list_signals.index(max(list_signals)) + 1
    else:
        index_in_sort_dictionary = 1


    # finish list of modules after 1 step calculation
    rezult_1step = (dict_by_price[index_in_sort_dictionary])
    return rezult_1step



def calclulator (input_from_operator):

    # task from operator accordint next order AI BI AO BO UI CO
    INPUT_OPERATOR = input_from_operator
    next_step = False
    finish_spisok_controller_modules = []


    while next_step != True:
        
        control_list = []


        # save to list signals of the controller

        for value in controller.values():
            for key in value.values():
                control_list.append(key)       

        print(control_list)

        # calculate amount of signals in the SIGNAL_TASK for next steps of programme

        SIGNAL_TASK = list(map(operator.sub, INPUT_OPERATOR, control_list))

        print(SIGNAL_TASK)
        
        # calculate max of index in SIGNAL_TASK

        cal_type_max_signal_task = index_max_SIGNAL_TASK(SIGNAL_TASK)

        # check conditional after substraction from input operator 

        if max(SIGNAL_TASK) > 0:

            # calculate type of signal according max of index in SIGNAL_TASK

            type_of_signal = str(switch_type(cal_type_max_signal_task))

            print('calculate type of signals {}'.format(type_of_signal))

            # combination for controller JC, 8 - max count of the modules connection to controller
            spisok = modefideModulesController(modules_controller, type_of_signal)
            #print(spisok)

            # how many modules you have to use
            rezult_by_signals = modules_calculate(spisok, type_of_signal, SIGNAL_TASK)

            # finish dictionary we filteres by signals from Task to reduce elements.

            rezult_1step = filterModulesSpisok(rezult_by_signals)
            print( 'количество модулей после первой итерации {}'.format(len(rezult_1step)))
            list_rezult = []

            for i in range(0,6):
                summa_sig = calcBackVolume_signals(rezult_1step, switch_type(i))
                list_rezult.append(summa_sig)

            SIGNAL_TASK = list(map(operator.sub, SIGNAL_TASK, list_rezult))

            print('rezult SIGNAL TASK before next iteration {}'.format(SIGNAL_TASK))

            next_step = all([False if (x > 0) and (x != 0) else  True for x in SIGNAL_TASK])

            print('out condition TRUE/FALSE before next step {}'.format(next_step))

            INPUT_OPERATOR = SIGNAL_TASK
            if len(rezult_1step) >= 8:
                finish_spisok_controller_modules.append(list(controller.keys()))
                
            else:
                finish_spisok_controller_modules.append(rezult_1step)
        
        else:
            finish_spisok_controller_modules.append(list(controller.keys()))
            next_step = all([False if (x > 0) and (x != 0) else  True for x in SIGNAL_TASK]) 

    else:
        print('finish calculation')
        
    return finish_spisok_controller_modules


# name of the controoler and module with signals

controller = {'MS-FAC3611-0': {'AI':8, 'BI':6, 'AO':6, 'BO':6, 'UI':0, 'CO':0}
        }
modules_controller = {'MS-IOM3721-0': {'AI':0, 'BI':16, 'AO':0, 'BO':0, 'UI':0, 'CO':0, 'price':75},
                    'MS-IOM1711-0': {'AI':0, 'BI':4, 'AO':0, 'BO':0,  'UI':0, 'CO':0, 'price':77},
                    'MS-IOM2721-0': {'AI':8, 'BI':0, 'AO':2, 'BO':0, 'UI':0, 'CO':0, 'price':83},
                    'MS-IOM3731-0': {'AI':0, 'BI':8, 'AO':0, 'BO':8, 'UI':0, 'CO':0,'price':85},
                    'MS-IOM2711-2': {'AI':2, 'BI':0, 'AO':0, 'BO':2, 'UI':0, 'CO':2, 'price':118},
                    'MS-IOM4711-0': {'AI':6, 'BI':2, 'AO':2, 'BO':3, 'UI':0,'CO':4, 'price':127},
                    'MS-IOM3711-2': {'AI':4, 'BI':0, 'AO':0, 'BO':4, 'UI':0, 'CO':4, 'price':154}             
                
        }
