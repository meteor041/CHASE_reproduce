class DataReader:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_data(self) -> List[Dict[str, str]]:
        """
        加载训练数据。

        返回：
            一个字典列表，其中每个字典包含'question'和'sql'键。
        """
        data = []
        # 具体实现取决于数据格式（例如，JSON、CSV）
        return data