#!/usr/bin/env python3 

a = 0
print ("Initial Conditions:")
print ("1st sequence is ", a)

b= 1
print ("2nd sequence is ", b)

print_sequences = int(input ("Enter desired sequences (Sequences continue after 2nd): ")) + 1

current_seq = 2 

for i in range(print_sequences):
  current_seq = current_seq + 1
  c = a + b
  a = b
  b = c
  print ("Current Sequance ", current_seq, ": Number is ", c)

 
