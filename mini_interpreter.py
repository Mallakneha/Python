def precedence(op):
    if op=='+' or op=='-':
        return 1
    elif op=="*" or op=='/':
        return 2
    else:
        return 0
def operations(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
def evaluate(exp):
    values=[]
    ops=[]
    i=0
    while i<len(exp):
        ch=exp[i]
        if ch==' ':
            i+=1
            continue
        if ch.isdigit():
            val=0
            while i<len(exp) and exp[i].isdigit():
                val=(val*10)+int(exp[i])
                i+=1
            values.append(val)
            continue
        elif ch=='(':
            ops.append(ch)
            i+=1
        elif ch==')':
            while ops and ops[-1]!='(':
                a=values.pop()
                b=values.pop()
                op=ops.pop()
                result=operations(b,a,op)
                values.append(result)
            ops.pop()
            i+=1
        elif ch in '+-*/':
            while ops and precedence(ops[-1])>=precedence(ch):
                a=values.pop()
                b=values.pop()
                op=ops.pop()
                result=operations(b,a,op)
                values.append(result)
            ops.append(ch)
            i+=1
    while ops:
        a=values.pop()
        b=values.pop()
        op=ops.pop()
        result=operations(b,a,op)
        values.append(result)
    return values[-1]
print(evaluate("5 + 2*(3-1)"))

