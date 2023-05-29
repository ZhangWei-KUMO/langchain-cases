# 使用LLMRequestChain构建爬虫

`LLMRequestChain`可以通过URL的输入帮助我们实现爬虫的功能，并且根据搜索到了文本内容，提出问题并生成答案。

首先第一步初始化一个chain：

```js
prompt = PromptTemplate(
    input_variables=["requests_result"],
    template=template
)
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0)
chain = LLMRequestsChain(llm_chain=LLMChain(llm=llm, prompt=prompt))
```

在OpenAI中，temperature是一种用于控制生成文本的多样性和创造力的参数。这个参数控制了模型在生成每个单词时对其后续单词的概率分布的缩放程度。较低的值会使模型更加保守，更倾向于选择概率高的单词。而较高的温度值会使模型更加大胆，更倾向于选择概率较低的单词。在这里我们设置为0。
