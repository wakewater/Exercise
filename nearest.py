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
        return incre

