import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 359238083 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    return 2/9604*( 0 - 0.5 + min(x) ), \
           2/9604*( -np.log((1 - p)/len(x)) - 0.5 + min(x) )
