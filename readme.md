## A MCP Server which lets AI Agents talk to each other.


### Steps to initiate the server

- Create a huggingface account and get the access token

- Open a terminal of start the web server using the command 
        uvicron sql_base.main:app --reload
- Open another terminal 
        -- - set teh access token to the environment vairables using 
            $env:HF_TOKEN = "hf_..."
        --  navigate to the agents directory and run python llm_agent
        -- this agent will read the messages that are sent from the /send endpoint and use the content to hit the Inference API 