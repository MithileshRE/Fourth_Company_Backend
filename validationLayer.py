from pydantic import BaseModel,EmailStr


class EmailContent(BaseModel):
    SENDER :EmailStr = "noreply@hashtechinfo.com"
    RECIPIENT :EmailStr = "puneeth3sprime@gmail.com"
    SUBJECT: str
    BODY_TEXT: str
    BODY_HTML: str

