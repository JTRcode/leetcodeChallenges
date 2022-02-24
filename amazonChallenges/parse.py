f = open("questions.txt", "r")
output = open("formatedquestions.txt", "w")

# print(f.readline())

body = f.readline()
starting = 0
end = body.find(': ', starting)
print(end)
while (end != -1):
    output.write(body[starting:end]+"\n")
    starting = end + 1 
    end = body.find(': ', starting)
    print(end)
f.close()
output.close()