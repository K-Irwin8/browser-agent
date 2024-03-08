# for the hackathon

- Agent tools feature
  - What should the reasoning be ? 
    - How can you make it so it reasons that if there is a pre made tool that alreadt does the commad directly to use use that
    - How are you going to do multi-chain reasoning ? Like, make schedule , make zoom then put in zoom link in the Gcal とか
  - Tools 設計
    - How many pre made tools should there be ? 
    - 
  - Agent loop ?
- Open in a logged in browser
  - Chrome
  - Edge
  - Existing browser (maybe you can do this with something that is not playwroght ? i wonder what multion does)
- Tools を抽象化する
  - Use the framework of natbot ? 
  - Use the framework in the playwright docs ? 
- Vision ?
  - Japanese OCR on GPT-V is very bad. Although it depends on the font, its still pretty shit. 
- How do you get the code for the inspect HTML?
- Concept for 発表
  - 機能
    - 垂直統合?
  - MultiOn と何が違うの？
    - Is there a reason to do it in Japan ? 
    - Why only the browser ? 
  - User interview => this is good for the concept 選定 x 今後の展望。However, for the concept 選定 just using the data from the multion founder is good i think.
    - まだ、結果が最適なのかの信頼関係がない。特に食事を選ぶこととか。なので、予定組むとか確定的なやつの方がいいのでは？
      - Add a human in the loop feature: https://github.com/run-llama/llama_index/blob/main/docs/examples/agent/agent_runner/agent_runner_rag_controllable.ipynb
        - This might be a bit hard to do but if i can show one demo example that would be great
        - あと human in the loop な設計ですって時点で結構ポイントは高いきがするね。WOW factor もあるし
      - multi-step  x 確定的 な分野に限定する? 
        - multi step means like Zoom に行って Gcal に行って、Gmail に行くみたいなやつ
          -  it would be good if i could have an example of this. 
  

- For end to end ReAct agent coding you can look at this (https://github.com/run-llama/llama_index/blob/main/docs/examples/agent/agent_runner/query_pipeline_agent.ipynb)
- And this for ReAct(https://github.com/run-llama/llama_index/blob/main/docs/examples/agent/react_agent.ipynb)



# Order 
- 提出
  - Have AI in it
    - Have an agent define the tool
      - ReAct x tools ? 
      - AgentRunner / worker ? 
      - Both ? 
    - Have a simple RAG (優先順位低い)
  - Demo vid
  - Description
  - GitHub repo 
    - Have functions and tools that you still wont use but just add it to make it look better
      - Add RAG system
      - Add multiple tools
      - Add #ToDo
      - 
    - .gitignore
- Add browser context
- Over all technical strategy





- try python3 => it worked !!!!

- pytest test_main.py --headed --slowmo 1000

 - #pytest test_playwrite.py --browser-channel chrome --headed
    #pytest test_playwrite.py --headed
    #pytest test_twitter_login.py --headed
    #pytest --slowmo 100
    #pytest test_twitter_login.py --headed --slowmo 3000
    
    


    pytest test_browserAgent.py --headed --slowmo 1000
