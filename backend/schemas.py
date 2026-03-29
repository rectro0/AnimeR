from pydantic import BaseModel


class request(BaseModel) :
    name : str
    email : str
    password : str

class response(BaseModel) :
    id : int
    name : str
    email : str
