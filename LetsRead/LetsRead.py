
# coding: utf-8

# In[7]:


#demonstrate reading files
print("Open and close file")
text_file=open("read_it.txt","r",encoding='utf-8')
text_file.close()
print("\nReading file symbol by symbol")
text_file=open("read_it.txt","r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()
print("\nRead file entirely")
text_file=open("read_it.txt","r",encoding='utf-8')
whole_thing=text_file.read()
print(whole_thing)
text_file.close()
print("\nRead one stroke symbol by symbol")
text_file=open("read_it.txt","r",encoding='utf-8')
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()
print("\nRead one stroke entirely")
text_file=open("read_it.txt","r",encoding='utf-8')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()
print("\nREad file into list")
text_file=open("read_it.txt","r",encoding='utf-8')
lines=text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()
print("\nTaking file symbol by symbol")
text_file=open("read_it.txt","r",encoding='utf-8')
for line in text_file:
    print(line)
text_file.close()

input("\n\npress enter to exit")

