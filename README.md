# qr-code-kit 二维码生成与解析工具

[![PyPI version](https://img.shields.io/pypi/v/qr-code-kit)](https://pypi.org/project/qr-code-kit/)
[![Downloads](https://img.shields.io/pypi/dm/qr-code-kit)](https://pypi.org/project/qr-code-kit/)
[![License](https://img.shields.io/pypi/l/qr-code-kit)](https://github.com/BoiledSaltedDuck/qr-code-kit/blob/main/LICENSE)

> **Office Tools Kit 系列** — 用AI写代码，用工具提效。一行命令搞定日常办公与开发杂务。

## 安装

```bash
pip install qr-code-kit
```

## 用法

```bash
# 生成二维码
qr-code encode "https://example.com" myqr.png

# 解析二维码
qr-code decode qrcode.png

# 批量生成（从文本文件每行一条数据）
qr-code batch data.txt ./qrcodes/
```

## 功能

### 生成二维码 (encode)
- 支持任意文本/URL数据
- 自动纠错级别 H（最高）
- 圆角模块样式
- 可自定义颜色

### 解析二维码 (decode)
- 从图片中读取二维码内容
- 显示二维码类型和位置
- 需要安装 pyzbar

### 批量生成 (batch)
- 从文本文件读取多条数据
- 自动以内容命名文件
- 批量输出到指定目录

## 🧰 Office Tools Kit 系列工具

本工具属于 **Office Tools Kit 系列**，同类工具推荐：

| 工具 | 功能 | 安装 |
|------|------|------|
| [office-tools-kit](https://pypi.org/project/office-tools-kit/) | Excel合并拆分、PDF合并 | `pip install office-tools-kit` |
| [file-org-kit](https://pypi.org/project/file-org-kit/) | 文件智能分类整理 | `pip install file-org-kit` |
| [img-convert-kit](https://pypi.org/project/img-convert-kit/) | 图片格式批量转换 | `pip install img-convert-kit` |
| [img-resize-kit](https://pypi.org/project/img-resize-kit/) | 图片批量缩放与压缩 | `pip install img-resize-kit` |
| [json-tool-kit](https://pypi.org/project/json-tool-kit/) | JSON 文件处理 | `pip install json-tool-kit` |
| [markdown-kit](https://pypi.org/project/markdown-kit/) | Markdown 文档辅助 | `pip install markdown-kit` |
| [qr-code-kit](https://pypi.org/project/qr-code-kit/) | 二维码生成与解析 | `pip install qr-code-kit` |
| [text-clean-kit](https://pypi.org/project/text-clean-kit/) | 文本文件清洗处理 | `pip install text-clean-kit` |
| [unit-convert-kit](https://pypi.org/project/unit-convert-kit/) | 单位换算 | `pip install unit-convert-kit` |

> 📚 更多工具请访问 [BoiledSaltedDuck 工具主页](https://boiledsaltedduck.github.io/)

## 支持

如果 qr-code-kit 帮到了您，欢迎打赏支持：

```
USDT (TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa
```

您的支持是开源项目持续发展的动力 ❤️
