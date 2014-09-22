from pandas import date_range
import random
import csv

NUM_MINUTES_TRAINING = 365 * 24 *60
NUM_MINUTES_TEST_PUBLIC = 1 * 24 * 60
NUM_MINUTES_TEST_PRIVATE = 1 * 24 * 60

weights = {
	'00': 1,
	'0': 1,
	'1': 1,
	'2': 1,
	'3': 1,
	'4': 1,
	'5': 1,
	'6': 1,
	'7': 1,
	'8': 1,
	'9': 1,
	'10': 1,
	'11': 1,
	'12': 1,
	'13': 1,
	'14': 1,
	'15': 1,
	'16': 1,
	'17': 1,
	'18': 1,
	'19': 1,
	'20': 1,
	'21': 1,
	'22': 1,
	'23': 1,
	'24': 1,
	'25': 1,
	'26': 1,
	'27': 1,
	'28': 1,
	'29': 1,
	'30': 1,
	'31': 1,
	'32': 1,
	'33': 1,
	'34': 1,
	'35': 1,
	'36': 1,
}

weights_table_3 = {
    '00': 1,
    '0': 1,
    '1': 1,
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 2,
    '6': 1,
    '7': 1,
    '8': 1,
    '9': 1,
    '10': 1,
    '11': 1,
    '12': 1,
    '13': 1,
    '14': 1,
    '15': 1,
    '16': 1,
    '17': 1,
    '18': 1,
    '19': 1,
    '20': 1,
    '21': 1,
    '22': 1,
    '23': 1,
    '24': 1,
    '25': 1,
    '26': 1,
    '27': 1,
    '28': 1,
    '29': 1,
    '30': 1,
    '31': 1,
    '32': 1,
    '33': 1,
    '34': 1,
    '35': 1,
    '36': 1,   
}

dist = []
print(weights.keys())
for x in weights.keys():
	for weight in range(weights[x]):
		dist.append(x)
print(dist)

dist_table_3 = []
for x in weights_table_3.keys():
    for weight in range(weights_table_3[x]):
        dist_table_3.append(x)

time_index_training = date_range('2013-1-1', periods=NUM_MINUTES_TRAINING, freq='min')

numbers_table_1_training = {}
for i in range(NUM_MINUTES_TRAINING):
        wRndChoice = random.choice(dist)
        numbers_table_1_training[time_index_training[i]] = wRndChoice

numbers_table_2_training = {}
for i in range(NUM_MINUTES_TRAINING):
        wRndChoice = random.choice(dist)
        numbers_table_2_training[time_index_training[i]] = wRndChoice

numbers_table_3_training = {}
for i in range(NUM_MINUTES_TRAINING):
        wRndChoice = random.choice(dist_table_3)
        numbers_table_3_training[time_index_training[i]] = wRndChoice

numbers_table_4_training = {}
for i in range(NUM_MINUTES_TRAINING):
        wRndChoice = random.choice(dist)
        numbers_table_4_training[time_index_training[i]] = wRndChoice

numbers_table_5_training = {}
for i in range(NUM_MINUTES_TRAINING):
        wRndChoice = random.choice(dist)
        numbers_table_5_training[time_index_training[i]] = wRndChoice

numbers_table_6_training = {}
for i in range(NUM_MINUTES_TRAINING):
        wRndChoice = random.choice(dist)
        numbers_table_6_training[time_index_training[i]] = wRndChoice

numbers_table_7_training = {}
for i in range(NUM_MINUTES_TRAINING):
        wRndChoice = random.choice(dist)
        numbers_table_7_training[time_index_training[i]] = wRndChoice

numbers_table_8_training = {}
for i in range(NUM_MINUTES_TRAINING):
        wRndChoice = random.choice(dist)
        numbers_table_8_training[time_index_training[i]] = wRndChoice

numbers_table_9_training = {}
for i in range(NUM_MINUTES_TRAINING):
        wRndChoice = random.choice(dist)
        numbers_table_9_training[time_index_training[i]] = wRndChoice

numbers_table_10_training = {}
for i in range(NUM_MINUTES_TRAINING):
        wRndChoice = random.choice(dist)
        numbers_table_10_training[time_index_training[i]] = wRndChoice

with open('casino_2_training.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for minute in time_index_training:
    	csvwriter.writerow([minute, numbers_table_1_training[minute], numbers_table_2_training[minute], numbers_table_3_training[minute], numbers_table_4_training[minute], numbers_table_5_training[minute], numbers_table_6_training[minute], numbers_table_7_training[minute], numbers_table_8_training[minute], numbers_table_9_training[minute], numbers_table_10_training[minute]])

#Generate public test data -
time_index_test_public = date_range('2014-1-1', periods=NUM_MINUTES_TEST_PUBLIC, freq='min')

numbers_table_1_test_public = {}
for i in range(NUM_MINUTES_TEST_PUBLIC):
        wRndChoice = random.choice(dist)
        numbers_table_1_test_public[time_index_test_public[i]] = wRndChoice

numbers_table_2_test_public = {}
for i in range(NUM_MINUTES_TEST_PUBLIC):
        wRndChoice = random.choice(dist)
        numbers_table_2_test_public[time_index_test_public[i]] = wRndChoice

numbers_table_3_test_public = {}
for i in range(NUM_MINUTES_TEST_PUBLIC):
        wRndChoice = random.choice(dist_table_3)
        numbers_table_3_test_public[time_index_test_public[i]] = wRndChoice

numbers_table_4_test_public = {}
for i in range(NUM_MINUTES_TEST_PUBLIC):
        wRndChoice = random.choice(dist)
        numbers_table_4_test_public[time_index_test_public[i]] = wRndChoice

numbers_table_5_test_public = {}
for i in range(NUM_MINUTES_TEST_PUBLIC):
        wRndChoice = random.choice(dist)
        numbers_table_5_test_public[time_index_test_public[i]] = wRndChoice

numbers_table_6_test_public = {}
for i in range(NUM_MINUTES_TEST_PUBLIC):
        wRndChoice = random.choice(dist)
        numbers_table_6_test_public[time_index_test_public[i]] = wRndChoice

numbers_table_7_test_public = {}
for i in range(NUM_MINUTES_TEST_PUBLIC):
        wRndChoice = random.choice(dist)
        numbers_table_7_test_public[time_index_test_public[i]] = wRndChoice

numbers_table_8_test_public = {}
for i in range(NUM_MINUTES_TEST_PUBLIC):
        wRndChoice = random.choice(dist)
        numbers_table_8_test_public[time_index_test_public[i]] = wRndChoice

numbers_table_9_test_public = {}
for i in range(NUM_MINUTES_TEST_PUBLIC):
        wRndChoice = random.choice(dist)
        numbers_table_9_test_public[time_index_test_public[i]] = wRndChoice

numbers_table_10_test_public = {}
for i in range(NUM_MINUTES_TEST_PUBLIC):
        wRndChoice = random.choice(dist)
        numbers_table_10_test_public[time_index_test_public[i]] = wRndChoice

with open('casino_2_test_public.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for minute in time_index_test_public:
    	csvwriter.writerow([minute, numbers_table_1_test_public[minute], numbers_table_2_test_public[minute], numbers_table_3_test_public[minute], numbers_table_4_test_public[minute], numbers_table_5_test_public[minute], numbers_table_6_test_public[minute], numbers_table_7_test_public[minute], numbers_table_8_test_public[minute], numbers_table_9_test_public[minute], numbers_table_10_test_public[minute]])

#Generate private test data -
time_index_test_private = date_range('2014-1-2', periods=NUM_MINUTES_TEST_PRIVATE, freq='min')

numbers_table_1_test_private = {}
for i in range(NUM_MINUTES_TEST_PRIVATE):
        wRndChoice = random.choice(dist)
        numbers_table_1_test_private[time_index_test_private[i]] = wRndChoice

numbers_table_2_test_private = {}
for i in range(NUM_MINUTES_TEST_PRIVATE):
        wRndChoice = random.choice(dist)
        numbers_table_2_test_private[time_index_test_private[i]] = wRndChoice

numbers_table_3_test_private = {}
for i in range(NUM_MINUTES_TEST_PRIVATE):
        wRndChoice = random.choice(dist_table_3)
        numbers_table_3_test_private[time_index_test_private[i]] = wRndChoice

numbers_table_4_test_private = {}
for i in range(NUM_MINUTES_TEST_PRIVATE):
        wRndChoice = random.choice(dist)
        numbers_table_4_test_private[time_index_test_private[i]] = wRndChoice

numbers_table_5_test_private = {}
for i in range(NUM_MINUTES_TEST_PRIVATE):
        wRndChoice = random.choice(dist)
        numbers_table_5_test_private[time_index_test_private[i]] = wRndChoice

numbers_table_6_test_private = {}
for i in range(NUM_MINUTES_TEST_PRIVATE):
        wRndChoice = random.choice(dist)
        numbers_table_6_test_private[time_index_test_private[i]] = wRndChoice

numbers_table_7_test_private = {}
for i in range(NUM_MINUTES_TEST_PRIVATE):
        wRndChoice = random.choice(dist)
        numbers_table_7_test_private[time_index_test_private[i]] = wRndChoice

numbers_table_8_test_private = {}
for i in range(NUM_MINUTES_TEST_PRIVATE):
        wRndChoice = random.choice(dist)
        numbers_table_8_test_private[time_index_test_private[i]] = wRndChoice

numbers_table_9_test_private = {}
for i in range(NUM_MINUTES_TEST_PRIVATE):
        wRndChoice = random.choice(dist)
        numbers_table_9_test_private[time_index_test_private[i]] = wRndChoice

numbers_table_10_test_private = {}
for i in range(NUM_MINUTES_TEST_PRIVATE):
        wRndChoice = random.choice(dist)
        numbers_table_10_test_private[time_index_test_private[i]] = wRndChoice

with open('casino_2_test_private.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for minute in time_index_test_private:
    	csvwriter.writerow([minute, numbers_table_1_test_private[minute], numbers_table_2_test_private[minute], numbers_table_3_test_private[minute], numbers_table_4_test_private[minute], numbers_table_5_test_private[minute], numbers_table_6_test_private[minute], numbers_table_7_test_private[minute], numbers_table_8_test_private[minute], numbers_table_9_test_private[minute], numbers_table_10_test_private[minute]])