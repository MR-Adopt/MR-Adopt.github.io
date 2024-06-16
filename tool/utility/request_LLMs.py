import os, sys
import time
_PROJECT_NAME = "tool"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

from utility import file_processing,json_processing
import config
import openai

prompt_dir = "./..//data/ITrans/cache/prompts/"
prompt_results_content_dir_default = "./..//data/ITrans/cache/prompts_results_content/"
prompt_results_raw_dir_default = "./..//data/ITrans/cache/prompts_results_raw/"
prompt_generated_ITrans_dir_default = config.PROMPT_GENERATED_ITRANS_DIR

# setting 
model_symbols = {   
    "WizardCoder-15B-V1.0": "w",
    "gpt-35-turbo": "g3",
    "gpt-4": "g4",
    "starcoder2-15b-instruct-v0.1": "s2",
    "CodeQwen1.5-7B-Chat": "qw",
    "Meta-Llama-3-8B-Instruct": "ml",
    "deepseek-coder-7b-instruct-v1.5": "dp"
}
symbols_model = {   
    "w": "WizardCoder-15B-V1.0",
    "g3": "gpt-35-turbo",
    "g4": "gpt-4",
    "s2": "starcoder2-15b-instruct-v0.1",
    "qw": "CodeQwen1.5-7B-Chat",
    "ml": "Meta-Llama-3-8B-Instruct",
    "dp": "deepseek-coder-7b-instruct-v1.5"
}
# meta-llama/Meta-Llama-3-8B-Instruct

max_tokens = 10000

def request_GPT(prompt, model="gpt-35-turbo", promt_id="default",temperature=0,prompt_results_raw_dir=prompt_results_raw_dir_default,prompt_results_content_dir=prompt_results_content_dir_default, system_message="You are a helpful programming assistant", few_shot_info=[], prompt_messages_path=""):
    """_summary_
    """
    client = openai.AzureOpenAI(
       api_key="TODO",
       api_version="TODO",
       azure_endpoint="TODO"
    )

    messages = []
    messages.append({"role": "system", "content": system_message})
    for shot_info in few_shot_info:
      Q = shot_info["Q"]
      A = shot_info["A"]
      messages.append({"role": "user", "content": Q})
      messages.append({"role": "assistant", "content": A})
    messages.append({"role": "user", "content": prompt})
  
    # create a chat completion
    # response = client.chat.completions.create(
    #     model=model,
    #     messages=messages,
    #     temperature=temperature
    # )
    response = None
    retries = 3    
    while retries > 0:    
        try: 
          response = client.chat.completions.create(
              model=model,
              messages=messages,
              temperature=temperature
          )
          retries = 0
        except Exception as e:    
         if e: 
             print(e)   
             print('LOG, INGO: Timeout error, retrying...')    
             retries -= 1    
             time.sleep(10) # sleep 10 secs    
         else:    
             raise e  

    # store response
    """ store """
    if prompt_messages_path:
      json_processing.write(path=prompt_messages_path, json_content=messages)

    if response: content = response.choices[0].message.content
    else: content = "ERROR: No response"
    if prompt_results_content_dir: 
      file_processing.write_TXTfile(path=f"{prompt_results_content_dir}{promt_id}.md", content=content)
    else:  
      file_processing.write_TXTfile(path=f"{prompt_results_content_dir_default}{promt_id}.md", content=content)

    return content


def request_fastChat(prompt, model="gpt-35-turbo", promt_id="default",temperature=0,prompt_results_raw_dir="",prompt_results_content_dir="", system_message="You are a helpful programming assistant", few_shot_info=[], prompt_messages_path=""):
    # for fast chat
    # openai.api_base = "http://localhost:10000/v1"  # python 3.7
    # s2: 10010(in 8) 10020 (in 7), w: 10000
    openai.api_key = "EMPTY"                        # opena0 1.12.0 
    openai.base_url = "http://localhost:10000/v1/"

    if model in ["w", "WizardCoder-15B-V1.0"]:
       openai.base_url = "http://localhost:10000/v1/" # 
    if model in ["s2", "starcoder2-15b-instruct-v0.1"]:
       openai.base_url = "http://localhost:10020/v1/" # 
    if model in ["qw", "CodeQwen1.5-7B-Chat"]:
       openai.base_url = "http://localhost:10010/v1/" # 
    if model in ["ml", "Meta-Llama-3-8B-Instruct"]:
       openai.base_url = "http://localhost:10030/v1/" # 
    if model in ["dp", "deepseek-coder-7b-instruct-v1.5"]:
       openai.base_url = "http://localhost:10040/v1/" # 
      
    
    
    """ request """
    # create a completion
    # response = openai.completions.create(model=model, prompt=prompt, max_tokens=64,temperature=temperature)

    # messages = [
    #        {"role": "system", "content": system_message},
    #        {"role": "user", "content": prompt}
    #        ]
    messages = []
    messages.append({"role": "system", "content": system_message})
    for shot_info in few_shot_info:
      Q = shot_info["Q"]
      A = shot_info["A"]
      messages.append({"role": "user", "content": Q})
      messages.append({"role": "assistant", "content": A})
    messages.append({"role": "user", "content": prompt})
  
    # create a chat completion
    retries = 2  
    response = None  
    while retries > 0:    
        try: 
          response = openai.chat.completions.create(
              model=model,
              messages=messages,
              temperature=temperature
          )
          retries = 0
        except Exception as e:    
         if e: 
             print(e)   
             print('LOG, INGO: Timeout error, retrying...')    
             retries -= 1    
             time.sleep(60*10) # sleep 10 minutes    
         else:    
             raise e  

    """ store """
    if prompt_messages_path:
      json_processing.write(path=prompt_messages_path, json_content=messages)
    # # raw: not json format, 不可用
    # if prompt_results_raw_dir: 
    #   json_processing.write(path=f"{prompt_results_raw_dir}{promt_id}.json", json_content=response.json)
    # else:
    #   json_processing.write(path=f"{prompt_results_raw_dir_default}{promt_id}.json", json_content=response.json)
    # content
    if response: content = response.choices[0].message.content
    else: content = "ERROR: No response"
    if prompt_results_content_dir: 
      file_processing.write_TXTfile(path=f"{prompt_results_content_dir}{promt_id}.md", content=content)
    else:  
      file_processing.write_TXTfile(path=f"{prompt_results_content_dir_default}{promt_id}.md", content=content)
    return content


def extract_generated_ITrans_class(response_content, promt_id,prompt_generated_ITrans_dir=prompt_generated_ITrans_dir_default):
    code_lines = []
    code_flag = False
    codes = []
    code=[]
    for line in response_content.split("\n"):
      if code_flag==False and line.strip().startswith("```"):
        code_flag = True
        continue
      if code_flag==True and line.strip().startswith("```"):
         code_flag = False
         code = ("\n").join(code_lines)
         codes.append(code)
         code=[]
         code_lines = []
      if code_flag:
        code_lines.append(line)
    

    # pattern = re.compile("?<=```java\n)(.*?)(?=```")
    # matches = pattern.findall(response_content)
    # # for match in matches:
    # #   print(match)
    # code_blocks = matches
    # print(response_content)
    # print(codes)
    class_code = ""
    for code in codes:
       if f"class {promt_id}" in code:
          class_code = code
          break
    
    file_processing.write_TXTfile(path = f"{prompt_generated_ITrans_dir}{promt_id}.java", content=class_code)

    return code


def extract_generated_inputs_blocks(response_content):
    code_lines = []
    code_flag = False
    codes = []
    code=[]
    for line in response_content.split("\n"):
      if code_flag==False and line.strip().startswith("```"):
        code_flag = True
        continue
      if code_flag==True and line.strip().startswith("```"):
         code_flag = False
         code = ("\n").join(code_lines)
         codes.append(code)
         code=[]
         code_lines = []
      if code_flag:
        code_lines.append(line)
    return codes
  
def extract_generated_one_inputs_block(response_content):
    # return the last one
    code_lines = []
    code_flag = False
    codes = []
    code=[]
    for line in response_content.split("\n"):
      if code_flag==False and line.strip().startswith("```"):
        code_flag = True
        continue
      if code_flag==True and line.strip().startswith("```"):
         code_flag = False
         code = ("\n").join(code_lines)
         codes.append(code)
         code=[]
         code_lines = []
      if code_flag:
        code_lines.append(line)

    return code

# request_fastChat(prompt= "give a sorting algorithm in Python", model= "WizardCoder-15B-V1.0", promt_id="test_store_sorting")
# request_GPT(prompt= "give a sorting algorithm in Python")