# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os

import get_data
import text_preparation

import warnings
warnings.filterwarnings('ignore')

test_text = "Hi, I want to make pasta with tomato sauce. Can you give me a recipe for this?"


embedded_text = text_preparation.get_openai_embedding(text=test_text, text_type="query")
print(f"Here is a sample: {embedded_text[:5]}... ")


# Get the absolute path by joining the current directory with the relative path
current_directory = os.path.dirname(os.path.abspath(__file__))

# The relative path from the current location to the target file
html_relative_path = "./data_files/Alice's Adventures in Wonderland -- Chapter I.html"
html_file_path = os.path.join(current_directory, html_relative_path)

txt_relative_path = "./data_files/alice_in_wonderland.txt"
txt_file_path = os.path.join(current_directory, txt_relative_path)

csv_relative_path = "./data_files/2021-survey_results_public.csv"
csv_file_path = os.path.join(current_directory, csv_relative_path)

pdf_relative_path = "./data_files/Chapter I_ Down the Rabbit-Hole - Alice-in-Wonderland.pdf"
pdf_file_path = os.path.join(current_directory, pdf_relative_path)


doc = get_data.read_txt_file(txt_file_path)
chunks = text_preparation.split_docs_recursively(docs=doc)
print(len(chunks))
for chunk in chunks:
    print(len(chunk.page_content))

docs = get_data.load_local_file(txt_file_path)
re_chunks = text_preparation.split_docs_recursively(docs=docs)
for chunk in re_chunks:
    print(len(chunk.page_content))

query = "what kind of food did alice eat?"
relevant_docs = text_preparation.extract_relevant_docs(text=query, docs=docs)
# print preview of relevant docs
print('\n\n'.join(doc.page_content[:200] for doc in relevant_docs))

embedding_list = text_preparation.get_openai_embedding_list(docs=relevant_docs)

