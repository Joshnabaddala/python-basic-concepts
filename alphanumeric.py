str=input('Enter a String in the format(A8HyH88)')
alphabets=[]
numeric=[]
for ch in str:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        numeric.append(ch)
final_list=sorted(alphabets)+sorted(numeric)
output=''.join(final_list)
print(output)