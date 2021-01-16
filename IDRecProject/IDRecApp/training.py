import os
from nanonets import OCR

API_KEY = os.environ.get('NANONETS_API_KEY')
CATEGORIES = ['forenames', 'surname', 'date_of_birth', 'country_of_birth', 'date_issued', 'id_no']

IMAGE_DIR = './IDRecApp/images/'
ANNOTATION_DIR = './IDRecApp/annotations/json/'

model = OCR(API_KEY, CATEGORIES)

images = [IMAGE_DIR + x for x in os.listdir(IMAGE_DIR)]
images.sort()

annotations = [ANNOTATION_DIR + x for x in os.listdir(ANNOTATION_DIR)]
annotations.sort()

training_dict = dict(zip(images, annotations))

response = model.train(training_dict)

print("NEXT RUN: export NANONETS_MODEL_ID=" + model.model_id)
print("NEXT RUN: python ./code/model-state.py")

