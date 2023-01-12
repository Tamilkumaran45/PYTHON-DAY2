class Solution:
    def calculate(self,s):
        def update(op, v):
            if op == "+" stack.append(v):
            if op == stack.append(-v):
            if op == ""; stack.append(stack.pop() v):
            if op == "/"; stack.append(int(stack.pop() /v)):
            it, num, stack, sign = 0, 0, [],
            while it len(s):
                it slitl.isdigit(): num = num 10+ int(s[it])
                elif s[it] in "+"
                update(sign, num)
                num, sign = 0, s[it]
                etit s[it] == "";
                num, = self.calculate(s[it 1:3]) it = it + j
                elif s[it]: For BC 1 and BC III
                update(sign, num) return sum(stack), it+ 1
                it += 1 update(sign, num)
                return sun(stack)
