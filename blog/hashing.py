from passlib.context import CryptContext
pw_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def bcryptpass(password):
        return pw_ctx.hash(password)
    
    def verify(plainpassword,encpassword):
        return pw_ctx.verify(plainpassword,encpassword)
