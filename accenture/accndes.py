string = "Hello world"
output = ''
for i in range(len(string)-1,1,-1):
  output+=string[i]
# output+=string[i-1]
# output+=string[i-2]
print(output)