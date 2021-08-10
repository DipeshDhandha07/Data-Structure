# The main function that converts given infix expression
# to postfix expression
def infixToPostfix(self, exp):

    # Iterate over the expression for conversion
    for i in exp:
        # If the character is an operand,
        # add it to output
        if self.isOperand(i):
            self.output.append(i)

        # If the character is an '(', push it to stack
        elif i  == '(':
            self.push(i)

        # If the scanned character is an ')', pop and
        # output from the stack until and '(' is found
        elif i == ')':
            while( (not self.isEmpty()) and self.peek() != '('):
                a = self.pop()
                self.output.append(a)
            if (not self.isEmpty() and self.peek() != '('):
                return -1
            else:
                self.pop()

        # An operator is encountered
        else:
            while(not self.isEmpty() and self.notGreater(i)):
                self.output.append(self.pop())
            self.push(i)

    # pop all the operator from the stack
    while not self.isEmpty():
        self.output.append(self.pop())

    print "".join(self.output)

# Driver program to test above function
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)
