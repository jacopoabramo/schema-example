from datamodel_code_generator import generate
from datamodel_code_generator import PythonVersion, InputFileType
from pathlib import Path

def generate_json_schema() -> None:
    """
    Generate Pydantic models from a JSON file.
    """
    # read the content of JSON files from the
    # .\json directory; dump the generated
    # pydantic models in the .\models directory
    input_path = Path(__file__).parent / "json"
    
    # check if the input directory exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input directory {input_path} does not exist.")
    output_path = Path(__file__).parent / "models"
    output_path.mkdir(exist_ok=True)
    for json_file in input_path.glob("*.json"):
        output_file = output_path / f"{json_file.stem}.py"
        generate(
            json_file,
            input_file_type=InputFileType.Json,
            target_python_version=PythonVersion.PY_310,
            output=output_file
        )
        print(f"Generated {output_file}")

if __name__ == "__main__":
    generate_json_schema()
    print("All JSON schemas have been generated successfully.")