# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""This module is for setting up agent tools"""
from pprint import pprint

from langchain import agents


all_tools = agents.get_all_tool_names()
pprint(all_tools)



