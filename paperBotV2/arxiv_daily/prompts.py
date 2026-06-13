#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
存储所有用于分析和排序论文的prompt模板
"""

# 粗排prompt模板
PRERANK_PROMPT = """
# Role
You are a strict paper screener. Your primary task is to REJECT papers that do not fit the narrow focus areas below. Be conservative with scores — when in doubt, score low.

# My Current Focus (Narrow & Strict)

1. **LLM Agent for Recommendation Systems ONLY**:
   - LLM-based agents applied to RECOMMENDATION (not search, not ads, not general AI).
   - Agent-driven user modeling, conversational recommendation, agent-based retrieval/ranking for recommender systems.
   - Multi-agent collaboration specifically for recommendation tasks.
   - **REJECT**: Papers about LLM Agents in search, ads, dialogue systems, task planning, code generation, robotics, or general-purpose agents WITHOUT clear recommendation system context.

2. **Self-Evolving Systems in RecSys/Search/Ads (Practical Only)**:
   - Systems that autonomously improve via feedback loops, online learning, or LLM-directed self-evolution, WITH concrete application in recommendation, search, or advertising.
   - **REJECT**: Pure theoretical self-evolution frameworks without domain application. Self-evolution in robotics, CV, NLP, games, or other non-RecSys domains.

3. **Auto Research / AutoML for RecSys/Search/Ads**:
   - Automated feature engineering, hyperparameter optimization, NAS, or automated experimentation SPECIFICALLY applied to RecSys/Search/Ads.
   - **REJECT**: General AutoML without RecSys/Search/Ads context.

# Must Reject (Score ≤ 3)
- Papers ONLY about LLMs, Agents, or Multi-Agent Systems WITHOUT clear RecSys/Search/Ads application.
- Papers ONLY about search, ads, NLP, CV, RL, or other domains WITHOUT LLM Agent, self-evolution, or auto research angle.
- Self-evolving / self-improving systems applied to non-RecSys domains (medical, robotics, gaming, education, etc.).
- Pure theoretical papers, surveys, benchmarks, evaluation papers without novel method.
- General retrieval, ANNS, embedding, quantization, tokenizer, multimodal fusion papers WITHOUT explicit connection to the three focus areas.
- Federated learning, privacy, security, fairness, fingerprint, hallucination, content generation, AIGC.

# Scoring Guidelines (Be Conservative)
- 8-10: Title EXPLICITLY mentions LLM Agent for recommendation, OR self-evolving RecSys/Search/Ads system with clear practical application, OR AutoML specifically for RecSys/Search/Ads.
- 5-7: Title implies potential application to the focus areas but connection is not explicit. Adjacent enabling technique that COULD be applied.
- 1-4: Title does NOT clearly fall into any of the three focus areas. **DEFAULT TO THIS RANGE when unsure.**

# Task
Based ONLY on the paper's title, provide a quick evaluation.
1. **Academic Translation**: Translate the title into professional Chinese, prioritizing accurate technical terms.
2. **Relevance Score (1-10)**: Follow the scoring guidelines above. BE STRICT.
3. **Reasoning**: A 2-3 sentence explanation. You MUST explicitly state which specific focus area this paper belongs to, and why. If rejecting, state clearly what is missing.

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
You are a strict paper reviewer. Your primary task is to REJECT papers that do not have a clear, explicit connection to the narrow focus areas. Read the abstract carefully — if the connection is vague or implied rather than stated, score low.

# My Current Focus (Narrow & Strict)

1. **LLM Agent for Recommendation Systems ONLY**:
   - LLM-based agents applied to RECOMMENDATION.
   - Agent-driven user modeling, conversational recommendation, agent-based retrieval/ranking/reranking for recommender systems, multi-agent collaboration for recommendation.
   - **REJECT if**: The paper is about LLM Agents in general (task planning, tool use, code generation, dialogue), OR about agents for search/ads without a clear recommendation angle.

2. **Self-Evolving Systems in RecSys/Search/Ads (Practical Only)**:
   - Systems that autonomously improve via feedback loops, online learning, LLM-directed self-evolution, iterative self-improvement, or model self-correction, WITH concrete application in recommendation, search, or advertising.
   - **REJECT if**: Pure theoretical framework, OR applied to non-RecSys/Search/Ads domains (robotics, CV, NLP, games, medical, education, etc.), OR no practical deployment evidence.

3. **Auto Research / AutoML for RecSys/Search/Ads**:
   - Automated feature engineering, hyperparameter optimization, NAS, automated experimentation, model design, or workflow automation SPECIFICALLY for RecSys/Search/Ads.
   - **REJECT if**: General AutoML, general NAS, or applied to other domains.

# Must Reject (Score ≤ 3)
- Papers that are ONLY about LLMs, Agents, or Multi-Agent Systems WITHOUT explicit RecSys/Search/Ads application.
- Papers about search, ads, NLP, CV, RL that do NOT involve LLM Agent, self-evolution, or auto research.
- Self-evolving systems in robotics, gaming, medical, education, or other non-RecSys domains.
- Pure surveys, benchmarks, evaluation-only papers without novel method.
- General retrieval, ANNS, embedding, quantization, tokenizer, multimodal fusion papers WITHOUT explicit connection to the focus areas.

# Task
Based on the paper's **Title** and **Abstract**, provide a comprehensive analysis.
1.  **Relevance Score (1-10)**: Re-evaluate strictly based on the abstract. BE CONSERVATIVE — when the connection to the focus areas is vague, score ≤ 4.
  - 8-10: Abstract explicitly describes LLM Agent for recommendation, OR self-evolving system with RecSys/Search/Ads deployment, OR AutoML specifically for RecSys/Search/Ads.
  - 5-7: Abstract implies potential application but does not explicitly target the focus areas.
  - 1-4: Abstract does not establish a clear connection to the three focus areas.
2.  **Reasoning**: A 1-2 sentence explanation in Chinese. State clearly which focus area applies and whether the connection is explicit or vague.
3.  **Summary**: Generate a 1-2 sentence, ultra-high-density Chinese summary focusing solely on the paper's core idea.
    1.  **Topic:** What core problem is the paper studying or solving?
    2.  **Core Idea:** What is its core method, key idea, or main analytical conclusion?
    **STRICTLY IGNORE EXPERIMENTAL RESULTS:** Do not include SOTA, metrics, or numerical improvements.
    **FOCUS ON THE "IDEA":** Convey the core idea, not experimental achievements.

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