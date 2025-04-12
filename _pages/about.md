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

I am a third-year master’s student in the School of Computer Science and Technology at [**Huazhong University of Science and Technology (HUST)**](https://www.hust.edu.cn), under the guidance of [**Prof. Yao Wan**](http://wanyao.me). I am currently seeking a PhD position in AI/SE for Spring/Fall 2026. For an overview of my academic background, please look at my [**CV**](../assets/ZhaoyangChu_CV.pdf). If you are interested, please feel free to contact me: [zychu418@gmail.com](mailto:zychu418@gmail.com) \| [chuzhaoyang@hust.edu.cn](mailto:chuzhaoyang@hust.edu.cn).

My research interest focuses on the intersection of **artificial intelligence** and **software engineering**, where I am particularly intrigued by:
- **Code Intelligence**, e.g., code generation, code search, and vulnerability detection.
- **Trustworthy Artificial Intelligence**, e.g., explainability, privacy, and robustness.

<!--
🌟🌟 **I will be in Vienna, Austria in September for ISSTA 2024! Hope to meet many of you there!** 🤗🤗
-->


# 🔥 News
- *2025.03*: &nbsp;🎉 Our SANER 2025 paper has been awarded the IEEE TCSE Distinguished Paper Award🏆!
- *2025.01*: &nbsp;🎉 Our research on test generation benchmark for LLMs has been accepted by NAACL 2025 Findings.
- *2024.12*: &nbsp;🎉 Our research on pre-trained code LLM selection for reuse has been accepted by SANER 2025.
- *2024.03*: &nbsp;🎉 Our research on counterfactual reasoning for GNN-based vulnerability detection has been accepted by ISSTA 2024.
- *2022.09*: &nbsp;🎉 One paper is published in Information Sciences.


# 📝 Publications 

<!--
- ``Preprint`` **TESTEVAL: Benchmarking Large Language Models for Test Case Generation**.<br>
Wenhan Wang, Chenyuan Yang, Zhijie Wang, Yuheng Huang, [**Zhaoyang Chu**](), Da Song, Lingming Zhang, An Ran Chen, Lei Ma.<br>
\[ [Paper](../assets/TestEval.pdf) \] \[ [Benchmark](https://llm4softwaretesting.github.io/) \] \[ [Code](https://github.com/LLM4SoftwareTesting/TestEval) \] \[ [arXiv](https://arxiv.org/abs/2406.04531) \]
-->

\* indicates equal contribution. † indicates the corresponding author.

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISSTA 2024</div><img src='images/CFExplainer_Illustration.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Graph Neural Networks for Vulnerability Detection: A Counterfactual Explanation**.<br>
[**Zhaoyang Chu**](), Yao Wan†, Qian Li, Yang Wu, Hongyu Zhang, Yulei Sui, Guandong Xu, Hai Jin.<br>
[**ISSTA 2024**](https://2024.issta.org). *The ACM SIGSOFT International Symposium on Software Testing and Analysis*. **CORE A**.<br>
\[ [Paper](../assets/CFExplainer.pdf) \] \[ [Code](https://github.com/Zhaoyang-Chu/counterfactual-vulnerability-detection) \] \[ [arXiv](https://arxiv.org/abs/2404.15687) \] \[ [Link](https://dl.acm.org/doi/10.1145/3650212.3652136) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SANER 2025</div><img src='images/CodeModelReuse_Illustration.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**How to Select Pre-Trained Code Models for Reuse? A Learning Perspective**.<br>
Zhangqian Bi, Yao Wan†, [**Zhaoyang Chu**](), Yufei Hu, Junyi Zhang, Hongyu Zhang, Guandong Xu, Hai Jin.<br>
[**SANER 2025**](https://conf.researchr.org/home/saner-2025). *The IEEE International Conference on Software Analysis, Evolution and Reengineering*. **CORE A**.<br>
**IEEE TCSE Distinguished Paper Award🏆**.<br>
\[ [Paper](../assets/CodeModelReuse.pdf) \] \[ [Code](https://github.com/CGCL-codes/naturalcc/tree/main/examples/pcm-reuse) \] \[ [arXiv](https://arxiv.org/abs/2501.03783) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2025 Findings</div><img src='images/TestEval_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**TESTEVAL: Benchmarking Large Language Models for Test Case Generation**.<br>
Wenhan Wang\*, Chenyuan Yang\*, Zhijie Wang\*, Yuheng Huang, [**Zhaoyang Chu**](), Da Song, Lingming Zhang, An Ran Chen, Lei Ma.<br>
[**NAACL 2025 Findings**](https://2025.naacl.org). *The Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics*. **CORE A**.<br>
\[ [Paper](../assets/TestEval.pdf) \] \[ [Benchmark](https://llm4softwaretesting.github.io/) \] \[ [Code](https://github.com/LLM4SoftwareTesting/TestEval) \] \[ [arXiv](https://arxiv.org/abs/2406.04531) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/CodeRPE_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Can Large Language Models Serve as Evaluators for Code Summarization?** <br>
Yang Wu, Yao Wan†, [**Zhaoyang Chu**](), Wenting Zhao, Ye Liu, Hongyu Zhang, Xuanhua Shi, Philip S. Yu.<br>
Preprint.<br>
\[ [Paper](../assets/CodeRPE.pdf) \] \[ [Code](https://github.com/CGCL-codes/naturalcc/tree/main/examples/CodeSum-Eval) \] \[ [arXiv](https://arxiv.org/abs/2412.01333) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/CodeSync_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**CODESYNC: Synchronizing Large Language Models with Dynamic Code Evolution at Scale**.<br>
Chenlong Wang\*, [**Zhaoyang Chu\***](), Zhengxiang Cheng\*, Xuyi Yang, Kaiyue Qiu, Yao Wan†, Zhou Zhao, Xuanhua Shi, Dongping Chen.<br>
Preprint.<br>
\[ [Paper](../assets/CodeSync.pdf) \] \[ [Code](https://github.com/Lucky-voyage/Code-Sync) \] \[ [arXiv](https://arxiv.org/abs/2502.16645) \]

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Information Sciences</div><img src='images/HGRL-DTA_Framework.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Hierarchical Graph Representation Learning for the Prediction of Drug-Target Binding Affinity**.<br>
[**Zhaoyang Chu\***](), Feng Huang\*, Haitao Fu, Yuan Quan, Xionghui Zhou, Shichao Liu, Wen Zhang†.<br>
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
- *2022.09 - 2025.06 (anticipated)*, Master, Huazhong University of Science and Technology. 
- *2018.09 - 2022.06*, Undergraduate, Huazhong Agricultural University (Graduated with Honors).
