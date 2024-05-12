from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from modules import setInterval
from model import predictor, get_accuracy, get_unique_features


app = FastAPI()

origins = [
  "https://main--salary-predictor-ml.netlify.app/"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Get Accuracy
accuracy = {'date': datetime.today(), 'accuracy_rate': get_accuracy()}
def accuracy_getter():
  gotton_accuracy = get_accuracy()
  accuracy['date'] = datetime.today()
  accuracy['accuracy_rate'] = gotton_accuracy
accuracy_interval_timer = 24*60*60 # one day
accuracy_interval = setInterval(accuracy_getter, accuracy_interval_timer)
@app.get('/get_accuracy')
def accuracy_getter():
  return {'last_from_last_update': datetime.today()-accuracy['date'], 'accuracy_rate': accuracy['accuracy_rate']}  

# Prediction
@app.get('/predict')
def predic(work_year: int,
  experience_level: str,
  employment_type: str,
  job_title: str,
  employee_residence: str,
  remote_ratio: int,
  company_location: str,
  company_size: str):
  value = {"work_year": work_year, "experience_level": experience_level, "employment_type": employment_type, "job_title": job_title, "employee_residence": employee_residence, "remote_ratio": remote_ratio, "company_location": company_location, "company_size": company_size}
  y_pred = int(predictor(value))
  return y_pred

# Get Unique Fields
@app.get('/get_unique_features')
def unique_features_getter():
  uniques = get_unique_features()
  for col in uniques.keys():
    uniques[col] = (uniques[col]).tolist()
  print(uniques)
  return uniques