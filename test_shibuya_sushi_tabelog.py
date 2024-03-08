# def my_function():
#     return "This is my function"


def shibuya_sushi_reserve_tabelog():
    import re
    from playwright.sync_api import Page, expect
    # import json
    # from typing import Sequence, List
    # import openai
    # from llama_index.llms.openai import OpenAI, openai
    # from llama_index.core.llms import ChatMessage
    # from llama_index.core.tools import BaseTool, FunctionTool
    # from llama_index.agent.openai import OpenAIAgent

    # openai.api_key = "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"
    #user_input = input("Please enter some text: ")

    def test_has_title(page: Page):
    
        # tabelog method
        page.goto("https://www.google.co.jp/",timeout=1000000)
        page.goto("https://www.google.com/search?q=%E6%B8%8B%E8%B0%B7+%E5%AF%BF%E5%8F%B8+tabelog&oq=%E6%B8%8B%E8%B0%B7+%E5%AF%BF%E5%8F%B8+tabelog+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiiBBiJBTIKCAMQABiABBiiBDIKCAQQABiABBiiBNIBCDc4MTdqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8")
        page.goto("https://tabelog.com/sushi/tokyo/A1303/A130301/rank/",timeout=1000000)
        page.goto("https://tabelog.com/tokyo/A1303/A130301/13199924/",timeout=1000000)
        page.goto("https://ssl.tabelog.com/account/login/?from_yoyaku_entry=true",timeout=1000000)
        page.click('div[class="c-btn c-btn--full register-login-action__btn-detail js-analytics"]',timeout=1000000)
        page.mouse.click(100, 100)
        page.click('button[class="c-btn c-btn--full p-login-panel__btn p-login-panel__btn--line"]',timeout=1000000)
        page.fill('input[data-v-1f9fe43d=""]', 'aqlo984@gmail.com')
        page.fill('input[data-v-9106cf85=""]', 'Pihpih1008',timeout=1000000)
        page.click('span[class="ldsm-box-button__text"]',timeout=1000000)
        page.goto("https://tabelog.com/rst/rstdtl_top?LstAre=A130301&LstPrf=A1303&pal=tokyo&rcd=13199924&svd=20240314&svps=2&svt=1900")
        page.goto("https://tabelog.com/booking/form/new?member=2&rcd=13199924&visit_date=20240314&visit_time=1900&lid=yoyaku_rstdtl_side_calendar")
        locator = page.get_by_role("button", name="選択する")

        locator.first.hover()
        locator.first.click()
        
        locator = page.get_by_role("button", name="選択する")

        locator.first.hover()
        locator.first.click()
        
        expect(page).to_have_title(re.compile("Playwright"), timeout=1000000)
        
        
    # def test_book_tabelog_sushi():
    #     test_has_title()
            
    # add_tool = FunctionTool.from_defaults(fn=test_book_tabelog_sushi)


    # llm = OpenAI(model="gpt-3.5-turbo-0613")
    # agent = OpenAIAgent.from_tools([test_book_tabelog_sushi], llm=llm, verbose=True)

    # user_input = input("Please enter some text: ")

    # response = agent.chat(user_input, tool_choice="test_book_tabelog_sushi")
