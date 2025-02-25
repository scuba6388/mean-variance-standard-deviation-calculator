import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    tempArr = np.array(list)

    arr = np.fill((3,3), tempArr[0:3], tempArr[3:6], tempArr[6:9]) 

    calculations = {
        'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr)],
        'variance': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr)],
        'standard deviation': [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr)],
        'max': [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr)],
        'min': [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr)],
        'sum': [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr)]
    }

    return calculations