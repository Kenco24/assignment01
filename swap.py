def swapping(x,y):
 
    try:
        if x>3 or x<0:
            return "error number must be between 0 - 3"
        if y>3 or y<0:
            return "error number must be between 0 - 3"
        
        
        a,b = y,x
        return a,b
    
    except Exception as e:
        print(str(e))
        
