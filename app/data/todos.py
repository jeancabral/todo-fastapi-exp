from typing import List, Dict, Any

class Todos:
  todo: List[Dict[str, Any]] = [
    { 
      "id": 1, 
      "title": "Estudar Python", 
      "description": "Cap 3 do Fluente Python", 
      "status": "a fazer"
    }
  ]

  actual_id = 1

  def list_todo(self):
    return self.todo
  
  def create_todo(self, item: Dict[str, Any]) -> Dict[str, Any]:
    self.actual_id += 1
    item["id"] = self.actual_id
    print(item)
    self.todo.append(item)
    return item

