class DatabaseRecord:
    def __init__(self, record_id , data):
        self.record_id=record_id
        self.data=data

    def __str__(self):
        return f"Record(id={self.record_id}, data ={self.data})"
    def __repr__(self):
        return f"Record(id={self.record_id}, data ={self.data})" 
class ResultSetIterator:
    def __init__(self):

        
        index_counter=0
class DatabaseResultSet:
    pass
