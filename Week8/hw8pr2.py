def string_times(str, n):
  return n * str

def front_times(str, n):
  if (len(str) < 3):
    temp = str[:len(str)]
    return n * temp
  else:
    temp = str[:3]
    return n * temp
  
def string_bits(str):
  return str[0:len(str):2]

def string_splosion(str):
  num = len(str)
  s = ""
  for i in range(num):
    s += str[:i + 1]
  return s

def last2(str):
  last2 = str[len(str) - 2:]
  count = 0
  for i in range (len(str) - 2):
    if (str[i:i+2] == last2):
      count += 1
  return count


def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count += 1
  return count

def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):
    if nums[i] == 9:
      return True
  return False

def array123(nums):
  if len(nums) < 3:
    return False
  for i in range(len(nums) - 2):
    if nums[i:i+3] == [1,2,3]:
      return True
   
  return False


def string_match(a, b):
  count = 0
  for i in range(len(a) - 1):
    if a[i:i+2] == b[i: i+2]:
      count += 1
  return count

def double_char(str):
  new_str = ""
  for i in range(len(str)):
    new_str += str[i] * 2
  return new_str


def count_hi(str):
  counter = 0
  for i in range(len(str) - 1):
    if str[i:i+2] == "hi":
      counter +=1
  return counter
