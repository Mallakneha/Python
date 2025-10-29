def word_count(sent,n):
   new_sen=""
   for ch in sent:
      if ch.isalpha() or ch==" ":
         new_sen+=ch.lower()
   word=""
   words=[]
   for ch in new_sen:
      if ch !=" ":
         word+=ch
      else:
         if word !=" ":
            words.append(word)
            word=""
   if word !=" ":
       words.append(word)
   d={}
   for w in words:
      if w in d:
         d[w]+=1
      else:
         d[w]=1
   items=[]
   for key in d:
      items.append((key,d[key]))
   for i in range(len(items)):
      for j in range(len(items)-i-1):
         if(items[j][1]<items[j+1][1]):
            temp=items[j]
            items[j]=items[j+1]
            items[j+1]=temp
   top_n=[]
   count=0
   for i in items:
      if count<n:
         top_n.append(i)
         count+=1
      else:
         break
   return top_n
n=3
sent= "Hello world! Hello, Python world. Python is great, and Python is fun!"


print(word_count(sent,n))
      

         
      


      
         
      
      
    
      
