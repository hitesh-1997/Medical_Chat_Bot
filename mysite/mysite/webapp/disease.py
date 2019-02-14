import  numpy, math
#dengue = nltk.defaultdict(str)

num_disease = 3
num_symptom = 19
disease = numpy.zeros((num_disease, num_symptom))
disease_inv = numpy.zeros((num_disease, num_symptom))
mutual_info = numpy.zeros((num_disease, num_symptom))
info_gain = numpy.zeros((num_disease, num_symptom))
a = numpy.zeros((num_disease, num_symptom))
a[0] = [ 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]

disdata = ['dengue','typhoid','malaria']
'''            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18 '''
disease[0] = [ 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0] #,1 ,1 ,0, 1 ,0]
disease[1] = [ 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
disease[2] = [ 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0]
disease_inv = 1-disease
#print disease
#print disease[1]*disease[2]

rsum = numpy.zeros((num_disease))
csum = numpy.zeros((num_symptom))
rsumi = numpy.zeros((num_disease))
csumi = numpy.zeros((num_symptom))
msum=0
i=0
j=0
rsum = disease.sum(axis=1)
csum = disease.sum(axis=0)
rsumi = disease_inv.sum(axis=1)
csumi = disease_inv.sum(axis=0)
msum = disease.sum()
msumi = disease_inv.sum()



for i in range (0,num_disease):
    for j in range (0,num_symptom):
        if disease[i][j] != 0:
            mutual_info[i][j] = disease[i][j]*math.log((disease[i][j]*msum*msum)/(rsum[i]*csum[j]))
            info_gain[i][j] = 0
            #info_gain[i][j] = disease[i][j]*math.log((disease[i][j]*msum*msum)/(rsum[i]*csum[j]))
        else:
            mutual_info[i][j] = 0
            info_gain[i][j] = disease_inv[i][j]*math.log((disease_inv[i][j]*msum*msum)/(rsum[i]*(msum-csum[j])))
'''
print 'aa'
print disease_inv        
        

print rsumi
print "\n"
print csumi
print "mutual info" 

print  mutual_info
print info_gain
print disdata[0]

dengue['headache'] = 'SYM'
dengue['pain'] = 'SYMP'
dengue['eye'] = 'SYMPBP'
dengue['muscle'] = 'SYMPBP'
dengue['ligament'] = 'SYMPBP'
dengue['tendon'] = 'SYMPBP'
dengue['nerve'] = 'SYMPBP'
dengue['joint'] = 'SYMPBP'
dengue['bleed'] = 'SYMB'
dengue['gum'] = 'SYMBBP'
dengue['rash'] = 'SYM'
dengue['itch'] = 'SYM'
dengue['vomit'] = 'SYM'
dengue['nausea'] = 'SYM'
dengue['fever'] = 'SYMF'
dengue['rash'] = 'SYMR'



body = nltk.defaultdict(str)
body['arm'] = 'BODY'
body['eye'] = 'BODY'
body['eyebrow'] = 'BODY'
body['belly'] = 'BODY'
body['leg'] = 'BODY'
body['breast'] = 'BODY'
body['thumb'] = 'BODY'
body['elbow'] = 'BODY'
body['fist'] = 'BODY'
body['finger'] = 'BODY'
body['foot'] = 'BODY'
body['ankle'] = 'BODY'
body['buttock'] = 'BODY'
body['hair'] = 'BODY'
body['neck'] = 'BODY'
body['hand'] = 'BODY'
body['wrist'] = 'BODY'
body['hip'] = 'BODY'
body['chin'] = 'BODY'
body['knee'] = 'BODY'
body['head'] = 'BODY'
body['lip'] = 'BODY'
body['mouth'] = 'BODY'
body['nose'] = 'BODY'
body['nostril'] = 'BODY'
body['upper'] = 'BODY'
body['arm'] = 'BODY'
body['thigh'] = 'BODY'
body['ear'] = 'BODY'
body['bottom'] = 'BODY'
body['back'] = 'BODY'
body['underarm'] = 'BODY'
body['forearm'] = 'BODY'
body['lower'] = 'BODY'
body['leg'] = 'BODY'
body['shoulder'] = 'BODY'
body['forehead'] = 'BODY'
body['waist'] = 'BODY'
body['calf'] = 'BODY'
body['cheek'] = 'BODY'
body['eyelash'] = 'BODY'
body['lash'] = 'BODY'
body['tooth'] = 'BODY'
body['teeth'] = 'BODY'
body['toe'] = 'BODY'
body['tongue'] = 'BODY'
'''
