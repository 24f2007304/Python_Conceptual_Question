import time 

class TimeError(Exception):
      """""A Cosustem to Raise the Exeption Error"""
      
class Time():
    
    def _init_(self):
        self._start_time = None
        self._enclapsed_time = None
        
        
    def start(self):
        if self._start_time is not None:
            raise TimeError(f"Timer is running .Use .stop() to stop it")
        self._start_time = time.perf_counter()
            
        
    def stop(self):
        if self._start_time is None:
            raise TimeError(f"Timer is not running .Use .start() to start it")
        self._enclapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Time: {self._enclapsed_time:0.4f} seconds")     
    
    
    def enclapsed_time(self):
        if self._enclapsed_time is None:
            raise TimeError(f"Timer has not been started")
        if self._start_time is not None:
            return(time.perf_counter() - self._start_time)
        else:
            return(self._enclapsed_time)
        
        
        
t  = Time()

a  = int(input("Enter the Number of Seconds to Start the Timer: "))
 
 
t.start()
for   i in range(a**7):
    if i == 100000000000:
        print(True)
t.stop()
    
print(t.enclapsed_time())