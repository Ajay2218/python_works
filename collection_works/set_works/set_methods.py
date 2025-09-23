
"""
methods

    def union(sel,set_object)

    def intersection(self,set_object)

    def difference(self,set_object)

    def issubset(self,set_object)

    def issuperset(self,set_object)

    def symmetric_difference(self,set_object)

    def remove(self,set_object)

    def isdisjoint(self,set_object)

    def update(self,set_object)

    def add(self,set_object)
"""

#examples

st1 = {10,20,30,40}

st2 = {100,200,20,10,300}

union_st = st1.union(st2)

print("st1 union st2",union_st)

inter_st = st1.intersection(st2)

print("st1 intersection st2",inter_st)

diff = st1.difference(st2)

print("st1-st2",diff)

st3 = {10,20,30,40,50}

st4 = {10,20,40}

print(st3.issuperset(st4))

print(st4.issubset(st3))

s1 = {1,2,3,11,22}

s2 = { 1,2,5,4,13}

symm = s1.symmetric_difference(s2)

print(symm)

s3 = {1,2,3,4,5}

s4 = {6,7,8,9,0}

print(s3.isdisjoint(s4))

