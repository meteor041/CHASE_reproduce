class SQLExecutor:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def execute_sql(self, sql: str) -> Tuple[List[Tuple], float]:
        """
        执行给定的SQL查询并测量执行时间。

        参数：
            sql：要执行的SQL查询。

        返回：
            一个元组，包含查询结果和执行时间。
        """
        start_time = time.time()
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        end_time = time.time()
        execution_time = end_time - start_time
        return results, execution_time

    def close(self):
        self.connection.close()