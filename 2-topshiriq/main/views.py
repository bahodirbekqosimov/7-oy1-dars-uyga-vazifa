from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class HelloView(APIView):
    data = [{"message":"Hello, API!"}]
    
    def get(self,res:Request):
        return Response(self.data[0],status=200)
    
    # def post(self,req:Request):
    #     self.data.append({"message":"Hello, API!"})
    #     return Response(self.data,status=201)
    
    # def put(self,req:Request):
    #     data = []
    #     for obj in self.data:
    #         obj['message'] = 'Hello world'
    #         data.append(obj)
        
    #     self.data = data
        
    #     return Response(self.data,status=200)
    # def delete(self,req:Request):
    #     self.data = []
        
    #     return Response(self.data,status=200)
    
    
class GreetView(APIView):
    
    def get(self,req:Request):
        
        params = req.query_params
        data = []
        
        for param in params.items():
            data.append({f"{param[0]}":f"{param[1]}"})
            
        return Response(data, status=200)
    


    
class EchoView(APIView):
    # def get(self,req:Request):
    #     data = {
    #         "matn":req.data.get("text")
    #     }
    #     return Response(data,status=200)

    def post(self,req:Request):
        data = {
            "matn":req.data.get("text")
        }
        return Response(data,status=200)

    # def delete(self,req:Request):
    #     data = {
    #         "matn":req.data.get("text")
    #     }
    #     return Response(data,status=200)

    # def put(self,req:Request):
    #     data = {
    #         "matn":req.data.get("text")
    #     }
    #     return Response(data,status=200)



class Check_ageView(APIView):
    # def get(self,req:Request):
    #     age = req.data.get("age")
        
    #     if age != None and int(age)<18:
    #         return Response({"message":'Access denied'} , status=403)
        
    #     return Response({"message":"Access granted"} , status=200)
    
    def post(self,req:Request):
        age = req.data.get("age")
        
        if age != None and  int(age)<18:
            return Response({"message":'Access denied'} , status=403)
        
        return Response({"message":"Access granted"} , status=200)
    
    # def delete(self,req:Request):
    #     age = req.data.get("age")
        
    #     if age != None and int(age)<18:
    #         return Response({"message":'Access denied'} , status=403)
        
    #     return Response({"message":"Access granted"} , status=200)
    
    # def put(self,req:Request):
    #     age = req.data.get("age")
        
    #     if age != None and  int(age)<18:
    #         return Response({"message":'Access denied'} , status=403)
        
    #     return Response({"message":"Access granted"} , status=200)



class RegisterView(APIView):
    
    # def get(self,req:Request):
    #     if req.data.get("username"):
    #         return Response({"messgae":'User registered'}, status=201)
    #     return Response(status=400)
    
    def post(self,req:Request):
        if req.data.get("username"):
            return Response({"messgae":'User registered'}, status=201)
        return Response(status=400)
    
    # def delete(self,req:Request):
    #     if req.data.get("username"):
    #         return Response({"messgae":'User registered'}, status=201)
    #     return Response(status=400)

    # def put(self,req:Request):
    #     if req.data.get("username"):
    #         return Response({"messgae":'User registered'}, status=201)
    #     return Response(status=400)
    
    
class SquareView(APIView):
    def get(self,req:Request, number):
        data = {
            "number":number,
            "square": number*number
        }
        return Response(data,status=200)


