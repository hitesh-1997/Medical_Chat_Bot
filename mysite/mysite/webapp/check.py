import disease, aiml, numpy , heapq
bot = aiml.Kernel()
bot.learn("std-startup.xml")
bot.respond("load aiml c")

from disease import *
from symptoms import *
from med import *

num_of_disease = 3
num_of_symptoms = 19
dis = numpy.zeros((num_of_disease,1))
sym_arr = [0]*num_of_symptoms
sym_check = [0]*num_of_symptoms
 
def initialise():
	for i in range(0,num_of_symptoms):
		sym_arr[i] = 0
		sym_check[i] = 0
	for i in range(0,num_of_disease):
		dis[i] = 0
	
	


def check_neg(word):
	if (word.startswith('no') or word.startswith('not') or word.startswith('nil') or word.startswith('zero') or word.startswith('nothing') or word.startswith('loss') or word.startswith('none') or word.startswith('never')):
		return True
	else:
		return False
		
		
def check_p(word):
	#print word
	if (word.startswith('pain') or word.startswith('trouble') or word.startswith('problem') or word.startswith('ache') or word.startswith('agon') or word.startswith('bad') or word.startswith('excruciat') or word.startswith('groan') or word.startswith('hurt') or word.startswith('irrit') or word.startswith('sting') or word.startswith('stab') or word.startswith('sore') or word.startswith('suffer') or word.startswith('throb') or word.startswith('twing') or word.startswith('injur') or word.startswith('sharp')):
		return word
	else:
		return ''
		
		

def check_sym(word):
	if( word.startswith('pain') or word.startswith('chill')    or word.startswith('itch') or word.startswith('sleep')    or word.startswith('fever') or word.startswith('rash') or word.startswith('headache')  or 	word.startswith('vomit')  or 	word.startswith('boredom') or 	word.startswith('nause')  or 	word.startswith('ill') or word.startswith('bleed') or word.startswith('diarrhea')  or 	word.startswith('dizz')  or word.startswith('weak')  or 	word.startswith('fatigue')  or 	word.startswith('uneas')  or word.startswith('discomfort')  or 	word.startswith('malaise')):
		return True
	else:
		return False
		

def check_body(word):
	if( word.startswith('arm') or word.startswith('eye') or word.startswith('eyebrow') or word.startswith('belly') or word.startswith('leg') or word.startswith('breast') or word.startswith('thumb') or word.startswith('elbow') or word.startswith('fist') or word.startswith('finger') or word.startswith('foot') or word.startswith('ankle') or word.startswith('muscle') or word.startswith('buttocks') or word.startswith('skin') or word.startswith('hair') or word.startswith('neck') or word.startswith('hand') or word.startswith('arm') or word.startswith('wrist') or word.startswith('hip') or word.startswith('chin') or word.startswith('knee') or word.startswith('head') or word.startswith('lip') or word.startswith('mouth') or word.startswith('nose') or word.startswith('nostril') or word.startswith('upper arm') or word.startswith('thigh') or word.startswith('ear') or word.startswith('bottom') or word.startswith(' bum') or word.startswith('back') or word.startswith('underarm') or word.startswith(' forearm') or word.startswith('lower leg') or word.startswith('shoulder') or word.startswith('forehead') or word.startswith('waist') or word.startswith('calf ') or word.startswith('cheek') or word.startswith('eyelash') or word.startswith(' lash') or word.startswith('tooth') or word.startswith('teeth') or word.startswith('toe') or word.startswith('tongue') ):
		return word
	else:
		return ''

'''this func. takes sym as input which is an array containing symptoms in textual
format and it returns an array of 0's and 1's if the symptom is present or not'''

def get_sym_arr(sym = []):
	print sym_arr
	j=0
	for i in sym:
		print i
		#sym[j] = ''.join(sym[j].split())
		if(symptom[i] is not ''):
			j = symptom[i]
			if ( j >= 0 and j <= 100):
				sym_arr[j] = 1
			#j = j+1
	return sym_arr
''' master function taking input the above calculated array of 0's and 1's of
symptoms and returns the disease'''

def dis_id(sym = []):
        #ana_pain(sym)
        dis_sym(sym)
        dis_break = dis
        while stop_cond():
                #print dis
                cri_sym = find_max()
                if(cri_sym == -1):
                        return disdata[find_max_dis()]
                sym_check[cri_sym] = 1
                pres = anal_sym(cri_sym)
                #print pos
                #if(pres == 1):
                update_dis(cri_sym,pres)
        return disdata[find_max_dis()]
		
def dis_id2(sym = []):
        #ana_pain(sym)
			
        dis_sym(sym)
        dis_break = dis
        if stop_cond():
			#print dis
			cri_sym = find_max()
			if(cri_sym == -1):
				return disdata[find_max_dis()], True
			sym[cri_sym] = 2
			return sym, False
        return disdata[find_max_dis()], True

        

''' takes array of 0's and 1's of symptoms it updates the array sym_check with
whatever symptoms have already been covered. If a symptom has been observed then
it would check the value as 1 which by default is 0'''
def dis_sym(sym = []):
	for i in range(0,num_of_symptoms):
		if(sym[i] == 1):
			sym_check[i] = 1
			update_dis(i,1)
		if(sym[i] == 2):
			sym[i] = 0
			sym_check[i] = 1
             
'''updates the dis array which contains the sum of mutual information of all the
symptoms that have been observed till now of all the symptoms'''

def update_dis(symno,pres):
        #print symno
        if(pres==1):
                for j in range(0,num_of_disease):
                        dis[j] = dis[j] + mutual_info[j][symno]
                        #print info_gain[j][symno]
        else:
                for j in range(0,num_of_disease):
                        dis[j] = dis[j] + info_gain[j][symno]
                        #print info_gain[j][symno]
                
        
        
        print (str(dis[0])  + str(dis[1]) + str(dis[2]) )
        

''' firstly finds the disease with highest probability of having and then finds
the most important symbol for that disease and returns the number of
that disease'''
def find_max():  # getting the next symptom to be checked based on current situation
        max=-1
        k=0  
        for i in range(0,num_of_disease):  # getting the max of probability of a disease
                if(dis[i]>max):
                        max = dis[i]
                        k=i
        max=-1
        s=-1
        for i in range(0,num_of_symptoms):
                if(mutual_info[k][i]>max and sym_check[i]==0):  # getting which is the most important symptom for the most probable disease
                        max = mutual_info[k][i]
                        #sym_check[i] = 1
                        s = i
        return s
                
''' takes symptom number as input and checks whether that symptom is observed
in the patient or not using the Q/A analysis'''
def anal_sym(i): #return +1 if this particular symptom (i) is found based on Q/A analysis else returns -1
                #print i
                ans='no'
                if ( i == 1):
                      ans = raw_input('Have you been experiencing headache (yes/no)\n>>')
                      
                elif ( i == 2):
                        ans = raw_input('Have you been experiencing vomit (yes/no)\n>>')
                        
                elif ( i == 3):
                        ans = raw_input('Have you been experiencing nausea (yes/no)\n>>')
                        
                elif ( i == 4):
                        ans = raw_input('Have you been experiencing pain in eye (yes/no)\n>>')
                        
                elif ( i == 5):
                        ans = raw_input('Have you been experiencing pain in muscle (yes/no)\n>>')
                        
                elif ( i == 6):
                        ans = raw_input('Have you been experiencing pain in chest (yes/no)\n>>')
                        
                elif ( i == 7):
                        ans = raw_input('Have you been experiencing chills or high spike in fever (yes/no)\n>>')
                        
                elif ( i == 8):
                        ans = raw_input('Have you been experiencing pain in nerve (yes/no)\n>>')
                        

                elif ( i == 9):
                        ans = raw_input('Have you been experiencing pain in joint (yes/no)\n>>')
                        
                elif ( i == 10):
                        ans = raw_input('Have you been experiencing bleeding gums (yes/no)\n>>')
                        
                elif ( i == 11):
                        ans = raw_input('Have you been experiencing itching  (yes/no)\n>>')
                        
                elif ( i == 12):
                        ans = raw_input('Are there any rashes occuring (yes/no)\n>>')
                        
                elif ( i == 13):
                        ans = raw_input('Have you been experiencing fever (yes/no)\n>>')
                        
                elif ( i == 14):
                        ans = raw_input('Have you been experiencing abdominal pain or stomach ache (yes/no)\n>>')
                        
                elif ( i == 15):
                        ans = raw_input('Have you been experiencing diarrhea (yes/no)\n>>')
                        
                elif ( i == 16):
                        ans = raw_input('Have you been experiencing dizziness (yes/no)\n>>')
                        
                elif ( i == 17):
                        ans = raw_input('Have you been experiencing discomfort (yes/no)\n>>')
                        
                elif ( i == 18):
                        ans = raw_input('Have you been experiencing bleeding nose (yes/no)\n>>')

                print ans
                if ( ans == 'yes'):
                        return 1
                else :
                        return -1


'''this just returns the disease with the max. probability of the disease'''
def find_max_dis():
        max=-1
        k=0  
        for i in range(0,num_of_disease):  # getting the max of probability of a disease
                if(dis[i]>max):
                        max = dis[i]
                        k=i
        return k

'''returns true if a particular disease is identified with a significant weightage'''
def stop_cond():
        max_dis = find_max_dis()
        if((disease[max_dis]*sym_check).sum() == disease[max_dis].sum() and (dis.max()-max_diff())>uncom_sym()):
                return 0
        else:
                return 1
                
                

'''returns the weightage of the 2nd most probable disease'''
def max_diff():
        maxv = heapq.nlargest(2, dis)
        return maxv[1]

''' returns the '''
def uncom_sym():
        m = numpy.where(dis==dis.max())
        s = numpy.where(dis==max_diff())
        most = m[0][0]
        smost = s[0][0]
        
        least_diff = []
        for i in range(0,num_of_symptoms):
                if( mutual_info[most][i] !=0 and mutual_info[smost][i] ==0):
                        least_diff.append(mutual_info[most][i])

        
        #print min(least_diff)
        return min(least_diff)
                        
                        
                        
                
                
        
		
def dis_check(a = []):
	count=0
	j=0
	for i in a:
		a[j] = ''.join(a[j].split())
		print a[j]
		if(dengue[a[j]] is 'SYM'):
			dis[0] = dis[0]+1	
		j = j+1
	return dis[0]
	
	
def ana_pain(d = []):
        c = 1
        b=1
        while (c): #
                print bot.respond("pain")
                c = c-1
                while (b>0):
                        a = bot.respond(raw_input("> "))
                        a = a.lower()
                        d.append(a)
                        b = b-1
                    
   
        return d
                        
def ana_bleed(d = []):
        c = 1
        b = 1
        while (c):
                 #print bot.respond("bleed")
                 c = c-1
                 while (b>0):
                        a = bot.respond(raw_input("> "))
                        a = a.lower()
                        d.append(a)
                        b = b-1
        return d

def ana_fever(d = []):
        c = 1
        b = 1
        while (c):
                 #print bot.respond("bleed")
                 c = c-1
                 while (b>0):
                        a = bot.respond(raw_input("> "))
                        a = a.lower()
                        d.append(a)
                        b = b-1
        return d
'''
                                
def get_med(sys = []):
        med = []
        j=0
        k=0
        for i in sys:
                if(medicine[i] is not ''):
                        med.append(medicine[i])
                        j=j+1
        print "\nSuggested medications for the given medical condition\n"
        while k<j:
                print med[k]
                k = k+1
        return j
def ana_sym(i,sym = []):
        j=0
        for i in sym:
                sym[j] = ''.join(sym[j].split()) 
                if(dengue[sym[j]] is 'SYMP'):
                        p = []
                        p = ana_pain(i,p)
                elif(dengue[sym[j]] is 'SYMB'):
                        b = []
                        b = ana_bleed(i,b)
                elif(dengue[sym[j]] is 'SYMF'):
                        f = []
                        f = ana_fever(i,f)


'''
