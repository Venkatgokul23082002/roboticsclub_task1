# Import required module/s
import csv

def readMarkSheet(file_name):
	"""Reads the input CSV file of Mark Sheet and creates a mapping of student name with his/her marks for each subject.

	Parameters
	----------
	file_name : str
		CSV file name of Mark Sheet

	Returns
	-------
	dict
		Mapping of each student's name and his/her marks for each subject as { Key : Value } pair
	
	Example
	-------
	>>> csv_file_name = 'task1_sample.csv'
	>>> print( readMarkSheet( csv_file_name ) )
	{
		'Artus Syne': {'marks': [43.0, 71.0, 55.0, 16.0, 51.0]}, 'Evey Reburn': {'marks': [49.0, 7.0, 53.0, 50.0, 63.0]}, 
		'Giff Wickmann': {'marks': [63.0, 37.0, 21.0, 87.0, 9.0]}, 'Garrot Casetta': {'marks': [22.0, 3.0, 91.0, 75.0, 52.0]}, 
		'Roselle Maes': {'marks': [71.0, 90.0, 96.0, 79.0, 48.0]}, 'Torin Ziehms': {'marks': [71.0, 31.0, 83.0, 1.0, 25.0]}, 
		'Jaye Etock': {'marks': [92.0, 9.0, 2.0, 78.0, 55.0]}, 'Thomasina Tinkham': {'marks': [25.0, 78.0, 46.0, 46.0, 90.0]}, 
		'Adolphus Biernat': {'marks': [91.0, 96.0, 98.0, 94.0, 100.0]}, 'Rex Aspinell': {'marks': [34.0, 75.0, 51.0, 38.0, 99.0]}
	}
	"""

	name_marks_mapping = {}
	input_file_obj = open(file_name, 'r')

	##############	ADD YOUR CODE HERE	##############
	import csv
        import pprint
        name_marks_mapping={}
        strg='marks'
        with open('task1_sample.csv', mode='r') as inp:
           reader = csv.reader(inp)
        name_marks_mapping = {rows[0]:{strg:[rows[1],rows[2],rows[3],rows[4],rows[5]]} for rows in reader}
        del(name_marks_mapping['name'])

        pprint.pprint(name_marks_mapping)
	

	##################################################
	
	input_file_obj.close()

	return name_marks_mapping


def generateGradeCard(mapping_dict):
	"""Generate the Grade Card for all students in the given mapping of student and their scores in all subjects with the grade each one has received.

	Parameters
	----------
	mapping_dict : dict
		Mapping of each student's name and his/her marks for each subject as { Key : Value } pair

	Returns
	-------
	dict
		Grade Card for all students with their scores in all subjects and the grade each one has received
	
	Example
	-------
	>>> name_marks_mapping = {
								'Artus Syne': {'marks': [43.0, 71.0, 55.0, 16.0, 51.0]}, 'Evey Reburn': {'marks': [49.0, 7.0, 53.0, 50.0, 63.0]}, 
								'Giff Wickmann': {'marks': [63.0, 37.0, 21.0, 87.0, 9.0]}, 'Garrot Casetta': {'marks': [22.0, 3.0, 91.0, 75.0, 52.0]}, 
								'Roselle Maes': {'marks': [71.0, 90.0, 96.0, 79.0, 48.0]}, 'Torin Ziehms': {'marks': [71.0, 31.0, 83.0, 1.0, 25.0]}, 
								'Jaye Etock': {'marks': [92.0, 9.0, 2.0, 78.0, 55.0]}, 'Thomasina Tinkham': {'marks': [25.0, 78.0, 46.0, 46.0, 90.0]}, 
								'Adolphus Biernat': {'marks': [91.0, 96.0, 98.0, 94.0, 100.0]}, 'Rex Aspinell': {'marks': [34.0, 75.0, 51.0, 38.0, 99.0]}
							}
	>>> print( generateGradeCard( name_marks_mapping ) )
	{
		'Artus Syne': {'subject_wise_marks': [43.0, 71.0, 55.0, 16.0, 51.0], 'grade_received': 'D'}, 
		'Evey Reburn': {'subject_wise_marks': [49.0, 7.0, 53.0, 50.0, 63.0], 'grade_received': 'D'}, 
		'Giff Wickmann': {'subject_wise_marks': [63.0, 37.0, 21.0, 87.0, 9.0], 'grade_received': 'D'}, 
		'Garrot Casetta': {'subject_wise_marks': [22.0, 3.0, 91.0, 75.0, 52.0], 'grade_received': 'D'}, 
		'Roselle Maes': {'subject_wise_marks': [71.0, 90.0, 96.0, 79.0, 48.0], 'grade_received': 'A'}, 
		'Torin Ziehms': {'subject_wise_marks': [71.0, 31.0, 83.0, 1.0, 25.0], 'grade_received': 'D'}, 
		'Jaye Etock': {'subject_wise_marks': [92.0, 9.0, 2.0, 78.0, 55.0], 'grade_received': 'D'}, 
		'Thomasina Tinkham': {'subject_wise_marks': [25.0, 78.0, 46.0, 46.0, 90.0], 'grade_received': 'C'}, 
		'Adolphus Biernat': {'subject_wise_marks': [91.0, 96.0, 98.0, 94.0, 100.0], 'grade_received': 'O'}, 
		'Rex Aspinell': {'subject_wise_marks': [34.0, 75.0, 51.0, 38.0, 99.0], 'grade_received': 'C'}
	}
	"""

	grade_card = {}

	##############	ADD YOUR CODE HERE	##############
import csv
grade_card={}
name_marks_mapping={'Adolphus Biernat': {'marks': ['91', '96', '98', '94', '100']},
 'Artus Syne': {'marks': ['43', '71', '55', '16', '51']},
 'Evey Reburn': {'marks': ['49', '7', '53', '50', '63']},
 'Garrot Casetta': {'marks': ['22', '3', '91', '75', '52']},
 'Giff Wickmann': {'marks': ['63', '37', '21', '87', '9']},
 'Jaye Etock': {'marks': ['92', '9', '2', '78', '55']},
 'Rex Aspinell': {'marks': ['34', '75', '51', '38', '99']},
 'Roselle Maes': {'marks': ['71', '90', '96', '79', '48']},
 'Thomasina Tinkham': {'marks': ['25', '78', '46', '46', '90']},
 'Torin Ziehms': {'marks': ['71', '31', '83', '1', '25']}}
keys=list(name_marks_mapping.keys())
output=list(name_marks_mapping.values())
n=len(name_marks_mapping)
sum=0
for i in range(0,n):
 for j in range(0,5):
  if j<4:
   sum=sum+int(output[i]["marks"][j])
  else:
   sum=sum+int(output[i]["marks"][j])
   avg=sum/5
   if avg>=90:
     grade='O'
   elif avg>=70:
     grade='A'
   elif avg>=60:
     grade='B'
   elif avg>=50:
     grade='C'
   elif avg>=40:
     grade='D'
   else:
     grade='FAIL'
   grade_card[keys[i]]={'subject_wise_marks':output[i]["marks"],'grade_recieved':grade}
   sum=0
print('{')  
for key, value in grade_card.items():
    print(key, ' : ', value)
print('}')
	

	##################################################

	return grade_card


if __name__ == "__main__":
	"""Main function, code begins here.
	"""
	csv_file_name = 'task1_sample.csv'
	name_marks_mapping = readMarkSheet(csv_file_name)
	print(name_marks_mapping)
	grade_card = generateGradeCard(name_marks_mapping)
	print(grade_card)
