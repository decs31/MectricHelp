import os
from markitdown import MarkItDown
import zipfile
import shutil



def list_docx_files(directory):
    return [f for f in os.listdir(directory) if f.lower().endswith('.docx') and os.path.isfile(os.path.join(directory, f))]

def extract_images_from_docx(docx_file, output_dir):
    images_dir = os.path.join(output_dir, os.path.splitext(os.path.basename(docx_file))[0])
    os.makedirs(images_dir, exist_ok=True)
    with zipfile.ZipFile(docx_file, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.startswith('word/media/'):
                filename = os.path.basename(file)
                if filename:
                    with zip_ref.open(file) as source, open(os.path.join(images_dir, filename), 'wb') as target:
                        shutil.copyfileobj(source, target)
    return images_dir

def convert_docx_to_md(docx_file, output_dir):
    md = MarkItDown(enable_plugins=False)
    md_file = os.path.splitext(docx_file)[0] + '.md'
    md_path = os.path.join(output_dir, md_file)
    md_content = md.convert(docx_file)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content.text_content)

def main():
    cwd = os.getcwd()
    print(f"Working directory: {cwd}")
    files = os.listdir(cwd)
    print("Files in directory:")
    for f in files:
        print(f)
    docx_files = list_docx_files(cwd)
    print("\nFound .docx files:")
    for docx in docx_files:
        print(docx)
        try:
            convert_docx_to_md(docx, cwd)
            print(f"Converted {docx} to markdown.")
            images_dir = extract_images_from_docx(docx, cwd)
            print(f"Extracted images to {images_dir}")
        except Exception as e:
            print(f"Failed to process {docx}: {e}")

if __name__ == "__main__":
    main()