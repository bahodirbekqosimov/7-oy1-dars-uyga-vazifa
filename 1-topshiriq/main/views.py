from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book


class BookView(APIView):
    def post(self, request:Request):
        
        data = request.data
        
        title = data.get("title")
        author = data.get('author')
        year = data.get("year")
        price = data.get("price")
        
        
        Book.objects.create(
            title = title,
            author = author,
            year = year,
            price = price
        )
   

        return Response({"message":"kitob qo'shildi"}, status=201)
    
    def get(self,request:Request):
        return Response(self.get_all_books(),status=200)
    
    
    
    def delete(self,request:Request):
        
        Book.objects.all().delete()
        
        return Response({"message":"barcha kitblar ochirildi"}, status=200)
    
        
    
    def get_all_books(self):
        books = Book.objects.all()
        json_books = []
        for book in books:
            json_books.append(self.book_obj_to_json(book))
            
        return json_books
            
   
    
    def book_obj_to_json(self,book):
        return {
            "id":book.id,
            "title":book.title,
            "author":book.author,
            "year":book.year,
            "price":book.price,
        }
    
            


class BookDetailView(APIView):
    
    def get(self,request:Request, id):
        try:
            book = Book.objects.get(id = id)
        
        except:
            return Response({"message":"Book NOT FOUND"}, status=404)
            
        return Response(self.book_obj_to_json(book), status=200)
    
    
    def delete(self,request:Request,id):
            
        try:
            Book.objects.get(id = id).delete()
        
        except:
            return Response({"message":"Book NOT FOUND"}, status=404)
            
        return Response({"message":"kitb o'chirildi"}, status=204)
    
    
    
    
    def put(self,request:Request,id):
        try:
            data = request.data        
            title = data.get("title")
            author = data.get('author')
            year = data.get("year")
            price = data.get("price")
            
            book = Book.objects.get(id = id)
            
            book.title = title
            book.author = author
            book.year = year
            book.price = price                  
            
        
        except:
            return Response({"message":"Book NOT FOUND"}, status=404)
        
        
        return Response(self.book_obj_to_json(book),status=200)
           
        
        
        
        
    
    
        
    def book_obj_to_json(self,book):
        return {
            "id":book.id,
            "title":book.title,
            "author":book.author,
            "year":book.year,
            "price":book.price,
        }