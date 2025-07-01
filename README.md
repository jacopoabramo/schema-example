# Example JSON schema generation

Small example on how to generate JSON documents from `pydantic` and base schemas.

These are demonstration scripts on how to convert the existing openUC2 REST-API from pure JSON to schemas for better dataflow management.
The script depends on [`datamodel-code-generator`](https://koxudaxi.github.io/datamodel-code-generator/) and [`pydantic`](https://docs.pydantic.dev/latest/).

## Installation

Clone the repository:

```
git clone https://github.com/jacopoabramo/schema-example
```

Create and activate a virtual environment

```
python -m venv
.venv\Scripts\activate
```

In the active environment, install the dependencies:

```
pip install datamodel-code-generator pydantic
```

## Usage

There are two main scritps:

- `generate.py`: generates a bundle of `pydantic.BaseModel` from the JSON files in the `json` folder
  - Each generated python file will have the same name as the original JSON file
  - Generated models will be stored in the `models` folder
    - i.e. `json\motor_request.json` -> `models\motor_request.py`
- `evalute.py`: a demonstration script using the contents of `models\motor_request.py` that will
  - generate the equivalent JSON __schema__ in the `schema` folder under the same original filename
  - demonstrate how to create JSON objects directly from the generated models