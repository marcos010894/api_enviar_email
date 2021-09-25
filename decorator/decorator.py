from flask import request
import os


key_master =  os.environ.get('secretKey')
def decorator_key(func):
    def func_args(*args,**kwargs):
        key = ""
        try:
            key = request.headers['Key']
        except:
            return {"message":"key cannot be empty in headers"}, 200
        if key != key_master:
            
            return {"message": "Unauthorized"}, 200
       
        response = func(*args,**kwargs)
        return response
        
        
    return func_args