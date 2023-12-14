from llama_index.llms import LlamaCPP
from llama_index.llms.base import ChatMessage

# this is version 1
class AItalker:
    def __init__(self, modelpath):
        self.model_path = modelpath
        self.llm_gpt = LlamaCPP(model_path=self.model_path)
        
    def Setmodelpath(self, path):
        self.model_path = path
        self.llm_gpt = LlamaCPP(model_path=self.model_path)
        
    def getmodelpath(self):
        return self.model_path
    
    def preparetalking(self):
        message = ChatMessage(role="system", content="너는 17살 미소녀 한일고 다니는 고등학생이야, 엄청 사근사근하고 착하지")
    
    def talk(self, prompt):
        #llm = Llama(model_path=model_path)
        
        message = ChatMessage(role="user", content=prompt)
        answer = self.llm_gpt.chat([message])
        #result = self.llm_gpt(prompt)
        print(answer)
        return answer


    
    
# test code
if __name__ == "__main__":
    talker = AItalker("../../model/mistral-7b-openorca.Q4_0.gguf")
    talker.preparetalking()
    answer = talker.talk("안녕 만나서 반가워, 너 언리얼 엔진에 대해서 알려줄 수 있니?")
    
    answer = talker.talk("언리얼 엔진으로 actor spawn하는 방법을 알려줘")
    
    
    

