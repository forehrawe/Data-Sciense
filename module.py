import numpy as np
import pandas as pd

class School:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        
    def replace_nan_instead_mean(self):
        self.dataframe['math'] = self.dataframe['math'].fillna(self.dataframe['math'].mean())
        self.dataframe['physics'] = self.dataframe['physics'].fillna(self.dataframe['physics'].mean())
        self.dataframe['chemistry'] = self.dataframe['chemistry'].fillna(self.dataframe['chemistry'].mean())
        return self.dataframe
    
    def add_avg_column(self):
        self.dataframe['average'] = self.dataframe[['math', 'physics', 'chemistry']].mean(axis=1)
        return self.dataframe
    
    def top_student_math(self):
        student = self.dataframe.loc[self.dataframe['math'].idxmax()]
        return student
    
    def top_student_physics(self):
        student = self.dataframe.loc[self.dataframe['physics'].idxmax()]
        return student
    
    def top_student_chemistry(self):
        student = self.dataframe.loc[self.dataframe['chemistry'].idxmax()]
        return student
    
    def course_mean(self):
        math = self.dataframe['math'].mean()
        physics = self.dataframe['physics'].mean()
        chemistry = self.dataframe['chemistry'].mean()
        return {'math':math, 'physics':physics, 'chemistry':chemistry}
    
    def min_score(self):
        math = self.dataframe['math'].min()
        physics = self.dataframe['physics'].min()
        chemistry = self.dataframe['chemistry'].min()
        return {'math':math, 'physics':physics, 'chemistry':chemistry}
    
    def max_score(self):
        math = self.dataframe['math'].max()
        physics = self.dataframe['physics'].max()
        chemistry = self.dataframe['chemistry'].max()
        return {'math':math, 'physics':physics, 'chemistry':chemistry}
    
    def best_student(self):
        self.add_avg_column()
        student = self.dataframe.loc[self.dataframe['average'].idxmax()]
        return student
    
    def get_dataframe(self):
        return self.dataframe