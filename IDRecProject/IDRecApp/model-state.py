import os
import json
from nanonets import OCR

API_KEY = os.environ.get('NANONETS_API_KEY')
MODEL_ID = os.environ.get('NANONETS_MODEL_ID')
CATEGORIES = ['forenames', 'surname', 'date_of_birth', 'country_of_birth', 'date_issued', 'id_no']

model = OCR(API_KEY, CATEGORIES, model_id=MODEL_ID)

response = model._check_model_state()

state = json.loads(response.text)["state"]

if state == 5:
	print("NEXT RUN: python3 ./code/prediction.py ./images/33.jpeg")
