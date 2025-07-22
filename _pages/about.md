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

I am an incoming PhD student in the Department of Computer Science at [**University College London (UCL)**](https://www.ucl.ac.uk/), where I will begin my studies in Fall 2025, co-supervised by [**Prof. He Ye**](https://heye.me/) and [**Prof. Federica Sarro**](http://www0.cs.ucl.ac.uk/staff/F.Sarro/).
Previously, I completed my master's degree at the School of Computer Science and Technology, [**Huazhong University of Science and Technology (HUST)**](https://www.hust.edu.cn), advised by [**Prof. Yao Wan**](http://wanyao.me).
My academic journey has also been enriched by collaborations with [**Prof. Lingming Zhang**](https://lingming.cs.illinois.edu/) at UIUC and [**Prof. Hongyu Zhang**](https://sites.google.com/site/hongyujohn/) at Chongqing University.

> My research is inspired by the exciting frontiers at the intersection of **artificial intelligence** and **software engineering**, with a current focus on **multimodal coding agents**. I am passionate about building next-generation tools that make code smarter, more accessible, and more trustworthy.
For more details about my academic background, please see my [**CV**](../assets/ZhaoyangChu_CV.pdf).

I am always eager to connect and collaborate—whether you share my interests or bring a different perspective from another field. If you’d like to discuss research, exchange ideas, or just say hi, feel free to reach out at [zychu418@gmail.com](mailto:zychu418@gmail.com).

🌟🌟 **Excited to share: I will be in Rio de Janeiro for [ICSE 2026](https://conf.researchr.org/home/icse-2026) next April—looking forward to meeting many of you there!** 🤗🤗

<!--
🌟🌟 **I will be in Vienna, Austria in September for ISSTA 2024! Hope to meet many of you there!** 🤗🤗
- **Code Intelligence**, e.g., code generation, code search, and vulnerability detection.
- **Trustworthy Artificial Intelligence**, e.g., explainability, privacy, and robustness.
-->

# 🔥 News

- *2025.07*: &nbsp;🎉 Our work on *LLM-as-a-Judge for code summarization* was accepted by **IEEE Transactions on Software Engineering**.
- *2025.06*: &nbsp;🎉 Our paper on *machine unlearning for code LLMs* was accepted to **ICSE 2026**.
- *2025.05*: &nbsp;🎉 Our research on *dynamic code knowledge synchronization for LLMs* was accepted to **ICML 2025**.
- *2025.03*: &nbsp;🎉 Our SANER 2025 paper received the **IEEE TCSE Distinguished Paper Award🏆**!
- *2025.01*: &nbsp;🎉 Our work on *test generation benchmark for LLMs* was accepted to **NAACL 2025 Findings**.
- *2024.12*: &nbsp;🎉 Our study on *pre-trained code model selection for reuse* was accepted to **SANER 2025**.
- *2024.03*: &nbsp;🎉 Our research on *counterfactual reasoning for GNN-based vulnerability detectio* was accepted to **ISSTA 2024**.

<!--
- *2022.09*: &nbsp;🎉 One paper was published in **Information Sciences**.
-->

# 📝 Publications 

<!--
- ``Preprint`` **TESTEVAL: Benchmarking Large Language Models for Test Case Generation**.<br>
Wenhan Wang, Chenyuan Yang, Zhijie Wang, Yuheng Huang, [**Zhaoyang Chu**](), Da Song, Lingming Zhang, An Ran Chen, Lei Ma.<br>
\[ [Paper](../assets/TestEval.pdf) \] \[ [Benchmark](https://llm4softwaretesting.github.io/) \] \[ [Code](https://github.com/LLM4SoftwareTesting/TestEval) \] \[ [arXiv](https://arxiv.org/abs/2406.04531) \]
-->

† indicates equal contribution. ‡ indicates the corresponding author.


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICSE 2026</div><img src='images/CodeEraser_Illustration.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning**.<br>
[**Zhaoyang Chu**](), Yao Wan‡, Zhikun Zhang, Di Wang, Zhou Yang, Hongyu Zhang, Pan Zhou, Xuanhua Shi, Hai Jin, David Lo.<br>
[**ICSE 2026**](https://conf.researchr.org/home/icse-2026). *The IEEE/ACM International Conference on Software Engineering*. **CORE A\***.<br>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISSTA 2024</div><img src='images/CFExplainer_Illustration.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Graph Neural Networks for Vulnerability Detection: A Counterfactual Explanation**.<br>
[**Zhaoyang Chu**](), Yao Wan‡, Qian Li, Yang Wu, Hongyu Zhang, Yulei Sui, Guandong Xu, Hai Jin.<br>
[**ISSTA 2024**](https://2024.issta.org). *The ACM SIGSOFT International Symposium on Software Testing and Analysis*. **CORE A**.<br>
\[ [Paper](../assets/CFExplainer.pdf) \] \[ [Code](https://github.com/Zhaoyang-Chu/counterfactual-vulnerability-detection) \] \[ [arXiv](https://arxiv.org/abs/2404.15687) \] \[ [Link](https://dl.acm.org/doi/10.1145/3650212.3652136) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/CodeSync_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**CODESYNC: Synchronizing Large Language Models with Dynamic Code Evolution at Scale**.<br>
Chenlong Wang†, [**Zhaoyang Chu†**](), Zhengxiang Cheng†, Xuyi Yang, Kaiyue Qiu, Yao Wan‡, Zhou Zhao, Xuanhua Shi, Dongping Chen.<br>
[**ICML 2025**](https://icml.cc/Conferences/2025). *International Conference on Machine Learning*. **CORE A\***.<br>
\[ [Paper](../assets/CodeSync.pdf) \] \[ [Code](https://github.com/Lucky-Wang-Chenlong/CodeSync) \] \[ [arXiv](https://arxiv.org/abs/2502.16645) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE Transactions on Software Engineering</div><img src='images/CodeRPE_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Can Large Language Models Serve as Evaluators for Code Summarization?** <br>
Yang Wu, Yao Wan‡, [**Zhaoyang Chu**](), Wenting Zhao, Ye Liu, Hongyu Zhang, Xuanhua Shi, Philip S. Yu.<be>
[**IEEE Transactions on Software Engineering**](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32), 2025. **Impact Factor 5.6, CORE A\***.<br>
\[ [Paper](../assets/CodeRPE.pdf) \] \[ [Code](https://github.com/CGCL-codes/naturalcc/tree/main/examples/CodeSum-Eval) \] \[ [arXiv](https://arxiv.org/abs/2412.01333) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SANER 2025 Distinguished Paper 🏆</div><img src='images/CodeModelReuse_Illustration.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**How to Select Pre-Trained Code Models for Reuse? A Learning Perspective**.<br>
Zhangqian Bi, Yao Wan‡, [**Zhaoyang Chu**](), Yufei Hu, Junyi Zhang, Hongyu Zhang, Guandong Xu, Hai Jin.<br>
[**SANER 2025**](https://conf.researchr.org/home/saner-2025). *The IEEE International Conference on Software Analysis, Evolution and Reengineering*. **CORE A**.<br>
**IEEE TCSE Distinguished Paper Award🏆**.<br>
\[ [Paper](../assets/CodeModelReuse.pdf) \] \[ [Code](https://github.com/CGCL-codes/naturalcc/tree/main/examples/pcm-reuse) \] \[ [arXiv](https://arxiv.org/abs/2501.03783) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2025 Findings</div><img src='images/TestEval_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**TESTEVAL: Benchmarking Large Language Models for Test Case Generation**.<br>
Wenhan Wang†, Chenyuan Yang†, Zhijie Wang†, Yuheng Huang, [**Zhaoyang Chu**](), Da Song, Lingming Zhang, An Ran Chen, Lei Ma.<br>
[**NAACL 2025 Findings**](https://2025.naacl.org). *The Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics*. **CORE A**.<br>
\[ [Paper](../assets/TestEval.pdf) \] \[ [Benchmark](https://llm4softwaretesting.github.io/) \] \[ [Code](https://github.com/LLM4SoftwareTesting/TestEval) \] \[ [arXiv](https://arxiv.org/abs/2406.04531) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/NoWait_Illustration.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Wait, We Don't Need to "Wait"! Removing Thinking Tokens Improves Reasoning Efficiency**.<br>
Chenlong Wang, Yuanning Feng, Dongping Chen, [**Zhaoyang Chu**](), Ranjay Krishna‡, Tianyi Zhou‡.<br>
Preprint.<br>
\[ [arXiv](https://arxiv.org/abs/2506.08343) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Information Sciences</div><img src='images/HGRL-DTA_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Hierarchical Graph Representation Learning for the Prediction of Drug-Target Binding Affinity**.<br>
[**Zhaoyang Chu†**](), Feng Huang†, Haitao Fu, Yuan Quan, Xionghui Zhou, Shichao Liu, Wen Zhang‡.<br>
[**Information Sciences**](https://www.sciencedirect.com/journal/information-sciences), 2022. **Impact Factor 8.1, CORE A**.<br>
\[ [Paper](../assets/HGRL-DTA.pdf) \] \[ [Code](https://github.com/Zhaoyang-Chu/HGRL-DTA) \] \[ [Link](https://www.sciencedirect.com/science/article/abs/pii/S0020025522010908) \]

</div>
</div>


# 🎖 Honors and Awards
- *2024-2025*, **National Scholarship for Postgraduates**.
- *2022-2023*, Merit Postgraduate, First-class Scholarship for Postgraduates. 
- *2021-2022*, Undergraduate Thesis Innovation Award, Outstanding Undergraduate.
- *2019-2020*, **National Scholarship for Undergraduates**, Merit Student.


# 📖 Educations
- *2022.09 - 2025.06*, Master, Huazhong University of Science and Technology (Graduated with Honors). 
- *2018.09 - 2022.06*, Undergraduate, Huazhong Agricultural University (Graduated with Honors).
