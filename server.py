import os
# Import the markdown2 library and abort for error handling
from flask import Flask, render_template, abort, url_for
import markdown2

def remove_dash(str: str) -> str:
    return str.replace("_", " ").title()

if __name__ == "__main__":
    ROOT_DIR = "."
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, ROOT_DIR)


    app = Flask(__name__, template_folder='.')
    print(f"Serving books from root directory: {os.path.abspath(folder_path)}")

    @app.route("/")
    def index():
        books = []
        ignoreBooks = [".git"]
        try:
            for item_name in sorted(os.listdir(folder_path)):
                item_path = os.path.join(folder_path, item_name)
                if os.path.isdir(item_path):
                    books.append(item_name)
            
            for item in ignoreBooks:
                if item in books:
                    books.remove(item)
                        
            if not books:
                return render_template('index.html', books=[], no_books_message=f"No book subdirectories found in '{os.path.abspath(folder_path)}'. Please ensure subdirectories exist directly under {os.path.abspath(folder_path)}.")
            return render_template('index.html', books=books)
        except Exception as e:
            print(f"An error occurred while listing books: {e}")
            return render_template('index.html', error_message="Error listing books. Check server logs.")

    @app.route("/book/<string:book_name>/")
    def list_files_in_book(book_name):
        if '/' in book_name or '\\' in book_name: # Basic security for book_name
            abort(400, "Invalid book name.")

        book_actual_path = os.path.join(folder_path, book_name)

        if not os.path.isdir(book_actual_path):
            abort(404, f"Book '{book_name}' not found in '{os.path.abspath(folder_path)}'.")

        files_to_render = []

        try:
            for f_name in sorted(os.listdir(book_actual_path)):
                if f_name.endswith(".md") and os.path.isfile(os.path.join(book_actual_path, f_name)):
                    display_name = remove_dash(f_name[:-3]) # Remove .md extension before formatting
                    files_to_render.append({'id': f_name, 'name': display_name})
            
            if not files_to_render:
                return render_template('index.html', files=[], current_book_name=book_name, book_display_name=remove_dash(book_name), no_files_message=f"No Markdown files found in book '{remove_dash(book_name)}'.")
            
            return render_template('index.html', files=files_to_render, current_book_name=book_name, book_display_name=remove_dash(book_name))
        except Exception as e:
            print(f"An error occurred while listing files for book '{book_name}': {e}")
            return render_template('index.html', error_message=f"Error listing files for book '{book_name}'. Check server logs.", current_book_name=remove_dash(book_name))

    @app.route("/view/<string:book_name>/<string:filename>")
    def view_file(book_name, filename):
        # Basic security: ensure names are just names, not path components.
        if '/' in book_name or '\\' in book_name or '/' in filename or '\\' in filename:
            abort(400, "Invalid book or file name.")

        # Ensure it's an .md file we're trying to access
        if not filename.endswith(".md"):
            abort(404, f"File '{filename}' is not a Markdown file.")

        book_actual_path = os.path.join(folder_path, book_name)
        if not os.path.isdir(book_actual_path): # Check if book directory exists
            abort(404, f"Book '{book_name}' not found.")

        file_path = os.path.join(book_actual_path, filename)

        if not os.path.isfile(file_path):
            abort(404, f"Markdown file '{filename}' not found in book '{book_name}' at path '{os.path.abspath(file_path)}'.")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            html_content = markdown2.markdown(md_content, extras=["fenced-code-blocks", "tables", "strike"])
            return render_template('index.html', 
                                   content=html_content, 
                                   current_book_name=book_name, book_display_name=remove_dash(book_name),
                                   current_filename=filename, file_display_name=remove_dash(filename[:-3])
                                   )
        except Exception as e:
            print(f"Error reading or converting file {file_path}: {e}")
            abort(500, f"Error processing file '{filename}' in book '{book_name}'.")
            
    app.run(port=8080, debug=True)