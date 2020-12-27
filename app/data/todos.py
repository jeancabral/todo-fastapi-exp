from typing import List, Dict, Any

class Todos:
  todo: List[Dict[str, Any]] = [
    { 
      "id": 1, 
      "title": "Estudar Python", 
      "description": 
      "Cap 3 do Fluente Python", 
      "status": "a fazer"
    }
  ]

  actual_id: 1

  def list_todo(self):
    return todo

