import random
import pandas as pd

InvalidCard=["111",'221']
ControlVal=True

def ValidationError(card):
    if any([Card in card.lower() for Card in InvalidCard]):
        ControlVal=False
        raise ValueError('This is an invalid card!')
        

    
