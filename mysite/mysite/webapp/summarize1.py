'''Code Submitted by
Akash Saxena 2010A7PS168P
Annu Sharma 2010A7PS003P
in partial Fulfilment of course
BITS C331
under Dr. A.S. Mandal Sir '''



import nltk, re, check, disease



from disease import *
from check import *



def sentenizer(str): #getting sentences
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    sents = sent_tokenizer.tokenize(str)
    return sents




def stem(word):
     regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment|ous)?$'
     stem, suffix = re.findall(regexp, word)[0]
     return stem

def stem2(word):
     regexp = r'^(.*?)(s|ous|ness|iness)?$'
     stem, suffix = re.findall(regexp, word)[0]
     return stem

    
count = 0 
prob = [] #stores problems faced 
symc = [] #symc stores all symptoms
cp=0
while(1):
    cond = raw_input('Enter your current conditions and sufferings if any \n') #input 
    ind_sen = sentenizer(cond)
    for num in ind_sen:
        cp = cp+1
        sym = '' #sym stores symptoms in a sentence
        pain = ''
        b_part = ''
        neg = ''
        count=0
        ind_wod = nltk.word_tokenize(num)
        for t in ind_wod:
            t = t.lower()
            if(check_neg(t)== True):
                neg = 'no'
            t1 = stem(t)
            t2 = stem2(t)
            if(check_sym(t1)== True):
                if(sym is not ''):
                    sym = sym + ' and ' + t
                    symc.append(t1)
                else:
                    sym = t
                    symc.append(t1)
    
                if(sym is not ''):
                    prob.append(neg + ' ' + sym)


        
   


        
    print 'Symptoms Observed are\n'
    j=0
    '''symc stores all the symptoms after the cleaning part'''
    print symc
    sym_arr = get_sym_arr(symc)
    '''sym_arr is an array of 0's and 1's if the symptoms is present sym_arr[symp_number]=1
    else it is 0'''
    print sym_arr
    d = dis_id(sym_arr)
    print '\nThe disease with maximum probability is \n'
    print d
    '''
    for i in prob:
    j = j+1
    print (j)
    print (i + '\n')'''

    #print 'Symptoms Matching to that of Dengue\n'


    #get_med(symc)

    
    


'''
import nltk, re, check
from check import *

dis = {}

def sentenizer(str): #getting sentences
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    sents = sent_tokenizer.tokenize(str)
    return sents



def stem(word):
     regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment|ous)?$'
     stem, suffix = re.findall(regexp, word)[0]
     return stem

def stem2(word):
     regexp = r'^(.*?)(s|ous)?$'
     stem, suffix = re.findall(regexp, word)[0]
     return stem

    
count = 0 
prob = []
cp=0
cond = raw_input('Enter your current conditions and sufferings if any \n') #input 
ind_sen = sentenizer(cond)
for num in ind_sen:
    cp = cp+1
    sym = ''
    pain = ''
    b_part = ''
    neg = ''
    count=0
    ind_wod = nltk.word_tokenize(num)
    for t in ind_wod:
        if(check_neg(t)== True):
            neg = 'no'
        t1 = stem(t)
        t2 = stem2(t)
        if(check_sym(t1)== True):
                sym = t
        if(check_p(t1) is not ''):
                pain = t
        if(check_body(t2) is not ''):
                b_part = t

    
    if(sym is not ''):
        if(pain is not ''):
            prob.append(neg + ' ' + pain + ' in ' + sym)
        else:
            prob.append(neg + ' ' + sym)
    elif(b_part is not ''):
        if(pain is not ''):
            prob.append(neg + ' ' + pain + ' in ' + b_part)
        else:
            prob.append(neg + ' ' + b_part)
        
print 'Symptoms Observed are\n'
for i in prob:

    print (i + '\n')
    
			
	
            if(sym is not ''):
                if(count==0):
                    dis[sym] = 'SYMP'
                else:
                    sym = 'no ' + sym
                    dis[sym] = 'SYMP'
					
			
					

print dis



            
                
         
##                      
            
tok = nltk.word_tokenize(ex2)
[check(t) for t in 

#pprint.pprint(sents)



def check(word):
	print word
	if (word.startswith('no') or word.startswith('not') or word.startswith('nil') or word.startswith('zero') or word.startswith('nothing') or word.startswith('none') or word.startswith('never'):
		return True
	else:
		return False
		
		
[check(t) for t in tok]
tok = nltk.word_tokenize(ex2)

data = nltk.defaultdict(int)
data['sleep'] = 'SYMP'
data['fever'] = 'SYMP'
def check1(word):
	return data[word]
	

dis = nltk.defaultdict(int)

'''

