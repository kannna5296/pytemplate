# @classmethodをつけると、インスタンス化不要で、class.method的な呼び方ができる

# 何が嬉しいか
# インスタンス化が不要になって、設計しやすい

# 以下、classmethod使わないVer

import os
from pathlib import Path
import random
import shutil
from threading import Thread
from typing import Generator


class InputData:
    def read(self):
        raise NotImplementedError

class PathInputData(InputData):
    """pathをもらって、そのpathにあるファイルをreadで読み込む"""
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self) -> str:
        with open(self.path) as f:
            return f.read()

class PathInputZipData(InputData):
    """pathをもらって、そのpathにあるファイルをreadで読み込む"""
    def __init__(self, path):
        super.__init__()
        self.path = path

    def read(self):
        pass # 本当はここにzip解凍関数を書いたりする

class Worker:
    def __init__(self, input_data: InputData):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other: Worker):
        """他のWorkerの結果をもらって、まとめる(畳み込み)"""
        self.result += other.result

class StringCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = "a" #本当はなんか文字列を数える関数を作る

    def reduce(self, other: Worker):
        """他のWorkerの結果をもらって、まとめる(畳み込み)"""
        self.result += other.result

### 以下、上記クラスをまとめて実行可能人する


def generate_inputs(data_dir: str) -> Generator:
    """ディレクトリパスをもらって、その中のファイルを読み込んだデータを返すGeneratorを返す"""
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))

def create_workers(input_list: list[InputData]) -> list[Worker]:
    """読み込んだデータのリストをもらって、それぞれのデータに対して行数をカウントするWorkerのリストを返す"""
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

def execute(workers: list[Worker]):
    """Workerのリストをもらって、それぞれを別Threadで並列処理させる.結果を最終的にまとめて、返す"""
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join() #作ったスレッドの処理が終わるまで、メインスレッドに待たせる

    # 最初のワーカーに処理をまとめてリターンする
    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(data_dir):
    """inputの読み込み、ワーカーの作成、スレッドでの実行を順に行う"""
    inputs = generate_inputs(data_dir=data_dir)
    workers = create_workers(input_list=inputs)
    return execute(workers=workers)


def write_test_files(tmpdir):
    """行数カウントプログラムのテスト用ファイルを作成する。行数は作成ごとにランダム"""
    path = Path(tmpdir)
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), "w") as f:
            f.write("\n" * random.randint(0,100))

tmpdir = "src/7_class/test_inputs_non_classmethod"
write_test_files(tmpdir)
result = mapreduce(tmpdir)
print(f"行数カウント: {result}")
