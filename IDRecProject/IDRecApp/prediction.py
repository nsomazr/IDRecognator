from nanonets import OCR
import os, sys
import pandas as pd
import json

API_KEY = os.environ.get('NANONETS_API_KEY')
MODEL_ID = os.environ.get('NANONETS_MODEL_ID')
CATEGORIES = ['forenames', 'surname', 'date_of_birth', 'country_of_birth', 'date_issued', 'id_no']

IMAGE_PATH = sys.argv[1]

model = OCR(API_KEY, CATEGORIES, model_id=MODEL_ID)

result = model.predict_for_file(IMAGE_PATH)

#print(result)

json_name = list(result.keys())[0]

# print("json name: "+json_name)

# print('file name', str(json_name).split('.')[-2])

keyList = ['id_no', 'surname', 'forenames', 'country_of_birth', 'date_of_birth', 'date_issued']

data_dict = {key: '' for key in keyList}

result_dict_keys = []

for i in range(len(result[json_name])):
    result_dict_keys.append(list(result[json_name][i].values())[0])

# print(result_dict_keys)

for i,ii in zip(result_dict_keys,range(len(result_dict_keys))):
    if i in keyList:
        data_dict[i] = result[json_name][ii]['ocr_text']
    if data_dict[i] == '':
        data_dict[i] = 'Oop! Fill your '+i


# print(data_dict)


# data_dict = {'id_no': result[json_name][0]['ocr_text'],
#              'surname': result[json_name][1]['ocr_text'],
#              'forenames': result[json_name][2]['ocr_text'],
#              'country_of_birth': result[json_name][3]['ocr_text'],
#              'date_of_birth': result[json_name][4]['ocr_text'],
#              'date_issued': result[json_name][5]['ocr_text']}


with open('./IDRecApp/json_files/{}.json'.format(str(json_name).split('.')[-2]), 'w') as fp:
    json.dump(data_dict, fp)


