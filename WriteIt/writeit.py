
# coding: utf-8

# In[1]:

#demonstrate writing in text file
print("Creatin txt file by write() method.")
text_file=open("write_it.txt","w",encoding='utf-8')
text_file.write("String1\n")
text_file.write("String2\n")
text_file.write("String3\n")
text_file.close()


# In[2]:

print("\nReading this file")
text_file=open("write_it.txt","r",encoding='utf-8')
print(text_file.read())
text_file.close()


# In[4]:

print("\nCreatin txt file by writelines() method")
text_file=open("write_it.txt","w", encoding='utf-8')
lines=["String1\n",
      "String2\n",
      "String3\n"]
text_file.writelines(lines)
text_file.close()
print("Reading txt file")
text_file=open("write_it.txt","r",encoding='utf-8')
print(text_file.read())
text_file.close()
input("\n\nPress enter to exit")


# In[ ]:



