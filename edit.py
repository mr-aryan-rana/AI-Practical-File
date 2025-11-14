import os
from docx import Document

def replace_in_py_files(file_path, old_text, new_text):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content.replace(old_text, new_text)

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated PY: {file_path}")

    except Exception as e:
        print(f"Error processing PY {file_path}: {e}")

def replace_in_docx_files(file_path, old_text, new_text):
    try:
        doc = Document(file_path)

        changed = False
        for para in doc.paragraphs:
            if old_text in para.text:
                para.text = para.text.replace(old_text, new_text)
                changed = True

        if changed:
            doc.save(file_path)
            print(f"Updated DOCX: {file_path}")

    except Exception as e:
        print(f"Error processing DOCX {file_path}: {e}")

def replace_in_files(base_path, old_text, new_text):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)

            if file.endswith(".py"):
                replace_in_py_files(file_path, old_text, new_text)

            elif file.endswith(".docx"):
                replace_in_docx_files(file_path, old_text, new_text)


if __name__ == "__main__":
    base_dir = "."  # current directory

    old_value = input("Enter the text you want to replace: ").strip()
    new_value = input("Enter the new text: ").strip()

    replace_in_files(base_dir, old_value, new_value)
    print("Done.")
