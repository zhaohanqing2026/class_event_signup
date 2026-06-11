# 班级活动报名与统计网页

这是第15周课堂使用的 Flask 动态网页协作案例。

## 本地运行

在 Windows PowerShell 中进入项目根目录后执行：

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

如果 `python` 不可用，改用：

```powershell
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
py app.py
```

打开浏览器访问：

```text
http://127.0.0.1:5000
```

## 五人协作分工

| 角色 | 分支名 | 修改文件 | 网页可见效果 |
|---|---|---|---|
| 组长 | main | README.md、Vercel 设置 | GitHub 仓库和线上网址 |
| 组员 A | member-a-event-info | data/event_info.py | 首页标题、活动说明、协作提示变化 |
| 组员 B | member-b-options | data/options.py | 小组选项和活动方向变化 |
| 组员 C | member-c-page-text | data/page_text.py | 表单提示和结果页标题变化 |
| 组员 D | member-d-sample-data | data/registrations.py | 默认报名记录、统计人数和列表变化 |

## Vercel 部署

仓库合并完成后，组长在 Vercel 导入 GitHub 仓库。项目根目录保持默认，框架选择 Other，部署完成后访问 Vercel 提供的网址。
