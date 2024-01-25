from langchain.prompts import PromptTemplate

if __name__ == '__main__':
    prompt = PromptTemplate(input_variables=["product"],
                   template="what is a good name for a company that makes {product}?")

    print(prompt.format(product="candies"))