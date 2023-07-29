# -*- coding: utf-8 -*-
# !/usr/bin/env python


"""This module is for running the search agent use case."""

import warnings
warnings.filterwarnings("ignore")

from langchain.agents import load_tools
from langchain.agents import initialize_agent

import connect, models


def run_search_agent(llm, text):
    tools = load_tools(["serpapi"])
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
    )
    response = agent.run(input=text)
    return response


if __name__ == "__main__":
    llm = models.set_openai_model(max_tokens=400)
    text = "How many rainy days are there in July in Allgäu area in Germany"
    response = run_search_agent(llm, text)
    print(response)
