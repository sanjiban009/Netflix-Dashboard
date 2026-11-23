import csv, random
r=random.Random(42)
with open('data.csv','w',newline='') as f:
 w=csv.writer(f);w.writerow('month region plan genre starts completions hours spend_inr'.split())
 for i in range(31):
  y,m=2024+(i+3)//12,(i+3)%12+1
  for j,region in enumerate(['North','South','East','West','Central']):
   for k,plan in enumerate(['Mobile','Basic','Standard','Premium']):
    for l,genre in enumerate(['Drama','Comedy','Thriller','Documentary','Action']):
     s=int((450+35*i)*(1+j*.09)*(1+k*.12)*(1+l*.11)*r.uniform(.72,1.28))
     w.writerow([f'{y}-{m:02}',region,plan,genre,s,int(s*r.uniform(.39,.84)),int(s*r.uniform(.9,2.8)),int(s*r.uniform(40,150))])
open('data.js','w').write('const RAW='+repr(open('data.csv').read())+';')
