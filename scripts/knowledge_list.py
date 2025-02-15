class KnowledgeList:
    def __init__(self):
        self.knowledge_list = []

    def add_knowledge(self, knowledge):
        self.knowledge_list.append(knowledge)

    def prepare_data_to_save(self, knowledge_list):
        result = []

        for knowledge in knowledge_list:
            result.append({knowledge.name: knowledge.dates})
        
        return result
