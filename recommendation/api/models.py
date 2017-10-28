from django.db import models
import pandas as pd
import numpy as np

# Create your models here.

class CuisineSuggester():
    @staticmethod
    def suggest():

        frame = pd.read_csv('csv/rating_final.csv')
        cuisine = pd.read_csv('csv/chefmozcuisine.csv')

        return list(np.arange(0,10))