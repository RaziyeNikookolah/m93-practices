# This file is responsible for sign in incoding decoding and returning jwt
import time
import jwt  # For incoding and decoding jwt
from typing import Dict
from decouple import (
    config,  # for .env
)  # Decouple helps you to organize your settings so that you can change parameters without having to redeploy your app and store parameters in ini or .env files


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


# Function return generated token(JWTs)
def token_response(token: str):
    return {"access token": token}


# function used for signing jwt string
def signJWT(userID: str) -> str:
    payload = {"uerID": userID, "expires": time.time() + 600}
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)


def decodeJwT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)

        return decode_token if decode_token["expires"] > time.time() else None
    except:
        return {"message": "Error in decoding"}
