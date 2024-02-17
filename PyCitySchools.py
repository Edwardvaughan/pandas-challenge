#Program PyCitySchools: an analysis of fifteen American schools written in Python 3.11

import pandas as pd
schools_complete = pd.read_csv ('C:/Users/edwar/Downloads/schools_complete.csv')
students_complete = pd.read_csv ('C:/Users/edwar/Downloads/students_complete.csv')

school_id = schools_complete ['School ID']
school_name = schools_complete ['school_name']
type = schools_complete ['type']
size = schools_complete ['size']
budget = schools_complete ['budget']

student_id = students_complete ['Student ID']
student_name = students_complete ['student_name']
gender = students_complete ['gender']
grade = students_complete ['grade']
reading_score = students_complete ['reading_score']
math_score = students_complete ['math_score']

#Do the ststistics for the District Summary

school_count = max (school_id) + 1 
student_count = max (student_id) + 1
total_budget = sum (budget)
average_math_score = '{:.4}'.format (sum (math_score) / len (math_score))
average_reading_score = '{:.4}'.format (sum (reading_score) / len (reading_score))
passing_math_count = students_complete [(students_complete ['math_score'] >= 70)].count ()['student_name']
passing_math_percentage = '{:.4}'.format (passing_math_count / float (student_count) * 100)
passing_reading_count = students_complete [(students_complete ['reading_score'] >= 70)].count ()['student_name']
passing_reading_percentage = '{:.4}'.format (passing_reading_count / float (student_count) * 100)
passing_math_reading_count = students_complete [(students_complete ['math_score'] >= 70) & 
                                                (students_complete ['reading_score'] >= 70)].count ()['student_name']
overall_passing_rate = '{:.4}'.format (passing_math_reading_count / float (student_count) * 100)

f = open ('C:/Users/edwar/Downloads/PyCitySchools_output.txt', 'a')

f.write ('District Summary\n\n')

f.write (str (school_count) + ' ' +
         str (student_count) + ' ' +
         str (total_budget) + ' ' +
         str (average_math_score) + ' ' +
         str (average_reading_score) + ' ' +
         str (passing_math_percentage) + ' ' +
         str (passing_reading_percentage) + ' ' +
         str (overall_passing_rate) + '\n\n')

f.write ('Values are:\n' +
         'School Count\n' +
         'Student Count\n' +
         'Total Budget\n' +
         'Average Math Score\n' +
         'Average Reading Score\n' +
         'Passing Math Percentage\n' +
         'Passing Reading Percentage\n' +
         'Overall Passing Rate\n\n')

district_summary_data = [school_count,
                    student_count,
                    total_budget,
                    average_math_score,
                    average_reading_score,
                    passing_math_percentage,
                    passing_reading_percentage,
                    overall_passing_rate]

#School Summary

district_summary = pd.DataFrame (district_summary_data)

number_of_rows = len (students_complete)

school_name_1 = students_complete ['school_name']

total_students = [0 for j in range (15)]

per_student_budget = [0 for j in range (15)]

total_math_scores = 0
total_reading_scores = 0

average_math_score_1 = [0 for j in range (15)]
average_reading_score_1 = [0 for j in range (15)]

passing_math_count_1 = [0 for j in range (15)]
passing_reading_count_1 = [0 for j in range (15)]
passing_math_reading_count_1 = [0 for j in range (15)]

passing_math_percentage_1 = [0 for j in range (15)]
passing_reading_percentage_1 = [0 for j in range (15)]
overall_passing_rate_1 = [0 for j in range (15)] 

previous_i = 1

j = 1

for i in range (2, number_of_rows):

    total_math_scores = total_math_scores + math_score [i - 1]
    total_reading_scores = total_reading_scores + reading_score [i - 1]

    if math_score [i - 1] >= 70:

        passing_math_count_1 [j - 1] = passing_math_count_1 [j - 1] + 1

    if reading_score [i - 1] >= 70:

        passing_reading_count_1 [j - 1] = passing_reading_count_1 [j - 1] + 1

    if math_score [i - 1] >= 70 and reading_score [i - 1] >= 70:

        passing_math_reading_count_1 [j - 1] = passing_math_reading_count_1 [j - 1] + 1

#Iterating through the student records, if we come to a new school, compute the statistics for the previous one     

    if school_name_1 [i] != school_name_1 [i - 1]:

        total_students [j - 1] = i - previous_i

        per_student_budget [j - 1] = '{:.4}'.format (budget [j - 1] / total_students [j - 1])

        average_math_score_1 [j - 1] = '{:.4}'.format (total_math_scores / (i - previous_i))
        average_reading_score_1 [j - 1] = '{:.4}'.format (total_reading_scores / (i - previous_i))

        passing_math_percentage_1 [j - 1] = '{:.4}'.format (passing_math_count_1 [j - 1] / total_students [j - 1] * 100)
        passing_reading_percentage_1 [j - 1] = '{:.4}'.format (passing_reading_count_1 [j - 1] / total_students [j -1] * 100)
        overall_passing_rate_1 [j - 1] = '{:.4}'.format (passing_math_reading_count_1 [j - 1] / total_students [j - 1] * 100)

        total_math_scores = 0
        total_reading_scores = 0

        previous_i = i

        j = j + 1

per_school_summary_data = [[school_name [0], type [0], total_students [0], budget [1], per_student_budget [0], average_math_score_1 [0], average_reading_score_1 [0], passing_math_percentage_1 [0], passing_reading_percentage_1 [0], overall_passing_rate_1 [0]],
                           [school_name [1], type [1], total_students [1], budget [1], per_student_budget [1], average_math_score_1 [1], average_reading_score_1 [1], passing_math_percentage_1 [1], passing_reading_percentage_1 [1], overall_passing_rate_1 [1]],
                           [school_name [2], type [2], total_students [2], budget [1], per_student_budget [2], average_math_score_1 [2], average_reading_score_1 [2], passing_math_percentage_1 [2], passing_reading_percentage_1 [2], overall_passing_rate_1 [2]],
                           [school_name [3], type [3], total_students [3], budget [1], per_student_budget [3], average_math_score_1 [3], average_reading_score_1 [3], passing_math_percentage_1 [3], passing_reading_percentage_1 [3], overall_passing_rate_1 [3]],
                           [school_name [4], type [4], total_students [4], budget [1], per_student_budget [4], average_math_score_1 [4], average_reading_score_1 [4], passing_math_percentage_1 [4], passing_reading_percentage_1 [4], overall_passing_rate_1 [4]],
                           [school_name [5], type [5], total_students [5], budget [1], per_student_budget [5], average_math_score_1 [5], average_reading_score_1 [5], passing_math_percentage_1 [5], passing_reading_percentage_1 [5], overall_passing_rate_1 [5]],
                           [school_name [6], type [6], total_students [6], budget [1], per_student_budget [6], average_math_score_1 [6], average_reading_score_1 [6], passing_math_percentage_1 [6], passing_reading_percentage_1 [6], overall_passing_rate_1 [6]],
                           [school_name [7], type [7], total_students [7], budget [1], per_student_budget [7], average_math_score_1 [7], average_reading_score_1 [7], passing_math_percentage_1 [7], passing_reading_percentage_1 [7], overall_passing_rate_1 [7]],
                           [school_name [8], type [8], total_students [8], budget [1], per_student_budget [8], average_math_score_1 [8], average_reading_score_1 [8], passing_math_percentage_1 [8], passing_reading_percentage_1 [8], overall_passing_rate_1 [8]],
                           [school_name [9], type [9], total_students [9], budget [1], per_student_budget [9], average_math_score_1 [9], average_reading_score_1 [9], passing_math_percentage_1 [9], passing_reading_percentage_1 [9], overall_passing_rate_1 [9]],
                           [school_name [10], type [10], total_students [10], budget [1], per_student_budget [10], average_math_score_1 [10], average_reading_score_1 [10], passing_math_percentage_1 [10], passing_reading_percentage_1 [10], overall_passing_rate_1 [10]],
                           [school_name [11], type [11], total_students [11], budget [1], per_student_budget [11], average_math_score_1 [11], average_reading_score_1 [11], passing_math_percentage_1 [11], passing_reading_percentage_1 [11], overall_passing_rate_1 [11]],
                           [school_name [12], type [12], total_students [12], budget [1], per_student_budget [12], average_math_score_1 [12], average_reading_score_1 [12], passing_math_percentage_1 [12], passing_reading_percentage_1 [12], overall_passing_rate_1 [12]],
                           [school_name [13], type [13], total_students [13], budget [1], per_student_budget [13], average_math_score_1 [13], average_reading_score_1 [13], passing_math_percentage_1 [13], passing_reading_percentage_1 [13], overall_passing_rate_1 [13]],
                           [school_name [14], type [14], total_students [14], budget [1], per_student_budget [14], average_math_score_1 [14], average_reading_score_1 [14], passing_math_percentage_1 [14], passing_reading_percentage_1 [14], overall_passing_rate_1 [14]]]

f.write ('School Summary\n\n')

for j in range (1, 14):
    
    f.write (school_name [j] + ' ' +
             type [j] + ' ' +
             str (total_students [j]) + ' ' +
             str (budget [j]) + ' ' +
             str (per_student_budget [j]) + ' ' +
             str (average_math_score_1 [j]) + ' ' +
             str (average_reading_score_1 [j]) + ' ' +
             str (passing_math_percentage_1 [j]) + ' ' +
             str (passing_reading_percentage_1 [j]) + ' ' +
             str (overall_passing_rate_1 [j]) + '\n')
    
    per_school_summay = pd.DataFrame (per_school_summary_data, columns = [school_name [j],
                                                                                type [j],
                                                                                total_students [j],
                                                                                budget [j],
                                                                                per_student_budget [j],
                                                                                '{:.4}'.format (average_math_score_1 [j]),
                                                                                '{:.4}'.format (average_reading_score_1 [j]),
                                                                                '{:.4}'.format (passing_math_percentage_1 [j]),
                                                                                '{:.4}'.format (passing_reading_percentage_1 [j]),
                                                                                '{:.4}'.format (overall_passing_rate_1 [j])])

f.write ('\nColumns are:\n' +
         '1: School Name\n' +
         '2: Type\n' +
         '3: Total Students\n' 
         '4: Budget\n' +
         '5: Per Student Budget\n' +
         '6: Average Math Score\n' +
         '7: Average Reading Score\n' +
         '8: Passing Math Percentage\n' +
         '9: Passing Reading Percentage\n' +
         '10: Overall Passing Rate\n\n')

#Best- and Lowest-Performing Schools

list = []

for j in range (0, 15):

    list.append (float (overall_passing_rate_1 [j]))

#Sort the overall passing rates of the various schools in ascending order

for i in range (0, 14):

    for j in range (0, 14):

        if list [j + 1] < list [j]:

            n = list [j + 1]
            list [j + 1] = list [j]
            list [j] = n

#Reverse the order and identify the five best-performing schools

reversed_list = sorted (list, reverse = True)

school_name_list = []

for i in range (0, 5):

    for j in range (0, 14):

        if reversed_list [i] == float (overall_passing_rate_1 [j]):

                school_name_list.append (school_name [j])

f.write ('Best-Performing Schools (by % Overall Passing)\n\n')

for i in range (0, 5):

    f.write (school_name_list [i] + ' ' + str (reversed_list [i]) + '\n')

top_schools = pd.DataFrame (columns = (reversed_list, school_name_list))

#Get the five lowest-performing schools

school_name_list = []

for i in range (0, 5):

    for j in range (0, 14):

        if list [i] == float (overall_passing_rate_1 [j]):

            school_name_list.append (school_name [j])

f.write ('\nLowest-Performing Schools by % Overall Passing)\n\n')

for i in range (0, 5):

    f.write (school_name_list [i] + ' ' + str (list [i + 1]) + '\n')

bottom_schools = pd.DataFrame (columns = (list, school_name_list))

#Maths Scores by Grade

total_math_scores_9th = 0
total_math_scores_10th = 0
total_math_scores_11th = 0
total_math_scores_12th = 0

total_students_9th = 0
total_students_10th = 0
total_students_11th = 0
total_students_12th = 0

average_math_score_9th = [0 for j in range (15)]
average_math_score_10th = [0 for j in range (15)]
average_math_score_11th = [0 for j in range (15)]
average_math_score_12th = [0 for j in range (15)]

j = 0

for i in range (1, number_of_rows):

    if grade [i] == '9th':

        total_math_scores_9th = total_math_scores_9th + math_score [i]
        total_students_9th = total_students_9th + 1

    elif grade [i] == '10th':

        total_math_scores_10th = total_math_scores_10th + math_score [i]
        total_students_10th = total_students_10th + 1

    elif grade [i] == '11th':

        total_math_scores_11th = total_math_scores_11th + math_score [i]
        total_students_11th = total_students_11th + 1

    else:

        total_math_scores_12th = total_math_scores_12th + math_score [i]
        total_students_12th = total_students_12th + 1

    if school_name_1 [i] != school_name_1 [i - 1]: 

        average_math_score_9th [j] = total_math_scores_9th / (total_students_9th - 1)
        average_math_score_10th [j] = total_math_scores_10th / (total_students_10th - 1)
        average_math_score_11th [j] = total_math_scores_11th / (total_students_11th - 1)
        average_math_score_12th [j] = total_math_scores_12th / (total_students_12th - 1)

        total_math_scores_9th = 0
        total_math_scores_10th = 0
        total_math_scores_11th = 0
        total_math_scores_12th = 0

        total_students_9th = 0
        total_students_10th = 0
        total_students_11th = 0
        total_students_12th = 0

        j = j + 1

average_math_score_data = [[school_name [0], '{:.4}'.format (average_math_score_9th [0]), '{:.4}'.format (average_math_score_10th [0]), '{:.4}'.format (average_math_score_11th [0]), '{:.4}'.format (average_math_score_12th [0])],
                           [school_name [1], '{:.4}'.format (average_math_score_9th [1]), '{:.4}'.format (average_math_score_10th [1]), '{:.4}'.format (average_math_score_11th [1]), '{:.4}'.format (average_math_score_12th [1])],
                           [school_name [2], '{:.4}'.format (average_math_score_9th [2]), '{:.4}'.format (average_math_score_10th [2]), '{:.4}'.format (average_math_score_11th [2]), '{:.4}'.format (average_math_score_12th [2])],
                           [school_name [3], '{:.4}'.format (average_math_score_9th [3]), '{:.4}'.format (average_math_score_10th [3]), '{:.4}'.format (average_math_score_11th [3]), '{:.4}'.format (average_math_score_12th [3])],
                           [school_name [4], '{:.4}'.format (average_math_score_9th [4]), '{:.4}'.format (average_math_score_10th [4]), '{:.4}'.format (average_math_score_11th [4]), '{:.4}'.format (average_math_score_12th [4])],
                           [school_name [5], '{:.4}'.format (average_math_score_9th [5]), '{:.4}'.format (average_math_score_10th [5]), '{:.4}'.format (average_math_score_11th [5]), '{:.4}'.format (average_math_score_12th [5])],
                           [school_name [6], '{:.4}'.format (average_math_score_9th [6]), '{:.4}'.format (average_math_score_10th [6]), '{:.4}'.format (average_math_score_11th [6]), '{:.4}'.format (average_math_score_12th [6])],
                           [school_name [7], '{:.4}'.format (average_math_score_9th [7]), '{:.4}'.format (average_math_score_10th [7]), '{:.4}'.format (average_math_score_11th [7]), '{:.4}'.format (average_math_score_12th [7])],
                           [school_name [8], '{:.4}'.format (average_math_score_9th [8]), '{:.4}'.format (average_math_score_10th [8]), '{:.4}'.format (average_math_score_11th [8]), '{:.4}'.format (average_math_score_12th [8])],
                           [school_name [9], '{:.4}'.format (average_math_score_9th [9]), '{:.4}'.format (average_math_score_10th [9]), '{:.4}'.format (average_math_score_11th [9]), '{:.4}'.format (average_math_score_12th [9])],
                           [school_name [10], '{:.4}'.format (average_math_score_9th [10]), '{:.4}'.format (average_math_score_10th [10]), '{:.4}'.format (average_math_score_11th [10]), '{:.4}'.format (average_math_score_12th [10])],
                           [school_name [11], '{:.4}'.format (average_math_score_9th [11]), '{:.4}'.format (average_math_score_10th [11]), '{:.4}'.format (average_math_score_11th [11]), '{:.4}'.format (average_math_score_12th [11])],
                           [school_name [12], '{:.4}'.format (average_math_score_9th [12]), '{:.4}'.format (average_math_score_10th [12]), '{:.4}'.format (average_math_score_11th [12]), '{:.4}'.format (average_math_score_12th [12])],
                           [school_name [13], '{:.4}'.format (average_math_score_9th [13]), '{:.4}'.format (average_math_score_10th [13]), '{:.4}'.format (average_math_score_11th [13]), '{:.4}'.format (average_math_score_12th [13])]]

f.write ('\nMath Scores by Grade\n\n')

for j in range (0, 14):

    f.write (school_name [j] + ' ' +
             str ('{:.4}'.format (average_math_score_9th [j])) + ' ' +
             str ('{:.4}'.format (average_math_score_10th [j])) + ' ' +
             str ('{:.4}'.format (average_math_score_11th [j])) + ' ' +
             str ('{:.4}'.format (average_math_score_12th [j])) + '\n')

    average_math_scores = pd.DataFrame (average_math_score_data, columns = [school_name [j],
                                                                            '{:.4}'.format (average_math_score_9th [j]),
                                                                            '{:.4}'.format (average_math_score_10th [j]),
                                                                            '{:.4}'.format (average_math_score_11th [j]),
                                                                            '{:.4}'.format (average_math_score_12th [j])])

f.write ('\nColumns are 9th to 12th Grades\n\n')

#Reading Scores by Grade (this is coded by just copying and pasting Maths Scores by Grade and changing 'maths' to 'reading')

total_reading_scores_9th = 0
total_reading_scores_10th = 0
total_reading_scores_11th = 0
total_reading_scores_12th = 0

total_students_9th = 0
total_students_10th = 0
total_students_11th = 0
total_students_12th = 0

average_reading_score_9th = [0 for j in range (15)]
average_reading_score_10th = [0 for j in range (15)]
average_reading_score_11th = [0 for j in range (15)]
average_reading_score_12th = [0 for j in range (15)]

j = 0

for i in range (1, number_of_rows):

    if grade [i] == '9th':

        total_reading_scores_9th = total_reading_scores_9th + reading_score [i]
        total_students_9th = total_students_9th + 1

    elif grade [i] == '10th':

        total_reading_scores_10th = total_reading_scores_10th + reading_score [i]
        total_students_10th = total_students_10th + 1

    elif grade [i] == '11th':

        total_reading_scores_11th = total_reading_scores_11th + reading_score [i]
        total_students_11th = total_students_11th + 1

    else:

        total_reading_scores_12th = total_reading_scores_12th + reading_score [i]
        total_students_12th = total_students_12th + 1

    if school_name_1 [i] != school_name_1 [i - 1]: 

        average_reading_score_9th [j] = total_reading_scores_9th / (total_students_9th - 1)
        average_reading_score_10th [j] = total_reading_scores_10th / (total_students_10th - 1)
        average_reading_score_11th [j] = total_reading_scores_11th / (total_students_11th - 1)
        average_reading_score_12th [j] = total_reading_scores_12th / (total_students_12th - 1)

        total_reading_scores_9th = 0
        total_reading_scores_10th = 0
        total_reading_scores_11th = 0
        total_reading_scores_12th = 0

        total_students_9th = 0
        total_students_10th = 0
        total_students_11th = 0
        total_students_12th = 0

        j = j + 1

average_reading_score_data = [[school_name [0], '{:.4}'.format (average_reading_score_9th [0]), '{:.4}'.format (average_reading_score_10th [0]), '{:.4}'.format (average_reading_score_11th [0]), '{:.4}'.format (average_reading_score_12th [0])],
                              [school_name [1], '{:.4}'.format (average_reading_score_9th [1]), '{:.4}'.format (average_reading_score_10th [1]), '{:.4}'.format (average_reading_score_11th [1]), '{:.4}'.format (average_reading_score_12th [1])],
                              [school_name [2], '{:.4}'.format (average_reading_score_9th [2]), '{:.4}'.format (average_reading_score_10th [2]), '{:.4}'.format (average_reading_score_11th [2]), '{:.4}'.format (average_reading_score_12th [2])],
                              [school_name [3], '{:.4}'.format (average_reading_score_9th [3]), '{:.4}'.format (average_reading_score_10th [3]), '{:.4}'.format (average_reading_score_11th [3]), '{:.4}'.format (average_reading_score_12th [3])],
                              [school_name [4], '{:.4}'.format (average_reading_score_9th [4]), '{:.4}'.format (average_reading_score_10th [4]), '{:.4}'.format (average_reading_score_11th [4]), '{:.4}'.format (average_reading_score_12th [4])],
                              [school_name [5], '{:.4}'.format (average_reading_score_9th [5]), '{:.4}'.format (average_reading_score_10th [5]), '{:.4}'.format (average_reading_score_11th [5]), '{:.4}'.format (average_reading_score_12th [5])],
                              [school_name [6], '{:.4}'.format (average_reading_score_9th [6]), '{:.4}'.format (average_reading_score_10th [6]), '{:.4}'.format (average_reading_score_11th [6]), '{:.4}'.format (average_reading_score_12th [6])],
                              [school_name [7], '{:.4}'.format (average_reading_score_9th [7]), '{:.4}'.format (average_reading_score_10th [7]), '{:.4}'.format (average_reading_score_11th [7]), '{:.4}'.format (average_reading_score_12th [7])],
                              [school_name [8], '{:.4}'.format (average_reading_score_9th [8]), '{:.4}'.format (average_reading_score_10th [8]), '{:.4}'.format (average_reading_score_11th [8]), '{:.4}'.format (average_reading_score_12th [8])],
                              [school_name [9], '{:.4}'.format (average_reading_score_9th [9]), '{:.4}'.format (average_reading_score_10th [9]), '{:.4}'.format (average_reading_score_11th [9]), '{:.4}'.format (average_reading_score_12th [9])],
                              [school_name [10], '{:.4}'.format (average_reading_score_9th [10]), '{:.4}'.format (average_reading_score_10th [10]), '{:.4}'.format (average_reading_score_11th [10]), '{:.4}'.format (average_reading_score_12th [10])],
                              [school_name [11], '{:.4}'.format (average_reading_score_9th [11]), '{:.4}'.format (average_reading_score_10th [11]), '{:.4}'.format (average_reading_score_11th [11]), '{:.4}'.format (average_reading_score_12th [11])],
                              [school_name [12], '{:.4}'.format (average_reading_score_9th [12]), '{:.4}'.format (average_reading_score_10th [12]), '{:.4}'.format (average_reading_score_11th [12]), '{:.4}'.format (average_reading_score_12th [12])],
                              [school_name [13], '{:.4}'.format (average_reading_score_9th [13]), '{:.4}'.format (average_reading_score_10th [13]), '{:.4}'.format (average_reading_score_11th [13]), '{:.4}'.format (average_reading_score_12th [13])]]

f.write ('Reading Scores by Grade\n\n')

for j in range (0, 14):

    f.write (school_name [j] + ' ' +
             str ('{:.4}'.format (average_reading_score_9th [j])) + ' ' +
             str ('{:.4}'.format (average_reading_score_10th [j])) + ' ' +
             str ('{:.4}'.format (average_reading_score_11th [j])) + ' ' +
             str ('{:.4}'.format (average_reading_score_12th [j])) + '\n')

    average_reading_scores = pd.DataFrame (average_reading_score_data, columns = [school_name [j],
                                                                                '{:.4}'.format (average_reading_score_9th [j]),
                                                                                '{:.4}'.format (average_reading_score_10th [j]),
                                                                                '{:.4}'.format (average_reading_score_11th [j]),
                                                                                '{:.4}'.format (average_reading_score_12th [j])])
    
f.write ('\nColumns are 9th to 12th Grades')

f.close