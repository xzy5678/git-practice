"""我的第一个用 Git 管理的 Python 脚本。

试着改点东西，然后用 git status / git add / git commit 把它记录下来。
"""


def greet(name: str) -> str:
    return f"你好，{name}！"


def main() -> None:
    print(greet("练习"))
    print("这个文件正被 Git 管理着。")


if __name__ == "__main__":
    main()
