####################################################
Interactive Medical Diagnostic Package


Report submitted in partial fulfillment of the course BITS C331


Akash Saxena 						Annu Sharma
2010A7PS168P 						2010A7PS003P

Supervised by
Dr. A. S. Mandal
IC Design Group
CEERI Pilani
May 2nd, 2013


ABSTRACT


This project aims at developing an interactive system to help recognize, weigh and thereby predict one of the diseases – malaria, dengue or typhoid. It takes as input natural utterances of symptom descriptive sentences and performs sentenising, stemming and tokenizing to extract the symptoms and place them in the two categories of – present and absent. Thereby using the Mutual Information and Information Gain matrices, these symptoms were analysed and the cumulative weightage gave indications of the most probable disease. Finally the most crucial symptom for the disease is verified explicitly and a final diagnosis made.

####################################################

//////////////////////////////////////////////////
Installations and requirements
- Install Python 2.7 win 32bit
- Install numpy
- Install nltk
- Download nltk data
- Install aiml

//////////////////////////////////////////////////


//////////////////////////////////////////////////

The code starts by running medical_diagnosis pyhton file using python interpreter an input transcript can be given but is not mandatory about the problems being suffered.

If transcript given a the software starts the analysis on the symptoms it has extracted from the transcript and based on that it asks only relevant questions particular to the most probable disease

If not provided it starts the analysis by itself asking about the most crucial symptoms 

//////////////////////////////////////////////////


//////////////////////////////////////////////////

About files

medical_diagnosis.py - analog of main file the analysis begins from here
check.py - contains all the functions to be implemented for analysis
			as well as for the identification
disease.py - contains the database of disease vs. symptoms and 
			mutual information matrix and information gain matrix
symptoms.py - contains the database of all the diseases


//////////////////////////////////////////////////
