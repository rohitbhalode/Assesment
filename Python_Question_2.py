def printFrequency(strr):
	M = {}
	
	word = ""
	
	for i in range(len(strr)):
		if (strr[i] == ' '):
			
			
			if (word not in M):
				M[word] = 1
				word = ""
			
			else:
				M[word] += 1
				word = ""
		
		else:
			word += strr[i]
	
	if (word not in M):
		M[word] = 1
	
	else:
		M[word] += 1
		
    
	return M 

		
	
	for it in M:
		print(it, "-", M[it])
def sort_dict_by_value_and_key_length_both_descending(my_dict):

  sorted_items = sorted(
      my_dict.items(),
      key=lambda item: (item[1], len(item[0])),
      reverse=True,
  )
  return sorted_items

##Test case  1 
strr = "writer writer writer all the number fromere fromere fromere 1 to 100"
M=printFrequency(strr)
sorted_dic=sort_dict_by_value_and_key_length_both_descending(M)
print("Test case 1 answer:" ,len(sorted_dic[0][0]))

## Test case 2

strr="My name is shing shing john and play with play player and dont play"
M=printFrequency(strr)
sorted_dic=sort_dict_by_value_and_key_length_both_descending(M)
print("Test case 2 answer:" ,len(sorted_dic[0][0]))

## Test case 3
 
strr="cricket is best sports in world and cricket is favorite to all cricket ground are available all over the world"
M=printFrequency(strr)
sorted_dic=sort_dict_by_value_and_key_length_both_descending(M)
print("Test case 2 answer:" ,len(sorted_dic[0][0]))




