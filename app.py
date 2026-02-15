import pandas as pd
import numpy as np
from module import School

data = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Hadi", "Nima", "Zahra"],
    "math": [18, 15, np.nan, 20, 17, 14, 19],
    "physics": [17, np.nan, 16, 19, 18, 13, 20],
    "chemistry": [19, 20, 1, 4, 9, np.nan, np.nan],
    "class": ["A", "A", "B", "B", "A", "B", "A"]
}
df = pd.DataFrame(data)
ins = School(df)
while True:
    print('''
          1-replace nan fields with mean of course
          2-add avg column
          3-top student in courses
          4-courses mean
          5-min score
          6-max score
          7-best student
          8-export to csv
          or exit
          ''')
    opt = input('choose option: ')
    
    if opt == '1':
        print(ins.replace_nan_instead_mean())
        
    elif opt == '2':
        print(ins.add_avg_column())
        
    elif opt == '3':
        print('''
              1-math
              2-chemistry
              3-physics
              ''')
        ts_opt = input('enter course: ')
        if ts_opt == '1':
            print(ins.top_student_math())
        elif ts_opt == '2':
            print(ins.top_student_chemistry())
        elif ts_opt == '3':
            print(ins.top_student_physics())
        else:
            print('invalid value')
            
    elif opt == '4':
        print(ins.course_mean())
        
    elif opt == '5':
        print(ins.min_score())
    
    elif opt =='6':
        print(ins.max_score())
        
    elif opt == '7':
        print(ins.best_student())
        
    elif opt =='8':
        new_df = ins.get_dataframe()
        new_df.to_csv('school.csv', index=False)
        
    elif opt == 'exit':
        break
    
    else:
        print('invalid value')