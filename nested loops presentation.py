# nested loops
# l1=['sandeep','sanket','pankaj','krushna']
# for i in l1:
#     for j in i:
#      print(f"name:{j}")

D={'emp1':{'name':'bob','job':'mgr','sal':23000},
   'emp2':{'name':'kim','job':'dev','sal':28000},
   'emp3':{'name':'sam','job':'dev','sal':24000}}
#l=[]
max=0
empty_dict={}
for i,j in D.items():
   for p,q in j.items():
      if p=="sal":
         if max<q:
            max=q
            empty_dict.update(j)
            empty_dict.update({p:q})
#l.append(empty_dict)
print(empty_dict)













