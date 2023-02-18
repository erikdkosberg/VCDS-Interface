from sqlalchemy import create_engine, Column, Integer, Float, String, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DataRecords(Base):
    __tablename__ = 'DataRecords'
    RecordID = Column(Integer, primary_key=True)
    SessionID = Column(Integer)
    PartNumber = Column(String)
    Value = Column(Float)
    TimeStamp = Column(Float)

def start_engine():
    global session
    engine = create_engine('sqlite:///Database.db')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()


def add_record(sessionID, partno, value, dt):
    record = DataRecords(SessionID=sessionID, RecordID=most_recent_record(), PartNumber=partno, Value=value, TimeStamp=dt)
    session.add(record)
    session.commit()

def get_records():
    records = session.query(DataRecords).order_by(DataRecords.TimeStamp)
    for record in records:
        print(record.SessionID, record.RecordID, record.PartNumber, record.Value, record.TimeStamp)

def most_recent_record():
    max_record_id = session.query(func.max(DataRecords.RecordID)).scalar()
    if max_record_id == None:
        return 0
    else:
        return max_record_id + 1

def most_recent_session():
    max_session_id = session.query(func.max(DataRecords.SessionID)).scalar()
    if max_session_id == None:
        return 0
    else:
        return max_session_id + 1

def test_sensor():
    start_engine()

    # Query all records where the PartNumber column contains "Engine Speed"
    results = session.query(DataRecords).filter(DataRecords.PartNumber.like('%Engine Speed%')).all()

    # Iterate over the results and print the values
    for result in results:
        print(result.PartNumber, result.Value, result.TimeStamp)

    stop_engine()

def stop_engine():
    session.close()


# Delete all records from the DataRecords table
def delete_records():
    start_engine()
    session.query(DataRecords).delete()
    session.commit()
    stop_engine()

def test_engine():
    import random
    start_engine()
    add_record("Engine Speed", random.randint(1,100), str(random.randint(1,10)))
    get_records()
    stop_engine()

#test_engine()
#delete_records()
#test_sensor()

