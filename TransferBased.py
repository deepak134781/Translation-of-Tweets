#!/usr/bin/python2
import enchant
import csv
import nltk

     
d=enchant.Dict("en_US")


s = raw_input("enter your string \n")
class Queue:
	    def __init__(self):
	        self.items = []
	
	    def isEmpty(self):
	        return self.items == []
	
	    def enqueue(self, item):
	        self.items.insert(0,item)
	
	    def dequeue(self):
	        return self.items.pop()	

	    def size(self):
	        return len(self.items)
q=Queue()
m=[]
m=s.split(" ")
#print m
for i in range(len(m)):
    with open('Dict.csv','rb') as csvfile:
        spamreader=csv.reader(csvfile,delimiter=',')
        for row in spamreader:
          if(m[i]==row[0]):
             m[i]=row[1]
            
#for i in range(len(m)):
  #print m[i]
s1=""
for i in range(len(m)):
    s1+=m[i]+" "
#print  s1
text=nltk.word_tokenize(s1)
m1=[]
PRONOUN=""
NOUN=""
VERB=""
ADVERB=""
ADJECTIVE=""
m1= nltk.pos_tag(text)
#print m1
for i in range(len(m1)):
    if(m1[i][1]=='PRP' or m1[i][1]=='PRP$' or m1[i][1]=='WP' or m1[i][1]=='WP$'):
       PRONOUN=m1[i][0]
    if(m1[i][1]=='NN' or m1[i][1]=='NNS' or m1[i][1]=='NNP'or m1[i][1]=='NNPS'):
       NOUN=m1[i][0]
    if(m1[i][1]=='VB' or m1[i][1]=='VBD' or m1[i][1]=='VBG' or m1[i][1]=='VBN'  or m1[i][1]=='VBZ' or m1[i][1]=='VBP'):
       VERB=m1[i][0]
    if(m1[i][1]=='RB' or m1[i][1]=='RBR' or m1[i][1]=='RBS' or m1[i][1]=='WRB'):
       ADVERB=m1[i][0]
    if(m1[i][1]=='JJ' or m1[i][1]=='JJR' or m[i][1]=='JJS' ):
       ADJECTIVE=m1[i][0]
#print PRONOUN , NOUN , VERB , ADVERB , ADJECTIVE 
m2=["S","NP","VP","PRON","NOUN","AUX","Y","ADV","ADJ",PRONOUN,NOUN,VERB,ADVERB,ADJECTIVE]
#for i in range(len(m2)):
#  print i , m2[i]

a=[[1,2],[3,4],[5,6],[9],[10],[11],[12,13],[],[],[],[],[],[],[]]

visit=[False]*14

def dfs(s2,a,visit,m2):
   visit[s2]=True
   for i in range(len(a[s2])):
       if(visit[a[s2][i]]==False):
             dfs(a[s2][i],a,visit,m2)
   if(s2>8 and m2[s2]!=" "):
     print m2[s2],
   return   

dfs(0,a,visit,m2)











