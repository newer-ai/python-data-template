# python数据实验项目模板

用于做数据分析、算法、机器学习等实验的python模板。

## 模板要点

- 📦 [uv](https://docs.astral.sh/uv/) 包管理
- 📓 [Jupyter](https://jupyter.org/) 管理笔记
- [ty](https://docs.astral.sh/ty/) 类型检查和 LSP（vscode）
- [ruff](https://docs.astral.sh/ruff/) 格式化、代码静态检查
- [pytest](https://docs.pytest.org/en/stable/) 单元测试

## 项目结构

```text
ROOT_PATH/
|-- notebooks       ------ 笔记
|-- src
    |-- package_a    ------ 包a
        |-- __init__.py
    |-- utils        ------ utils 包
        |-- __init__.py
|-- scripts         ------ 脚本，如运行模型训练的脚本、数据处理脚本
|-- tests           ------ 单元测试
    |__ test_sample.py
|-- pixi.toml
```

## 常用命令行

### 初始化项目

```shell
uv sync
```

### 检查项目

```shell
uv run ruff check
uv run ruff format
uv run ty check
```
