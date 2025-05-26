from typing import Any, Optional

class Queue:
    
    def __init__(self):
        self.__elements = []
        
    def arrive(self, value: Any) -> None:
        self.__elements.append(value)
    
    def attention (self) -> Optional[Any]:
        if self.__elements:
            return self.__elements.pop(0)
        else:
            return None
        
    def size(self) -> int:
        return len(self.__elements)
    
    def on_from(self) -> Optional[Any]:
        if self.__elements:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self) -> Optional[Any]:
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
    
    def show(self):
        for i in range(len(self.__elements)):
            print(self.move_to_end())

    