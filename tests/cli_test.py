"""Test the CLI commands"""
import os
from click.testing import CliRunner

from dragonfly_designbuilder.cli.translate import model_to_dsbxml_cli


def test_model_to_dsbxml():
    runner = CliRunner()
    input_df_model = './tests/assets/model_complete_simple.dfjson'
    project_info = './tests/assets/project_info.json'
    out_file = './tests/assets/model_complete_simple.xml'

    in_args = [input_df_model, '--project-info', project_info, '--output-file', out_file]
    result = runner.invoke(model_to_dsbxml_cli, in_args)

    assert result.exit_code == 0
    assert os.path.isfile(out_file)
    os.remove(out_file)
