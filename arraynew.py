import array 
arr = array.array('i',[1, 3, 5])
print('the created array is:',end=' ')
for i in range(0,3):
    print(arr[i],end=' ')
print('\r')
arr.append(4);
print('the appended array is :'end=' ')
for i in range(0,4):
    print(arr[i],end=' ')
arr.insert(2,5)
print('\r')
print('the array after insertion is:',end=' ')
for i in range( 0,5):
    print(arr[i],end=' ')