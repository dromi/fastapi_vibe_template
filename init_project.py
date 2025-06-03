#!/usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Initialize a new FastAPI project from template')
    parser.add_argument('--name', type=str, help='Name of the new project')
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Get the current directory (template directory)
    template_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    parent_dir = template_dir.parent
    
    # If project name wasn't provided as an argument, ask for it
    project_name = args.name
    if not project_name:
        project_name = input("Enter new project name: ").strip()
    
    if not project_name:
        print("Error: Project name cannot be empty")
        sys.exit(1)
    
    # Create the target directory path (sibling to current directory)
    target_dir = parent_dir / project_name
    
    # Check if the target directory already exists
    if target_dir.exists():
        overwrite = input(f"Directory {target_dir} already exists. Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Aborting.")
            sys.exit(1)
        shutil.rmtree(target_dir)
    
    # Create the target directory
    target_dir.mkdir(exist_ok=True)
    
    print(f"Creating new project in {target_dir}")
    
    # Define directories and files to exclude
    exclude = [
        '.git',
        '.git/',
        '__pycache__',
        '*.pyc',
        '.DS_Store',
        'init_project.py',  # Don't copy this script itself
        'TODO.md'
    ]
    
    # Copy files and directories
    for item in template_dir.glob('*'):
        item_name = item.name
        
        # Skip excluded items
        if item_name in exclude or any(item.match(pattern) for pattern in exclude):
            print(f"Skipping {item_name}")
            continue
        
        target_path = target_dir / item_name
        
        if item.is_dir():
            print(f"Copying directory {item_name}...")
            shutil.copytree(item, target_path, ignore=shutil.ignore_patterns(*exclude))
        else:
            print(f"Copying file {item_name}...")
            shutil.copy2(item, target_path)
    
    # Create a new README.md with project name
    print("Creating new README.md...")
    readme_content = f"# {project_name}\n\nThis project was created from the FastAPI Vibe Template. Update this README with your project details."
    with open(target_dir / "README.md", 'w') as f:
        f.write(readme_content)
    
    # Update pyproject.toml with the new project name
    print("Updating pyproject.toml...")
    pyproject_path = target_dir / "pyproject.toml"
    if pyproject_path.exists():
        with open(pyproject_path, 'r') as f:
            pyproject_content = f.read()
        
        # Replace the project name
        pyproject_content = pyproject_content.replace('name = "fastapi-vibe-template"', f'name = "{project_name}"')
        
        with open(pyproject_path, 'w') as f:
            f.write(pyproject_content)
    
    print(f"\nProject {project_name} has been created successfully!")
    print(f"Location: {target_dir}")
    print("\nNext steps:")
    print("1. Navigate to your project directory:")
    print(f"   cd {target_dir}")
    print("2. Install with poetry")
    print("3. Configure your .env file based on .env.example")
    print("4. Run your FastAPI application with docker compose")

if __name__ == "__main__":
    main()
