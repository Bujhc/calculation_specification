



controller = {'MS-FAC3611-0': {'AI':8, 'BI':6, 'AO':6, 'BO':6, 'CO':0}
        }
modules_controller = {'MS-IOM2721-0': {'AI':8, 'BI':0, 'AO':2, 'BO':0, 'CO':0},
                    'MS-IOM3711-2': {'AI':4, 'BI':0, 'AO':0, 'BO':4, 'CO':4},
                    'MS-IOM3721-0': {'AI':0, 'BI':16, 'AO':0, 'BO':0, 'CO':0},
                    'MS-IOM3731-0': {'AI':0, 'BI':8, 'AO':0, 'BO':8, 'CO':0},
                    'MS-IOM4711-0': {'AI':6, 'BI':2, 'AO':2, 'BO':3, 'CO':4},
                    'MS-IOM1711-0': {'AI':0, 'BI':4, 'AO':0, 'BO':0, 'CO':0},
                    'MS-IOM2711-0': {'AI':2, 'BI':0, 'AO':0, 'BO':2, 'CO':2}
        }
signal_task = [11, 81, 5, 7]

control_list = []
modules_control_list = []
rezult = []

for i in controller:
    signals_controller = list(dict.values(controller[i]))
    control_list.append(i)

print(control_list)


# substraction signals of controller
for i in range(len(signal_task)):
    calc = signal_task[i]-signals_controller[i]
    rezult.append(calc)
# calculation module
while sum(rezult) > 0:
    for i in modules_controller:
         for y in modules_controller[i]:
             if 'AI' in y:
                if modules_controller[i][y] <= rezult[0] and (rezult[0]-modules_controller[i][y])>8:
                    modules_control_list.append(modules_controller[i])
                    rezult[0] = rezult[0] - modules_controller[i][y]
                elif modules_controller[i][y] <= rezult[0] and ((rezult[0]-modules_controller[i][y])<8 or (rezult[0]-modules_controller[i][y])>5):
                    modules_control_list.append(modules_controller[i])
                    rezult[0] = rezult[0] - modules_controller[i][y]
                elif modules_controller[i][y] <= rezult[0] and ((rezult[0]-modules_controller[i][y])<5 or (rezult[0]-modules_controller[i][y])>=4):
                    modules_control_list.append(modules_controller[i])
                    rezult[0] = rezult[0] - modules_controller[i][y]
                elif modules_controller[i][y] <= rezult[0] and ((rezult[0]-modules_controller[i][y])<4 or (rezult[0]-modules_controller[i][y])>=2):
                    modules_control_list.append(modules_controller[i])
                    rezult[0] = rezult[0] - modules_controller[i][y]
                else:
                    print(modules_control_list) 
             else:
                 print ('херня')   