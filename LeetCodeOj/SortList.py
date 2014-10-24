#coding:utf-8

def mergeSort(lst,f,e):
    if f<e:
        mid=(f+e)/2
        mergeSort(lst,f,mid)
        mergeSort(lst,mid+1,e)
        merge(lst,f,mid,e)

def merge(lst,f,mid,e):
    list1=lst[f:mid+1]
    list2=lst[mid+1:e+1]
    print "***********"
    for i in range(len(list1)+len(list2)):
        if list1 and list2:
            if list1[0]>list2[0]:
                n=list2.pop()
            else:
                n=list1.pop()
        elif list1:
            n=list1.pop()
        else:
            n=list2.pop()
        lst[i+f]=n
        print i,n

lst=[2,3,1,5,4]
mergeSort(lst,0,len(lst)-1)
print lst
