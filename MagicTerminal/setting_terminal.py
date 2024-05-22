import subprocess
import yaml
import os

# terminal, git, npmの設定
def set_setting_windows(item, content):
    os.environ[item] = content

def set_setting_git(item, content):
    command = f"git config --global {item} {content}"
    subprocess.call(command, shell=True)

def set_setting_npm(item, content):
    command = f"call npm -g config set {item} {content}"
    subprocess.call(command, shell=True)

# terminal, git, npmの解除
def unset_setting_window(item):
    os.environ.pop(item, None)

def unset_setting_git(item):
    command = f"git config --global --unset {item}"
    subprocess.call(command, shell=True)

def unset_setting_npm(item):
    command = f"call npm -g config delete {item}"
    subprocess.call(command, shell=True)

# ターミナルの起動
def launch_terminal(terminal:str="cmd"):
    if terminal == "wt":
        command = "wt.exe"

    else:
        command = "start cmd.exe"

    subprocess.Popen(command, shell=True)

# yamlの操作
def set_yaml():
    with open('setting.yaml', 'r') as file:
        yaml_data = yaml.load(file, Loader=yaml.FullLoader)
        for i in range( len(yaml_data["setting_windows"]) ):
            set_setting_windows(yaml_data["setting_windows"][i]["item"], yaml_data["setting_windows"][i]["content"])

        for i in range( len(yaml_data["setting_git"]) ):
            set_setting_git(yaml_data["setting_git"][i]["item"], yaml_data["setting_git"][i]["content"])

        for i in range( len(yaml_data["setting_npm"]) ):
            set_setting_npm(yaml_data["setting_npm"][i]["item"], yaml_data["setting_npm"][i]["content"])
        
def unset_yaml():
    with open('setting.yaml', 'r') as file:
        yaml_data = yaml.load(file, Loader=yaml.FullLoader)
        for i in range( len(yaml_data["setting_windows"]) ):
            unset_setting_window(yaml_data["setting_windows"][i]["item"])

        for i in range( len(yaml_data["setting_git"]) ):
            unset_setting_git(yaml_data["setting_git"][i]["item"])

        for i in range( len(yaml_data["setting_npm"]) ):
            unset_setting_npm(yaml_data["setting_npm"][i]["item"])

set_yaml()
launch_terminal()
input("Press Enter to disable proxy and exit.")
unset_yaml()