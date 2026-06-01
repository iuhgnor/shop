"""
丝网花售卖网站 - 产品数据模型
包含三大类产品：传统丝网花、创新丝网花、新产品
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List


class ProductCategory(Enum):
    """产品分类枚举"""

    TRADITIONAL = "传统丝网花"
    INNOVATIVE = "创新丝网花"
    NEW = "新产品"


@dataclass
class Product:
    """产品数据类"""

    id: str
    name: str
    description: str
    price: float
    category: ProductCategory
    image_path: str
    stock: int = 10  # 默认库存


# 传统丝网花产品
TRADITIONAL_PRODUCTS = [
    Product(
        id="trad-001",
        name="单只梅花丝网花",
        description="经典梅花造型，手工制作，适合家居装饰",
        price=25.0,
        category=ProductCategory.TRADITIONAL,
        image_path="images/01-常规产品/基础款-01-单只梅花丝网花.jpg",
    ),
    Product(
        id="trad-002",
        name="金鱼挂件",
        description="可爱金鱼造型，可作挂件或装饰",
        price=18.0,
        category=ProductCategory.TRADITIONAL,
        image_path="images/01-常规产品/基础款-02-金鱼挂件.jpg",
    ),
    Product(
        id="trad-003",
        name="孔雀和鸟丝网花",
        description="精品孔雀与小鸟组合，艺术感强",
        price=68.0,
        category=ProductCategory.TRADITIONAL,
        image_path="images/01-常规产品/精品款-01-丝网花制作的孔雀和鸟.jpg",
    ),
    Product(
        id="trad-004",
        name="丝网花花束",
        description="多种花朵组合成的精美花束，永不凋谢",
        price=45.0,
        category=ProductCategory.TRADITIONAL,
        image_path="images/01-常规产品/进阶款-01-丝网花花束.jpg",
    ),
    Product(
        id="trad-005",
        name="仿盆栽装饰花",
        description="盆栽造型，适合办公室或客厅装饰",
        price=38.0,
        category=ProductCategory.TRADITIONAL,
        image_path="images/01-常规产品/进阶款-02-仿盆栽装饰花.jpg",
    ),
    Product(
        id="trad-006",
        name="仿盆栽装饰花（多肉）",
        description="多肉植物造型，可爱精致",
        price=42.0,
        category=ProductCategory.TRADITIONAL,
        image_path="images/01-常规产品/进阶款-03-仿盆栽装饰花.jpg",
    ),
]

# 创新丝网花产品
INNOVATIVE_PRODUCTS = [
    Product(
        id="innov-001",
        name="婚礼路引花艺",
        description="婚庆专用路引花，浪漫优雅",
        price=120.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/01-婚庆产品-婚礼路引花艺-02.jpg",
    ),
    Product(
        id="innov-002",
        name="婚礼路引花艺（白色系）",
        description="白色系婚礼路引，纯洁高雅",
        price=125.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/01-婚庆产品-婚礼路引花艺-03.png",
    ),
    Product(
        id="innov-003",
        name="新娘手捧花",
        description="新娘专用手捧花，精致浪漫",
        price=88.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/01-婚庆产品-手捧花.png",
    ),
    Product(
        id="innov-004",
        name="商业美陈装饰",
        description="商场橱窗装饰，吸引眼球",
        price=150.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/02-商业美陈和橱窗装饰-01.jpg",
    ),
    Product(
        id="innov-005",
        name="商业美陈装饰（现代风）",
        description="现代风格商业装饰",
        price=160.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/02-商业美陈和橱窗装饰-02.png",
    ),
    Product(
        id="innov-006",
        name="商业美陈装饰（艺术风）",
        description="艺术风格商业装饰",
        price=155.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/02-商业美陈和橱窗装饰-03.jpg",
    ),
    Product(
        id="innov-007",
        name="新娘手腕花",
        description="新娘手腕装饰花，精致优雅",
        price=35.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/02-婚庆产品-手腕花-04.png",
    ),
    Product(
        id="innov-008",
        name="摄影写真道具",
        description="摄影专用道具，增加艺术感",
        price=65.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/03-摄影写真舞台道具-01.jpg",
    ),
    Product(
        id="innov-009",
        name="舞台道具装饰",
        description="舞台表演专用装饰道具",
        price=75.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/03-摄影写真舞台道具-02.jpg",
    ),
    Product(
        id="innov-010",
        name="文旅融合装饰",
        description="文化旅游景点装饰",
        price=180.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/04-文旅融合-01.jpg",
    ),
    Product(
        id="innov-011",
        name="文旅融合装饰（传统风）",
        description="传统风格文旅装饰",
        price=175.0,
        category=ProductCategory.INNOVATIVE,
        image_path="images/02-创新丝网花/04-文旅融合-02.png",
    ),
]

# 新产品
NEW_PRODUCTS = [
    Product(
        id="new-001",
        name="风铃捕梦网",
        description="风铃与捕梦网结合，梦幻装饰",
        price=55.0,
        category=ProductCategory.NEW,
        image_path="images/03-新产品/01-风铃捕梦网等装饰品-01.png",
    ),
    Product(
        id="new-002",
        name="风铃装饰品",
        description="精美风铃装饰，声音清脆",
        price=48.0,
        category=ProductCategory.NEW,
        image_path="images/03-新产品/01-风铃捕梦网等装饰品-02.png",
    ),
    Product(
        id="new-003",
        name="串珠手链",
        description="手工串珠手链，时尚配饰",
        price=28.0,
        category=ProductCategory.NEW,
        image_path="images/03-新产品/02-串珠产品-01.png",
    ),
    Product(
        id="new-004",
        name="串珠项链",
        description="手工串珠项链，优雅时尚",
        price=35.0,
        category=ProductCategory.NEW,
        image_path="images/03-新产品/02-串珠产品-02.png",
    ),
    Product(
        id="new-005",
        name="草编收纳篮",
        description="手工草编收纳篮，环保实用",
        price=42.0,
        category=ProductCategory.NEW,
        image_path="images/03-新产品/03-草编产品-01.jpg",
    ),
    Product(
        id="new-006",
        name="草编装饰品",
        description="草编艺术装饰品，自然风格",
        price=38.0,
        category=ProductCategory.NEW,
        image_path="images/03-新产品/03-草编产品-02.jpg",
    ),
    Product(
        id="new-007",
        name="不织布玩偶",
        description="不织布手工玩偶，可爱温馨",
        price=32.0,
        category=ProductCategory.NEW,
        image_path="images/03-新产品/04-不织布制品-01.png",
    ),
    Product(
        id="new-008",
        name="不织布装饰画",
        description="不织布装饰画，创意家居",
        price=45.0,
        category=ProductCategory.NEW,
        image_path="images/03-新产品/04-不织布制品-02.jpg",
    ),
]

# 所有产品列表
ALL_PRODUCTS = TRADITIONAL_PRODUCTS + INNOVATIVE_PRODUCTS + NEW_PRODUCTS

# 按ID快速查找产品的字典
PRODUCTS_BY_ID = {product.id: product for product in ALL_PRODUCTS}

# 按分类组织的产品字典
PRODUCTS_BY_CATEGORY = {
    ProductCategory.TRADITIONAL: TRADITIONAL_PRODUCTS,
    ProductCategory.INNOVATIVE: INNOVATIVE_PRODUCTS,
    ProductCategory.NEW: NEW_PRODUCTS,
}


def get_products_by_category(category: ProductCategory) -> List[Product]:
    """获取指定分类的产品列表"""
    return PRODUCTS_BY_CATEGORY.get(category, [])


def get_product_by_id(product_id: str) -> Product | None:
    """根据ID获取产品"""
    return PRODUCTS_BY_ID.get(product_id)


if __name__ == "__main__":
    # 测试数据
    print(f"总产品数量: {len(ALL_PRODUCTS)}")
    print(f"传统丝网花: {len(TRADITIONAL_PRODUCTS)} 个")
    print(f"创新丝网花: {len(INNOVATIVE_PRODUCTS)} 个")
    print(f"新产品: {len(NEW_PRODUCTS)} 个")

    # 显示前3个产品
    for i, product in enumerate(ALL_PRODUCTS[:3]):
        print(f"\n产品 {i + 1}:")
        print(f"  名称: {product.name}")
        print(f"  价格: ¥{product.price}")
        print(f"  分类: {product.category.value}")
        print(f"  图片: {product.image_path}")
