class QP_CoT_Prompter:
    def __init__(self, llm, db_executor: SQLExecuto):
        self.llm = llm
        self.db_executor = db_executor

    def generate_sql(self, question: str, schema: str, sql: str) -> str:
        """
        使用查询计划CoT提示生成SQL。

        参数：
            question：自然语言问题。
            schema：数据库schema。
            sql： question对应的正确SQL查询
            
        返回：
            生成的SQL查询。
        """
        query_plan = self.get_query_plan(sql)
        final_prompt = self.construct_prompt(query_plan, question, schema, sql)
        
        return final_prompt

    def get_query_plan(self, sql: str) -> str:
        """TODO 基于sql查询，使用EXPLAIN命令获取查询计划。"""
        explain_query = "EXPLAIN " + sql  # 假设LLM输出部分查询
        query_plan, _ = self.db_executor.execute_sql(explain_query)
        return self.format_query_plan(query_plan)

    def format_query_plan(self, query_plan: List[Tuple]) -> str:
        """TODO 将查询计划格式化为人类可读的格式。"""
        # 将query_plan转换为字符串的实现
        return "Formatted Query Plan"
    
    def construct_prompt(self, query_plan: str, question: str, schema: str, sql: str) -> str:
        """TODO 构建最终的提示。"""
        return prompt