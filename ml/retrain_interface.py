import os

def get_command(images_path, module_url, model_path, model_name):
    pass
    # return ("python retrain.py \\" +
    #     "--tfhub_module test_url \\" +
    #     "--image_dir test_dir \\" +
    #     "--bottleneck_dir ./model/bottleneck \\" +
    #     "--output_graph ./model/model_name.pb \\" +
    #     "--output_labels ./model/model_name_labels.txt \\" +
    #     "--intermediate_output_graphs_dir ./model/intermediate_graph/ \\" +
    #     "--summaries_dir ./model/retrain_logs \\" +
    #     "'--saved_model_dir' ./model/exported_graph")

def run_bash_command(command):
    os.system(command)
