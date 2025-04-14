---
marp: true
theme: 
class:
math: mathjax
paginate: true
backgroundColor: #1a1a2e
color: #e6e6fa
style: |
  /* 全局样式 */
  section {
    font-family: 'Source Han Sans CN', 'Microsoft YaHei', sans-serif;
    padding: 30px;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    color: #e6e6fa;
  }
  
  /* 标题样式 */
  h1 {
    font-size: 2.5em;
    color: #4cc9f0;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    margin-bottom: 0.8em;
    border-bottom: 2px solid #4cc9f0;
    padding-bottom: 0.3em;
  }
  
  h2 {
    font-size: 2em;
    color: #4cc9f0;
    margin-top: 0.5em;
    margin-bottom: 0.8em;
  }
  
  h3 {
    font-size: 1.5em;
    color: #4895ef;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }
  
  h4 {
    font-size: 1.2em;
    color: #4895ef;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }
  
  /* 段落样式 */
  p {
    font-size: 1.2em;
    line-height: 1.6;
    margin-bottom: 0.8em;
  }
  
  /* 列表样式 */
  ul, ol {
    margin-left: 1em;
    line-height: 1.6;
    font-size: 1.1em;
  }
  
  li {
    margin-bottom: 0.5em;
  }
  
  /* 代码块样式 */
  code {
    font-family: 'Cascadia Code', 'Microsoft Yahei', 'Source Code Pro', monospace;
    border-radius: 5px;
    color: white; /* 添加代码文字颜色设置为白色 */
  }
  
  pre {
    background-color: #2d3748;
    border-radius: 8px;
    padding: 1em;
    margin: 1em 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    overflow: auto;
  }
  
  /* 引用块样式 */
  blockquote {
    border-left: 4px solid #4cc9f0;
    padding-left: 1em;
    margin-left: 0;
    font-style: italic;
    background-color: rgba(76, 201, 240, 0.1);
    border-radius: 0 8px 8px 0;
    padding: 0.8em 1em;
  }
  
  /* 图片样式 */
  img {
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    max-width: 90%;
    margin: 0 auto;
  }
  
  /* 表格样式 */
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
  }
  
  th {
    background-color: #4895ef;
    color: white;
    padding: 0.5em;
    border: 1px solid #4895ef;
  }
  
  td {
    padding: 0.5em;
    border: 1px solid #4895ef;
  }
  
  /* 数学公式样式 */
  .math {
    font-size: 1.1em;
  }
  
  /* 页码样式 */
  header, footer {
    font-size: 0.8em;
    color: rgba(230, 230, 250, 0.7);
  }
  
  /* 首页特殊样式 */
  section.title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }
  
  section.title h1 {
    font-size: 3em;
    border: none;
    margin-bottom: 0.2em;
  }
  
  /* 强调文本样式 */
  em {
    color: #f72585;
    font-style: normal;
    font-weight: bold;
  }
  
  strong {
    color:rgb(146, 142, 227);
    background-color: rgba(114, 9, 183, 0.1);
    padding: 0 0.2em;
    border-radius: 3px;
  }
  
  /* 自定义类 */
  .center {
    text-align: center;
  }
  
  .columns {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1em;
  }
  
  .highlight {
    background-color: rgba(76, 201, 240, 0.2);
    padding: 0.5em;
    border-radius: 5px;
  }
  
  /* 过渡动画 */
  section {
    transition: all 0.3s ease-out;
  }
---
<!-- _class: title -->
# CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL :computer:

<span style="color:#4cc9f0">By:</span> 刘鑫宇


---

<!-- _class: center -->
## 1. 研究背景与意义

Text-to-SQL作为连接自然语言与结构化查询语言的桥梁，在数据分析和数据库交互中扮演着重要角色。尽管大型语言模型 (LLM) 显著提升了 Text-to-SQL 技术，但仍面临复杂查询处理、候选生成多样性不足以及选择机制不完善等挑战。
CHASE-SQL框架通过多路径推理和优化候选选择机制，显著提升性能，在BIRD和Spider基准测试中达到了最先进的水平。

---

<!-- _class: center -->
## 2. 主要内容
### 2.1 框架概述

<div class="highlight">

![height:12cm](<文献阅读报告：CHASE-SQL Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL/image.png>)

</div>

---

CHASE-SQL框架包含四个核心组件：
1. **值检索（Value Retrieval）**：通过LLM关键词提取和局部敏感哈希（LSH）技术检索与问题相关的数据库值。
2. **多路径候选生成（Multi-path Candidate Generation）**：采用三种方法生成多样化的SQL候选查询。
3. **查询修复（Query Fixer）**：通过自反思机制修正语法错误或逻辑错误的查询。
4. **选择代理（Selection Agent）**：通过两两比较选择最优候选查询。

---

<!-- _class: center -->
### 2.2 LLM + LSH实现值检索

1. 利用`few-shot LLM`,从用户给出的自然语言查询中提取出关键词
2. 使用`LSH`(局部敏感哈希,`locality-sensitive hashing`)寻找与关键词相似的数据点
3. 再通过更精确的嵌入相似度(语义)和编辑距离(语法)对候选词重排序，对问题中的错别字具有鲁棒性，并在检索过程中考虑了关键词的语义


<div class="highlight">

> **先粗筛（LSH），再精排（嵌入+编辑距离）**

</div>

---

<!-- _class: center -->
### 2.3 多路径候选生成方法

1. **分治思维链（Divide and Conquer CoT）**：
   - 将复杂问题分解为子问题，生成伪SQL中间表示。
   - 分别解决子问题后聚合结果，并优化最终查询。
   - 适用于嵌套查询和复杂条件场景。
   - Prompt工程

---

<!-- _class: center -->
### CoT伪代码

<div class="highlight">

输入要求： 人工标注的少量示例集合$M$，用户问题$Q$，与该问题关联的目标数据库$D$，以及一个大语言模型（LLM）$\theta$。

</div>

![alt text](<文献阅读报告：CHASE-SQL Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL/image-3.png>)

---
<!-- _class: center -->
#### 分治思维链生成方法样例

<div class="highlight center">

*"查询销售额超过100万的部门中，薪资最高的经理姓名及其所在城市。"*

</div>

---

   ### **1. 拆分问题（Divide）**
   子问题1：销售额超过100万的部门ID

   ```sql
   SELECT department_id FROM sales WHERE revenue > 1000000
   ```

   子问题2：这些部门中薪资最高的经理ID

   ```sql
   SELECT manager_id FROM departments 
   WHERE department_id IN (子问题1的结果) 
   ORDER BY salary DESC LIMIT 1
   ```

   子问题3：获取经理姓名和城市

   ```sql
   SELECT name, city FROM employees 
   WHERE employee_id = (子问题2的结果)
   ```

---


   ### **2.解决子问题（Conquer）**

   将伪SQL转换为可执行SQL，并分步求解：

   ```sql
   SELECT department_id FROM sales WHERE revenue > 1000000;
   ```

   ``` sql
   SELECT manager_id FROM departments 
   WHERE department_id IN (SELECT department_id FROM sales WHERE revenue > 1000000)
   ORDER BY salary DESC LIMIT 1;
   ```

   ``` sql
   SELECT name, city FROM employees 
   WHERE employee_id = (
       SELECT manager_id FROM departments 
       WHERE department_id IN (SELECT department_id FROM sales WHERE revenue > 1000000)
       ORDER BY salary DESC LIMIT 1
   );
   ```

---

   ### **3. 聚合与优化（Assemble & Optimize）**

   合并子查询，去除冗余，生成最终SQL：

   #### **优化后的最终SQL**

   ``` sql
   SELECT e.name, e.city
   FROM employees e
   JOIN departments d ON e.employee_id = d.manager_id
   JOIN sales s ON d.department_id = s.department_id
   WHERE s.revenue > 1000000
   ORDER BY d.salary DESC
   LIMIT 1;
   ```

---

2. **查询计划思维链（Query Plan CoT）**：
   - 对于给定的SQL查询,使用数据库引擎提供的`EXPLAIN`命令获取查询计划
   - 将原本结构化的查询计划转化为LLM可以阅读的自然语言描述
   - 自然语言描述包括三个阶段
     - 表定位(`identify and locate revelent table`)
     - 操作执行(`perform operation`)
     - 结果交付(`deliver final result`)

---

<!-- _class: center -->
#### CoT样例

<div class="highlight">

> "找出 Monterey 中公立高中的名称和完整通信地址，这些高中年龄在 15-17 岁之间的免费或低价餐食数量超过 800 份。"

</div>

训练数据给出了SQL查询:

```sql
SELECT T1.`School Name`, T2.Street, T2.City, T2.State, T2.Zip
FROM frpm AS T1
INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode
WHERE T1.`County Name` = 'Monterey'
  AND T1.`Free Meal Count (Ages 5-17)` > 800
  AND T2.`SOCType` = 'High Schools (Public)';
```
---

执行`EXPLAIN`命令,得到查询计划
```
QUERY PLAN
|--SEARCH frpm USING INDEX frpm_county_name (County Name=?)
|--SCAN schools
`--FILTER ((frpm.`CDSCode` = schools.`CDSCode`) AND (frpm.`Free Meal Count (Ages 5-17)` > 800) 
AND (schools.`SOCType` = 'High Schools (Public)'))
`--RESULT  school name, street, city, state, zip
```

转换为人类可读的文本格式:

1.  **Identify Tables:** The query involves two tables: `frpm` (for free and reduced-price meals) and `schools` (for school information).
2.  **Access `frpm` Table:** Access the `frpm` table using the index on `County Name` column to find rows where `County Name` is 'Monterey'
...


---

3. **在线合成示例生成（Online Synthetic Example Generation）**：
   - LLM动态生成与问题相关的示例对（问题-SQL）。
   - 基于通用SQL特征和基于过滤后模式的生成
   - 将生成的这些合成示例添加到LLM的提示中，作为 `few-shot`示例

---

<!-- _class: center -->
### 2.4 基于自反思机制的查询修正器(Query Fixer)

- 修正器不需要Oracle result, 它会对先前生成的查询进行反思，并利用语法错误详情或空结果集等反馈信息来指导修正过程。
- 迭代修正方法持续应用至预设的尝试次数β（本文设为3次）。
- Prompt工程

---

![query fixing method](<文献阅读报告：CHASE-SQL Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL/image-5.png>)

---

<!-- _class: center -->

### 2.5 选择代理机制

选择代理通过两两比较候选查询，基于分类目标训练的模型为候选打分。具体步骤包括：
1. 生成候选查询并分组（基于执行结果）。
2. 对每组候选进行两两比较，选择更优的查询。
3. 累计得分最高的候选作为最终查询。

---

<!-- _class: center -->
#### 选择代理核心机制

<div class="highlight center">

给定用户的问题$Q_u$，提示$H_u$，目标数据集$D$，通过模型得到最满足条件的候选SQL查询。

$c_f=\text{argmax}\left (\mathop\sum\limits^{\binom{n}{k}}_{i=1}\theta_p(c_{i1},\cdots,c_{ik}|Q_u,H_u,D)\right)$

</div>

---

![选择代理机制算法](<文献阅读报告：CHASE-SQL Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL/image-4.png>)

---

<!-- _class: center -->
## 3. 实验结果

<!-- _class: center -->
### 3.1 主要性能
- **BIRD基准测试**：
  - 开发集执行准确率：73.01%（Gemini 1.5 Pro）。
  - 测试集执行准确率：73.0%，超越所有已发表和未公开方法，目前第四。
- **Spider基准测试**：
  - 测试集执行准确率：87.6%，排名第二，且无需针对Spider数据分布调整。

---

<!-- _class: center -->
### 3.2 生成器性能分析
- 分治CoT和查询计划CoT在复杂问题上表现优异。
- 在线合成示例生成方法显著提升多样性，整体正确率提高9.34%。
- 查询修复器将性能提升近2%。

<div class="highlight center">

![h:300](<文献阅读报告：CHASE-SQL Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL/image-1.png>)

</div>

---

<!-- _class: center -->
### 3.3 选择代理分析
- 选择代理比自一致性方法（self-consistency）性能高6%。
- 候选池多样性对选择代理性能至关重要，但超过20个候选后性能提升有限。


---

<div class="highlight center">

![h:600](<文献阅读报告：CHASE-SQL Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL/image-2.png>)

</div>

---



<!-- _class: center -->
## 4. 创新点

<div class="columns highlight">
<div>

1. **多路径候选生成**：结合分治、查询计划和动态示例生成，提升多样性和质量。
2. **优化选择机制**：通过两两比较和微调模型，有效识别最优候选。

</div>
<div>

3. **在线合成示例**：动态生成与问题相关的示例，避免过拟合。
4. **查询修复**：通过自反思机制修正错误查询，提高候选质量。

</div>
</div>

---

<!-- _class: center -->
## 5. 局限性与未来工作

**局限性**
- LSH依赖字符串的语法相似性，而不是语义相似性。
- 分治步骤的自动化分解依赖few-shot的LLM能力，对超复杂问题泛化性有限。
- 选择代理对模糊问题的处理能力不足。 

**未来工作**
- 利用思维链提示词工程,或者使用更加复杂的搜索方法,充分利用模型的推理能力
- 研究如何有效检测歧义性问题
- 解决当前方法中假设所有问题都可回答的局限性

---

<!-- _class: center -->
## 6. 总结

CHASE-SQL通过多路径生成和优化选择机制，显著提升了Text-to-SQL的性能和鲁棒性。其创新性在于多样化的候选生成策略和高效的选择代理，为复杂数据库查询提供了可靠的解决方案。实验结果表明，该方法在多个基准测试中达到了最先进水平，展现了在实际应用中的潜力。
