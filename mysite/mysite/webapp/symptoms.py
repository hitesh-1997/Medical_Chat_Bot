import nltk
symptom = nltk.defaultdict(str)
symptom[''] = 0
symptom['headache'] = 1
symptom['vomit'] = 2
symptom['nausea'] = 3
symptom['pain'] = {'eye': 4, 'muscle': 5 ,'chest': 6, 'nerve': 8, 'joint': 9 ,'abdomin': 14 , 'stomach': 14}
symptom['bleed'] = {'gum': 10, 'nose' : 18}#, 'muscle': 5' ,'ligament': 6', 'tendon': 7' ,'nerve': 8', 'joint': 9' }
symptom['chill'] = 7
symptom['itch'] = 11
symptom['rash'] = 12
symptom['fever'] = 13
symptom['diarrhea'] = 15
symptom['bradycardia'] = 16
symptom['dizz'] = 16
symptom['weak'] = 16
symptom['fatigue'] = 16
symptom['malaise'] = 17
symptom['uneas'] = 17
symptom['discomfort'] = 17

#print symptom['fatigue']


'''
Symptoms of dengue:
headache
vomit
nausea
pain in eye, muscle, ligament, joint, tendon, nerve
bleeding gum
itch
rash
fever

Symptoms of Typhoid:
headache
vomit
diarrhea
nausea
pain in abdomin, muscle
bleeding nose, gums
rash
fever
weak
discomfort

Symptoms of Malaria
lack of a sense of well-being
fatigue - tiredness
fever
prominence of headache
chest pain
abdominal pain
arthralgia
myalgia - muscle pain
diarrhea
Nausea
vomiting
chills'''
