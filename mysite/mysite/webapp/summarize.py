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
     regexp = r'^(.*?)(s|ous)?$'
     stem, suffix = re.findall(regexp, word)[0]
     return stem

    
count = 0 
prob = []
symc = []
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
        elif(check_p(t1) is not ''):
                pain = t
        elif(check_body(t2) is not ''):
                b_part = t2

    
    if(sym is not ''):
        #if(pain is not ''):
            #prob.append(neg + ' ' + pain + ' in ' + sym)
        if(b_part is not ''):
            prob.append(neg + ' ' + sym + ' in ' + b_part)
        elif(sym.startswith('bleed')):
            get_ana('bleed',symc)
            prob.append(neg + ' ' + sym)
        else:
            prob.append(neg + ' ' + sym)
    elif(b_part is not ''):
        if(pain is not ''):
            prob.append(neg + ' ' + b_part + ' ' + pain )
            symc.append(neg + ' ' + b_part + ' ' + pain )
        else:
            prob.append(neg + ' ' + b_part)
    elif(pain is not ''):
        get_ana('pain', symc)
        prob.append(neg + ' ' + pain)
        
        
print 'Symptoms Observed are\n'
j=0
for i in prob:
    j = j+1
    print (j)
    print (i + '\n')

print 'Symptoms Matching to that of Dengue\n'
print dis_check(symc)

    

