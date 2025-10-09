import pytest
import sys
from unittest.mock import patch
from pathlib import Path

# 学び
# capsys.readouterr()は、標準出力のテスト用のやつ

# srcディレクトリをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from arg.arge import main


class TestArgeMain:
    """arge.pyのmain関数のテスト"""

    def test_single_file_argument(self, capsys):
        """単一ファイルを引数として渡した場合のテスト"""
        test_args = ['arge.py', 'file1.csv']

        with patch.object(sys, 'argv', test_args):
            main()

        captured = capsys.readouterr()
        assert 'file1.csv' in captured.out

        assert captured.out.strip() == "['file1.csv']"

    def test_multiple_files_argument(self, capsys):
        """複数ファイルを引数として渡した場合のテスト"""
        test_args = ['arge.py', 'file1.csv', 'file2.csv', 'file3.csv']

        with patch.object(sys, 'argv', test_args):
            main()

        captured = capsys.readouterr() # 関数を作るやつ
        assert 'file1.csv' in captured.out
        assert 'file2.csv' in captured.out
        assert 'file3.csv' in captured.out
        assert captured.out.strip() == "['file1.csv', 'file2.csv', 'file3.csv']"

    def test_relative_path_argument(self, capsys):
        """相対パスを引数として渡した場合のテスト"""
        test_args = ['arge.py', 'data/input/file.csv', '../output/result.csv']

        with patch.object(sys, 'argv', test_args):
            main()

        captured = capsys.readouterr()
        assert 'data/input/file.csv' in captured.out
        assert '../output/result.csv' in captured.out

    def test_no_arguments_raises_error(self):
        """引数なしで実行した場合にエラーが発生することを確認"""
        test_args = ['arge.py']

        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                main()

            # argparseはエラー時にexit code 2を返す
            assert exc_info.value.code == 2

