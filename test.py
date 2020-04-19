dict_by_price = {}
max_label = 0
list_signals = []
counter_1 = 0

rezult_by_signals = {1: [77, 4, ('MS-IOM1711-0',)], 2: [85, 8, ('MS-IOM3731-0',)], 3: [127, 2, ('MS-IOM4711-0',)], 4: [154, 8, ('MS-IOM1711-0', 'MS-IOM1711-0')], 5: [204, 6, ('MS-IOM1711-0', 'MS-IOM4711-0')], 6: [254, 4, ('MS-IOM4711-0', 'MS-IOM4711-0')], 7: [331, 8, ('MS-IOM1711-0', 'MS-IOM4711-0', 'MS-IOM4711-0')], 8: [381, 6, ('MS-IOM4711-0', 'MS-IOM4711-0', 'MS-IOM4711-0')], 9: [508, 8, ('MS-IOM4711-0', 'MS-IOM4711-0', 'MS-IOM4711-0', 'MS-IOM4711-0')]}


for i in rezult_by_signals:
    if rezult_by_signals[i][1] >= max_label:
        counter_1 +=1
        max_label = rezult_by_signals[i][1]
        dict_by_price.update({counter_1: rezult_by_signals[i][2]})
        
        list_signals.append(rezult_by_signals[i][1])

if len(list_signals) > 1:
    print(len(list_signals))
    print(list_signals)
    index_in_sort_dictionary = list_signals.index(max(list_signals)) + 1
else:
    index_in_sort_dictionary = list_signals.index(max(list_signals))

print(index_in_sort_dictionary)

# finish list of modules after 1 step calculation

rezult_1step = (dict_by_price[index_in_sort_dictionary])
print(rezult_1step)