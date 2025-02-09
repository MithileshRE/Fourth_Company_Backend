from pydantic import BaseModel,EmailStr


class EmailContent(BaseModel):
    SENDER :EmailStr = "puneeth3sprime@gmail.com"
    RECIPIENT :EmailStr = "puneeth3sprime@gmail.com"
    SUBJECT: str
    BODY_TEXT: str
    BODY_HTML: str

