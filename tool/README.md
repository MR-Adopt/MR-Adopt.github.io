# MR-Adopt Prototype

**MR-Adopt** is an automated approach to automatically deduce input transformation functions for metamorphic testing


### Environment Configuration 

* Java: 11.0.18
* Python: 3.10, the required depdencies can be found in `requirements.txt`

#### setting API key for GPT-3.5/4
open file `tool/utility/request_LLMs.py` and update the following fields.

``` python 
client = openai.AzureOpenAI(
    api_key="TODO",         # change to your OpenAI API key
    api_version="TODO",     # choose the api version
    azure_endpoint="TODO"   # set the endpoint
)
```


### Quick Start

1. Phase1: input pairs preparation
    
    Navigate to MR-Adopt's directory and execute the following command:

    ```cmd
   $ cd $MR_Adopt_dir$; python generate_Inputs_with_LLMs.py 
   ```

   Output:
   * generate input pairs and the validation results can be found at `tool/data/ITrans/cache/generateInputs/CodeQwen1.5-7B-Chat_Ti5-1_Temprature0.2_[0-9]/evaluation_generated_inputs.json` 


2. Phase2: input transformation generation

    Navigate to MR-Adopt's directory and execute the following command:

    ```cmd
   $ cd $MR_Adopt_dir$; python generate_Trans_with_LLMs.py 
   ```
   Output:
   * generate input transforamtions can be found at `tool/data/ITrans/cache/generateTrans/gpt-35-turbo_T5-1_Shot0_Temprature0.2_[0-4]/generated_ITrans/`
   * validation and evaluation results can be found at `tool/data/ITrans/cache/generateTrans/gpt-35-turbo_T5-1_Shot0_Temprature0.2_[0-4]/evaluation_generated_ITrans.json` 



### Update

If you have any questions or issues, please feel free to report an issue. We will continue to maintain this project. Thanks for your feedback😄. 