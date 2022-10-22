
class predictionTree:
    def __init__(self):
        self.children = {}
    
    def getPrediction(self,text):
        text = text.lower()
        if len(text) > 0:
            if text[0] in self.children.keys():
                return self.children[text[0]].getPrediction(text)
            else:
                return []
    
    def populateTree(self,text,weight):
        if len(text) > 0:
            if text[0].lower() not in self.children.keys():
                self.children[text[0].lower()] = letterNode(1)
            self.children[text[0].lower()].populateTree(text,weight)
                
class letterNode:
    def __init__(self,depth):
        self.depth = depth
        self.predictions = {}
        self.children = {}
  
    def getPrediction(self,text):
        if len(text) == self.depth:
            return self.predictions.values()
        else:
            letter = text[self.depth]
        if letter in self.children.keys():
            return self.children[letter].getPrediction(text)
        else:
            return []
            
    def populateTree(self,text,weight):
        if len(self.predictions)<10:
            self.predictions[weight] = text
        else:
            minKey = min(self.predictions.keys())
            if( minKey < weight):
                self.predictions.pop(minKey)
                self.predictions[weight] = text
        
        if len(text) > self.depth:
            if text[self.depth].lower() not in self.children.keys():
                self.children[text[self.depth].lower()] = letterNode(self.depth+1)
            self.children[text[self.depth].lower()].populateTree(text,weight)
            
            
tree = predictionTree()
tree.populateTree("This",40)
tree.populateTree("Thit",22)
tree.populateTree("The Other",1)
print(tree.getPrediction("th"))

