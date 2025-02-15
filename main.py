import datetime

from config import DATE_FORMAT, TODAY
from scripts.knowledge import Knowledge
from scripts.knowledge_list import KnowledgeList
from scripts.data import Data
from scripts.utils import convert_dates_to_strings


class Facade:
    def __init__(self):
        self.knowledge_list = KnowledgeList()
        self.data = Data()

        self.load_knowledge()

    def load_knowledge(self):
        try:
            file = self.data.load('data.json')
            for knowledge in file:
                name = list(knowledge.keys())[0]
                start_day = datetime.datetime.strptime(list(knowledge.values())[0][0], DATE_FORMAT) - datetime.timedelta(days=1)

                self.add_knowledge(name, start_day=start_day)
        except FileNotFoundError:
            self.data.save([], 'data.json')

    def add_knowledge(self, name, save=False, start_day=TODAY):
        self.knowledge_list.add_knowledge(Knowledge(name, start_day))
        if save:
            temp_knowledge_list = self.knowledge_list.knowledge_list

            for knowledge in temp_knowledge_list:
                knowledge.dates = convert_dates_to_strings(knowledge.dates)
            
            temp_knowledge_list = self.knowledge_list.prepare_data_to_save(temp_knowledge_list)
            self.data.save(temp_knowledge_list, 'data.json')


facade = Facade()
