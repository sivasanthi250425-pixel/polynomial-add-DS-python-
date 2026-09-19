class node:
    def __init__(self,c,e):
        self.c,self.e,self.next=c,e,None

class poly:
    def __init__(self):
        self.head=None

    def insert(self,c,e):
        n=node(c,e)
        if not self.head or e>self.head.e:
            n.next=self.head
            self.head=n
        else:
            p=self.head
            while p.next and p.next.e>e:
                p=p.next
            if p.next and p.next.e==e:
                p.next.c+=c
            else:
                n.next=p.next
                p.next=n

    def display(self):
        p=self.head
        while p:
            print(f"{p.c}x^{p.e}",end=" ")
            p=p.next
        print()

    def evaluate(self,x):
        p,s=self.head,0
        while p:
            s+=p.c*x**p.e
            p=p.next
        return s

def add(p1,p2):
    r=poly()
    a,b=p1.head,p2.head
    while a and b:
        if a.e==b.e:
            r.insert(a.c+b.c,a.e)
            a,b=a.next,b.next
        elif a.e>b.e:
            r.insert(a.c,a.e)
            a=a.next
        else:
            r.insert(b.c,b.e)
            b=b.next
    while a:
        r.insert(a.c,a.e)
        a=a.next
    while b:
        r.insert(b.c,b.e)
        b=b.next
    return r

p1,p2=poly(),poly()

n=int(input("terms in p1: "))
for _ in range(n):
    c,e=map(int,input().split())
    p1.insert(c,e)

n=int(input("terms in p2: "))
for _ in range(n):
    c,e=map(int,input().split())
    p2.insert(c,e)

r=add(p1,p2)

print("p1:",end=" ")
p1.display()
print("p2:",end=" ")
p2.display()
print("sum:",end=" ")
r.display()


