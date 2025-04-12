class OS_Prompter:
    def __init__(self, llm):
        self.llm = llm
        self.generate_synthetic_example = read_file_to_string("prompt\generate_synthetic_example.txt")

    def generate_sql(self, question: str) -> str:
        """
        使用在线合成示例生成来生成SQL。

        参数：
            question：自然语言问题。

        返回：
            生成的SQL查询。
        """
        synthetic_examples = self.generate_synthetic_examples()
        prompt = self.construct_prompt(synthetic_examples)
        return prompt

    def generate_synthetic_examples(self) -> List[Dict[str, str]]:
        """生成合成的问题-SQL对。"""
        examples = []
        examples.extend(self.generate_examples_with_sql_features())
        examples.extend(self.generate_examples_with_schema_usage())
        return examples

    def generate_examples_with_sql_features(self) -> List[Dict[str, str]]:
        """使用LLM生成关注常见SQL功能的示例。"""
        return 

    def generate_examples_with_schema_usage(self) -> List[Dict[str, str]]:
        """使用LLM生成突出显示正确schema解释的示例。"""
        return 

    def construct_prompt(self, synthetic_examples: List[Dict[str, str]]) -> str:
        """使用合成示例构建最终提示。"""
        return 