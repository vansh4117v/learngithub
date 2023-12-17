def create():
    task=input("Enter task name : ")
    f=open("pydev.txt","a")
    f.write(task+'\n')
    f.close()
    print("\nTask Created")
def edit():
    f = open("pydev.txt", "r")
    r = f.readlines()
    for ind, value in enumerate(r):
        print(ind, ':', value,end='')
    print()
    f.close()
    n=int(input("Which Task : "))
    while n not in range(0,len(r)):
        print("Enter valid input")
        n=int(input("Which Task : "))
    print("Editing task :",r[n])
    r[n]=input("New name : ")+'\n'
    print("Done Editing")
    f=open("pydev.txt",'w')
    f.writelines(r)
    f.close()

def delete():
    f = open("pydev.txt", "r")
    r = f.readlines()
    for ind, value in enumerate(r):
        print(ind, ':', value,end='')
    print()
    f.close()
    n=int(input("Which task: "))
    while n not in range(0, len(r)):
        print("Enter valid input")
        n = int(input("Which Task : "))
    del r[n]
    print("Deleted")
    f = open("pydev.txt", 'w')
    f.writelines(r)
    f.close()

def listt():
    f=open("pydev.txt","r")
    r=f.readlines()
    for ind,value in enumerate(r):
        print(ind,':',value,end='')
    f.close()

def main():
    try:
        f=open('pydev.txt','r')
        f.close()
    except:
        f=open('pydev.txt','w')
        f.close()
    while True:
        print("\nWhat do you want to do")
        n=int(input("1.Create\n2.Edit\n3.List\n4.Delete\n5.Exit\n"))
        while n not in range(1,6):
            print("Enter valid input")
            print("\nWhat do you want to do")
            n = int(input("1.Create\n2.Edit\n3.List\n4.Delete\n5.Exit\n"))
        if n==1:
            create()
        elif n==2:
            edit()
        elif n==3:
            listt()
        elif n==4:
            delete()
        elif n==5:
            print("Thank You for using :)")
            break
    quit()
main()
# Made By - vanshgupta4117v