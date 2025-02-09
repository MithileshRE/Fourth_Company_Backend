from fastapi import FastAPI,Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from validationLayer import Base_asserts, Domains_url, UserInfo, EmailContent, MailResponse
from celery_ser import sendMail
from toolService import EmailService
import Sample_Data
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
auth_scheme = HTTPBearer()


VALID_TOKEN = "supersecrettoken"

def validate_token(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return credentials.credentials


@app.get("/")
async def base_asserts(token: str = Depends(validate_token),response_model = list[Base_asserts]):
    return Sample_Data.base_Asserts


@app.get("/Domains_url")
async def Domain_URL(token: str = Depends(validate_token),response_model = list[Domains_url]):
    return Sample_Data.Domains_Url

@app.post("/mail_Service")
async def Mail_service(UserInput : UserInfo,token: str = Depends(validate_token),response_model = list[MailResponse]):
    Pre_process = {
        "SUBJECT": f"New Application: {UserInput.Name}",
        "BODY_TEXT": f"New Application: {UserInput.Name}",
        "BODY_HTML": f"""<head></head>
    <body>
    <h1>Hi Dear</h1>
    <p>We have a new client<strong><br>
    Name: {UserInput.Name}<br>
    Qualification: {UserInput.Qualification}<br>
    Request: {UserInput.Description}<br>
    </strong></p>
    </body>
    </html>"""
    }
    obj1 = EmailService(EmailContent(**Pre_process))
    result = obj1.EmailFormat()
    if(sendMail.delay(result).get()):
        return  [MailResponse(mail_status = True)]
    raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="SomeThing Went Wrong",
        )


if __name__=="__main__":
    uvicorn.run(app)