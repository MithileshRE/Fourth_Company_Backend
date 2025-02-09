from pydantic import BaseModel,EmailStr,HttpUrl


class EmailContent(BaseModel):
    SENDER :EmailStr = "puneeth3sprime@gmail.com"
    RECIPIENT :EmailStr = "puneeth3sprime@gmail.com"
    SUBJECT: str
    BODY_TEXT: str
    BODY_HTML: str

class Base_asserts(BaseModel):
    id: int
    name: str
    desc: str
    image_url: HttpUrl

class Domains_url(BaseModel):
    class Config:
        json_encoders = {
            HttpUrl: str 
        }
    ID: int
    Service_name: str
    URL: HttpUrl
    logoImage: HttpUrl
    smallDescription: str

class UserInfo(BaseModel):
    Name:str
    Qualification: str
    Description: str