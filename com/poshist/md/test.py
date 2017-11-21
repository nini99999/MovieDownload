'my test'
__author__='poshist'
from  com.poshist.frist.db import DB
import time
import sched



def main():

    db=DB()
    db.open()
    values=db.query('select * from user')
    print(values)
    db.close()
    s=sched.scheduler(time.time ,time.sleep)
    print (time.time())
    s.enter(3,1,main)
    s.run()


main()