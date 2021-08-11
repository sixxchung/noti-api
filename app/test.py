from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
#데이터 베이스에 접속한다.
DATABASES = create_engine('mysql+mysqldb://<user>:<password>@<localhost>:<port>:<databaseName>', echo = True)
 
# orm과의 매핑을 명시하는 함수를 선언한다.
Base = declarative_base()
 
class Tada(Base):
    __tablename__ = 'tada'
    id       = Column(Integer, primary_key=True)
    name     = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))
     
    def __init__(self, name, fullname, password):
    
        self.name     = name
        self.fullname = fullname
        self.password = password
    
    def __repr__(self):
        return "<Tada('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

if __name__ == '__main__':
    
    #  Database를 없으면 생성 또는 사용의 의미 django에서  create_or_update() (table) 같은것
    Base.metadata.create_all(DATABASES)
    
    # 세션을 만들어서 연결시킨다.
    Session = sessionmaker()
    Session.configure(bind=DATABASES)
    session = Session()
    
    # 위의 클래스,인스턴스 변수를 지킨 다음에
    tada = Tada('ks','ks','1111')
    
    # 세션에 추가를 한다.
    session.add(tada)
    session.commit()