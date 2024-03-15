import psycopg2 as ps

commands = (
     """CREATE TABLE author_
(
  Author_name VARCHAR(200) NOT NULL,
  PRIMARY KEY (Author_name)
)""",

"""CREATE TABLE publication_venue
(
  venue_name VARCHAR(500) NOT NULL,
  PRIMARY KEY (venue_name)
)""",

"""CREATE TABLE RESEARCH_PAPER_
(
  paper_title_ VARCHAR(5000) NOT NULL,
  year INT NOT NULL,
  an_abstract_ VARCHAR(100000),
  index INT NOT NULL,
  venue_name VARCHAR(500),
  PRIMARY KEY (index),
  FOREIGN KEY (venue_name) REFERENCES publication_venue(venue_name)
)""",

"""CREATE TABLE authorship
(
  position_of_importance INT NOT NULL,
  index INT NOT NULL,
  Author_name VARCHAR(200),
  PRIMARY KEY (index, Author_name),
  FOREIGN KEY (index) REFERENCES RESEARCH_PAPER_(index),
  FOREIGN KEY (Author_name) REFERENCES author_(Author_name)
)""",

"""CREATE TABLE references_
(
  index_1 INT NOT NULL,
  references_index_2 INT NOT NULL,
  PRIMARY KEY (index_1, references_index_2),
  FOREIGN KEY (index_1) REFERENCES RESEARCH_PAPER_(index),
  FOREIGN KEY (references_index_2) REFERENCES RESEARCH_PAPER_(index)
)"""
)

conn = None

try:

    conn = ps.connect(
        host="localhost",
        database="researchDB",
        user="postgres",
        password="@0postgresql0@")

    cur = conn.cursor()

    for command in commands:
        cur.execute(command)
        # close communication with the PostgreSQL database server
    

    
    cur.close()
    conn.commit()

    
except (Exception, ps.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()