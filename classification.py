#!/usr/bin/python2
import re
import csv
import langid
import enchant
import goslate

s = raw_input("enter your string \n")
f=0
f1=0
p=langid.classify(s)
if(p[0]=='en'):
 gs=goslate.Goslate()
 print(gs.translate(s,'en'))
 #print p[0]
 #f=1
elif(p[0]=='hi'):
 #print p[0]
 gs=goslate.Goslate()
 print(gs.translate(s,'en'))
else:
 gs=goslate.Goslate()
 print(gs.translate(s,'en')) 
 #f1=1
 #print 'language is neither english nor hindi .'
m=[]
m=s.split(" ")
n=len(m)
n1=0
d=enchant.Dict("en_US")
if(f==1):
 for i in range(n):
    #print m[i]
    if(m[i]<>''):
     p1=d.check(m[i])
     if(p1==True):
      n1+=1
 #print n1
 if(n/2>=n1):
  f1=1
  #print 'text is target text' 
 else:
  print 'text is english text'



if(f1==1):
 #for i in range(len(m)):
 #    print m[i]
 #print n
 type1=0
 word1=''
 word2=''
 flag=0
 g=''
 if(m[n-1]=='h' or m[n-1]=='hai' or m[n-1]=='hun' or m[n-1]=='h' or m[n-1]=='he'):
  type1=1
  if(n-2>=0):
     word1=m[n-2]
  if(n-3>=0):
     word2=m[n-3]
  del m[n-1]
  n=n-1  
 elif(m[n-1]=='tha' or m[n-1]=='the' or m[n-1]=='thi'or m[n-1]=='thin'):
  type1=2
  if(n-2>=0):
     word1=m[n-2]
  if(n-3>=0):
     word2=m[n-3]
  del m[n-1]
  n=n-1 
 elif(m[n-1]=='rahega' or m[n-1]=='rahegi' or m[n-1]=='rahengi' or m[n-1]=='rahegi' or m[n-1]=='rhega' or m[n-1]=='rhegi' or m[n-1]=='rhege' or m[n-1]=='rhengi'):
   type1=3
   if(n-2>=0):
      word1=m[n-2]
   if(n-3>=0):
      word2=m[n-3]
   del m[n-1]
   n=n-1  
 elif(m[n-1]=='chukega' or m[n-1]=='chukegi' or m[n-1]=='chukegi'or m[ n-1]=='chukenge' or m[n-1]=='chukege'):
     type1=3
     flag=3
     if(m[n-1]=='chukega'):
        g='m'
     if(m[n-1]=='chukegi' or m[n-1]=='chukegee'):
        g='f'   
     del m[n-1]
     n=n-1  
 elif(m[n-1]=='gaya' or m[n-1]=='gya' or m[n-1]=='gayi' or m[n-1]=='gayee' or m[n-1]=='gyi' or m[n-1]=='gyee' or m[n-1]=='gee' or m[n-1]=='gi' or m[n-1]=='gye' or m[n-1]=='gaye' or m[n-1]=='gyin' or m[n-1]=='gyeen' or m[n-1]=='gayin' or m[n-1]=='gayeen'):
     type1=2
     flag=5
     if(m[n-1]=='gaya' or m[n-1]=='gya'):
       g='m'
     if(m[n-1]=='gayi' or m[n-1]=='gayee' or m[n-1]=='gyi' or m[n-1]=='gyee' or m[n-1]=='gee' or m[n-1]=='gi'):
       g='f' 
     del m[n-1]
     n=n-1
 elif(m[n-1]=='jayega' or m[n-1]=='jaega' or m[n-1]=='jayegi' or m[n-1]=='jaegi' or m[n-1]=='jayenge' or m[n-1]=='jaenge' or m[n-1]=='jayengi' or m[n-1]=='jaengi'):
     type1=3
     flag=5
     if(m[n-1]=='jayega' or m[n-1]=='jaega'):
       g='m'
     if(m[n-1]=='jayegi' or m[n-1]=='jaegi'):
       g='f'
     del m[n-1]
     n=n-1    
 if(type1==0):
  try:
    word1=m[n-1]
    m1=re.search('ega$|egi$|egee$|enge$|ege$',m[n-1])
    if(m1.group(0)=='ega' or m1.group(0)=='egi' or m1.group(0)=='egee' or m1.group(0)=='enge' or m1.group(0)=='ege'):
       type1=3
       flag=1 
       if(m1.group(0)=='ega'):
          g='m'
       if(m1.group(0)=='egi' or m1.group(0)=='egee'):
          g='f' 
  except AttributeError:
      xyz=0
 if(type1==0):
  try:
     word1=m[n-1]
     m1=re.search('a$|ee$|i$|e$',m[n-1])
     if(m1.group(0)=='a' or m1.group(0)=='ee' or m1.group(0)=='i' or m1.group(0)=='e'):
       type1=2
       flag=1  
       if(m1.group(0)=='a'):
          g='m'
       if(m1.group(0)=='i' or m1.group(0)=='ee'):
          g='f'  
  except AttributeError:
      xyz=0
 #print type1 , word1 ,word2


 if(type1==1):
  flag1=0
  flag2=0
  flag3=0
  flag4=0
  flag7=0
  flag8=0 
  flag9=0 
  flag10=0
 
  try:
      if(word1=='rha' or word1=='rhi' or word1=='rhe' or word1=='raha' or word1=='rahi' or word1=='rahe' or word1=='rahee' or word1=='rhee'):
         flag2=1
         if(word1=='raha' or word1=='rha'):
             g='m'
         if(word1=='rahi' or word1=='rhi' or word1=='rahee' or word1=='rhee'):
             g='f'   
         del m[n-1]
         n=n-1  
         if(word2=='ja' or word2=='jaa'):
           flag8=1
           del m[n-1]
           n=n-1    
         else:
          m1=re.search('ta$|ti$|te$',word2)
          if(m1.group(0)=='ta' or m1.group(0)=='ti' or m1.group(0)=='te'):
            flag4=1
            if(m1.group(0)=='ta'):
                 g='m'
            if(m1.group(0)=='ti'):
                 g='f'  
      elif(flag2==0):
         m1=re.search('ta$|ti$|te$',word1) 
         if(m1.group(0)=='ta' or m1.group(0)=='ti' or m1.group(0)=='te'):
           flag1=1
         if(m1.group(0)=='ta'):
             g='m'
         if(m1.group(0)=='ti'):
             g='f'  
         if(word1=='jata' or word1=='jati' or word1=='jate'):
           flag7=1
           del m[n-1]
           n=n-1  
         
  except AttributeError:
          xyz=0
  """
  try:
    if(word1=='gaya' or word1=='gee' or word1=='gi' or word1=='gye' or word1=='ge'or word1=='gyee' or word1=='gyi',word1=='gya' or word1=='gayee'or word1=='gayi' or word1=='gaye'):
       #print word1,'called' 
       m3=re.search('a$|i$|ee$|e$',word2)
       if(m3.group(0)=='a' or m3.group(0)=='i' or m3.group(0)=='ee' or m3.group(0)=='e'):
         flag9=1   
         if(m3.group(0)=='a'):
             g='m'
         if(m3.group(0)=='i' or m3.group(0)=='ee'):
             g='f'
         del m[n-1]
         n=n-1         
  except AttributeError:
      xyz=0
  """
   
  try:
     if(flag1==0 and flag2==0 and flag4==0):
       m2=re.search('a$|ee$|i$|e$',word1)
       if(word1=='chuka' or word1=='chuki' or word1=='chuke' or word1=='chukee'):
            flag3=1
            if(word1=='chuka'):
                g='m'
            if(word1=='chuki' or word1=='chukee'):
                g='f' 
            del m[n-1]
            n=n-1 
            if(word2=='ja' or word2=='jaa'):
              flag9=1
              del m[n-1]
              n=n-1 
       elif(m2.group(0)=='a' or m2.group(0)=='ee' or m2.group(0)=='e' or m2.group(0)=='i'):
            flag3=1
            if(m2.group(0)=='a'):
                g='m'
            if(m2.group(0)=='i' or m2.group(0)=='ee'):
                g='f'   
  except AttributeError:
          xyz=0
   
  subject=''
  verb=''
  object1=''
  no=''
  flag5=0
  flag6=0  
  for i in range(len(m)):
      with open('hindi_english_mix.csv','rb') as csvfile:
         spamreader=csv.reader(csvfile,delimiter=',')
         for row in spamreader:
           try: 
             m1=re.search(row[0],m[i])
             if(m1.group(0)<>''):
               #print row[1],row[0]
               m[i]=row[1]
               #print m[i]
               if(m[i]=='not'):
                no=m[i]
               break
           except AttributeError:
               xyz=0    
   
  for i in range(n):
        with open('PartOfSpeech.csv','rb') as csvfile1:
         spamreader1=csv.reader(csvfile1,delimiter=',')
         for row in spamreader1:
            if(m[i]==row[0] and (row[1]=='Noun' or row[1]=='Pronoun') and flag5==0):
               subject=m[i]
               flag5=1
               break 
            elif(m[i]==row[0] and (row[1]=='Noun' or row[1]=='Pronoun') and flag5==1):
               object1=m[i]
               break  
            elif(m[i]==row[0] and row[1]=='Verb'):
               verb=m[i]
               break
      
  if(flag8==1 and flag2==1): 
     #print 6   
     with open('FormsOfVerb.csv','rb') as csvfile2:
            spamreader2=csv.reader(csvfile2,delimiter=',')
            for row in spamreader2:
              if(verb==row[0]):
                verb=row[2]
                break  

     if(object1<>''):
        object1='by '+object1
     if(subject=='we' or subject=='you' or subject=='they'):
          flag10=1
          print subject,'are',no,'being',verb,object1,'.'
     elif(subject=='i'):
          flag10=1
          print subject,'am',no,'being',verb,object1,'.'
     elif(subject=='it'):
          flag10=1
          print subject,'is',no,'being',verb,object1,'.'
     elif(subject=='he' and g=='m'):
          flag10=1
          print subject,'is',no,'being',verb,object1,'.'
     elif(subject=='he' and g=='f'):
          flga10=1
          subject='she'
          print subject,'is',no,'being',verb,object1,'.'
     try:
         if(flag10==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag10=1
              print subject,'are',no,'being',verb,object1,'.'
         
     except AttributeError:
       xyz=0
     if(flag10==0):
       print subject,'is',no,'being',verb,object1,'.'  
      
  elif(flag4==1 and flag2==1):
      #print 4 
      with open('FormsOfVerb.csv','rb') as csvfile2:
            spamreader2=csv.reader(csvfile2,delimiter=',')
            for row in spamreader2:
              if(verb==row[0]):
                verb=row[4]
                break 
      
      if(subject=='i' or subject=='we' or subject=='you' or subject=='they'):
           flag10=1
           print subject,'have',no,'been',verb,object1,'.'
      elif(subject=='it'):
           flag10=1
           print subject,'has',no,'been',verb,object1,'.'
      elif(subject=='he' and g=='m'):
           flag10=1
           print subject,'has',no,'been',verb,object1,'.'
      elif(subject=='he' and g=='f'):
           flag10=1
           subject='she'
           print subject,'has',no,'been',verb,object1,'.'
      try:
         if(flag10==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag10=1
              print subject,'have',no,'been',verb,object1,'.'
         
      except AttributeError:
       xyz=0
      if(flag10==0):
        print subject,'has',no,'been',verb,object1,'.'  
         
  elif(flag4==0 and flag2==1):
      #print 2
      with open('FormsOfVerb.csv','rb') as csvfile2:
            spamreader2=csv.reader(csvfile2,delimiter=',')
            for row in spamreader2:
              if(verb==row[0]):
                verb=row[4]
                break 
      
      if(subject=='we' or subject=='you' or subject=='they'):
          flag10=1
          print subject ,  'are' , no , verb , object1,'.'
      elif(subject=='i'):
          flag10=1
          print subject,'am',no,verb,object1,'.'  
      elif(subject=='it'):
          flag10=1
          print subject,'is',no,verb,object1,'.'
      elif(subject=='he' and g=='m'):
          flag10=1 
          print subject,'is',no,verb,object1,'.'
      elif(subject=='he' and g=='f'):
          flag10=1
          subject='she'
          print subject,'is',no,verb,object1,'.' 
      try:
         if(flag10==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag10=1
              print subject,'are',no,verb,object1,'.'
         
      except AttributeError:
        xyz=0
      if(flag10==0):
        print subject,'is',no,verb,object1,'.'  
     
  elif(flag1==1 and flag7==1 and flag2==0):
       #print 5
       with open('FormsOfVerb.csv','rb') as csvfile2:
            spamreader2=csv.reader(csvfile2,delimiter=',')
            for row in spamreader2:
              if(verb==row[0]):
                verb=row[2]
                break 
       if(object1<>''):
          object1='by ' + object1 
       if(subject=='we' or subject=='you' or subject=='they'):
           flag10=1
           print subject,'are',no,verb,object1,'.'
       elif(subject=='i'):
           flag10=1
           print subject,'am',no,verb,object1,'.'
       elif(subject=='it'):
           flag10=1
           print subject,'is',no,verb,object1,'.'
       elif(subject=='he' and g=='m'):
           flag10=1
           print subject,'is',no,verb,object1,'.'
       elif(subject=='he' and g=='f'):
           flag10=1 
           subject='she'
           print subject,'is',no,verb,object1,'.'
       try:
         if(flag10==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag10=1
              print subject,'are',no,verb,object1,'.'
         
       except AttributeError:
         xyz=0
       if(flag10==0):
          print subject,'is',no,verb,object1,'.'  
  elif(flag1==1 and flag2==0):
      #print 1
      if(subject=='i' or subject=='you' or subject=='we' or subject=='they'):
        flag10=1 
        if(no=='not'):
          no='do not'
        print subject,no,verb,object1,'.'
      elif(subject=='it'):
          flag10=1 
          if(no=='not'):
            print subject,'does',no,verb,object1,'.'
          else:
            with open('FormsOfVerb.csv','rb') as csvfile2:
              spamreader2=csv.reader(csvfile2,delimiter=',')
              for row in spamreader2:
                if(verb==row[0]):
                  verb=row[3]
                  break 
            print subject,verb,object1,'.'
      elif(subject=='he' and g=='m'):
         flag10=1  
         if(no=='not'):
           print subject,'does',no,verb,object1,'.'
         else:
           with open('FormsOfVerb.csv','rb') as csvfile2:
              spamreader2=csv.reader(csvfile2,delimiter=',')
              for row in spamreader2:
                if(verb==row[0]):
                  verb=row[3]
                  break 
           print subject,verb,object1,'.'  
       
      elif(subject=='he' and g=='f'):
         subject='she' 
         flag10=1
         if(no=='not'):
            print subject,'does',no,verb,object1,'.'   
         else:
          with open('FormsOfVerb.csv','rb') as csvfile2:
            spamreader2=csv.reader(csvfile2,delimiter=',')
            for row in spamreader2:
               if(verb==row[0]):
                  verb=row[3]
                  break
          print subject,verb,object1,'.'
      try:
         if(flag10==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag10=1
              if(no=='not'):
                no='do not' 
              print subject,no,verb,object1,'.'
         
      except AttributeError:
        xyz=0
      if(flag10==0):
         if(no=='not'):
           print subject,'does',no,verb,object1,'.'
         else:
           with open('FormsOfVerb.csv','rb') as csvfile2:
            spamreader2=csv.reader(csvfile2,delimiter=',')
            for row in spamreader2:
               if(verb==row[0]):
                  verb=row[3]
                  break 
           print subject,verb,object1,'.'
  elif(flag9==1):
      #print 7
      with open('FormsOfVerb.csv','rb') as csvfile2:
              spamreader2=csv.reader(csvfile2,delimiter=',')
              for row in spamreader2:
                 if(verb==row[0]):
                  verb=row[2]
                  break
      if(object1!=''):
        object1='by '+object1
      if(subject=='i' or subject=='we' or subject=='you' or subject=='they'):
        flag10=1
        print subject,'have',no,'been',verb,object1,'.'
      elif(subject=='it'):
        flag10=1
        print subject,'has',no,'been',verb,object1,'.'
      elif(subject=='he' and g=='m'):
        flag10=1
        print subject,'has',no,'been',verb,object1,'.'
      elif(subject=='he' and g=='f'):
        flag10=1
        subject='she'
        print subject,'has',no,'been',verb,object1,'.'
      try:
         if(flag10==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag10=1
              print subject,'have',no,'been',verb,object1,'.'
         
      except AttributeError:
        xyz=0
      if(flag10==0):
         print subject,'has',no,'been',verb,object1,'.'             
  elif(flag3==1 and flag2==0 and flag1==0):
      #print 3
      with open('FormsOfVerb.csv','rb') as csvfile2:
              spamreader2=csv.reader(csvfile2,delimiter=',')
              for row in spamreader2:
                 if(verb==row[0]):
                  verb=row[2]
                  break    
    
      if(subject=='i' or subject=='we' or subject=='you' or subject=='they'):
            flag10=1
            print subject,'have',no,verb,object1,'.'
      elif(subject=='it'):
            flag10=1
            print subject,'has',no,verb,object1,'.'
      elif(subject=='he' and g=='m'):
             flag10=1 
             print subject ,'has',no,verb,object1,'.'
      elif(subject=='he' and g=='f'):
           flag10=1
           subject='she'
           print subject,'has',no,verb,object1,'.' 
      try:
         if(flag10==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag10=1
              print subject,'have',no,verb,object1,'.'
         
      except AttributeError:
        xyz=0
      if(flag10==0):
         print subject,'has',no,verb,object1,'.'  
 elif(type1==2):
   flag1=0
   flag2=0
   flag3=0
   flag4=0 
   flag7=0 
   flag8=0 
   """
   try:
    if(word1=='gaya' or word1=='gee' or word1=='gi' or word1=='gye' or word1=='ge'or word1=='gyee' or word1=='gyi',word1=='gya' or word1=='gayee'or word1=='gayi' or word1=='gaye'):
       m3=re.search('a$|i$|ee$|e$',word2)
       if(m3.group(0)=='a' or m3.group(0)=='i' or m3.group(0)=='ee' or m3.group(0)=='e'):
         flag7=1
         if(word1=='gaya' or word1=='gya'):
           g='m'
         if(word1=='gyi' or word1=='gayi' or word1=='gyee' or word1=='gayee' or word1=='gee' or word1=='gi'):
           g='f'
         del m[n-1]
         n=n-1     
       
   except AttributeError:
      xyz=0
   """  
   try:
    if(flag==1):
     xyz=0
    elif(word1=='raha' or word1=='rahi' or word1=='rahe' or word1=='rha' or word1=='rhi' or word1=='rhe'):
      flag1=1
      if(word1=='raha' or word1=='rha'):
        g='m'
      if(word1=='rahi' or word1=='rhi'):
        g='f'
      del m[n-1]
      n=n-1     
      if(word2=='ja' or word2=='jaa'):
          flag4=1
          del m[n-1]
          n=n-1 
      else:

         m1=re.search('ta$|ti$|te$',word2)
         if(m1.group(0)=='ta' or m1.group(0)=='ti' or m2.group(0)=='te'):
            flag2=1
            if(m1.group(0)=='ta'):
                    g='m'
            if(m1.group(0)=='ti'):
                    g='f' 
    elif(flag1==0):
       m1=re.search('a$|ee$|i$|e$',word1)
       if(word1=='chuka' or word1=='chuki' or word1=='chuke'or word1=='chukee'):
          flag3=1
          if(word1=='chuka'):
              g='m'
          if(word1=='chuki' or word1=='chukee'):
              g='f' 
          del m[n-1]
          n=n-1
          if(word2=='ja' or word2=='jaa'):
              flag7=1
              del m[n-1]
              n=n-1 
       elif(m1.group(0)=='a' or m1.group(0)=='ee' or m1.group(0)=='e' or m1.group(0)=='i'):
          flag3=1   
          if(m1.group(0)=='a'):
             g='m'
          if(m1.group(0)=='ee' or m1.group(0)=='i'):
             g='f'  
   except AttributeError:
       xyz=0  
   subject=''
   verb=''
   object1=''
   no=''
   flag5=0
   flag6=0
   for i in range(len(m)):
      with open('hindi_english_mix.csv','rb') as csvfile:
         spamreader=csv.reader(csvfile,delimiter=',')
         for row in spamreader:
           try: 
             m1=re.search(row[0],m[i])
             if(m1.group(0)<>''):
               #print row[1],row[0]
               m[i]=row[1]
               #print m[i]
               if(m[i]=='not'):
                no=m[i]
               break
           except AttributeError:
               xyz=0    
   for i in range(n):
        with open('PartOfSpeech.csv','rb') as csvfile1:
         spamreader1=csv.reader(csvfile1,delimiter=',')
         for row in spamreader1:
            if(m[i]==row[0] and (row[1]=='Noun' or row[1]=='Pronoun') and flag5==0):
               subject=m[i]
               flag5=1
               break 
            elif(m[i]==row[0] and (row[1]=='Noun' or row[1]=='Pronoun') and flag5==1):
               object1=m[i]
               break 
            elif(m[i]==row[0] and row[1]=='Verb'):
               verb=m[i]
               break 
            
  
   if(flag==1):
    #print 1
    if(subject=='i' or subject=='we' or subject=='you' or subject=='it' or subject=='they'):
      flag8=1 
      if(no=='not'):
         print subject,'did',no,verb,object1,'.'
      else:
        with open('FormsOfVerb.csv','rb') as csvfile2:
         spamreader2=csv.reader(csvfile2,delimiter=',')
         for row in spamreader2:
          if(verb==row[0]):
            verb=row[1]
            break
      print subject,verb,object1,'.'
    elif(subject=='he' and g=='m'):
      flag8=1 
      if(no=='not'):
           print subject,'did',no,verb,object1,'.'
      else:
         with open('FormsOfVerb.csv','rb') as csvfile2:
           spamreader2=csv.reader(csvfile2,delimiter=',')
           for row in spamreader2:
            if(verb==row[0]):
             verb=row[1]
             break
         print subject,verb,object1,'.'  
    elif(subject=='he' and g=='f'):
      flag8=1
      subject='she'
      if(no=='not'):
            print subject,'did',no,verb,object1,'.'
      else:
        with open('FormsOfVerb.csv','rb') as csvfile2:
         spamreader2=csv.reader(csvfile2,delimiter=',')
         for row in spamreader2:
          if(verb==row[0]):
            verb=row[1]
            break 
        print  subject,verb,object1,'.'
    try:
         if(flag8==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag8=1
              if(no=='not'):
                 print subject,'did',no,verb,object1,'.'
              else:
                 with open('FormsOfVerb.csv','rb') as csvfile2:
                    spamreader2=csv.reader(csvfile2,delimiter=',')
                    for row in spamreader2:
                        if(verb==row[0]):
                           verb=row[1]
                           break  
                 print subject,verb,object1,'.'
         
    except AttributeError:
          xyz=0
    if(flag8==0):
        if(no=='not'):
           print subject,'did',no,verb,object1,'.'
        else:
             with open('FormsOfVerb.csv','rb') as csvfile2:
                 spamreader2=csv.reader(csvfile2,delimiter=',')
                 for row in spamreader2:
                   if(verb==row[0]):
                     verb=row[1]
                     break
             print subject,verb,object1,'.'   
   elif(flag==5):
    #print 5
    with open('FormsOfVerb.csv','rb') as csvfile2:
         spamreader2=csv.reader(csvfile2,delimiter=',')
         for row in spamreader2:
          if(verb==row[0]):
            verb=row[2]
            break 
    if(object1<>''):
       object1='by '+object1
    if(subject=='we' or subject=='you' or subject=='they'):
         flag8=1
         print subject,'were',no,verb,object1,'.'
    elif(subject=='i' or subject=='it'):
         flag8=1 
         print subject,'was',no,verb,object1,'.'
    elif(subject=='he' and g=='m'):
         flag8=1
         print subject,'was',no,verb,object1,'.'
    elif(subject=='he' and g=='f'):
         flag8=1    
         subject='she'
         print subject,'was',no,verb,object1,'.'
    try:
         if(flag8==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag8=1
              print subject,'were',no,verb,object1,'.'
         
    except AttributeError:
          xyz=0
    if(flag8==0):
         print subject,'was',no,verb,object1,'.'  
   elif(flag1==1 and flag4==1):
      #print 6 
      with open('FormsOfVerb.csv','rb') as csvfile2:
         spamreader2=csv.reader(csvfile2,delimiter=',')
         for row in spamreader2:
          if(verb==row[0]):
            verb=row[2]
            break 
      if(object1<>''):
          object1='by '+object1
      if(subject=='we' or subject=='you' or subject=='they'):
          flag8=1
          print subject,'were',no,'being',verb,object1,'.'
      elif(subject=='i' or subject=='it'):
          flag8=1
          print subject,'was',no,'being',verb,object1,'.'
      elif(subject=='he' and g=='m'):
          flag8=1
          print subject,'was',no,'being',verb,object1,'.'
      elif(subject=='he' and g=='f'):
          flag8=1
          subject='she'
          print subject,'was',no,'being',verb,object1,'.'
      try:
         if(flag8==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag8=1
              print subject,'were',no,'being',verb,object1,'.'
         
      except AttributeError:
          xyz=0
      if(flag8==0):
         print subject,'was',no,'being',verb,object1,'.'   
   elif(flag1==1 and flag2==1):
    #print 4
    with open('FormsOfVerb.csv','rb') as csvfile2:
         spamreader2=csv.reader(csvfile2,delimiter=',')
         for row in spamreader2:
          if(verb==row[0]):
            verb=row[4]
            break 
    if(subject=='i' or subject=='we' or subject=='you' or subject=='it' or subject=='they'):
           flag8=1
           print subject,'had',no,'been',verb,object1,'.'
    elif(subject=='he' and g=='m'):
           flag8=1
           print subject,'had',no,'been',verb,object1,'.'
    elif(subject=='he' and g=='f'):
           flag8=1 
           subject='she'
           print subject,'had',no,'been',verb,object1,'.'
    try:
         if(flag8==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag8=1
              print subject,'had',no,'been',verb,object1,'.'
         
    except AttributeError:
          xyz=0
    if(flag8==0):
         print subject,'had',no,'been',verb,object1,'.'  
   
   elif(flag1==1 and flag2==0):
    #print 2
    with open('FormsOfVerb.csv','rb') as csvfile2:
         spamreader2=csv.reader(csvfile2,delimiter=',')
         for row in spamreader2:
          if(verb==row[0]):
            verb=row[4]
            break 
    
    if(subject=='we' or subject=='you' or subject=='they'):
         flag8=1
         print subject,'were',no,verb,object1,'.'
    elif(subject=='i' or subject=='it'):
         flag8=1
         print subject,'was',no,verb,object1,'.'
    elif(subject=='he' and g=='m'):
         flag8=1
         print subject,'was',no,verb,object1,'.'
    elif(subject=='he' and g=='f'):
         flag8=1
         subject='she'
         print subject,'was',no,verb,object1,'.' 
    try:
         if(flag8==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag8=1
              print subject,'were',no,verb,object1,'.'
         
    except AttributeError:
          xyz=0
    if(flag8==0):
         print subject,'was',no,verb,object1,'.'
    
   elif(flag7==1):
     #print 7
     with open('FormsOfVerb.csv','rb') as csvfile2:
         spamreader2=csv.reader(csvfile2,delimiter=',')
         for row in spamreader2:
          if(verb==row[0]):
            verb=row[2]
            break
     if(object1<>''):
        object1='by '+object1
     if(subject=='i' or subject=='we' or subject=='you' or subject=='it' or subject=='they'):
       flag8=1
       print subject,'had',no,'been',verb,object1,'.'
     elif(subject=='he' and g=='m'):
       flag8=1
       print subject,'had',no,'been',verb,object1,'.'
     elif(subject=='he' and g=='f'):
       flag8=1
       subject='she'
       print subject,'had',no,'been',verb,object1,'.'
     try:
         if(flag8==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag8=1
              print subject,'had',no,'been',verb,object1,'.'
         
     except AttributeError:
          xyz=0
     if(flag8==0):
         print subject,'had',no,'been',verb,object1,'.'  
   elif(flag3==1 and flag1==0):
    #print 3  
    with open('FormsOfVerb.csv','rb') as csvfile2:
         spamreader2=csv.reader(csvfile2,delimiter=',')
         for row in spamreader2:
          if(verb==row[0]):
            verb=row[2]
            break
    if(subject=='i' or subject=='we' or subject=='you' or subject=='it' or subject=='they'):
          flag8=1
          print subject,had,no,verb,object1,'.'
    elif(subject=='he' and g=='m'):
          flag8=1
          print subject,'had',no,verb,object1,'.' 
    elif(subject=='he' and flag6==0):
          flag8=1
          subject='she'
          print subject,'had',no,verb,object1,'.'
    try:
         if(flag8==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag8=1
              print subject,'had',no,verb,object1,'.'
         
    except AttributeError:
          xyz=0
    if(flag8==0):
         print subject,'had',no,verb,object1,'.'
    
 elif(type1==3):
   flag1=0
   flag2=0
   flag3=0 
   subject=''
   verb=''
   object1=''
   no=''
   flag5=0
   flag6=0
   try: 
      if(word1=='hua' or word1=='huaa' or word1=='hooa' or word1=='hooaa' or word1=='huee' or word1=='hui' or word1=='hooee' or word1=='hooi' or word1=='hue' or word1=='hooe'): 
         flag1=1 
         m1=re.search('ta$|ti$|te$',word2)
         if(m1.group(0)=='ta' or m1.group(0)=='ti' or m1.group(0)=='te'):
           if(m1.group(0)=='ta'):
             g='m'
           if(m1.group(0)=='ti'):
             g='f'
           del m[n-1]
           n=n-1   
   except AttributeError:
       xyz=0 
   try:
      if(flag1==0):
         m1=re.search('a$|i$|e$|ee$',word1)
         if(m1.group(0)=='a' or m1.group(0)=='i' or m1.group(0)=='e' or m1.group(0)=='ee'):
            flag2=1
            if(m1.group(0)=='a'):
                 g='m'
            if(m1.group(0)=='i' or m1.group(0)=='ee'):
                 g='f'  
   except AttributeError:
       xyz=0    
   for i in range(len(m)):
      with open('hindi_english_mix.csv','rb') as csvfile:
         spamreader=csv.reader(csvfile,delimiter=',')
         for row in spamreader:
           try: 
             m1=re.search(row[0],m[i])
             if(m1.group(0)<>''):
               #print row[1],row[0]
               m[i]=row[1]
               if(m[i]=='not'):
                no=m[i]
               break
           except AttributeError:
               xyz=0    
   for i in range(n):
        with open('PartOfSpeech.csv','rb') as csvfile1:
         spamreader1=csv.reader(csvfile1,delimiter=',')
         for row in spamreader1:
            if(m[i]==row[0] and (row[1]=='Noun' or row[1]=='Pronoun') and flag5==0):
               subject=m[i]
               flag5=1
               break   
            elif(m[i]==row[0] and (row[1]=='Noun' or row[1]=='Pronoun') and flag5==1):
               object1=m[i]
               break
            elif(m[i]==row[0] and row[1]=='Verb'):
               verb=m[i]
               break 
           
   if(flag==1):
     #print 1
     if(subject=='we' or subject=='you' or subject=='they' or subject=='it'):
        flag3=1
        print subject,'will',no,verb,object1,'.'
     elif(subject=='i'):
        flag3=1
        print subject,'shall',no,verb,object1,'.' 
     elif(subject=='he' and g=='m'):
        flag3=1
        print subject,'will',no,verb,object1,'.' 
     elif(subject=='he' and g=='f'):
        flag3=1 
        subject='she'
        print subject,'will',no,verb,object1,'.' 
     try:
         if(flag3==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag3=1
              print subject,'will',no,verb,object1,'.'
         
     except AttributeError:
          xyz=0
     if(flag3==0):
         print subject,'will',no,verb,object1,'.'
 
    
   elif(flag==3):
     #print 3
     with open('FormsOfVerb.csv','rb') as csvfile2:
             spamreader2=csv.reader(csvfile2,delimiter=',')
             for row in spamreader2:
               if(verb==row[0]):
                 verb=row[2]
                 break  

     if(subject=='we' or subject=='you' or subject=='they' or subject=='it'):
            flag3=1
            print subject,'will','have',no,verb,object1,'.'
     elif(subject=='i'):
            flag3=1
            print subject,'shall','have',no,verb,object1,'.'
     elif(subject=='he' and g=='m'):
            flag3=1
            print subject,'will','have',no,verb,object1,'.'
     elif(subject=='he' and g=='f'):
            flag3=1
            subject='she'
            print subject,'will','have',no,verb,object1,'.'  
     try:
         if(flag3==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag3=1
              print subject,'will','have',no,verb,object1,'.'
         
     except AttributeError:
          xyz=0
     if(flag3==0):
         print subject,'will','have',no,verb,object1,'.'
     
   elif(flag==5):
       #print 5
       with open('FormsOfVerb.csv','rb') as csvfile2:
             spamreader2=csv.reader(csvfile2,delimiter=',')
             for row in spamreader2:
               if(verb==row[0]):
                 verb=row[2]
                 break  
       if(object1<>''):
          object1='by ' +object1
       if(subject=='we' or subject=='they' or subject=='it' or subject=='you'):
          flag3=1
          print subject,'will',no,'be',verb,object1,'.'
       elif(subject=='i'):
          flag3=1
          print subject,'shall',no,'be',verb,object1,'.'
       elif(subject=='he' and g=='m'):
          flag3=1
          print subject,'will',no,'be',verb,object1,'.'
       elif(subject=='he' and g=='f'):
          flag3=1 
          subject='she'
          print subject,'will',no,'be',verb,object1,'.'
       try:
         if(flag3==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag3=1
              print subject,'will',no,'be',verb,object1,'.'
         
       except AttributeError:
          xyz=0
       if(flag3==0):
         print subject,'will',no,'be',verb,object1,'.'
      
   elif(word1=='chuka' or word1=='chuki' or word1=='chuke'):
      #print 6
      del m[n-1]
      n=n-1
      if(word2=='ja' or word2=='jaa'):
          if(word1=='chuka'):
              g='m'
          if(word1=='chuki'):
              g='f'
          del m[n-1]
          n=n-1  
          with open('FormsOfVerb.csv','rb') as csvfile2:
             spamreader2=csv.reader(csvfile2,delimiter=',')
             for row in spamreader2:
               if(verb==row[0]):
                 verb=row[2]
                 break 
          if(object1<>''):
             object1='by '+object1
          if(subject=='we' or subject=='you' or subject=='they' or subject=='it'):
             flag3=1
             print subject,'will have',no,'been',verb,object1,'.'
          elif(subject=='i'):
             flag3=1
             print subject,'will have',no,'been',verb,object1,'.'
          elif(subject=='he' and g=='m'):
             flag3=1
             print subject,'will have',no,'been',verb,object1,'.'
          elif(subject=='he' and g=='f'):
             flag3=1
             subject='she'
             print subject,'will have',no,'been',verb,object1,'.'
          try:
            if(flag3==0):
              m4=re.search('s$|es$',subject)
              if(m4.group(0)=='s' or m4.group(0)=='es'):
                flag3=1
                print subject,'will have',no,'been',verb,object1,'.'
         
          except AttributeError:
            xyz=0
          if(flag3==0):
             print subject,'will have',no,'been',verb,object1,'.'     
   elif(flag1==1):
        #print 4
        with open('FormsOfVerb.csv','rb') as csvfile2:
             spamreader2=csv.reader(csvfile2,delimiter=',')
             for row in spamreader2:
               if(verb==row[0]):
                 verb=row[4]
                 break 
        if(subject=='we' or subject=='you' or subject=='they' or subject=='it'):
           flag3=1
           print subject,'will have',no,'been',verb,object1,'.'
        elif(subject=='i'):
           flag3=1
           print subject,'shall have',no,'been',verb,object1,'.'
        elif(subject=='he' and g=='m'):
           flag3=1 
           print subject,'will have',no,'been',verb,object1,'.'
        elif(subject=='he' and g=='f'):
           flag3=1  
           subject='she'
           print subject,'will have',no,'been',verb,object1,'.' 
        try:
         if(flag3==0):
            m4=re.search('s$|es$',subject)
            if(m4.group(0)=='s' or m4.group(0)=='es'):
              flag3=1
              print subject,'will have',no,'been',verb,object1,'.'
         
        except AttributeError:
          xyz=0
        if(flag3==0):
           print subject,'will have',no,'been',verb,object1,'.'
   elif(flag2==1 and flag1==0):
           #print 2 
           with open('FormsOfVerb.csv','rb') as csvfile2:
             spamreader2=csv.reader(csvfile2,delimiter=',')
             for row in spamreader2:
               if(verb==row[0]):
                 verb=row[4]
                 break
           
           if(subject=='we' or subject=='you' or subject=='they' or subject=='it'):
                  flag3=1 
                  print subject,'will',no,'be',verb,object1,'.'
           elif(subject=='i'):
                  flag3=1
                  print subject,'shall',no,'be',verb,object1,'.'
           elif(subject=='he' and g=='m'):
                  flag3=1
                  print subject,'will',no,'be',verb,object1,'.'
           elif(subject=='he' and g=='f'):
                  flag3=1
                  subject='she'
                  print subject,'will',no,'be',verb,object1,'.'   
           try:
             if(flag3==0):
               m4=re.search('s$|es$',subject)
               if(m4.group(0)=='s' or m4.group(0)=='es'):
                 flag3=1
                 print subject,'will',no,verb,object1,'.'
           except AttributeError:
             xyz=0
           if(flag3==0):
              print subject,'will',no,verb,object1,'.'


 else:
  #print 4
  gs=goslate.Goslate()
  print(gs.translate(s,'en'))
  
