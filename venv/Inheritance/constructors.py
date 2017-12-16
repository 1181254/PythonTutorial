class A:
    def __init__(self):
        print "A Constructor"

class B(A):
    def __init__(self):
        print "B Constructor"

class C(B):
    def __init__(self):
        print "C Constructor"

c = C()