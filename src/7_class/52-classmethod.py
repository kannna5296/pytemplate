# 以下、classmethod使うVer


import os
import random
import shutil
from collections.abc import Generator
from pathlib import Path
from threading import Thread
from typing import Self


class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(data_dir: str) -> Generator:
        raise NotImplementedError


class PathInputData(GenericInputData):
    """pathをもらって、そのpathにあるファイルをreadで読み込む"""

    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self) -> str:
        with open(self.path) as f:
            return f.read()

    @classmethod
    def generate_inputs(cls, config) -> Generator:
        """ディレクトリパスをもらって、その中のファイルを読み込んだデータ(自分自身)を返すGeneratorを返す"""
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))

class PathInputZipData(GenericInputData):
    """pathをもらって、そのpathにあるファイルをreadで読み込む"""

    def __init__(self, path):
        super.__init__()
        self.path = path

    def read(self):
        pass  # 本当はここにzip解凍関数を書いたりする

    def generate_inputs(data_dir: str) -> Generator:
        pass

class GenericWorker:
    def __init__(self, input_data: GenericInputData):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class: GenericInputData, config) -> list[Self]:
        """読み込んだデータのリストをもらって、それぞれのデータに対して行数をカウントするWorkerのリストを返す"""
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other: GenericWorker):
        """他のWorkerの結果をもらって、まとめる(畳み込み)"""
        self.result += other.result

    # 実装しなくて良い。汎用クラスで実装しているから
    # @classmethod
    # def create_workers(cls, input_class: InputData, config) -> list[Self]:
    #     """読み込んだデータのリストをもらって、それぞれのデータに対して行数をカウントするWorkerのリストを返す"""
    #     workers = []
    #     for input_data in input_class.generate_inputs(config):
    #         workers.append(cls(input_data))
    #     return workers


class StringCountWorker(GenericWorker):
    def map(self):
        self.data = self.input_data.read()
        self.result = "a"  # 本当はなんか文字列を数える関数を作る

    def reduce(self, other: GenericWorker):
        """他のWorkerの結果をもらって、まとめる(畳み込み)"""
        self.result += other.result

    # 実装しなくて良い。汎用クラスで実装しているから
    # @classmethod
    # def create_workers(cls, input_class: InputData, config) -> list[Self]:
    #     """読み込んだデータのリストをもらって、それぞれのデータに対して行数をカウントするWorkerのリストを返す"""
    #     workers = []
    #     for input_data in input_class.generate_inputs(config):
    #         workers.append(cls(input_data))
    #     return workers


def execute(workers: list[GenericWorker]):
    """Workerのリストをもらって、それぞれを別Threadで並列処理させる.結果を最終的にまとめて、返す"""
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()  # 作ったスレッドの処理が終わるまで、メインスレッドに待たせる

    # 最初のワーカーに処理をまとめてリターンする
    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(worker_class: GenericWorker, input_class: GenericInputData,  config):
    """inputの読み込み、ワーカーの作成、スレッドでの実行を順に行う"""
    workers = worker_class.create_workers(input_class, config)
    return execute(workers=workers)


def write_test_files(tmpdir):
    """行数カウントプログラムのテスト用ファイルを作成する。行数は作成ごとにランダム"""
    path = Path(tmpdir)
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), "w") as f:
            f.write("\n" * random.randint(0, 100))


tmpdir = "src/7_class/test_inputs_classmethod"
write_test_files(tmpdir)
config = {"data_dir": tmpdir}
result = mapreduce(LineCountWorker, PathInputData, config) #実装方法を変えたいときは、具象クラスを作ってここを変えるだけで良い
print(f"行数カウント: {result}")
