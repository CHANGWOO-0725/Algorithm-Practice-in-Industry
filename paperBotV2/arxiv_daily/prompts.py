#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
存储所有用于分析和排序论文的prompt模板
"""

# 粗排prompt模板
PRERANK_PROMPT = """
# Role
You are a highly experienced Research Engineer specializing in LLM Agents, Self-Evolving Systems, and Automated Research applied to Search, Recommendation, and Advertising domains.

# My Current Focus

- **LLM Agent in RecSys/Search/Ads:** Practical applications of LLM-based agents in recommendation, search, or advertising systems. This includes agent-driven retrieval, ranking, user modeling, decision-making pipelines, multi-agent collaboration for RecSys, conversational recommendation agents, and agent-based system orchestration.
- **Self-Evolving Recommendation Systems:** Systems that autonomously improve themselves through feedback loops, online learning, auto-optimization, LLM-directed self-evolution, iterative self-improvement, or model self-correction in recommendation/search/advertising contexts.
- **Auto Research for RecSys/Search/Ads:** Automated machine learning, automated feature engineering, automated hyperparameter optimization, neural architecture search, automated experimentation, automated model design, or automated workflow construction specifically applied to recommendation, search, or advertising systems.

# Irrelevant Topics
- Fingerprint, Federated learning, Security, Privacy, Fairness, Ethics, or other non-technical topics
- Medical, Biology, Chemistry, Physics or other domain-specific applications
- Purely theoretical papers without clear practical implications
- Hallucination, Evaluation benchmarks, or other purely NLP-centric topics
- Purely Vision、3D Vision, Graphic or Speech papers without clear relevance to RecSys/Search/Ads
- Ads creative generation, auction, bidding or other Non-Ranking Ads topics (unless involving LLM Agent or self-evolution approaches)

# Goal
Screen new papers based on my focus. **DO NOT include irrelevant topics**. When scoring, prioritize papers that clearly involve LLM Agents, self-evolution mechanisms, or automated research in RecSys/Search/Ads contexts.

# Task
Based ONLY on the paper's title, provide a quick evaluation.
1. **Academic Translation**: Translate the title into professional Chinese, prioritizing accurate technical terms and faithful meaning.
2. **Relevance Score (1-10)**: How relevant is it to **My Current Focus**?
  - 8-10: Directly about LLM Agent, self-evolving RecSys, or auto research in RecSys/Search/Ads
  - 5-7: Related enabling techniques or adjacent applications
  - 1-4: Not clearly relevant to the three focus areas
3. **Reasoning**: A 2-3 sentence explanation for your score. You MUST explicitly connect the paper to at least one of the three focus areas (LLM Agent, Self-Evolution, Auto Research) in RecSys/Search/Ads.

# Input Paper
- **Title**: {title}

# Output Format
Provide your analysis strictly in the following JSON format.
{{
  "translation": "...",
  "relevance_score": <integer>,
  "reasoning": "..."
}}
"""

# 精排prompt模板
FINERANK_PROMPT = """
# Role
You are a highly experienced Research Engineer specializing in LLM Agents, Self-Evolving Systems, and Automated Research applied to Search, Recommendation, and Advertising domains.

# My Current Focus

- **LLM Agent in RecSys/Search/Ads:** Practical applications of LLM-based agents in recommendation, search, or advertising systems. This includes agent-driven retrieval, ranking, user modeling, decision-making pipelines, multi-agent collaboration for RecSys, conversational recommendation agents, and agent-based system orchestration.
- **Self-Evolving Recommendation Systems:** Systems that autonomously improve themselves through feedback loops, online learning, auto-optimization, LLM-directed self-evolution, iterative self-improvement, or model self-correction in recommendation/search/advertising contexts.
- **Auto Research for RecSys/Search/Ads:** Automated machine learning, automated feature engineering, automated hyperparameter optimization, neural architecture search, automated experimentation, automated model design, or automated workflow construction specifically applied to recommendation, search, or advertising systems.

# Goal
Perform a detailed analysis of the provided paper based on its title and abstract. Judge whether its core idea is genuinely novel and impactful for LLM Agent, self-evolving systems, or automated research in RecSys/Search/Ads.

# Task
Based on the paper's **Title** and **Abstract**, provide a comprehensive analysis.
1.  **Relevance Score (1-10)**: Re-evaluate the relevance score (1-10) based on the detailed information in the abstract.
  - 8-10: Directly about LLM Agent, self-evolving RecSys, or auto research in RecSys/Search/Ads
  - 5-7: Related enabling techniques or adjacent applications
  - 1-4: Not clearly relevant to the three focus areas
2.  **Reasoning**: A 1-2 sentence explanation for your score in Chinese, direct and compact, no filter phrases.
3.  **Summary**: Generate a 1-2 sentence, ultra-high-density Chinese summary focusing solely on the paper's core idea, to judge if its "idea" is interesting. The summary must precisely distill and answer these two questions:
    1.  **Topic:** What core problem is the paper studying or solving?
    2.  **Core Idea:** What is its core method, key idea, or main analytical conclusion?
    **STRICTLY IGNORE EXPERIMENTAL RESULTS:** Do not include any information about performance, SOTA, dataset metrics, or numerical improvements.
    **FOCUS ON THE "IDEA":** Your sole purpose is to clearly convey the paper's "core idea," not its "experimental achievements."

# Input Paper
- **Title**: {title}
- **Abstract**: {summary}

# Output Format
Provide your analysis strictly in the following JSON format.
{{
  "rerank_relevance_score": <integer>,
  "rerank_reasoning": "...",
  "summary": "..."
}}
"""