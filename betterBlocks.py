from docutils.parsers.rst import Directive, directives
from docutils import nodes

# 1. Define the new "node" (the HTML element)
class github_box_node(nodes.Element):
    pass

# 2. Define the new directive ".. github::"
class GitHubBox(Directive):
    has_content = True  # It has content inside it

    def run(self):
        # This parses the content you write inside the directive
        content_node = nodes.container()
        self.state.nested_parse(self.content, self.options.get('content_offset', 0), content_node)
        
        # Create our new node and pass the content to it
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

# 4. The "setup" function to register everything with Sphinx
def setup(app):
    # Register our new node and directive
    app.add_node(github_box_node, html=(visit_github_box_node, depart_github_box_node))
    app.add_directive("github", GitHubBox)
    
    # This is the new, cleaner way to add our CSS file
    app.add_css_file("custom.css")
    
    return {'version': '0.1', 'parallel_read_safe': True}