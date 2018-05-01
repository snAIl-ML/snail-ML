from retrain_interface import get_command, run_command

class MyOutput(object):
    def __init__(self):
        self.data = []

    def write(self, s):
        self.data.append(s)

    def __str__(self):
        return "".join(self.data)

def test_get_command_generates_command_string_properly():
    images_path = "test_dir"
    module_url = "test_url"
    model_path = "./model"
    model_name = "model_name"
    command_string = get_command(images_path, module_url, model_path)
    expected_return = ("python retrain.py \\" +
        "--tfhub_module test_url \\" +
        "--image_dir test_dir \\" +
        "--bottleneck_dir ./model/bottleneck \\" +
        "--output_graph ./model/model_name.pb \\" +
        "--output_labels ./model/model_name_labels.txt \\" +
        "--intermediate_output_graphs_dir ./model/intermediate_graph/ \\" +
        "--summaries_dir ./model/retrain_logs \\" +
        "'--saved_model_dir' ./model/exported_graph")
    assert(command_string) == expected_return

def test_run_command_runs_command():
    stdout_org = sys.stdout
    my_stdout = MyOutput()
    try:
        sys.stdout = my_stdout
        run_command("echo 'print_this'")
    finally:
        sys.stdout = stdout_org

    assert(str(my_stdout)) == "print this"
