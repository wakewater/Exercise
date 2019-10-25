import numpy as np

import pandas as pd

class sever_tasknode:
    def __init__(self,time,priority,pt_edge,pnext=None):
        self.time = time
        self.priority = priority
        self.pt_edge = pt_edge
        self.waittime = 0
        self.next = pnext

class sever_tasklist:
    def __init__(self):
        self.head = sever_tasknode(0,0,0)

    def printhead(self):
        print(self.head.priority)

    def is_empty(self):
        return self is None

    def append(self,data,priority,pt_edge):
        node = sever_tasknode(data,priority,pt_edge)
        if self.head is None:
            self.head = node

        else:
            head = self.head
            while head.priority > node.priority:
                node.waittime = node.waittime + head.pt_edge
                if head.next is not None:
                    head = head.next
                else:
                    break
            if head == self.head:
                node.next = self.head
                self.head = node
            else:
                node.next = head.next
                head.next = node
            wt = node.pt_edge
            while node.next is not None:
                 node.next.waittime = node.next.waittime + wt
                 node= node.next

    def sum(self):
        sum = 0
        iden = self.head
        while iden is not None:
            sum=sum+iden.priority*(iden.pt_edge+iden.waittime)
            iden=iden=iden.next
        return sum

    def increase(self,data,priority,pt_edge,transtime):
        id = self.head
        incre = 0
        while id.priority > priority:
            incre = incre + priority * id.pt_edge
            if id.next is not None:
                id = id.next
            else:
                break

        incre = incre + priority * pt_edge
        while id is not None:
            incre = incre + pt_edge * id.priority
            id = id.next
        incre = incre/1000 + transtime
        return incre













lec = pd.read_csv('d:/Job_dispatch/sample.csv')
tran_speed = pd.read_csv('d:/Job_dispatch/10sever_speed.csv')
process_ener  = pd.read_csv('d:/Job_dispatch/process_ener.csv')
s0 = sever_tasklist()
s1 = sever_tasklist()
s2 = sever_tasklist()
s3 = sever_tasklist()
s4 = sever_tasklist()
s5 = sever_tasklist()
s6 = sever_tasklist()
s7 = sever_tasklist()
s8 = sever_tasklist()
s9 = sever_tasklist()
sever_list = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9]

sum = 0
for i in range(5000):
    incre_time_edge = 0
    incre_local = process_ener.loc[i,'pt_local',] + process_ener.loc[i,'ener_local']
    mini_incre = 10000000
    choice = None

    for j,p in enumerate(sever_list):
        incre_sum = 0
        incre_time_edge = p.increase(i,lec.loc[i,'priority'],
                                process_ener.loc[i,'pt_edge'],tran_speed.iloc[i,j])

        incre_sum  = incre_time_edge + process_ener.loc[i,'ener_tran']
        if incre_sum < mini_incre:
            choice = p
            mini_incre = incre_sum
    if mini_incre < incre_local:
        choice.append(i,lec.loc[i,'priority'],
                                process_ener.loc[i,'pt_edge',])
    else:

        sum = sum + incre_local
print(sum)
for j,p in enumerate(sever_list):
    print(p.sum())
for j,p in enumerate(sever_list):

        sum = sum + p.sum()

print(sum)