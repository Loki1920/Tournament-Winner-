#  tournament winner program 
def winner(competetions,results):
  score = {}
  for i in range(len(competetions)):
    if results[i]==0:
      if competetions[i][1] not in score:
        score[competetions[i][1]] = 3
      else:
        score[competetions[i][1]] += 3
    elif results[i]==1:
      if competetions[i][0] not in score:
        score[competetions[i][0]] = 3
      else:
        score[competetions[i][0]] += 3

        
  maxpoint = max(score.values())
  for x,y in score.items():
    if int(y)==maxpoint:
      return x
      
  
       
competetions = [['HTML','C#'],['C#','PYTHON'],['PYTHON','HTML']]
results = [0,0,1]
print("winner is :",winner(competetions,results))