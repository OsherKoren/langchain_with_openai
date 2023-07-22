# -*- coding: utf-8 -*-
# !/usr/bin/env python
from typing import Optional

import connect
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.schema import AIMessage, HumanMessage, SystemMessage


def setup_recipe_prompt(text: str) -> str:
    template = """
    Extract the recipe name, the ingredients and the instructions from the text delimited by triple backticks:
    ```{recipe}``` .
    Provide them in JSON format with the following keys:
    the recipe name as the main key, and then ingredients and instructions as the sub-keys.
    """
    prompt = PromptTemplate(input_variables=["recipe"], template=template)
    return prompt.format(recipe=text)


def setup_travel_agent_messages(text: str, location: str = "the Black Forest area in Germany") -> str:
    messages = [
        SystemMessage(content=f"""
        You are a helpful travel agent specialized in {location} who helps build itineraries.
        """),
        HumanMessage(content=text),
    ]
    return messages


def setup_parsed_prompt(text: str, response_schemas: Optional[ResponseSchema] = None) -> str:
    if response_schemas is None:
        response_schemas = [
            ResponseSchema(name="invalid_recipe", description="The recipe is not valid."),
            ResponseSchema(name="valid_recipe", description="The recipe is valid."),
        ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas=response_schemas)
    format_instructions = output_parser.get_format_instructions()
    template = """
    Extract the recipe name, the ingredients and the instructions from the text delimited by triple backticks:
    {format_instructions}

    ```{recipe}``` .
    """
    prompt = PromptTemplate(input_variables=["recipe"],
                            template=template,
                            partial_variables={"format_instructions": format_instructions})
    adj_prompt = prompt.format(recipe=text)
    return adj_prompt


def setup_location_template_prompt() -> str:
    template = """
    Your job is to come up with a classic dish from the area that the users suggests.
    The user text is delimited by triple backticks:
    ```{location}``` .
    Provide a short answer. 
    """
    prompt_template = PromptTemplate(input_variables=["location"], template=template)
    return prompt_template


def setup_meal_template_prompt() -> str:
    template = """
    Given a meal, give a short and simple recipe on how to make that dish at home.
    Give recipe name, the ingredients and the instructions from the text delimited by triple backticks:
    ```{meal}``` .
    Provide them in JSON format with the following keys:
    the recipe name as the main key, and then ingredients and instructions as the sub-keys.
    """
    prompt_template = PromptTemplate(input_variables=["meal"], template=template)
    return prompt_template


