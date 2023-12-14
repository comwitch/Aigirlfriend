model_path = "../model/mistral-7b-openorca.Q4_0.gguf"

from llama_cpp import Llama
from llama_index.llms import LlamaCPP
from llama_index.llms.base import ChatMessage

#llm = Llama(model_path=model_path)
llm_gpt = LlamaCPP(model_path=model_path)

message = ChatMessage(role="user", content="만나서 반가워 난 동원 이야")

answer = llm_gpt.chat([message])

print(answer)

