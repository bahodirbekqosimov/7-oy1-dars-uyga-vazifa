from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class HelloView(APIView):
    data = [{"message":"Hello, API!"}]
    
    def get(self,res:Request):
        return Response(self.data[0],status=200)
    
    def post(self,req:Request):
        self.data.append({"message":"Hello, API!"})
        return Response(self.data,status=201)
    
    def put(self,req:Request):
        data = []
        for obj in self.data:
            obj['message'] = 'Hello world'
            data.append(obj)
        
        self.data = data
        
        return Response(self.data,status=200)
    def delete(self,req:Request):
        self.data = []
        
        return Response(self.data,status=200)
    
    
class GreetView(APIView):
    
    def get(self,req:Request):
        
        params = req.query_params
        data = []
        
        for param in params.items():
            data.append({f"{param[0]}":f"{param[1]}"})
            
        return Response(data, status=200)
    


            

    
        