---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

_**How to say my name?**<br>
You can just say it as “Jao-young Choo”.<br>
😊 No stress about precision — I’m happy with any close version._

---

I am a first-year PhD student in the Department of Computer Science at [**University College London (UCL)**](https://www.ucl.ac.uk/), where I am fortunate to be co-supervised by [**Prof. Federica Sarro**](http://www0.cs.ucl.ac.uk/staff/F.Sarro/) and [**Dr. He Ye**](https://heye.me/).
Previously, I completed my master's degree at the School of Computer Science and Technology, [**Huazhong University of Science and Technology (HUST)**](https://www.hust.edu.cn), advised by [**Prof. Yao Wan**](http://wanyao.me).
My academic journey has also been enriched by collaborations with [**Prof. Lingming Zhang**](https://lingming.cs.illinois.edu/) at UIUC and [**Prof. Hongyu Zhang**](https://sites.google.com/site/hongyujohn/) at Chongqing University.

<!--
I am also a co-founder of [**EuniAI**](https://euni.ai/), where we are building [**Prometheus**](https://github.com/EuniAI/Prometheus) — an open-source AI agent designed to push the boundaries of automated software development.
-->

> My research interests lie at the intersection of software engineering and artificial intelligence, with an emphasis on **reliable and safe coding agents** for real-world software engineering workflows.
I have published 10+ papers <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/endpoint?url={{ url }}&logo=googlescholar&logoColor=white&style=for-the-badge&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a> at top-tier international SE and AI conferences such as ICSE, FSE, ISSTA, ACL, EMNLP, ICML, and NAACL.
For more details about my academic background, please see my [**CV**](../assets/ZhaoyangChu_CV.pdf).

🤝 **Let’s Connect**: I am always eager to connect and collaborate, whether you share my interests or bring a different perspective from another field. If you’d like to discuss research, exchange ideas, or just say hi, feel free to reach out at [zhaoyang.chu.25@ucl.ac.uk](mailto:zhaoyang.chu.25@ucl.ac.uk), [zychu418@gmail.com](mailto:zychu418@gmail.com).

<!--
🌟🌟 **Excited to share: I will be in Rio de Janeiro, Brazil for [ICSE 2026](https://conf.researchr.org/home/icse-2026) next April—looking forward to meeting many of you there!** 🤗🤗
-->

<!--
🌟🌟 **I will be in Vienna, Austria in September for ISSTA 2024! Hope to meet many of you there!** 🤗🤗
- **Code Intelligence**, e.g., code generation, code search, and vulnerability detection.
- **Trustworthy Artificial Intelligence**, e.g., explainability, privacy, and robustness.
-->

# 🔥 News

- *2026.04*: &nbsp;🎉 Our two post-training papers on *code execution reasoning* and *structure-aware code understanding* was accepted to **ACL 2026**.
- *2026.03*: &nbsp;🎉 Our paper on *LLM hallucination mitigation in code summarization* was accepted to **FSE 2026**.
- *2025.08*: &nbsp;🎉 Our work on *efficient reasoning for R1-style LLMs* was accepted to **EMNLP 2025**.
- *2025.07*: &nbsp;🎉 Our work on *LLM-as-a-Judge for code summarization* was accepted by **IEEE Transactions on Software Engineering**.
- *2025.06*: &nbsp;🎉 Our paper on *machine unlearning for code LLMs* was accepted to **ICSE 2026**.
- *2025.05*: &nbsp;🎉 Our research on *dynamic code knowledge synchronization for LLMs* was accepted to **ICML 2025**.
- *2025.03*: &nbsp;🎉 Our SANER 2025 paper received the **IEEE TCSE Distinguished Paper Award🏆**!
- *2025.01*: &nbsp;🎉 Our work on *test generation benchmark for LLMs* was accepted to **NAACL 2025**.
- *2024.12*: &nbsp;🎉 Our study on *pre-trained code model selection for reuse* was accepted to **SANER 2025**.
- *2024.03*: &nbsp;🎉 Our research on *counterfactual reasoning for GNN-based vulnerability detectio* was accepted to **ISSTA 2024**.

<!--
- *2022.09*: &nbsp;🎉 One paper was published in **Information Sciences**.
-->

# 📝 Publications 

<!--
- ``Preprint`` **TESTEVAL: Benchmarking Large Language Models for Test Case Generation**.<br>
Wenhan Wang, Chenyuan Yang, Zhijie Wang, Yuheng Huang, [**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Da Song, Lingming Zhang, An Ran Chen, Lei Ma.<br>
\[ [Paper](../assets/TestEval.pdf) \] \[ [Benchmark](https://llm4softwaretesting.github.io/) \] \[ [Code](https://github.com/LLM4SoftwareTesting/TestEval) \] \[ [arXiv](https://arxiv.org/abs/2406.04531) \]
-->

\* indicates equal contribution. † indicates the corresponding author.

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/TerminalWorld.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks**.<br>
[**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Jiarui Hu\*, Xingyu Jiang\*, Pengyu Zou\*, Han Li, Chao Peng, Peter O'Hearn, Earl T. Barr, Mark Harman, Federica Sarro, He Ye†.<br>
Preprint.<br>
<a href="https://arxiv.org/abs/2605.22535"><img src="https://img.shields.io/badge/arXiv-2605.22535-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/EuniAI/TerminalWorld"><img src="https://img.shields.io/github/stars/EuniAI/TerminalWorld?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://huggingface.co/datasets/EuniAI/TerminalWorld"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=huggingface&logoColor=FFD21E&url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fdatasets%2FEuniAI%2FTerminalWorld%3Fexpand%3DdownloadsAllTime&query=%24.downloadsAllTime&label=HuggingFace&color=FFD21E" alt="HuggingFace" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://terminalworld.ai/"><img src="https://img.shields.io/website?url=https://terminalworld.ai/&up_message=terminalworld.ai&up_color=blue&down_message=terminalworld.ai&down_color=blue&style=for-the-badge" alt="Website" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3AufrVoPGSRksC%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/Prometheus.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Prometheus: Towards Long-Horizon Codebase Navigation for Repository-Level Problem Solving**.<br>
Yue Pan\*, Zimin Chen\*, Siyu Lu, [**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Xiang Li, Han Li, Yang Feng, Claire Le Goues, Federica Sarro, Martin Monperrus, He Ye†.<br>
Preprint.<br>
<a href="https://arxiv.org/abs/2507.19942"><img src="https://img.shields.io/badge/arXiv-2507.19942-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/EuniAI/Prometheus"><img src="https://img.shields.io/github/stars/EuniAI/Prometheus?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3AW7OEmFMy1HYC%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/ContextBench.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**ContextBench: A Benchmark for Context Retrieval in Coding Agents**.<br>
Han Li, Letian Zhu\*, Bohan Zhang\*, Rili Feng\*, Jiaming Wang, Yue Pan, Earl T. Barr, Federica Sarro, [**Zhaoyang Chu†**](), He Ye†.<br>
Preprint.<br>
<a href="https://arxiv.org/abs/2602.05892"><img src="https://img.shields.io/badge/arXiv-2602.05892-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/EuniAI/ContextBench"><img src="https://img.shields.io/github/stars/EuniAI/ContextBench?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://huggingface.co/datasets/Contextbench/ContextBench"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=huggingface&logoColor=FFD21E&url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fdatasets%2FContextbench%2FContextBench%3Fexpand%3DdownloadsAllTime&query=%24.downloadsAllTime&label=HuggingFace&color=FFD21E" alt="HuggingFace" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://contextbench.github.io/"><img src="https://img.shields.io/website?url=https://contextbench.github.io/&up_message=contextbench.github.io&up_color=blue&down_message=contextbench.github.io&down_color=blue&style=for-the-badge" alt="Website" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3AY0pCki6q_DkC%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICSE 2026</div><img src='images/CodeEraser_Illustration.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning**.<br>
[**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Yao Wan†, Zhikun Zhang, Di Wang, Zhou Yang, Hongyu Zhang, Pan Zhou, Xuanhua Shi, Hai Jin, David Lo.<br>
[**ICSE 2026**](https://conf.researchr.org/home/icse-2026). *The 48th IEEE/ACM International Conference on Software Engineering*.<br>
<a href="https://arxiv.org/abs/2509.13755"><img src="https://img.shields.io/badge/arXiv-2509.13755-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/Zhaoyang-Chu/code-unlearning"><img src="https://img.shields.io/github/stars/Zhaoyang-Chu/code-unlearning?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3AzYLM7Y9cAGgC%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">FSE 2026</div><img src='images/HALLU.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Hallucinations in LLM-based Code Summarization: Unveiling, Detection, and Mitigation**.<br>
Guanghua Wan, Yuanning Feng, Yao Wan†, [**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Zhangqian Bi, Junxiao Han, Zhou Zhao, Hongyu Zhang, Pingpeng Yuan, Xuanhua Shi, Hai Jin.<br>
[**FSE 2026**](https://conf.researchr.org/home/fse-2026). *The ACM International Conference on the Foundations of Software Engineering*.<br>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/ExecVerify.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning**.<br>
Lingxiao Tang, He Ye, [**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Muyang Ye, Zhongxin Liu, Xiaoxue Ren, Lingfeng Bao†.<br>
[**ACL 2026**](https://2026.aclweb.org/). *The 64th Annual Meeting of the Association for Computational Linguistics*.<br>
<a href="https://arxiv.org/abs/2603.11226"><img src="https://img.shields.io/badge/arXiv-2603.11226-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/tlx000000001/ExecVerify"><img src="https://img.shields.io/github/stars/tlx000000001/ExecVerify?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3AYsMSGLbcyi4C%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026 Findings</div><img src='images/CGBridge.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Bridging Code Graphs and Large Language Models for Better Code Understanding**.<br>
Zeqi Chen, [**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Yi Gui, Feng Guo, Yao Wan, Chuan Shi†.<br>
[**ACL 2026 Findings**](https://2026.aclweb.org/). *The 64th Annual Meeting of the Association for Computational Linguistics*.<br>
<a href="https://arxiv.org/abs/2512.07666"><img src="https://img.shields.io/badge/arXiv-2512.07666-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/OmniJax/CGBridge"><img src="https://img.shields.io/github/stars/OmniJax/CGBridge?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3ATyk-4Ss8FVUC%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/CodeSync_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**CODESYNC: Synchronizing Large Language Models with Dynamic Code Evolution at Scale**.<br>
Chenlong Wang\*, [**Zhaoyang Chu\***](), Zhengxiang Cheng\*, Xuyi Yang, Kaiyue Qiu, Yao Wan†, Zhou Zhao, Xuanhua Shi, Dongping Chen.<br>
[**ICML 2025**](https://icml.cc/Conferences/2025). *The 42nd International Conference on Machine Learning*.<br>
<a href="https://arxiv.org/abs/2502.16645"><img src="https://img.shields.io/badge/arXiv-2502.16645-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/Lucky-Wang-Chenlong/CodeSync"><img src="https://img.shields.io/github/stars/Lucky-Wang-Chenlong/CodeSync?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3AqjMakFHDy7sC%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SANER 2025 Distinguished Paper 🏆</div><img src='images/CodeModelReuse_Illustration.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**How to Select Pre-Trained Code Models for Reuse? A Learning Perspective**.<br>
Zhangqian Bi, Yao Wan†, [**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Yufei Hu, Junyi Zhang, Hongyu Zhang, Guandong Xu, Hai Jin.<br>
[**SANER 2025**](https://conf.researchr.org/home/saner-2025). *The 32nd IEEE International Conference on Software Analysis, Evolution and Reengineering*.<br>
**IEEE TCSE Distinguished Paper Award🏆**.<br>
<a href="https://arxiv.org/abs/2501.03783"><img src="https://img.shields.io/badge/arXiv-2501.03783-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/CGCL-codes/naturalcc/tree/main/examples/pcm-reuse"><img src="https://img.shields.io/github/stars/CGCL-codes/naturalcc?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3A2osOgNQ5qMEC%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE Transactions on Software Engineering</div><img src='images/CodeRPE_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Can Large Language Models Serve as Evaluators for Code Summarization?** <br>
Yang Wu, Yao Wan†, [**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Wenting Zhao, Ye Liu, Hongyu Zhang, Xuanhua Shi, Philip S. Yu.<br>
[**IEEE Transactions on Software Engineering (TSE)**](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32), 2025.<br>
<a href="https://arxiv.org/abs/2412.01333"><img src="https://img.shields.io/badge/arXiv-2412.01333-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/CGCL-codes/naturalcc/tree/main/examples/CodeSum-Eval"><img src="https://img.shields.io/github/stars/CGCL-codes/naturalcc?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3A9yKSN-GCB0IC%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025 Findings</div><img src='images/NoWait_Illustration.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Wait, We Don't Need to "Wait"! Removing Thinking Tokens Improves Reasoning Efficiency**.<br>
Chenlong Wang, Yuanning Feng, Dongping Chen, [**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Ranjay Krishna†, Tianyi Zhou†.<br>
[**EMNLP 2025 Findings**](https://2025.emnlp.org). *The 2025 Conference on Empirical Methods in Natural Language Processing*.<br>
<a href="https://arxiv.org/abs/2506.08343"><img src="https://img.shields.io/badge/arXiv-2506.08343-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3AIjCSPb-OGe4C%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2025 Findings</div><img src='images/TestEval_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**TESTEVAL: Benchmarking Large Language Models for Test Case Generation**.<br>
Wenhan Wang\*, Chenyuan Yang\*, Zhijie Wang\*, Yuheng Huang, [**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Da Song, Lingming Zhang, An Ran Chen, Lei Ma.<br>
[**NAACL 2025 Findings**](https://2025.naacl.org). *The 2025 Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics*.<br>
<a href="https://arxiv.org/abs/2406.04531"><img src="https://img.shields.io/badge/arXiv-2406.04531-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/LLM4SoftwareTesting/TestEval"><img src="https://img.shields.io/github/stars/LLM4SoftwareTesting/TestEval?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://llm4softwaretesting.github.io/"><img src="https://img.shields.io/website?url=https://llm4softwaretesting.github.io/&up_message=llm4softwaretesting.github.io&up_color=blue&down_message=llm4softwaretesting.github.io&down_color=blue&style=for-the-badge" alt="Website" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3Ad1gkVwhDpl0C%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISSTA 2024</div><img src='images/CFExplainer_Illustration.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Graph Neural Networks for Vulnerability Detection: A Counterfactual Explanation**.<br>
[**Zhaoyang Chu**](https://zhaoyang-chu.github.io/), Yao Wan†, Qian Li, Yang Wu, Hongyu Zhang, Yulei Sui, Guandong Xu, Hai Jin.<br>
[**ISSTA 2024**](https://2024.issta.org). *The 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis*.<br>
<a href="https://arxiv.org/abs/2404.15687"><img src="https://img.shields.io/badge/arXiv-2404.15687-A42C25?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://github.com/Zhaoyang-Chu/counterfactual-vulnerability-detection"><img src="https://img.shields.io/github/stars/Zhaoyang-Chu/counterfactual-vulnerability-detection?style=for-the-badge&logo=github&label=GitHub&color=black" alt="GitHub" style="vertical-align:middle;height:24px!important;width:auto"></a> <a href="https://scholar.google.com/citations?user=HYu3DyEAAAAJ"><img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&logo=googlescholar&logoColor=white&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FZhaoyang-Chu%2FZhaoyang-Chu.github.io%40google-scholar-stats%2Fgs_data.json&query=%24.publications%5B%27HYu3DyEAAAAJ%3Au-x6o8ySG0sC%27%5D.num_citations&label=Citations&color=4285F4" alt="Citations" style="vertical-align:middle;height:24px!important;width:auto"></a>

</div>
</div>



<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">Information Sciences</div><img src='images/HGRL-DTA_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Hierarchical Graph Representation Learning for the Prediction of Drug-Target Binding Affinity**.<br>
[**Zhaoyang Chu\***](), Feng Huang\*, Haitao Fu, Yuan Quan, Xionghui Zhou, Shichao Liu, Wen Zhang†.<br>
[**Information Sciences**](https://www.sciencedirect.com/journal/information-sciences), 2022. **Impact Factor 8.1, CORE A**.<br>
\[ [Paper](../assets/HGRL-DTA.pdf) \] \[ [Code](https://github.com/Zhaoyang-Chu/HGRL-DTA) \] \[ [Link](https://www.sciencedirect.com/science/article/abs/pii/S0020025522010908) \]

</div>
</div> -->


# 🎖 Honors and Awards
- *2025*, **IEEE TCSE Distinguished Paper Award**.


# 📖 Educations
- *2025.09 - now*, Ph.D., University College London.
- *2022.09 - 2025.06*, M.E., Huazhong University of Science and Technology (Graduated with Honors). 
- *2018.09 - 2022.06*, B.E., Huazhong Agricultural University (Graduated with Honors).
