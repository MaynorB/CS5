#Problem 1

def sleep_in(weekday, vacation):
  if weekday == True and vacation == False:
    return False
  elif vacation == True:
    return True
  else:
    return True

#Problem 2

def monkey_trouble(a_smile, b_smile):
  if(a_smile == True and b_smile == True):
    return True
  elif(a_smile == False and b_smile == False):
    return True
  else: 
    return False
  
#Problem 3

def sum_double(a, b):
  if(a == b):
    return 2 * (a+b)
  else:
    return a + b
  
# Problem 4

def diff21(n):
  if(n > 21):
    return (n - 21) * 2
  else:
    return 21 - n

# Problem 5

def parrot_trouble(talking, hour):
  if(hour < 7 and talking == True):
    return True
  if(hour > 20 and talking == True):
    return True
  else:
    return False

# Problem 6

def makes10(a, b):
  if(a == 10 or b ==10):
    return True
  elif(a + b == 10):
    return True
  else:
    return False

# Problem 7

def near_hundred(n):
  if (abs(100 - n) <= 10 or abs(200 - n) <= 10):
    return True
  else:
    return False

# Problem 8

def pos_neg(a, b, negative):
  if(negative):
    if(a < 0 and b < 0):
      return True
    else:
      return False
  else:
    if(a < 0 and b < 0):
      return False
    elif(a < 0 or b < 0):
      return True
    else:
      return False

# Problem 9

def not_string(str):
  if(str[0:3] != "not"):
    return "not " + str
  else:
    return str

# Problem 10

def missing_char(str, n):
  return str[:n] + str[n + 1:]

# Problem 11

def front_back(str):
  if (len(str) == 1):
    return str
  else:
    temp = str[0:1]
    temp2 = str[len(str)-1 :]
    temp3 = str[1:len(str)-1]
    return temp2 + temp3 + temp

# Problem 12

def front3(str):
  if (len(str) < 3):
    temp = str[:len(str)]
    return 3 * temp
  else:
    temp = str[:3]
    return 3 * temp


# Problem 13

def string_times(str, n):
  return n * str

# Problem 14

def front_times(str, n):
  if (len(str) < 3):
    temp = str[:len(str)]
    return n * temp
  else:
    temp = str[:3]
    return n * temp
  
# Problem 15
  
  def string_bits(str):
    return str[0:len(str):2]

# Problem 16

def string_splosion(str):
  num = len(str)
  s = ""
  for i in range(num):
    s += str[:i + 1]
  return s

# Problem 17

def last2(str):
  last2 = str[len(str) - 2:]
  count = 0
  for i in range (len(str) - 2):
    if (str[i:i+2] == last2):
      count += 1
  return count

# Problem 18

def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count += 1
  return count

# Problem 19

def array_front9(nums):
  last = len(nums)
  if last > 4:
    last = 4
  
  for i in range(last):
    if nums[i] == 9:
      return True
  return False

# Problem 20

def array123(nums):
  if len(nums) < 3:
    return False
  for i in range(len(nums) - 2):
    if nums[i:i+3] == [1,2,3]:
      return True
   
  return False

# Problem 21

def string_match(a, b):
  count = 0
  for i in range(len(a) - 1):
    if a[i:i+2] == b[i: i+2]:
      count += 1
  return count

# Problem 22

def hello_name(name):
  return "Hello " + name + "!"

# Problem 23

def make_abba(a, b):
  return a + 2 * b + a

# Problem 24

def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

# Problem 25

def make_out_word(out, word):
  half = len(out) / 2
  return out[:half] + word + out[half:]

# Problem 26

def extra_end(str):
  str = str[len(str) - 2:]
  return 3 * str

# Problem 27

def first_two(str):
  if len(str) < 2:
    return str[0:1]
  else:
    return str[0:2]
  
# Problem 28

def first_half(str):
    half = len(str) / 2    
    return str[:half]
