import ui
import json

#ファイルの読み込み
with open("data.txt", mode="w") as json_file:
    json_file.write("こんにちは\n")
    json_file.write("私は人間ですか?")
