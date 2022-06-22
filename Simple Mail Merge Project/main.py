
replace_name = '[name]'

with open('./Input/Names/invited_names.txt','r') as name:
    names = name.readlines()
    
with open('./Input/Letters/starting_letter.txt','r') as letter:
    word = letter.read()
    for add in names:
        new_letter = word.replace(replace_name,add)
        with open('./Output/ReadyToSend/'+add.replace('\n','')+".txt",'w') as done_file:
            done_file.write(new_letter)

        
