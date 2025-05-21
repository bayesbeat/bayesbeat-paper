"""Script to collate results into the final directory structure."""
import click
import yaml
import pathlib
import re
import shutil


@click.command()
@click.argument(
    "yaml_file",
)
@click.option(
    "--output-dir",
    default=".",
    type=pathlib.Path,
    help="Directory to save the collated results.",
)
@click.option(
    "--symlink",
    is_flag=True,
    help="Symlink the results instead of copying them.",
)
@click.option(
    "--flatten",
    is_flag=True,
    help="Flatten the directory structure.",
)
def collate_results(yaml_file, output_dir, symlink, flatten):

    with open(yaml_file, "r") as file:
        mapping = yaml.safe_load(file)
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Collating results into {output_dir}")
    for key, analyses in mapping.items():
        if not flatten:
            output_path = output_dir / key.replace(" ", "_")
            output_path.mkdir(parents=True, exist_ok=True)
        print(f"Collating results for: {key}")
        for analysis in analyses:
            base_path = pathlib.Path(analysis.get("path"))
            original_analysis_path = base_path / "analysis"
            result_files = list(original_analysis_path.glob("**/result.hdf5"))
            analysis_name = analysis.get("name").replace(" ", "_")
            if not flatten:
                new_path = output_path / analysis_name
                new_path.mkdir(parents=True, exist_ok=True)
            for result_file in result_files:
                result_file = result_file.resolve()
                match = re.search(r'index_(\d+)', str(result_file))
                if match:
                    index = int(match.group(1))
                else:
                    RuntimeError(f"Could not find index in {result_file}")
                if flatten:
                    new_file_name = pathlib.Path(f"{key.replace(" ", "_")}_{analysis_name}_result_ringdown_{index}.hdf5")
                    new_file_path = output_dir / new_file_name
                else:
                    new_file_name = f"result_ringdown_{index}.hdf5"
                    new_file_path = new_path / new_file_name
                if symlink:
                    new_file_path.symlink_to(result_file)
                else:
                    shutil.copy2(result_file, new_file_path)


if __name__ == "__main__":
    collate_results()
