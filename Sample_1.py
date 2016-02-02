import string

def ispangram(s, alphabet=string.ascii_lowercase):  
    l=set(alphabet)
    s = s.replace(' ','')
    s=s.lower()
    s=set(s)
    return(l==s)
        
    