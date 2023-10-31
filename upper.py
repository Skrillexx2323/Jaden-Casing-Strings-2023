









def to_jaden_case(string):
    words = string.split()    
    done_words = [i[0].upper() + i[1:].lower() for i in words]
    return ' '.join(done_words)






    