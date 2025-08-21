class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    return self._dfs(self.root, id)
  
  def _dfs(self, node, target_id):
    if not node:
      return None
    if node["id"] == target_id:
      return node
    for child in node['children']:
      result = self._dfs(child, target_id)
      if result:
        return result
    return None



  
