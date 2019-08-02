# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

train_data = np.load('training_data.npy')
print(len(train_data))

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

no_action = []
lefts = []
rights = []
forwards = []
brakes=[]


shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]
    
##    cv2.imshow('test',img)
##    print(choice)
##    if cv2.waitKey(25) & 0xFF == ord('q'):
##        cv2.destroyAllWindows()
##        

    #if choice is 'A' - left
    if choice == [1,0,0,0]:
        lefts.append([img,choice])
        print('left')
        
    #if choice is 'W' - forward
    elif choice == [0,1,0,0]:
        forwards.append([img,choice])
        print('forward')
        
    #if choice is 'D' - right
    elif choice == [0,0,1,0]:
        rights.append([img,choice])
        print('right')
    #if choice is 'SPACE' - brake
    elif choice == [0,0,0,1]:
        brakes.append([img,choice])
        print('brake')
    #if no action was taken
    else:
        no_action.append([img,choice])
        print('no_action')

no_action = no_action[:len(lefts)][:len(rights)][:len(brakes)][:len(forwards)]
forwards = forwards[:len(no_action)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]
brakes = brakes[:len(forwards)]

final_data = forwards + lefts + rights + brakes + no_action
shuffle(final_data)
print('No_action:',len(no_action))
print('forwards:',len(forwards))
print('lefts:',len(lefts))
print('rights:',len(rights))
print('brakes:',len(brakes))
print('Final data length:',len(final_data))
print('________________________')
f_df = pd.DataFrame(final_data)
print(f_df.head())
print(Counter(f_df[1].apply(str)))
np.save('final_training_data.npy', final_data)

