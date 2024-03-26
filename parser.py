import psycopg2 as ps

def unique(li):
    lis = []
    for i in li:
        if i not in lis:
            lis.append(i)
    return lis

conn = None

try:

    conn = ps.connect(
        host="localhost",
        database="researchDB",
        user="postgres",
        password="@0postgresql0@")

    cur = conn.cursor()

    references_dictionary = {}
    title_pro = []
    title = "weee"
    authors = []
    year = -2
    venue = "xx"
    index = -50
    references = []
    abstract = "wwee"
    doop = []
    allauthors = {}
    venues=[]
    """
    source file: https://drive.google.com/file/d/1wKx3z2nblF9kBtJO7LfY6wsI-MWpLYVa/view?usp=sharing
    """
    with open("source.txt", encoding="utf8") as lines: 

        for str in lines:
    
            if str[0:2] == "#*":

                if title_pro:
                    #to be done       
                    if authors:
                        for auth in authors:
                            
                            try:
                                allauthors[auth]
                            except KeyError:    
                                sql = """INSERT INTO author_ VALUES(%s)"""
                                cur.execute(sql, [auth])    
                                allauthors[auth] = 1
                                
                            
                    
                    if venue not in venues and venue != None:
                        sql = """INSERT INTO publication_venue VALUES(%s)"""
                        cur.execute(sql, [venue])
                        venues.append(venue)
                    sql = """ INSERT INTO RESEARCH_PAPER_ VALUES(%s, %s, %s, %s, %s) """
                    cur.execute(sql, [title, year, abstract, index, venue])
                    for auth in authors:
                        sql = """INSERT INTO authorship VALUES(%s, %s, %s)"""
                        cur.execute(sql, [authors.index(auth), index, auth])
                    
                    print(index)        
                    title_pro = "weee"
                    title = "weee"
                    authors = []
                    year = -2
                    venue = ""
                    index = -50
                    references = []
                    abstract = []
                    doop = []
                title_pro = str[2:] 
                title = str[2:]
                  
            if str[0:2] == "#@":
                if str[2:] == "\n":
                    authors = []
                else:
                    authors = str[2:].split(',')

                    alp = len(authors)
                    authors[alp - 1] = authors[alp - 1][0:len(authors[alp - 1])-1]
                    i = 0
                    while(i < alp):
                        
                        if len(authors[i]) <= 4:
                             

                            authors[i - 1] = authors[i - 1] + authors[i]
                            authors.remove(authors[i])
                            alp = alp - 1
                            i = i - 1
                            #list1= authors[0:i]
                            #list2 =authors[i+1:]
                            #print(list1)
                            #print(list2)                            
                            #authors = list1 + list2 
                            break
                        i = i + 1    
                    authors = unique(authors)
                    
            if str[0:2] == "#t":
                if str[2:] == "\n":
                    year = None
                else:
                    year = int(str[2:])
                    
                    
            if str[0:2] == "#c":
                if str[2:] == "\n":
                    #for j in range(len(title_pro)):
                     #   if title_pro[j:j+2].isnumeric() and title_pro[j + 3:j + 5].isnumeric() and title_pro[j + 2] == "-": 
                      #      for l in range(3):
                       #         while title_pro[j] != ",":
                        #            j = j - 1
                         #       k = j
                          #      j = j - 1
                           #     while title_pro[j] != ",":
                            #        j = j - 1
                             #   doop.append(title_pro[j + 1:k+1])
                            #venue = doop[2] + doop[1] + doop[0]
                            #title = title_pro[1:j]
                            #break
                        #else:
                    venue = None
                else:
                    venue = str[2:]
            
            if str[0:2] == "#i":
                index = int(str[6:])
                
            if str[0:2] == "#%":
                references.append(int(str[2:]))
                references_dictionary[index] = references
            if str[0:2] == "#!":
                abstract = str[2:]

        for str2 in references_dictionary:
            for str3 in references_dictionary[str2]:
                sql = """INSERT INTO references_ VALUES(%s, %s)"""
                cur.execute(sql, [str2, str3])
        
    cur.close()
    conn.commit()

        
except (Exception, ps.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()


