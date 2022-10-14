

def merge_recursive(array, byfunc, start, end):

  if(start< end):
    
    mid = (start + end) //2
    merge_recursive(array, byfunc, start, mid)
    merge_recursive(array, byfunc, mid+1, end)
    merge(array, byfunc, start, mid, end)


def mergesort(array, byfunc=None):
  n = len(array)

  merge_recursive(array, byfunc, 0, n-1)

  pass

def merge(array, byfunc, start, mid, end):
  left_array = array[start:mid+1]
  right_array = array[mid+1:end+1]
  left = 0
  right = 0

  while(left< len(left_array) and right<len(right_array)):

    if(byfunc(left_array[left]) <= byfunc(right_array[right])):

      array[start] = left_array[left]
      left += 1

    else:

      array[start] = right_array[right]
      right += 1

    start += 1

  while(left< len(left_array)):
    array[start] = left_array[left]
    left += 1 
    start += 1

  while(right < len(right_array)):
    array[start] = right_array[right]
    right += 1
    start += 1




class Stack:
  def __init__(self):
    self.__items = []
        
  def push(self, item):
    self.__items.append(item)

  def pop(self):
    if self.__items == []:
      return None
    else:
      pop_val = self.__items[-1]
      self.__items = self.__items[:len(self.__items)-1]
      #print (pop_val, self.__items)
      return pop_val 

  def peek(self):
    if self.__items == []:
      return None
    else:
      pop_val = self.__items[-1]
      return pop_val 

  @property
  def is_empty(self):
    if self.__items == []:
      return True
    else:
      return False

  @property
  def size(self):
    return len(self.__items)

  

class EvaluateExpression:
    # from the previous parts
  valid_char = '0123456789+-*/() '
  operator_str ='+-*/()'
  operand_str= '+-*/'
  num_str = '0123456789'

  def __init__(self, string=""): #private 
        valid_char = '0123456789+-*/() '
        self.string= string
        self.validstrchar= valid_char
        self.ls= list(string)
        self.valid= list(valid_char)
        self.stack = Stack()
        print (self.ls)
    

  @property # way to access data publicly
  def expression(self):
        if self.string== "":
            #print("exit if")
            return ""
        else:
            for i in self.ls:
                if i in self.validstrchar:
                    pass
                else: 
                    #print("exit else")
                    return ""
            #print (self.string)
            return self.string
                

  @expression.setter #public 
  def expression(self, new_expr):
        if isinstance(new_expr,str) and new_expr != "":
            # checks if its a string: isinstance(new_expr,str)
            self.ls = list(new_expr)
            self.string = new_expr


  def insert_space(self):

      return_str = ""
      
      for i in self.string:
        if i in self.operator_str:
          return_str += " " + i + " "
        else:
          return_str += i

      return return_str

  def process_operator(self, operand_stack, operator_stack):
    result = 0
    right_no = float(operand_stack.pop())
    left_no = float(operand_stack.pop())
    operator = operator_stack.pop()
    #print ("process operator",right_no, left_no, operator)

    if operator == "+":
        result = left_no + right_no
    elif operator == "-":
        result = left_no - right_no
    elif operator == "*":
        result = left_no * right_no
    elif operator == "/":
        result = left_no//right_no
                
    operand_stack.push(result)
    #print(result)
    result = int(operand_stack.peek())
    return result 

  def is_float(self,n):
    try:
        float(n)
        return True
    except ValueError:
        return False
    
  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    result = 0
    tokens = expression.split()
    for i in range(len(tokens)): #For numbers that is more than 1 digit to be treated as one number
        if (tokens[i] in self.num_str):
            j = i +1
            #print(j)
            lst =[]
            while (j < len(tokens)) and tokens[j] in self.num_str:
                tokens[i] = tokens[i]+tokens[j]
                #print(tokens[i])
                lst.append(j)
                j += 1
            for n in lst:
                tokens.pop(n)
            #print (len(tokens))
    #print (tokens)
   
    
    for n in tokens: 
        #print(n, type(n))
        if self.is_float(n):
            operand_stack.push(n)
            #print (" if, push\n")
        elif n == '(':
            operator_stack.push(n)
            #print ("1st elif, push\n")
        
        #For priority operators to evaluate first (* and /)
        elif n in self.operand_str:
            #print("In stack" , operator_stack.peek())
            while (operator_stack.peek() == '*' or operator_stack.peek() == '/'): 
                result = self.process_operator(operand_stack, operator_stack)
                #print ("2nd elif,shifted")
            if (n == "+" or n=="-") and operand_stack.size >1:
                self.process_operator(operand_stack, operator_stack)
            operator_stack.push(n)
           
            #print("2nd elif, push\n")
        
        elif n == ')':
            while n!='(':
                result = self.process_operator(operand_stack, operator_stack)
                #print ("3rd elif", result, "\n")
                n = operator_stack.peek()
            operator_stack.pop()

 
    while not operator_stack.is_empty:
        self.process_operator(operand_stack, operator_stack)
        #print ("last while", bool(not operator_stack.is_empty))
    
    result = operand_stack.peek()
    #print ("final", result,"\n")
    return int(result)


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





