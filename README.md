# 丝网花创意工坊 - 大学生创业项目

一个基于Streamlit的丝网花售卖网站，类似餐厅点单的小程序，用于大学生创业项目展示。

## 🌸 项目特点

- **三大类产品**：传统丝网花、创新丝网花、新产品
- **类似餐厅点单**：直观的购物车和结算流程
- **响应式设计**：适配手机和电脑浏览器
- **完整功能**：产品浏览、购物车管理、订单提交
- **图片统一尺寸**：所有产品图片自动缩放到300×200像素，保持界面整齐
- **免费部署**：支持Streamlit Cloud免费托管

## 📁 项目结构

```
shop/
├── main.py              # Streamlit应用主文件
├── products.py          # 产品数据模型
├── pyproject.toml       # Python项目配置
├── uv.lock             # 依赖锁定文件
├── README.md           # 项目说明
├── .gitignore          # Git忽略文件
└── images/             # 产品图片
    ├── 01-常规产品/     # 传统丝网花
    ├── 02-创新丝网花/   # 创新丝网花
    └── 03-新产品/       # 新产品
```

## 🚀 快速开始

### 本地运行

1. 确保已安装Python 3.13+和[uv](https://github.com/astral-sh/uv)

2. 安装依赖：

   ```bash
   uv sync
   ```

3. 运行应用：

   ```bash
   uv run streamlit run main.py
   ```

4. 在浏览器中打开 <http://localhost:8501>

### 使用Docker运行

```bash
docker build -t silkflower-shop .
docker run -p 8501:8501 silkflower-shop
```

## 🌐 部署到Streamlit Cloud

### 免费部署步骤

1. 将代码推送到GitHub仓库

2. 访问 [Streamlit Cloud](https://streamlit.io/cloud)

3. 点击 "New app" 并选择你的仓库

4. 配置：
   - **Main file path**: `main.py`
   - **Python version**: 3.13
   - **Branch**: main

5. 点击 "Deploy"

### 环境变量（可选）

在Streamlit Cloud的Settings中可配置：

- `STREAMLIT_SERVER_PORT`: 端口号（默认8501）
- `STREAMLIT_SERVER_ADDRESS`: 服务器地址

## 📱 功能说明

### 1. 主页

- 三大类产品导航
- 特色产品推荐
- 购物车预览

### 2. 产品分类页

- 传统丝网花（6个产品）
- 创新丝网花（11个产品）
- 新产品（8个产品）

### 3. 购物车功能

- 添加/删除商品
- 调整数量
- 实时计算总价
- 侧边栏购物车预览

### 4. 订单结算

- 收货信息表单
- 多种支付方式选择
- 订单确认和编号生成

## 🛠️ 技术栈

- **前端框架**: Streamlit 1.58+
- **编程语言**: Python 3.13+
- **包管理**: uv
- **部署平台**: Streamlit Cloud（免费）
- **图片处理**: PIL/Pillow（如需）

## 📊 产品数据

所有产品数据定义在 `products.py` 中，包含：

- 25个手工丝网花产品
- 每个产品有：ID、名称、描述、价格、分类、图片路径
- 价格范围：¥18 - ¥180

## 🔧 自定义配置

### 添加新产品

在 `products.py` 中添加新的 `Product` 对象：

```python
Product(
    id="new-product-id",
    name="产品名称",
    description="产品描述",
    price=99.0,
    category=ProductCategory.TRADITIONAL,  # 或 INNOVATIVE/NEW
    image_path="images/路径/图片.jpg"
)
```

### 修改价格或库存

直接编辑 `products.py` 中的产品数据。

### 更换图片

将新图片放入 `images/` 对应目录，更新 `image_path`。

## 🚢 部署选项

### 1. Streamlit Cloud（推荐）

- 免费托管
- 自动从GitHub部署
- 支持自定义域名

### 2. Hugging Face Spaces

- 免费容器化部署
- 支持Streamlit应用

### 3. Railway / Render

- 有免费额度
- 更灵活的配置

### 4. 自有服务器

- 使用Docker部署
- 需要域名和SSL证书

## 📞 联系与支持

- **项目负责人**: 大学生创业团队
- **联系电话**: 138-XXXX-XXXX
- **微信**: silkflower_shop
- **邮箱**: <contact@silkflower-shop.example.com>

## 📄 许可证

本项目为大学生创业项目，仅供学习和展示使用。

## 🙏 致谢

感谢所有支持大学生创业项目的老师和同学们！

---

**丝网花创意工坊 - 让手工艺术绽放数字时代** 🌸
