import os
# Import the markdown2 library and abort for error handling
from flask import Flask, render_template, abort, url_for, redirect
import markdown2

# --- Configuration ---
ROOT_BROWSABLE_DIR_NAME = "."
IGNORE_ITEMS = [".git", ".vscode", "__pycache__", "venv", ".venv", "node_modules", "server.py", "index.html", "README.md"] 
# --- End Configuration ---

# --- Helper Functions ---
def format_display_name(name: str) -> str:
    """Formats a filename or directory name for display (removes .md, replaces underscores/dashes, title cases)."""
    if name.lower().endswith(".md"):
        name = name[:-3]
    return name.replace("_", " ").replace("-", " ").title()

def generate_breadcrumbs(relative_path_str: str):
    """
    Generates breadcrumbs from a relative path string.
    Example: "foo/bar" -> [{'name': 'Home', 'path': ''}, {'name': 'Foo', 'path': 'foo'}, {'name': 'Bar', 'path': 'foo/bar'}]
    """
    breadcrumbs = [{'name': 'Home', 'path': ''}] # Link to root browse page
    if not relative_path_str:
        return breadcrumbs

    parts = relative_path_str.split('/')
    current_path_so_far = []
    for part in parts:
        current_path_so_far.append(part)
        breadcrumbs.append({
            'name': format_display_name(part),
            'path': '/'.join(current_path_so_far)
        })
    return breadcrumbs

# --- Global Setup ---
script_dir = os.path.dirname(os.path.abspath(__file__))
# base_serve_path is the absolute path to the root directory we are allowed to serve from.
base_serve_path = os.path.abspath(os.path.join(script_dir, ROOT_BROWSABLE_DIR_NAME))

if __name__ == "__main__":
    if not os.path.isdir(base_serve_path):
        print(f"Error: The root browsable directory '{ROOT_BROWSABLE_DIR_NAME}' was not found at '{base_serve_path}'.")
        exit(1)

    app = Flask(__name__, template_folder='.')
    print(f"Serving content from: {base_serve_path}")

    # --- Routes ---
    @app.route("/")
    @app.route('/browse/')
    @app.route('/browse/<path:sub_path>')
    def browse_directory(sub_path=""):
        """Handles listing contents of a directory."""
        current_relative_path = sub_path.strip('/')
        current_absolute_path = os.path.abspath(os.path.join(base_serve_path, current_relative_path))

        # Security check: Ensure the requested path is within the base_serve_path
        if not current_absolute_path.startswith(base_serve_path):
            abort(403, "Access forbidden: Path is outside the allowed serving directory.")
        
        if not os.path.isdir(current_absolute_path):
            # If it's a file, try to view it if it's markdown
            if os.path.isfile(current_absolute_path) and current_relative_path.lower().endswith(".md"):
                return redirect(url_for('view_file', file_rel_path=current_relative_path))
            abort(404, f"Directory not found: {format_display_name(current_relative_path)}")

        items = []
        try:
            for item_name in sorted(os.listdir(current_absolute_path)):
                if item_name in IGNORE_ITEMS:
                    continue

                item_abs_path = os.path.join(current_absolute_path, item_name)
                # Ensure relative_path always uses '/' for URL consistency
                item_rel_path_from_root = os.path.relpath(item_abs_path, base_serve_path).replace(os.sep, '/')
                
                item_type = 'dir' if os.path.isdir(item_abs_path) else 'file'
                is_md = item_name.lower().endswith(".md")

                items.append({
                    'name': item_name, 
                    'display_name': format_display_name(item_name),
                    'type': item_type,
                    'is_md': is_md,
                    'relative_path': item_rel_path_from_root 
                })
            
            breadcrumbs_list = generate_breadcrumbs(current_relative_path)
            # Determine display name for the current path/directory
            current_dir_display_name = "Home" # Default for root
            if current_relative_path:
                current_dir_display_name = format_display_name(os.path.basename(current_relative_path))

            return render_template('index.html', 
                                   items=items, 
                                   current_path_display=current_dir_display_name,
                                   breadcrumbs=breadcrumbs_list,
                                   is_listing=True)

        except Exception as e:
            print(f"Error listing directory '{current_absolute_path}': {e}")
            abort(500, "Error listing directory contents.")


    @app.route('/view/<path:file_rel_path>')
    def view_file(file_rel_path):
        """Handles viewing a Markdown file."""
        current_relative_path = file_rel_path.strip('/')
        
        if ".." in current_relative_path.split('/'): # Basic check
             abort(400, "Invalid path component.")

        if not current_relative_path.lower().endswith(".md"):
            abort(404, "File is not a Markdown file or path is incorrect.")

        file_absolute_path = os.path.abspath(os.path.join(base_serve_path, current_relative_path))

        # Security check: Ensure the requested path is within the base_serve_path
        if not file_absolute_path.startswith(base_serve_path):
            abort(403, "Access forbidden: File is outside the allowed serving directory.")

        if not os.path.isfile(file_absolute_path):
            abort(404, f"Markdown file not found: {format_display_name(current_relative_path)}")

        try:
            with open(file_absolute_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            html_content = markdown2.markdown(md_content, extras=["fenced-code-blocks", "tables", "strike", "footnotes"])
            
            # Generate breadcrumbs for the *directory* containing the file
            parent_dir_relative_path = os.path.dirname(current_relative_path)
            if parent_dir_relative_path == '.': # Handle files in root
                parent_dir_relative_path = ''
            breadcrumbs_list = generate_breadcrumbs(parent_dir_relative_path)
            
            return render_template('index.html', 
                                   content=html_content, 
                                   file_display_name=format_display_name(os.path.basename(current_relative_path)),
                                   breadcrumbs=breadcrumbs_list,
                                   is_listing=False)
        except Exception as e:
            print(f"Error processing file '{file_absolute_path}': {e}")
            abort(500, "Error processing file.")
            
    app.run(port=8080, debug=True)