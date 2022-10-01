

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
  pass

class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





