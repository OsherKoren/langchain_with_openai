# -*- coding: utf-8 -*-
# !/usr/bin/env python
import json
import re
from typing import List
from bs4 import BeautifulSoup
import requests
import models, prompts

import warnings
warnings.filterwarnings("ignore")

URLS = [
    "https://www.loveandlemons.com/vegan-ramen/",
    "https://www.loveandlemons.com/mushroom-broth/",
    "https://www.loveandlemons.com/broccolini/",
    ]


def parse_recipe(*, url: str) -> List[str]:
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    body = soup.find('body')
    pattern = re.compile(r'^wprm-recipe-container-')
    recipe_divs = body.find_all('div', id=pattern)
    # Access the contents of the recipe_div
    recipes = [recipe_div.text.strip() for recipe_div in recipe_divs if recipe_div.text.strip()]
    return recipes


def run_recipe_model(text: str):
    # prompt = prompts.setup_recipe_prompt(text)
    prompt = prompts.setup_parsed_prompt(text)
    recipe_model = models.set_openai_model(max_tokens=500)
    response = recipe_model(prompt)
    return response


if __name__ == '__main__':
    url = URLS[0]
    recipes = parse_recipe(url=url)
    fst_recipe = recipes[0]
    response = run_recipe_model(text=fst_recipe)
    print(response)
    file_name = url.split('/')[-2]
    # with open(f'WORKSPACE/{file_name}.json', 'w') as f:
    #     json.dump(response, f, indent=4)
