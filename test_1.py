s = {"a":"bb","b":"cc","c":"aa"}
def fun(s):
    d = sorted(s.iteritems(),key=lambda t:t[1],reverse=False)
    return d
     
d = fun(s)
print(d)
