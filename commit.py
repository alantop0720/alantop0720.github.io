from git import Repo


def auto_commit(repo_path, commit_message):
    try:
        # 初始化仓库对象
        repo = Repo(repo_path)

        # 添加所有更改到暂存区
        repo.git.add(all=True)

        # 提交更改
        repo.index.commit(commit_message)

        # 推送更改到远程仓库
        origin = repo.remote(name='origin')
        origin.push()

        print("提交成功！")
    except Exception as e:
        print(f"提交失败: {e}")


# 使用示例
repo_path = 'D:/alantop_dir/alantop_data/alantop_git/github'  # 替换为你的Git仓库路径
commit_message = '自动提交更改'  # 替换为你的提交信息
auto_commit(repo_path, commit_message)
