import models.motor_request as models
import json
from pathlib import Path

if __name__ == "__main__":
    # write the JSON schema in the
    # .\schema directory
    schema_path = Path(__file__).parent / "schema"
    schema_path.mkdir(exist_ok=True)
    with open(schema_path / "motor_request.json", "w") as f:
        f.write(json.dumps(models.Model.model_json_schema(), indent=2))
    print(f"JSON schema written to {schema_path / 'motor_request.json'}")
    print("\n#### Example JSON generated from the Model ####")
    model_instance = models.Model(
        task="move",
        qid=1,
        motor=models.Motor(
            steppers=[
                models.Stepper(
                    stepperid=1,
                    position=100,
                    speed=50,
                    isabs=1,
                    isaccel=0,
                    accel=10
                )
            ]
        )
    )
    print(model_instance.model_dump_json(indent=2))
    print("\n#### Model Instance JSON Schema ####")
    
