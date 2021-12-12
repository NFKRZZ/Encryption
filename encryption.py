from numpy import * 
 
def getInt(w):
    value = 0
    alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(len(alphabet)):
        if(w.lower() == alphabet[i].lower()):
            value = i
        else:
            None
    return value
def getChar(k):
    alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return alphabet[k]
 
encryption_matrix = [[1,1,1], [1,2,3],[2,5,9]] #encryption matrix
message = "Im Blue"
 
decryption_matrix = around(linalg.inv(encryption_matrix).astype(int)) #decryption matrix
 
 
stringlen = len(message);
s = ceil(stringlen/len(encryption_matrix))
#if(s%2!=0):
#    s=s+1
message_matrix = zeros((len(encryption_matrix),int(s)),dtype = int)
s = int(s)
 
for i in range(len(encryption_matrix)):
    for j in range(s):
        if((i*s)+j<len(message)):
            print("I: "+str(i)+" J: "+str(j)+" s: "+str(s))
            message_matrix[i][j] = getInt(message[(i*s)+j])
            print(message[(i*s)+j])
        else:
            message_matrix[i,j] = 0
print(message_matrix)
print(encryption_matrix)
new = dot(encryption_matrix,message_matrix)
 
for g in range(len(encryption_matrix)):
    for h in range(s):
        new[g][h] = new[g][h]%27
print(new)
finalstring = ""
string_matrix = zeros((len(encryption_matrix),int(s)),dtype = str)
for l in range(len(encryption_matrix)):
    for n in range(s):
        string_matrix[l][n] = getChar(new[l][n])
print(string_matrix)
emptyL = zeros((len(encryption_matrix),int(s)),dtype = str)
new = dot(decryption_matrix,new)
for ja in range(len(encryption_matrix)):
    for ew in range(s):
        new[ja][ew] = new[ja][ew]%27
for ll in range(len(encryption_matrix)):
    for wz in range(s):
        emptyL[ll][wz] = getChar(new[ll][wz])
        
        