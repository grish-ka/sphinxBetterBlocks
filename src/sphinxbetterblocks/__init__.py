import os
from docutils.parsers.rst import Directive, directives
from docutils import nodes

# 1. Define the new "node" (the HTML element)
class github_box_node(nodes.Element):
    pass

# 2. Define the new directive ".. github::"
class GitHubBox(Directive):
    has_content = True  # It has content inside it

    def run(self):
        content_node = nodes.container()
        self.state.nested_parse(self.content, self.options.get('content_offset', 0), content_node)
        
        new_node = github_box_node()
        new_node += content_node
        return [new_node]

# 3. Define the HTML "visit" functions (what to render)
def visit_github_box_node(self, node):
    self.body.append('<div class="github-repo">\n')
    self.body.append('<div class="github-title">GitHub Repository</div>\n')
    self.body.append('<div class="github-content">\n')

def depart_github_box_node(self, node):
    self.body.append('</div>\n</div>\n')

# 4. This function runs when Sphinx starts
def add_static_path(app):
    # This is the path to our 'static' folder *inside* the package
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    # We add this path to the list of paths Sphinx will check
    app.config.html_static_path.append(static_path)

# 5. The "setup" function to register everything with Sphinx
def setup(app):
    # Register our new node and directive
    app.add_node(github_box_node, html=(visit_github_box_node, depart_github_box_node))
    app.add_directive("github", GitHubBox)
    
    # Tell Sphinx to load our CSS file
    app.add_css_file("custom.css")
    
    # Connect our function to the 'builder-inited' event
    app.connect('builder-inited', add_static_path)
    
    return {'version': '0.1', 'parallel_read_safe': True}