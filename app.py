from flask import Flask, render_template, request
from openai import OpenAI
import os
import networkx as nx
import matplotlib.pyplot as plt

from graphviz import Digraph

import re
import ast

def extract_and_execute_function(response):
    # Regular expression to capture the function
    function_pattern = re.compile(r'def create_cfg_from_description\(description\):.*?return G', re.DOTALL)

    # Search for the function in the response
    function_match = function_pattern.search(response)

    # Extract the function code
    function_code = function_match.group(0) if function_match else None

    if not function_code:
        raise ValueError("Function definition not found in the response")

    # Execute the function code
    exec(function_code, globals())

    # The function is now available in the global namespace


def draw_graph(G):
    nx.draw_networkx(G, with_labels=True)
    plt.savefig("static/cfg.png")  # Save the graph as a PNG image
    plt.close()
    return "static/cfg.png"



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test-path', methods=['POST'])
def test_path():
    code = request.form['code']
    test_results = run_path_testing(code)

    # Use the new function to extract and execute the GPT-4 response
    extract_and_execute_function(test_results)

    # Assuming that the function create_cfg_from_description is now available
    # and you have a description to pass to it
    cfg_graph = create_cfg_from_description("Your description here")
    graph_image_path = draw_graph(cfg_graph)

    return render_template('index.html', test_results=test_results, graph_image=graph_image_path)


def run_path_testing(code):
    
    
    
    # Instantiate the OpenAI client
    client = OpenAI()

    # Make the API call
    response = client.chat.completions.create(
        model="gpt-4",#gpt-4
        messages=[
            {"role": "system", "content": "You are a helpful software tester working in a big tech company, you need to validate code given to you"},
            {"role": "user", "content": 
             f'''
              fill the blanks only to create a  control flow graph (given I am using networkx )(((
             def create_cfg_from_description(description):
                G = nx.DiGraph()

                #your code here 
             
                return G
             , give your response as G.add_node() G.add_edge() ))) 
              
               
                 for the following code : {code} '''},
            {"role": "user", "content": '''

                make the graph nice and add details to the nodes so they are understandable , make your max effort 
             

                WHAT IS THIS CODE TRYING TO ACHIVE ?
             
             '''}
        ]
    )

    # Extract the response
    if response.choices:
        #print(response.choices)
        return  response.choices[0].message.content
    else:
        return "No response from gpt-3.5-turbo"

if __name__ == '__main__':



    app.run()

