class DC_CoT_Prompter:
    def __init__(self, llm):
        self.llm = llm
        self.divide_system_prompt = read_file_to_string("prompt\COT_combine_system_prompt.txt")
        self.combine_system_prompt = read_file_to_string("prompt\COT_divide_system_prompt.txt")

    def generate_sql(self, question: str, schema: str) -> str:
        """
        使用分而治之CoT提示生成SQL。

        参数：
            question：自然语言问题。
            schema：数据库schema。

        返回：
            生成的SQL查询。
        """
        sub_queries = self.divide_queries(question, schema)
        final_query = self.assemble_sub_queries(sub_queries)
        optimized_query = self.optimize_query(final_query)
        return optimized_query

    def divide_queries(self, question, schema) -> List[str]:
        """TODO 结合系统描述,调用LLM拆分SQL查询"""
        return
    
    def assemble_sub_queries(self, sub_queries: List[str]) -> str:
        """TODO 通过LLM从子查询组装最终的SQL查询。"""

        return 

    def optimize_query(self, query: str) -> str:
        """TODO 优化最终的SQL查询（例如，删除冗余子句）。如果不需要可以删去"""
        # 查询优化的实现（可以是基于规则的或基于LLM的）
        return query