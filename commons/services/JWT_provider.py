import jwt
from settings.settings import SECRET_KEY

class JWTProvider:

    def validateToken(self):
        pass

    def generateToken(self, infomation):
        payload = {
            # nhà phát hành
            'iss': '1123',
            'exp': 30000,
            "iat": 1300819370,
            "qsh": "8063ff4ca1e41df7bc90c8ab6d0f6207d491cf6dad7c66ea797b4614b71922e9",
            "sub": "batman",
            "context": {
                "user": {
                    "userKey": "batman",
                    "username": "bwayne",
                    "displayName": "Bruce Wayne"
                }
            }
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
