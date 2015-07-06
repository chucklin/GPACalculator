#!/bin/python
import sys
import os

class Calculator(object):
    def __init__(self, grade_file):
        self._grade_file = os.path.abspath(grade_file)

    def calculate_overallGPA(self):
        overall_GPA = 0.0
        total_GPA = 0.0
        total_credit = 0
        
        grade_file = open(self._grade_file)
        for line in grade_file:
            credit = int(line.split()[0])
            score = float(line.split()[1])
            total_credit += credit
            total_GPA += (self.score2GPA(score) * credit)

        print "Total GPA = %lf, Total Credit = %d" %(total_GPA, total_credit)
        overall_GPA = total_GPA / total_credit
        return overall_GPA
        
    def score2GPA(self, score):
        GPA_mapping = list()
        GPA_mapping.append((85, 4.0))
        GPA_mapping.append((80, 3.7))
        GPA_mapping.append((77, 3.3))
        GPA_mapping.append((73, 3.0))
        GPA_mapping.append((70, 2.7))
        GPA_mapping.append((67, 2.3))
        GPA_mapping.append((63, 2.0))
        GPA_mapping.append((60, 1.7))
        GPA_mapping.append((50, 1.0))
        GPA_mapping.append((40, 0.8))
        GPA_mapping.append((0, 0.0))
        for i in range(len(GPA_mapping)):
            if score >= GPA_mapping[i][0]:
                return GPA_mapping[i][1]
        return 0.0

if __name__ == '__main__':
    calculator = Calculator(sys.argv[1])
    print "Overall GPA = %lf" %calculator.calculate_overallGPA()