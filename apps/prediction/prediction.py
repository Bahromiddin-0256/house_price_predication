from joblib import load
import os
from django.conf import settings
import subprocess

def prediction():
    print(subprocess.getoutput("ls ."))
    xgb = load(os.path.join(settings.BASE_DIR, "apps/prediction/ml_models/xgb.joblib"))
    print(xgb)
    