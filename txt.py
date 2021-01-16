'''
f = open("Jirko.txt", "r")
print(f.read())
'''

text = "Python is easy to learn."

result = text.endswith('to learn')
# returns False
print(result)

result = text.endswith('to learn.' or 'arn.')
# returns True
print(result)

result = text.endswith('Python is easy to learn.')
# returns True
print(result)