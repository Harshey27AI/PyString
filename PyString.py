#Harshey/10/19/2020


def duplicate_count(text):
    text=text.lower()
    
    text=list(text)
    duplicate=[]

    for items in text:
        if text.count(items)>1:
            if items not in duplicate:
                duplicate.append(items)
    return len(duplicate)                
     