# -*- coding: utf-8 -*-
# !/usr/bin/env python

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


def set_openai_model(model_name: str = "gpt-3.5-turbo", temperature: float = 0.2, **kwargs)\
        -> OpenAI:
    model = OpenAI(
        model_name=model_name,
        temperature=temperature,
        max_tokens=kwargs.get("max_tokens", 4000),
    )
    return model


def set_openai_chat_model(model_name: str = "gpt-3.5-turbo", temperature: float = 0.2, **kwargs) -> ChatOpenAI:
    model = ChatOpenAI(
        model_name=model_name,
        temperature=temperature,
        max_tokens=kwargs.get("max_tokens", 4000),
    )
    return model


